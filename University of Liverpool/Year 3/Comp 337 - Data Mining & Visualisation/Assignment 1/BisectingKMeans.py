import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from KMeans import KMeans  # Import KMeans for splitting clusters

# ------------------------------------------------
# 1) Load Dataset Function (Ensures Numerical Data)
# ------------------------------------------------
def load_dataset():
    """
    Loads the dataset

    Returns:
        np.ndarray: Data points as a 2D array.
    """
    try:
        df = pd.read_csv("dataset", header=None, delim_whitespace=True)
        print(f"✅ Original dataset shape: {df.shape}")
        
        df = df.iloc[:, 1:]  # Drop first column (assumed to be labels)
        df = df.apply(pd.to_numeric, errors='coerce')  # Convert non-numeric to NaN
        df.dropna(inplace=True)  # Remove rows with NaN
        
        print(f"📊 Dataset after cleaning: {df.shape[0]} rows, {df.shape[1]} columns")
        
        if df.shape[0] <= 1:
            raise Exception("Dataset must contain more than one data point.")
        
        return df.values  # Return data as a numpy array
    except FileNotFoundError:
        raise Exception("❌ Dataset file not found.")
    except Exception as e:
        raise Exception(f"❌ Error loading dataset: {e}")

# ------------------------------------------------
# 2) Compute Sum of Squared Errors (SSE)
# ------------------------------------------------
def computeSSE(x, labels, centroids):
    """
    Computes the Sum of Squared Errors (SSE) for each cluster.

    Args:
        x (np.ndarray): Dataset.
        labels (np.ndarray): Cluster labels.
        centroids (np.ndarray): Cluster centroids.

    Returns:
        dict: Dictionary of SSE values for each cluster.
    """
    sse = {}
    for cluster_id in np.unique(labels):
        cluster_points = x[labels == cluster_id]
        if len(cluster_points) > 0:
            sse[cluster_id] = np.sum((cluster_points - centroids[cluster_id])**2)
    return sse

# ------------------------------------------------
# 3) Bisecting K-Means Algorithm
# ------------------------------------------------
def BisectingKMeans(x, max_clusters=9):
    """
    Runs the Bisecting K-Means clustering algorithm.

    Args:
        x (np.ndarray): Dataset.
        max_clusters (int): Target number of clusters.

    Returns:
        list: Cluster assignments.
    """
    clusters = {0: x}  # Start with all points in one cluster
    labels = np.zeros(len(x), dtype=int)  # Initial labels

    cluster_id = 1  # Start new cluster IDs from 1

    while len(clusters) < max_clusters:
        # Select the cluster with the highest SSE to split
        cluster_sse = {cid: np.sum((clusters[cid] - clusters[cid].mean(axis=0))**2) for cid in clusters}
        cluster_to_split = max(cluster_sse, key=cluster_sse.get)

        # Apply K-Means with k=2 to split the selected cluster
        cluster_points = clusters[cluster_to_split]
        split_labels = KMeans(cluster_points, k=2)

        # Extract two new clusters
        new_clusters = {
            cluster_id: cluster_points[split_labels == 0],
            cluster_id + 1: cluster_points[split_labels == 1]
        }

        # Remove old cluster and add the new ones
        del clusters[cluster_to_split]
        clusters.update(new_clusters)

        # Update labels
        for new_id, points in new_clusters.items():
            mask = np.isin(x, points).all(axis=1)
            labels[mask] = new_id

        cluster_id += 2  # Increment cluster count

    return labels

# ------------------------------------------------
# 4) Plot Silhouette Scores for Bisecting K-Means
# ------------------------------------------------
def plotSilhouette(x, s_values):
    """
    Computes silhouette scores for Bisecting K-Means clustering.

    Args:
        x (np.ndarray): Dataset.
        s_values (list): Range of s values (number of clusters).

    Returns:
        None
    """
    silhouette_scores = []

    for s in s_values:
        labels = BisectingKMeans(x, max_clusters=s)
        score = silhouette_score(x, labels) if len(np.unique(labels)) > 1 else 0
        silhouette_scores.append(score)

    plt.figure(figsize=(8, 5))
    plt.plot(s_values, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel("Number of Clusters (s)")
    plt.ylabel("Silhouette Coefficient")
    plt.title("Silhouette Scores for Bisecting K-Means Clustering")
    plt.grid(True)
    plt.savefig("BisectingKMeans_Silhouette.png")
    plt.show()

# ------------------------------------------------
# 5) Main Execution
# ------------------------------------------------
if __name__ == "__main__":
    try:
        data = load_dataset()
        s_values = range(1, 10)
        plotSilhouette(data, s_values)

    except Exception as e:
        print(f"❌ Error: {e}")
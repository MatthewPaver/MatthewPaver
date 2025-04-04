import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------
# 1) Load Dataset Function with Error Handling
# ------------------------------------------------
def load_dataset():
    """
    Loads the dataset
    
    If the file has multiple columns, assumes the first column is a label and uses the rest as features.

    Returns:
        x (numpy.ndarray): Data as a 2D numpy array (samples, features).
    """
    try:
        df = pd.read_csv("dataset", header=None, delim_whitespace=True)
        if df.shape[1] > 1:
            x = df.iloc[:, 1:].values  # Use all columns except the first as features
        else:
            x = df.values
        return x
    except FileNotFoundError:
        raise Exception("Error: The dataset file is missing. Ensure 'dataset' is in the directory.")
    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")

# ------------------------------------------------
# 2) Compute Distance Function
# ------------------------------------------------
def ComputeDistance(p1, p2):
    """Computes the Euclidean distance between two points."""
    return np.linalg.norm(p1 - p2)

# ------------------------------------------------
# 3) Initial Selection of Cluster Centroids
# ------------------------------------------------
def initialSelection(x, k):
    """Selects k random initial centroids from the dataset."""
    np.random.seed(42)
    indices = np.random.choice(len(x), k, replace=False)
    return x[indices]

# ------------------------------------------------
# 4) Assign Cluster IDs
# ------------------------------------------------
def assignClusterIds(x, centroids):
    """Assigns each data point to the closest centroid."""
    distances = np.array([[ComputeDistance(pt, c) for c in centroids] for pt in x])
    return np.argmin(distances, axis=1)

# ------------------------------------------------
# 5) Compute New Centroids
# ------------------------------------------------
def computeClusterRepresentatives(x, labels, k):
    """Computes new centroids as the mean of assigned points."""
    centroids = []
    for cluster_id in range(k):
        cluster_points = x[labels == cluster_id]
        centroids.append(np.mean(cluster_points, axis=0) if len(cluster_points) > 0 else np.zeros(x.shape[1]))
    return np.array(centroids)

# ------------------------------------------------
# 6) Compute Silhouette Score with Error Handling
# ------------------------------------------------
def computeSilhouette(x, labels):
    """Computes the silhouette score for clustering."""
    unique_clusters = np.unique(labels)
    if len(unique_clusters) < 2:
        return 0.0  # If all points belong to one cluster, silhouette score is not defined.

    n = len(x)
    silhouette_scores = np.zeros(n)

    for i in range(n):
        current_cluster = labels[i]
        in_cluster = (labels == current_cluster)

        same_cluster_points = x[in_cluster]
        a = np.mean([ComputeDistance(x[i], pt) for pt in same_cluster_points if not np.array_equal(pt, x[i])]) if len(same_cluster_points) > 1 else 0.0
        
        b_values = []
        for c in unique_clusters:
            if c != current_cluster:
                other_cluster_points = x[labels == c]
                if len(other_cluster_points) > 0:
                    b_values.append(np.mean([ComputeDistance(x[i], pt) for pt in other_cluster_points]))

        b = np.min(b_values) if b_values else 0.0
        silhouette_scores[i] = (b - a) / max(a, b) if max(a, b) != 0 else 0.0

    return np.mean(silhouette_scores)

# ------------------------------------------------
# 7) K-Means Algorithm
# ------------------------------------------------
def KMeans(x, k, maxIter=100, tol=1e-4):
    """Runs the K-Means clustering algorithm."""
    centroids = initialSelection(x, k)
    
    for _ in range(maxIter):
        labels = assignClusterIds(x, centroids)
        new_centroids = computeClusterRepresentatives(x, labels, k)
        if np.all(np.abs(new_centroids - centroids) < tol):
            break
        centroids = new_centroids

    return labels

# ------------------------------------------------
# 8) Plot Silhouette Scores
# ------------------------------------------------
def plotSilhouette(x, k_values):
    """Computes and plots silhouette scores for different k values."""
    silhouette_scores = [computeSilhouette(x, KMeans(x, k)) for k in k_values]

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Scores for K-Means Clustering")
    plt.grid(True)
    plt.savefig("KMeans_Silhouette.png")
    plt.show()

# ------------------------------------------------
# 9) Main Execution
# ------------------------------------------------
if __name__ == "__main__":
    try:
        data = load_dataset()
        k_values = range(1, 10)
        plotSilhouette(data, k_values)
    except Exception as e:
        print(f"Error: {e}")
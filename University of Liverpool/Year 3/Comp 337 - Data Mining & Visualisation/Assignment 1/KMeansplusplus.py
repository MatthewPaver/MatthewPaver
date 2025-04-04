import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from KMeans import computeSilhouette  # Import silhouette function from KMeans.py

# ----------------------------------------
# Load Dataset (Ensures Numerical Data)
# ----------------------------------------
def load_dataset():
    """
    Loads the dataset while ensuring only numerical values are used.

    Returns:
        np.ndarray: Data points as a 2D array.
    """
    try:
        df = pd.read_csv("dataset", header=None, delim_whitespace=True)
        df = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')  # Remove labels, ensure numeric
        if df.isnull().values.any():
            raise Exception("Dataset contains NaN values after conversion. Check input format.")
        if df.shape[0] <= 1:
            raise Exception("Dataset must contain more than one data point.")
        return df.values  # Return numerical data only
    except FileNotFoundError:
        raise Exception("Dataset file not found.")
    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")

# ----------------------------------------
# Compute Distance Function
# ----------------------------------------
def ComputeDistance(p1, p2):
    """Computes the Euclidean distance between two points."""
    return np.linalg.norm(p1 - p2)

# ----------------------------------------
# K-Means++ Initialisation
# ----------------------------------------
def initialSelectionPlusPlus(x, k):
    """
    Selects k initial centroids using K-Means++ strategy.

    Args:
        x (numpy.ndarray): The dataset.
        k (int): Number of clusters.

    Returns:
        np.ndarray: Initial centroids.
    """
    np.random.seed(42)  # Fixed seed for consistency
    centroids = [x[np.random.choice(len(x))]]  # Pick first centroid randomly

    for _ in range(1, k):
        distances = np.array([min([ComputeDistance(point, c) for c in centroids]) for point in x])

        # Handle case where all distances are zero (identical points)
        if np.sum(distances) == 0:
            new_centroid = x[np.random.choice(len(x))]
        else:
            probabilities = distances / np.sum(distances)
            new_centroid = x[np.random.choice(len(x), p=probabilities)]

        centroids.append(new_centroid)

    return np.array(centroids)

# ----------------------------------------
# Assign Cluster Labels
# ----------------------------------------
def assignClusterIds(x, centroids):
    """
    Assigns each data point to the closest centroid.

    Args:
        x (numpy.ndarray): Dataset.
        centroids (numpy.ndarray): Current cluster centroids.

    Returns:
        np.ndarray: Cluster assignments.
    """
    distances = np.array([[ComputeDistance(pt, c) for c in centroids] for pt in x])
    return np.argmin(distances, axis=1)

# ----------------------------------------
# Compute New Centroids
# ----------------------------------------
def computeClusterRepresentatives(x, labels, k):
    """
    Computes new centroids based on cluster assignments.

    Args:
        x (numpy.ndarray): Dataset.
        labels (numpy.ndarray): Cluster labels.
        k (int): Number of clusters.

    Returns:
        np.ndarray: Updated centroids.
    """
    centroids = []
    for cluster_id in range(k):
        cluster_points = x[labels == cluster_id]
        centroids.append(cluster_points.mean(axis=0) if len(cluster_points) > 0 else np.zeros(x.shape[1]))
    return np.array(centroids)

# ----------------------------------------
# K-Means++ Algorithm
# ----------------------------------------
def KmeansPlusPlus(x, k, maxIter=100, tol=1e-4):
    """
    Runs K-Means++ clustering on dataset.

    Args:
        x (numpy.ndarray): Dataset.
        k (int): Number of clusters.
        maxIter (int): Max iterations for convergence.
        tol (float): Convergence threshold.

    Returns:
        np.ndarray: Final cluster labels.
    """
    centroids = initialSelectionPlusPlus(x, k)

    for _ in range(maxIter):
        labels = assignClusterIds(x, centroids)
        new_centroids = computeClusterRepresentatives(x, labels, k)
        shift = np.abs(new_centroids - centroids)
        if np.all(shift < tol):
            break
        centroids = new_centroids

    return labels

# ----------------------------------------
# Plot Silhouette Scores
# ----------------------------------------
def plotSilhouetteKMeansPP(x, k_values):
    """
    Computes silhouette scores for K-Means++ clustering.

    Args:
        x (numpy.ndarray): Dataset.
        k_values (list): Range of k values.

    Returns:
        None
    """
    silhouette_scores = []

    for k in k_values:
        labels = KmeansPlusPlus(x, k)
        score = computeSilhouette(x, labels)
        silhouette_scores.append(score)

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Coefficient")
    plt.title("Silhouette Scores for K-Means++ Clustering")
    plt.grid(True)
    plt.savefig("KMeansplusplus_Silhouette.png")
    plt.show()

# ----------------------------------------
# Main Execution
# ----------------------------------------
if __name__ == "__main__":
    try:
        data = load_dataset()
        k_values = range(1, 10)
        plotSilhouetteKMeansPP(data, k_values)

    except Exception as e:
        print(f"Error: {e}")
import numpy as np
import matplotlib.pyplot as plt
from KMeans import KMeans, computeSilhouette, load_dataset

# ------------------------------------------------
# 1) Generate Meaningful Synthetic Data
# ------------------------------------------------
def generate_synthetic_data(original_data):
    """
    Creates synthetic data with the same number of samples and features as the original dataset.
    
    Uses Gaussian Mixtures to create random cluster-like data instead of pure noise.

    Args:
        original_data (numpy.ndarray): The original dataset used as reference.

    Returns:
        numpy.ndarray: A new dataset with the same shape but generated from random clusters.
    """
    np.random.seed(42)  # Ensures reproducibility

    num_samples, num_features = original_data.shape
    num_clusters = min(5, num_samples)  # Avoid too many clusters for small datasets

    # Generate cluster centres randomly
    cluster_centres = np.random.uniform(
        np.min(original_data, axis=0), np.max(original_data, axis=0), size=(num_clusters, num_features)
    )

    # Generate synthetic data points around those clusters
    synthetic_data = []
    for _ in range(num_samples):
        cluster_idx = np.random.randint(0, num_clusters)  # Pick a random cluster
        point = cluster_centres[cluster_idx] + np.random.normal(scale=0.5, size=num_features)
        synthetic_data.append(point)

    return np.array(synthetic_data)

# ------------------------------------------------
# 2) Plot Silhouette Scores for Synthetic Data
# ------------------------------------------------
def plot_silhouette(x, k_values):
    """
    Runs K-Means on synthetic data for different cluster values and computes silhouette scores.

    Args:
        x (numpy.ndarray): The dataset to cluster.
        k_values (list or range): The different values of k to test.

    Returns:
        None (Saves the plot as an image file).
    """
    silhouette_scores = []

    for k in k_values:
        labels = KMeans(x, k)  # Run K-Means on synthetic data
        score = computeSilhouette(x, labels)  # Compute silhouette score
        silhouette_scores.append(score)

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, silhouette_scores, marker='o', linestyle='-')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Coefficient")
    plt.title("Silhouette Scores for K-Means Clustering on Synthetic Data")
    plt.grid(True)
    plt.savefig("KMeansSynthetic_Silhouette.png")  # Save figure
    plt.show()

# ------------------------------------------------
# 3) Main Execution
# ------------------------------------------------
if __name__ == "__main__":
    try:
        # Load real dataset to match size
        real_data = load_dataset()

        # Generate synthetic dataset
        synthetic_data = generate_synthetic_data(real_data)

        # Run silhouette analysis for k = 1 to 9
        k_values = range(1, 10)
        plot_silhouette(synthetic_data, k_values)

    except Exception as e:
        print(f"Error: {e}")
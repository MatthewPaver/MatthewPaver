# COMP337 – Assignment 1

Author: **Matthew Paver**  
Student ID: **201582813**

This folder contains the complete implementation and analysis for COMP337 Assignment 1. The assignment focuses on implementing and evaluating various clustering algorithms from scratch and analyzing their performance using the Silhouette coefficient.

## 🧠 Assignment Questions and Files

### ✅ Q1. Standard K-Means
- **File:** `KMeans.py`
- **Functionality:**
  - Implements standard k-Means clustering
  - Computes Silhouette coefficient for `k = 1` to `9`
  - Saves silhouette plot as `KMeans_Silhouette.png`

---

### ✅ Q2. K-Means with Synthetic Data
- **File:** `KMeansSynthetic.py`
- **Functionality:**
  - Generates synthetic dataset with the same number of points as the provided `dataset`
  - Clusters synthetic data using k-Means
  - Saves silhouette plot as `KMeansSynthetic_Silhouette.png`

---

### ✅ Q3. K-Means++
- **File:** `KMeansplusplus.py`
- **Functionality:**
  - Implements the k-Means++ initialization
  - Clusters the provided dataset
  - Saves silhouette plot as `KMeansplusplus_Silhouette.png`

---

### ✅ Q4. Bisecting K-Means
- **File:** `BisectingKMeans.py`
- **Functionality:**
  - Implements hierarchical clustering using bisecting k-Means
  - Computes Silhouette coefficients for `s = 1` to `9` clusters
  - Saves silhouette plot as `BisectingKMeans_Silhouette.png`

---

### ✅ Q5 & Q6. Evaluation Metrics
- **File:** `201582813_COMP337_Assignment1_Q5_Q6.pdf`
- **Functionality:**
  - Written report containing:
    - Confusion matrix
    - Macro-averaged precision, recall, and F-score
    - B-CUBED precision, recall, and F-score
  - Evaluations based on `Figure1_labels.txt`

---

## 📌 Notes

- All implementations are done **from scratch** using only allowed libraries (`numpy`, `matplotlib`, `random`, and basic file I/O).
- All clustering scripts are designed to:
  - Run independently using `python filename.py`
  - Generate the required silhouette plots in the current directory
  - Contain modular and well-commented functions:
    - `plot_silhouette()`
    - `ComputeDistance()`
    - `initialSelection()`
    - `clustername(x, k)`
    - Plus additional required methods for each question
- A fixed seed is used for reproducibility where random operations are involved.
- Edge cases like missing or malformed files are gracefully handled.

---

## 🛠️ How to Run

```bash
# Ensure you're inside the Assignment 1 directory
python KMeans.py
python KMeansSynthetic.py
python KMeansplusplus.py
python BisectingKMeans.py

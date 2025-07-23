# Customer Segmentation using KMeans and DBSCAN

This project applies machine learning clustering techniques to group customers based on demographic and behavioral data. It enables personalized marketing strategies and better business decisions.

---

## 📁 Dataset

**Columns:**

- `CustomerID`: Unique ID
- `Gender`: Male/Female (converted to 1/0)
- `Age`: Customer age
- `Annual Income (k$)`
- `Spending Score (1-100)`: Mall-defined score

---

## 📊 EDA Highlights

- Age and income distributions
- Gender imbalance (more females)
- Spending habits show distinct patterns

---

## 🧼 Preprocessing

- Cleaned `Gender`
- Standardized numerical features
- Removed null values (if any)

---

## 🧠 Clustering Algorithms

### KMeans

- Chosen via Silhouette Score (optimal k = 6)
- Balanced customer segments
- **Silhouette Score:** `0.4284` (varies)

### DBSCAN

- Density-based
- Useful for noise detection
- Performance depends on `eps` and `min_samples`
- **Silhouette Score (excluding noise):** `~0.45+` (varies)

---

## 📈 Visualizations

- Elbow curve for KMeans
- Scatter plots of clusters (KMeans & DBSCAN)

---

## 📁 Output Files

- `segmented_customers_kmeans_dbscan.csv` – Full dataset with cluster labels
  
---

## 🔧 Tools Used

- Python
- Pandas, Seaborn, Matplotlib
- scikit-learn

---

## 📌 Conclusion

KMeans works well for cleanly separable clusters. DBSCAN identifies noise and non-convex clusters but is sensitive to parameters.


## Clustering Comparison Summary

| Method      | No. of Clusters | Noise Points | Silhouette Score          | Suitable For                                    |
| ----------- | --------------- | ------------ | ------------------------- | ----------------------------------------------- |
| **K-Means** | 6               | 0            | ~0.42+                    | Balanced, general datasets                      |
| **DBSCAN**  | 3 (w/ noise)    | 1            | ~0.279 (excluding noise)  | Irregular or non-spherical clusters, noisy data |

import os
os.environ["OMP_NUM_THREADS"] = "1"

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


PLOTS_DIR = "static/plots/res"
PLOT_NAME = "elbow_method.png"

os.makedirs(PLOTS_DIR, exist_ok=True)

# Chargement des données
DATA_PATH = "data/processed/Customer_Purchasing_Behaviors_processed.csv"
df = pd.read_csv(DATA_PATH)

# Variables utilisées pour le clustering
features = [
    "age",
    "annual_income",
    "purchase_frequency",
    "average_purchase_amount"
]

X = df[features]


# Standardisation des données
scaler = StandardScaler()
X = scaler.fit_transform(X)


# Méthode du coude (Elbow)
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(
        n_clusters=k,
        init="k-means++",
        n_init=10,
        max_iter=300,
        random_state=42
    )
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Visualisation Elbow
plt.figure()
plt.plot(K_range, inertias, marker="o")
plt.xlabel("Nombre de clusters (K)")
plt.ylabel("Inertie")
plt.title("Méthode du coude (Elbow Method)")
output_path = os.path.join(PLOTS_DIR, PLOT_NAME)
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()


# Choix du K optimal
# À choisir visuellement à partir du graphique
K_optimal = 3

# Entraînement final K-Means
kmeans = KMeans(
    n_clusters=K_optimal,
    init="k-means++",
    n_init=10,
    max_iter=300,
    random_state=42
)

df["cluster"] = kmeans.fit_predict(X)

# Évaluation du clustering avec le Silhouette Score
sil_score = silhouette_score(X, df["cluster"])

# Sauvegarde des résultats
df.to_csv("data/processed/Customer_Purchasing_Behaviors_with_clusters.csv", index=False)

print("Clustering terminé avec succès.")
print("Nombre de clusters choisi :", K_optimal)
print("Silhouette Score :", round(sil_score, 4))

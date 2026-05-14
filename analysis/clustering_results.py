
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/processed/Customer_Purchasing_Behaviors_with_clusters.csv"   # CSV avec colonne 'cluster'
PLOTS_DIR = "static/plots/res"
PLOT_NAME = "clusters.png"

os.makedirs(PLOTS_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
required_cols = {"annual_income", "average_purchase_amount", "cluster"}
if not required_cols.issubset(df.columns):
    raise ValueError(
        f"Le dataset doit contenir les colonnes : {required_cols}"
    )

# Scatter plot des clusters
plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    df["annual_income"],
    df["average_purchase_amount"],
    c=df["cluster"],
    cmap="tab10",
    alpha=0.7
)

plt.title("Segmentation clients par K-Means", fontsize=14)
plt.xlabel("Annual Income")
plt.ylabel("Average Purchase Amount")

# Légende des clusters
legend = plt.legend(
    *scatter.legend_elements(),
    title="Cluster"
)
plt.gca().add_artist(legend)

plt.grid(True, linestyle="--", alpha=0.4)


# Sauvegarde du graphique
output_path = os.path.join(PLOTS_DIR, PLOT_NAME)
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()

# Log simple (optionnel)
print(f"Scatter plot des clusters sauvegardé : {output_path}")

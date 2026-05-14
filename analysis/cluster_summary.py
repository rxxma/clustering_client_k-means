import os
import pandas as pd
import matplotlib.pyplot as plt


# Chargement des données preprocessées
DATA_PATH = "data/processed/Customer_Purchasing_Behaviors_processed.csv"
df = pd.read_csv(DATA_PATH)


# Dossier pour sauvegarder les graphiques (utilisé par Flask via static/plots/st)
PLOT_PATH = "static/plots/st"
os.makedirs(PLOT_PATH, exist_ok=True)

numeric_cols = [
    "age",
    "annual_income",
    "purchase_frequency",
    "average_purchase_amount",
]

# Ne garder que les colonnes effectivement présentes dans le DataFrame
numeric_cols = [c for c in numeric_cols if c in df.columns]

#  Aperçu du dataset

print("=== APERÇU DU DATASET ===")
print("Chemin des données :", DATA_PATH)
print("\nInfo sur le DataFrame :")
print(df.info())

print("\nTypes des variables :")
print(df.dtypes)


# Statistiques descriptives globales

print("\n=== STATISTIQUES DESCRIPTIVES (NUMÉRIQUES) ===")
print(df.describe())

# Mesures de tendance centrale et de dispersion
# (adapté aux variables clés du projet)

if numeric_cols:
    print("\nVariables numériques utilisées pour le résumé :", numeric_cols)

    print("\nMoyennes :")
    means = df[numeric_cols].mean()
    print(means)

    print("\nMédianes :")
    medians = df[numeric_cols].median()
    print(medians)
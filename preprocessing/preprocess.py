import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Chargement des données
DATA_PATH = "data/raw/Customer_Purchasing_Behaviors.csv"
df = pd.read_csv(DATA_PATH)

# Suppression des colonnes inutiles
df = df.drop(columns=["user_id", "region"])

# Création du montant moyen par achat
df["average_purchase_amount"] = (
    df["purchase_amount"] / df["purchase_frequency"]
)

# Suppression de la colonne purchase_amount
df = df.drop(columns=["purchase_amount"])

# Sélection des variables pour K-Means
features = [
    "age",
    "annual_income",
    "purchase_frequency",
    "average_purchase_amount"
]

# Copie explicite des données sélectionnées
X = df[features].copy()

# types de données
print(X.dtypes) 

# Ligne pour vérifier l’existence des valeurs manquantes
print("Valeurs manquantes par colonne :\n", X.isnull().sum())




# Sauvegarde des données preprocessées
os.makedirs("data/processed", exist_ok=True)

df_processed = pd.DataFrame(
    X,
    columns=features
)

df_processed.to_csv(
    "data/processed/Customer_Purchasing_Behaviors_processed.csv",
    index=False
)

print(" Preprocessing terminé avec succès.")
print(" Fichier créé : data/processed/Customer_Purchasing_Behaviors_processed.csv")

# 🛍️ Customer Segmentation & Clustering (K-Means)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Présentation du Projet
Ce projet est une application de **Machine Learning** dédiée à la segmentation de clientèle. En utilisant l'algorithme **K-Means**, nous analysons les comportements d'achat des clients pour les regrouper en segments distincts. 

L'objectif est de permettre aux entreprises de mieux comprendre leur base client et d'adapter leurs stratégies marketing (ciblage, promotions, fidélisation) en fonction des caractéristiques de chaque groupe.

## 🚀 Fonctionnalités
- **Pipeline de Data Processing** : Nettoyage, feature engineering (calcul du montant moyen par achat) et standardisation des données.
- **Modélisation K-Means** : Recherche du nombre optimal de clusters via la **méthode du coude (Elbow Method)**.
- **Analyse Statistique** : Génération automatique de graphiques de distribution et de résumés par cluster.
- **Dashboard Flask** : Interface web interactive pour visualiser :
    - Les statistiques descriptives de la base client.
    - Les résultats du clustering.
    - Une synthèse détaillée de chaque profil type (Persona).

## 📁 Structure du Projet
```text
clustering_client_k-means/
├── analysis/               # Scripts d'analyse et génération de rapports
│   ├── outputs/            # CSV de synthèse des clusters
│   ├── cluster_summary.py
│   └── descriptive_stats.py
├── app/                    # Code de l'application Flask
│   ├── app.py              # Configuration Flask
│   └── routes.py           # Définition des points d'entrée (endpoints)
├── data/                   # Gestion des données
│   ├── raw/                # Données brutes (Customer_Purchasing_Behaviors.csv)
│   └── processed/          # Données nettoyées et taguées par cluster
├── models/                 # Scripts d'entraînement ML
│   ├── train_kmeans.py     # Script principal d'entraînement
│   └── kmeans_model.pkl    # Modèle sauvegardé
├── preprocessing/          # Scripts de nettoyage
│   └── preprocess.py
├── static/                 # Fichiers statiques (CSS, Images, Plots)
├── templates/              # Pages HTML du Dashboard
├── main.py                 # Point d'entrée pour lancer l'app
└── requirements.txt        # Dépendances du projet
```

## 🛠️ Installation et Utilisation

### 1. Clonage du projet
```bash
git clone https://github.com/votre-username/clustering_client_k-means.git
cd clustering_client_k-means
```

### 2. Installation des dépendances
Il est recommandé d'utiliser un environnement virtuel :
```bash
python -m venv venv
source venv/bin/scripts/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Exécution du Pipeline (Optionnel)
Si vous souhaitez ré-entraîner le modèle avec de nouvelles données :
```bash
python preprocessing/preprocess.py
python models/train_kmeans.py
python analysis/cluster_summary.py
```

### 4. Lancement du Dashboard
```bash
python main.py
```
L'application sera accessible sur `http://127.0.0.1:5000/`.

## 📊 Aperçu des Résultats
Le modèle identifie actuellement 3 segments de clients majeurs basés sur :
- **Âge**
- **Revenu Annuel**
- **Fréquence d'Achat**
- **Montant Moyen par Achat**

*Exemple de profils identifiés :*
- **Cluster 0** : Clients seniors à haut revenu avec une fréquence d'achat élevée.
- **Cluster 1** : Clients jeunes avec un budget plus limité et achats occasionnels.
- **Cluster 2** : Clients d'âge moyen avec une consommation équilibrée.

## 🧰 Technologies Utilisées
- **Python** : Langage principal.
- **Pandas & NumPy** : Manipulation et analyse de données.
- **Scikit-Learn** : Algorithme K-Means et preprocessing.
- **Matplotlib & Seaborn** : Visualisation de données.
- **Flask** : Serveur web pour le dashboard.

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une *Issue* ou à soumettre une *Pull Request*.



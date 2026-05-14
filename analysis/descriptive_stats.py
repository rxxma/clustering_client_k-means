import os
import pandas as pd
import matplotlib
# Use non-interactive backend to avoid Qt platform plugin errors when running
# in headless environments (CI, servers, container, or when no Qt is installed).
# This must be set before importing matplotlib.pyplot.
try:
    matplotlib.use('Agg')
except Exception:
    # If backend setting fails, continue and allow matplotlib to choose a backend
    pass
import matplotlib.pyplot as plt
import numpy as np

# Palette de couleurs Gris Blue Elegance (cohérente avec le CSS)
GRIS_BLUE_PALETTE = {
    # Palette principale du CSS
    'midnight_blue': '#2C3E50',
    'slate_gray': '#4A6572',
    'steel_blue': '#5D8AA8',
    'light_steel': '#8AAEC1',
    'pale_gray': '#ECF0F1',
    'silver': '#BDC3C7',
    'dark_slate': '#34495E',
    'soft_white': '#F8F9FA',
    
    # Accents du CSS
    'accent_blue': '#3498DB',
    'accent_teal': '#1ABC9C',
    'accent_coral': '#E74C3C',
    
    # Variations supplémentaires pour les graphiques
    'midnight_light': '#3A506B',
    'midnight_dark': '#1C2833',
    'slate_light': '#5B7483',
    'slate_dark': '#3A4A52',
    'steel_light': '#6F9AC2',
    'steel_dark': '#4C6B8A',
} 

# Configuration du style Matplotlib avec la palette Gris Blue
plt.style.use('seaborn-v0_8-whitegrid')  # Changé pour whitegrid pour thème clair
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = GRIS_BLUE_PALETTE['midnight_blue']
plt.rcParams['axes.labelcolor'] = GRIS_BLUE_PALETTE['midnight_blue']
plt.rcParams['text.color'] = GRIS_BLUE_PALETTE['midnight_blue']
plt.rcParams['xtick.color'] = GRIS_BLUE_PALETTE['slate_gray']
plt.rcParams['ytick.color'] = GRIS_BLUE_PALETTE['slate_gray']
plt.rcParams['grid.color'] = GRIS_BLUE_PALETTE['silver']
plt.rcParams['grid.alpha'] = 0.5

# Chargement des données preprocessées
DATA_PATH = "data/processed/Customer_Purchasing_Behaviors_processed.csv"
df = pd.read_csv(DATA_PATH)

# Dossier pour sauvegarder les graphiques
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

# Aperçu du dataset
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
if numeric_cols:
    print("\nVariables numériques utilisées pour le résumé :", numeric_cols)

    print("\nMoyennes :")
    means = df[numeric_cols].mean()
    print(means)

    print("\nMédianes :")
    medians = df[numeric_cols].median()
    print(medians)

    print("\nÉcarts-types :")
    stds = df[numeric_cols].std()
    print(stds)

    print("\nQuartiles (25%, 50%, 75%) :")
    quarts = df[numeric_cols].quantile([0.25, 0.5, 0.75])
    print(quarts)

# Histogrammes avec la palette Gris Blue
for idx, col in enumerate(df.columns):
    if pd.api.types.is_numeric_dtype(df[col]):
        plt.figure(figsize=(10, 6))
        
        # Choisir une couleur cyclique de la palette Gris Blue
        colors = [GRIS_BLUE_PALETTE['steel_blue'], GRIS_BLUE_PALETTE['accent_blue'], 
                  GRIS_BLUE_PALETTE['slate_gray'], GRIS_BLUE_PALETTE['light_steel']]
        color_idx = idx % len(colors)
        
        n, bins, patches = plt.hist(df[col], bins=30, edgecolor=GRIS_BLUE_PALETTE['midnight_blue'], 
                                   linewidth=1.5, alpha=0.85, color=colors[color_idx])
        
        # Ajouter des lignes pour la moyenne et ±1 écart-type
        if col in means.index and col in stds.index:
            mean_val = means[col]
            std_val = stds[col]
            
            plt.axvline(mean_val, color=GRIS_BLUE_PALETTE['accent_teal'], linewidth=3, 
                       linestyle='-', label=f'Moyenne ({mean_val:.2f})', alpha=0.9)
            plt.axvline(mean_val - std_val, color=GRIS_BLUE_PALETTE['slate_light'], 
                       linewidth=2, linestyle=':', label=f'-1 STD')
            plt.axvline(mean_val + std_val, color=GRIS_BLUE_PALETTE['slate_light'], 
                       linewidth=2, linestyle=':', label=f'+1 STD')
            
            # Remplir la zone entre ±1 écart-type
            plt.axvspan(mean_val - std_val, mean_val + std_val, 
                       alpha=0.15, color=GRIS_BLUE_PALETTE['steel_blue'], 
                       label='68% des données (1 STD)')
        
        plt.title(f"Distribution de {col}", fontsize=16, fontweight='bold', 
                 color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
        plt.xlabel(col, fontsize=14, fontweight='semibold')
        plt.ylabel("Fréquence", fontsize=14, fontweight='semibold')
        
        # Améliorer les ticks
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        # Ajouter une grille subtile
        plt.grid(True, alpha=0.3, linestyle='--')
        
        # Ajouter une légende
        legend = plt.legend(loc='upper right', fontsize=10, framealpha=0.9, 
                  edgecolor=GRIS_BLUE_PALETTE['silver'])
        legend.get_frame().set_facecolor('white')
        
        # Ajouter une boîte de statistiques
        stats_text = f'Moyenne: {mean_val:.2f}\nMédiane: {medians[col]:.2f}\nÉcart-type: {std_val:.2f}'
        plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', 
                         alpha=0.9, edgecolor=GRIS_BLUE_PALETTE['accent_teal']))
        
        plt.tight_layout()
        plt.savefig(f"{PLOT_PATH}/hist_{col}.png", dpi=150, 
                   facecolor='white', edgecolor='none')
        plt.close()

print("Histogrammes générés avec la palette Gris Blue")

# Boxplots avec la palette Gris Blue
for idx, col in enumerate(df.columns):
    if pd.api.types.is_numeric_dtype(df[col]):
        plt.figure(figsize=(10, 6))
        
        # Créer le boxplot avec nos couleurs
        boxprops = dict(linestyle='-', linewidth=2, color=GRIS_BLUE_PALETTE['midnight_blue'])
        medianprops = dict(linestyle='-', linewidth=3, color=GRIS_BLUE_PALETTE['accent_teal'])
        whiskerprops = dict(linestyle='-', linewidth=2, color=GRIS_BLUE_PALETTE['steel_blue'])
        capprops = dict(linestyle='-', linewidth=2, color=GRIS_BLUE_PALETTE['steel_blue'])
        meanprops = dict(marker='D', markeredgecolor=GRIS_BLUE_PALETTE['accent_teal'], 
                        markerfacecolor=GRIS_BLUE_PALETTE['accent_teal'], markersize=8)
        
        box = plt.boxplot(df[col], showmeans=True, vert=False, patch_artist=True,
                         boxprops=boxprops, medianprops=medianprops,
                         whiskerprops=whiskerprops, capprops=capprops,
                         meanprops=meanprops, flierprops=dict(marker='o', 
                         markeredgecolor=GRIS_BLUE_PALETTE['light_steel'], alpha=0.7))
        
        # Colorer la boîte avec une couleur de la palette
        box['boxes'][0].set_facecolor(GRIS_BLUE_PALETTE['slate_gray'])
        box['boxes'][0].set_alpha(0.6)
        
        # Ajouter des annotations pour les outliers
        stats = box['fliers'][0].get_ydata()
        if len(stats) > 0:
            outlier_text = f'{len(stats)} valeur(s) extrême(s)'
            plt.text(0.98, 0.02, outlier_text, transform=plt.gca().transAxes,
                    fontsize=10, horizontalalignment='right',
                    bbox=dict(boxstyle='round', facecolor='white', 
                             alpha=0.9, edgecolor=GRIS_BLUE_PALETTE['accent_coral']))
        
        plt.title(f"Boxplot de {col}", fontsize=16, fontweight='bold', 
                 color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
        plt.xlabel(col, fontsize=14, fontweight='semibold')
        
        # Améliorer les ticks
        plt.yticks([])  # Supprimer le tick y car c'est un seul boxplot
        plt.xticks(fontsize=12)
        
        # Ajouter une grille subtile
        plt.grid(True, alpha=0.3, linestyle='--', axis='x')
        
        # Ajouter une légende des éléments du boxplot
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color=GRIS_BLUE_PALETTE['slate_gray'], lw=8, label='IQR (50% des données)'),
            Line2D([0], [0], color=GRIS_BLUE_PALETTE['accent_teal'], lw=3, label='Médiane'),
            Line2D([0], [0], marker='D', color='w', label='Moyenne',
                  markerfacecolor=GRIS_BLUE_PALETTE['accent_teal'], markersize=10),
            Line2D([0], [0], color=GRIS_BLUE_PALETTE['steel_blue'], lw=2, label='Moustaches')
        ]
        legend = plt.legend(handles=legend_elements, loc='upper right', fontsize=10, 
                  framealpha=0.9, edgecolor=GRIS_BLUE_PALETTE['silver'])
        legend.get_frame().set_facecolor('white')
        
        plt.tight_layout()
        plt.savefig(f"{PLOT_PATH}/boxplot_{col}.png", dpi=150, 
                   facecolor='white', edgecolor='none')
        plt.close()

print("Boxplots générés avec la palette Gris Blue")

# Graphique supplémentaire : Matrice de corrélation (si plusieurs variables numériques)
if len(numeric_cols) > 1:
    corr_matrix = df[numeric_cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Créer une heatmap avec notre palette personnalisée Gris Blue
    from matplotlib.colors import LinearSegmentedColormap
    
    # Créer un colormap personnalisé basé sur notre palette
    colors_cmap = [GRIS_BLUE_PALETTE['pale_gray'], GRIS_BLUE_PALETTE['steel_blue'], 
                   GRIS_BLUE_PALETTE['accent_teal']]
    cmap = LinearSegmentedColormap.from_list("gris_blue", colors_cmap)
    
    im = ax.imshow(corr_matrix, cmap=cmap, vmin=-1, vmax=1, aspect='auto')
    
    # Ajouter les valeurs dans les cases
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            text_color = 'white' if abs(corr_matrix.iloc[i, j]) > 0.7 else GRIS_BLUE_PALETTE['midnight_blue']
            text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                          ha="center", va="center", 
                          color=text_color,
                          fontsize=11, fontweight='bold')
    
    # Configurer les ticks
    ax.set_xticks(np.arange(len(numeric_cols)))
    ax.set_yticks(np.arange(len(numeric_cols)))
    ax.set_xticklabels(numeric_cols, rotation=45, ha='right', fontsize=11)
    ax.set_yticklabels(numeric_cols, fontsize=11)
    
    # Titre et barre de couleur
    plt.title("Matrice de Corrélation", fontsize=16, fontweight='bold', 
             color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
    cbar = plt.colorbar(im, ax=ax, orientation='vertical', pad=0.02)
    cbar.ax.tick_params(labelsize=10)
    
    plt.tight_layout()
    plt.savefig(f"{PLOT_PATH}/correlation_matrix.png", dpi=150, 
               facecolor='white', edgecolor='none')
    plt.close()
    print("Matrice de corrélation générée")

# Graphique supplémentaire : Distribution cumulée (CDF)
for idx, col in enumerate(df.columns):
    if pd.api.types.is_numeric_dtype(df[col]):
        plt.figure(figsize=(10, 6))
        
        # Trier les données
        sorted_data = np.sort(df[col])
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        
        # Tracer la CDF
        plt.plot(sorted_data, cdf, linewidth=3, color=GRIS_BLUE_PALETTE['accent_blue'], 
                label='Fonction de répartition')
        
        # Ajouter des lignes pour les quartiles
        q25 = np.percentile(df[col], 25)
        q50 = np.percentile(df[col], 50)
        q75 = np.percentile(df[col], 75)
        
        plt.axvline(q25, color=GRIS_BLUE_PALETTE['light_steel'], linestyle='--', 
                   alpha=0.8, label=f'Q1 ({q25:.2f})', linewidth=2)
        plt.axvline(q50, color=GRIS_BLUE_PALETTE['accent_teal'], linestyle='--', 
                   alpha=0.8, label=f'Médiane ({q50:.2f})', linewidth=2.5)
        plt.axvline(q75, color=GRIS_BLUE_PALETTE['steel_blue'], linestyle='--', 
                   alpha=0.8, label=f'Q3 ({q75:.2f})', linewidth=2)
        
        plt.title(f"Distribution Cumulée (CDF) de {col}", fontsize=16, 
                 fontweight='bold', color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
        plt.xlabel(col, fontsize=14, fontweight='semibold')
        plt.ylabel("Probabilité Cumulée", fontsize=14, fontweight='semibold')
        
        # Configurer les axes
        plt.grid(True, alpha=0.3, linestyle='--')
        legend = plt.legend(loc='lower right', fontsize=10, framealpha=0.9, 
                  edgecolor=GRIS_BLUE_PALETTE['silver'])
        legend.get_frame().set_facecolor('white')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        # Ajouter une zone ombrée pour l'IQR
        plt.axvspan(q25, q75, alpha=0.15, color=GRIS_BLUE_PALETTE['slate_gray'], 
                   label='IQR (50% des données)')
        
        plt.tight_layout()
        plt.savefig(f"{PLOT_PATH}/cdf_{col}.png", dpi=150, 
                   facecolor='white', edgecolor='none')
        plt.close()

print("Distributions cumulées (CDF) générées")

# Graphique supplémentaire : Scatter plot matrix (si plusieurs variables)
if len(numeric_cols) > 1:
    fig, axes = plt.subplots(len(numeric_cols), len(numeric_cols), 
                            figsize=(15, 15))
    
    for i, col1 in enumerate(numeric_cols):
        for j, col2 in enumerate(numeric_cols):
            ax = axes[i, j]
            
            # Style de l'axe
            ax.set_facecolor('white')
            for spine in ax.spines.values():
                spine.set_color(GRIS_BLUE_PALETTE['silver'])
            
            if i == j:
                # Diagonal: histogramme
                ax.hist(df[col1], bins=20, alpha=0.7, 
                       color=GRIS_BLUE_PALETTE['steel_blue'], 
                       edgecolor=GRIS_BLUE_PALETTE['midnight_blue'])
                ax.set_title(col1, fontsize=10, fontweight='bold', 
                            color=GRIS_BLUE_PALETTE['midnight_blue'])
                ax.tick_params(colors=GRIS_BLUE_PALETTE['slate_gray'])
            else:
                # Scatter plot
                ax.scatter(df[col2], df[col1], alpha=0.6, s=20,
                          color=GRIS_BLUE_PALETTE['accent_blue'],
                          edgecolor=GRIS_BLUE_PALETTE['midnight_blue'], 
                          linewidth=0.5)
                ax.tick_params(colors=GRIS_BLUE_PALETTE['slate_gray'])
            
            # Configuration des axes
            if i < len(numeric_cols) - 1:
                ax.set_xticklabels([])
            else:
                ax.set_xlabel(col2, fontsize=9, color=GRIS_BLUE_PALETTE['midnight_blue'])
                plt.setp(ax.get_xticklabels(), rotation=45, ha='right', 
                        color=GRIS_BLUE_PALETTE['slate_gray'])
            
            if j > 0:
                ax.set_yticklabels([])
            else:
                ax.set_ylabel(col1, fontsize=9, color=GRIS_BLUE_PALETTE['midnight_blue'])
    
    plt.suptitle("Matrice de Scatter Plots", fontsize=16, fontweight='bold',
                color=GRIS_BLUE_PALETTE['midnight_blue'], y=1.02)
    plt.tight_layout()
    plt.savefig(f"{PLOT_PATH}/scatter_matrix.png", dpi=150, 
               facecolor='white', edgecolor='none')
    plt.close()
    print("Matrice de scatter plots générée")

# Graphique supplémentaire : Diagramme en violon pour chaque variable numérique
for col in numeric_cols:
    plt.figure(figsize=(10, 6))
    
    # Créer un diagramme en violon
    violin_parts = plt.violinplot(df[col], showmeans=False, showmedians=True, 
                                 showextrema=True)
    
    # Personnaliser les couleurs du violon
    for pc in violin_parts['bodies']:
        pc.set_facecolor(GRIS_BLUE_PALETTE['steel_blue'])
        pc.set_alpha(0.6)
        pc.set_edgecolor(GRIS_BLUE_PALETTE['midnight_blue'])
    
    # Personnaliser les médianes et extrema
    violin_parts['cmedians'].set_color(GRIS_BLUE_PALETTE['accent_teal'])
    violin_parts['cmedians'].set_linewidth(2)
    violin_parts['cmins'].set_color(GRIS_BLUE_PALETTE['slate_gray'])
    violin_parts['cmaxes'].set_color(GRIS_BLUE_PALETTE['slate_gray'])
    violin_parts['cbars'].set_color(GRIS_BLUE_PALETTE['slate_gray'])
    
    # Ajouter la moyenne
    mean_val = df[col].mean()
    plt.scatter(1, mean_val, color=GRIS_BLUE_PALETTE['accent_coral'], 
               s=100, zorder=3, label=f'Moyenne: {mean_val:.2f}')
    
    # Titre et labels
    plt.title(f"Diagramme en Violon de {col}", fontsize=16, fontweight='bold', 
             color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
    plt.ylabel(col, fontsize=14, fontweight='semibold')
    plt.xticks([])
    
    # Ajouter une grille subtile
    plt.grid(True, alpha=0.2, axis='y')
    
    # Ajouter une légende
    legend = plt.legend(loc='upper right', fontsize=10, framealpha=0.9,
                       edgecolor=GRIS_BLUE_PALETTE['silver'])
    legend.get_frame().set_facecolor('white')
    
    plt.tight_layout()
    plt.savefig(f"{PLOT_PATH}/violin_{col}.png", dpi=150, 
               facecolor='white', edgecolor='none')
    plt.close()

print("Diagrammes en violon générés")

# Rapport PDF avec tous les graphiques (optionnel)
try:
    from matplotlib.backends.backend_pdf import PdfPages
    
    pdf_path = f"{PLOT_PATH}/descriptive_analysis_report.pdf"
    with PdfPages(pdf_path) as pdf:
        # Page 1: Résumé statistique
        fig, ax = plt.subplots(figsize=(11, 8))
        ax.axis('tight')
        ax.axis('off')
        
        # Créer un tableau des statistiques
        stats_data = []
        for col in numeric_cols:
            stats_data.append([
                col,
                f'{means[col]:.2f}',
                f'{medians[col]:.2f}',
                f'{stds[col]:.2f}',
                f'{df[col].min():.2f}',
                f'{df[col].max():.2f}',
                f'{df[col].isna().sum()}'
            ])
        
        columns = ['Variable', 'Moyenne', 'Médiane', 'Écart-type', 'Min', 'Max', 'NA']
        table = ax.table(cellText=stats_data, colLabels=columns, 
                        cellLoc='center', loc='center',
                        colColours=[GRIS_BLUE_PALETTE['steel_blue']] * len(columns))
        
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        for key, cell in table.get_celld().items():
            if key[0] == 0:  # En-tête
                cell.set_text_props(weight='bold', color='white')
                cell.set_edgecolor(GRIS_BLUE_PALETTE['midnight_blue'])
                cell.set_facecolor(GRIS_BLUE_PALETTE['steel_blue'])
            else:
                cell.set_edgecolor(GRIS_BLUE_PALETTE['silver'])
                cell.set_facecolor('white')
                cell.get_text().set_color(GRIS_BLUE_PALETTE['midnight_blue'])
        table.scale(1, 1.5)
        
        plt.title("Résumé Statistique des Variables Numériques", 
                 fontsize=16, fontweight='bold', 
                 color=GRIS_BLUE_PALETTE['midnight_blue'], pad=20)
        
        pdf.savefig(fig, facecolor='white')
        plt.close()
        
        print(f"Rapport PDF généré : {pdf_path}")
        
except ImportError:
    print("Module PdfPages non disponible - Rapport PDF non généré")

print("\nAnalyse descriptive terminée avec succès.")
print(f"Tous les graphiques sont sauvegardés dans : {PLOT_PATH}/")

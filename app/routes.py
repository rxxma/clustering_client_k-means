import pandas as pd
from flask import Blueprint, render_template, send_from_directory, current_app
import os 

main = Blueprint("main", __name__)

@main.route('/favicon.ico')
def favicon():
    # Serve the svg favicon when browsers request /favicon.ico
    return send_from_directory(current_app.static_folder, 'favicon.svg', mimetype='image/svg+xml')

@main.route("/")
def index():
    return render_template("index.html")


# Page 1 — Statistiques descriptives
@main.route("/stats")
def stats():
    # Dossier physique des images
    images_dir = os.path.join("static", "plots", "st")

    # Construire la liste des chemins pour url_for('static', filename=...)
    image_files = [
        f"plots/st/{f}"
        for f in os.listdir(images_dir)
        if f.endswith(".png")
    ]

    return render_template(
        "stats.html",
        image_files=image_files
    )


# Page 2 — Clusters 
@main.route("/clusters")
def clusters():
    # Dossier physique des images
    images_dir = os.path.join("static", "plots", "res")
    image_files = [
        f"plots/res/{f}"
        for f in os.listdir(images_dir)
        if f.endswith(".png")
    ]

    return render_template(
        "clusters.html",
        image_files=image_files
    )


#  Page 3 — Synthèse par cluster
@main.route("/summary")
def summary():
    """
    Affiche le tableau de synthèse par cluster
    """
    summary_df = pd.read_csv("analysis/outputs/cluster_summary.csv")

    return render_template(
        "summary.html",
        tables=summary_df.to_dict(orient="records"),
        columns=summary_df.columns
    )

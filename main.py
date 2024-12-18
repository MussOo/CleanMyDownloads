import os
import shutil


dossier_telechargements = os.path.expanduser("~/Téléchargements")

# Les Categories
categories = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Vidéos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audios": [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Exécutables": [".exe", ".msi", ".bat"],
    "Autres": [] # le reste
}


def organiser_fichiers():
    # Parcours des fichiers dans le dossier Téléchargements
    for fichier in os.listdir(dossier_telechargements):
        chemin_fichier = os.path.join(dossier_telechargements, fichier)

        # Ignorer les dossiers
        if os.path.isdir(chemin_fichier):
            continue

        # Identifier la catégorie du fichier
        _, extension = os.path.splitext(fichier)
        extension = extension.lower()  # Normalisation des extensions
        categorie_trouvee = False

        for categorie, extensions in categories.items():
            if extension in extensions:
                # Déplacer le fichier dans le sous-dossier correspondant
                sous_dossier = os.path.join(dossier_telechargements, categorie)
                os.makedirs(sous_dossier, exist_ok=True)  # Créer le dossier si nécessaire
                shutil.move(chemin_fichier, os.path.join(sous_dossier, fichier))
                print(f"Déplacé : {fichier} -> {sous_dossier}")
                categorie_trouvee = True
                break

        # Si aucune catégorie ne correspond, déplacer dans "Autres"
        if not categorie_trouvee:
            sous_dossier = os.path.join(dossier_telechargements, "Autres")
            os.makedirs(sous_dossier, exist_ok=True)
            shutil.move(chemin_fichier, os.path.join(sous_dossier, fichier))
            print(f"Déplacé : {fichier} -> {sous_dossier}")

if __name__ == "__main__":
    organiser_fichiers()
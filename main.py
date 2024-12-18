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


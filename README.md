# CleanMyDownloads

CleanMyDownloads est un script Python qui automatise l'organisation des fichiers dans votre dossier "Téléchargements" en les triant automatiquement par type de fichier. Il vous permet de garder vos fichiers organisés et de gagner du temps.

---

## 🚀 Fonctionnalités

- Parcourt automatiquement votre dossier **Téléchargements**.
- Trie les fichiers en fonction de leurs extensions dans des sous-dossiers correspondants :
  - `PDF` pour les fichiers `.pdf`
  - `Images` pour les fichiers `.jpg`, `.jpeg`, `.png`, etc.
  - `Archives` pour les fichiers `.zip`, `.rar`, etc.
  - Et bien d'autres catégories.
- Crée automatiquement les sous-dossiers si nécessaire.
- Place les fichiers non classifiables dans un dossier `Autres`.
- Peut être automatisé pour une exécution quotidienne avec le **Planificateur de tâches Windows**.

---

## 🛠️ Technologies Utilisées

- **Langage :** Python 3
- **Modules principaux :**
  - `os` pour la gestion des fichiers et dossiers.
  - `shutil` pour déplacer les fichiers.
- **Automatisation :** Planificateur de tâches Windows.

---

## 📂 Structure des Dossiers

Voici un exemple de structure après l'exécution du script :

```plaintext
Téléchargements/
├── PDF/
│   └── document.pdf
├── Images/
│   ├── photo.jpg
│   └── capture.png
├── Archives/
│   └── archive.zip
├── Exécutables/
│   └── programme.exe
├── Autres/
│   └── fichier_inconnu.xyz
```

---

## 📋 Installation et Configuration

### 1. Cloner le Projet

```bash
git clone https://github.com/MussOo/CleanMyDownloads.git
cd CleanMyDownloads
```

### 2. Installer Python

Assurez-vous d'avoir Python 3 installé. Vous pouvez le télécharger depuis [python.org](https://www.python.org/).

### 3. Configurer le Script

Modifiez le chemin du dossier "Téléchargements" dans le script si nécessaire :

```python
# Chemin du dossier Téléchargements
dossier_telechargements = os.path.expanduser("~\Downloads")
```

### 4. Exécuter le Script

Lancez le script pour trier vos fichiers :

```bash
python main.py
```

### 5. Automatisation (Facultatif)

Configurez le **Planificateur de tâches Windows** pour exécuter le script quotidiennement :

- Ouvrez le Planificateur de tâches.
- Créez une nouvelle tâche et configurez-la pour exécuter Python avec le chemin du script comme argument.

---

## 🌟 Idées Futures

- Ajouter une interface graphique pour configurer facilement les paramètres.
- Intégrer des notifications pour afficher les fichiers triés.
- Étendre la compatibilité à Linux et macOS.

---

## ✨ Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

---

## 📝 Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

# 🆔 ID Compare 4 Fields (Batch)

Ce projet permet de comparer automatiquement les informations extraites d'une **carte d'identité** (via OCR) avec celles enregistrées dans un fichier **Excel**.  
Il vérifie 4 champs essentiels :

- N° d’identité  
- Date de naissance  
- Nom  
- Prénom  

Le résultat est un **rapport CSV** avec un score de similarité et des colonnes indiquant si les données correspondent ou non.

---

## ✨ Fonctionnalités
- 📸 OCR avec **Tesseract + OpenCV**  
- 🧹 Normalisation des textes (noms, prénoms, dates)  
- 🔎 Comparaison **exacte** et **fuzzy** (similarité avec RapidFuzz)  
- 📊 Résultat clair sous forme de tableau CSV avec score de 0–100  
- 📓 Notebook Jupyter prêt à l’emploi  

---

## 🚀 Comment exécuter
### 1. Installation
```bash
# Avec pip
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

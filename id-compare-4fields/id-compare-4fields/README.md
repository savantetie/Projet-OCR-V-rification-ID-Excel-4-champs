# ID Compare · 4 Fields (Batch)

Comparer automatiquement **N° d'identité**, **Date de naissance**, **Nom**, **Prénom**
extraits d’images (OCR) avec un registre Excel.

[![CI](https://img.shields.io/github/actions/workflow/status/USER/id-compare-4fields/ci.yml?branch=main)](https://github.com/USER/id-compare-4fields/actions)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/id-compare-4fields/blob/main/notebooks/id_compare_4fields_batch.ipynb)

## ✨ Fonctionnalités
- OCR (Tesseract) + pré-traitement OpenCV
- Normalisation (dates, accents, casse)
- Appariement exact/fuzzy (ratio de similarité)
- Rapport batch (CSV) avec score et colonnes “OK/KO”
- Notebook prêt à l’emploi + fonctions réutilisables (`src/id_compare/`)

## 📦 Prise en main rapide
```bash
# Option 1 : pip
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Option 2 : conda
conda env create -f environment.yml
conda activate id-compare
```

Assurez-vous d’avoir **Tesseract** installé (et la langue `fra` si nécessaire).

## ▶️ Exécuter le notebook
1. Ouvrir `notebooks/id_compare_4fields_batch.ipynb`
2. Renseigner les chemins dans la cellule “Paramètres” :
   - `IMAGES_DIR="examples/sample_ids"`
   - `EXCEL_PATH="examples/sample_registry.xlsx"`
3. Lancer toutes les cellules.  
   Un fichier `examples/expected_output.csv` est généré.

## 🔎 Logique (résumé)
1. **OCR** (`src/id_compare/ocr.py`) : OpenCV → grayscale/threshold → Tesseract
2. **Parsing** : extraction des 4 champs via regex/règles
3. **Normalisation** : dates au format ISO, trims/accents, upper
4. **Matching** (`src/id_compare/match.py`) : exact + fuzzy (ratio)
5. **Rapport** : score 0–100 + colonnes booléennes (ID_OK, DOB_OK, NOM_OK, PRENOM_OK)

## 🧪 Tests & CI
```bash
pytest -q
```
Le workflow GitHub Actions vérifie l’installation et exécute un **smoke test**.

## 🗂️ Données d’exemple
- `examples/sample_ids/` : images **anonymisées** (zones sensibles floutées)
- `examples/sample_registry.xlsx` : valeurs fictives conformes RGPD

## 🔐 Vie privée
- **Ne publiez jamais** d’images/pièces réelles non anonymisées.
- Floutez N° d’ID, visage, adresse et toute donnée personnelle.

## 🗺️ Roadmap
- [ ] CLI `id-compare` (batch sans notebook)
- [ ] Support multipays (formats d’ID)
- [ ] Docker + modèle OCR alternatif
- [ ] Publication Zenodo/DOI
- [ ] Tableau de bord Streamlit

## ⚖️ Licence
MIT – voir [LICENSE](LICENSE).

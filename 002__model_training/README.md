# 002__model_training

Ce projet sert a entrainer et exporter les modeles ML utilisés par
`002__model_webapp`.

---

## Structure

```
002__model_training/
├── dataset/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
├── models/
│   ├── LinearReg_Model.pkl
│   ├── ElasticNet_Model.pkl
│   ├── GradientB_Model.pkl
│   ├── AdaBoost_Model.pkl
│   └── feature_names.json
├── main.py
├── model_training.ipynb
├── train_export_models.py
├── utils.py
├── pyproject.toml
└── README.md
```

---

## Roles des fichiers

- `train_export_models.py` : entraine les modeles et exporte les fichiers `.pkl`
	ainsi que `feature_names.json`.
- `model_training.ipynb` : notebook d'exploration et d'entrainement.
- `utils.py` : fonctions utilitaires (telechargement des donnees).
- `dataset/` : donnees d'entrainement et de test.
- `models/` : sorties du training consommees par l'application web.

---

## Utilisation (uv)

```bash
uv sync
uv run python train_export_models.py
```

---

## Lien avec le projet web

Le dossier `models/` est lu par `002__model_webapp`.
Assurez-vous que `feature_names.json` est bien present apres l'entrainement.
# 🔬 QSAR-Divinator :  A QSAR Aqueous Solubility Prediction Dashboard

This chemoinformatics repository implements an end-to-end Machine Learning pipeline to predict molecular aqueous solubility log(mol/L) directly from SMILES strings.

## 💡 Project Concept

```text
├── data/
│   └── chembl_data.csv          # Raw molecular dataset from ChEMBL
├── models/
│   └── solubility_rf_model.joblib # Serialized, pre-trained Random Forest model
├── src/
│   ├── __init__.py
│   ├── data.py                  # Ingestion & Bemis-Murcko scaffold calculations
│   ├── features.py              # Feature extraction (Morgan Fingerprints)
│   └── model.py                 # Model training, saving, and loading wrappers
├── tests/
│   ├── __init__.py
│   └── test_features.py         # Automated unit testing suite via pytest
├── main.py                      # Main orchestration pipeline (Train, Split, Evaluate)
├── predict.py                   # Command-Line Interface (CLI) for quick inference
├── app.py                       # Streamlit interactive web dashboard
├── requirements.txt             # Project dependencies
├── run_project.bat              # One-click automation script for Windows
└── run_project.sh               # One-click automation script for Linux/macOS
```
## 🛠️ Features & Built-in Programs

The project architecture is cleanly divided into four production-ready components:
- Full Training Pipeline (main.py): Automates data ingestion, molecular vectorization, rigorous scaffold-based splitting, model training, and performance metrics logging ($R^2$ score and RMSE).
- Fast Predictor CLI (predict.py): A streamlined command-line interface that allows users to instantly pass a single SMILES string into the terminal to fetch its numeric solubility estimation.
- Interactive Web Application (app.py): A responsive dashboard powered by Streamlit. It dynamically renders the 2D chemical structure of the input compound, computes its solubility score, and provides a qualitative classification (highly soluble, moderately soluble, or insoluble).
• Software Engineering Quality Control (tests/): Standardized software validation using pytest to automatically test feature engineering integrity and verify correct error-handling behavior when processing invalid or corrupted chemical structures.

## 🚀 One-Click Executation via 'run_project'

To streamline navigation and eliminate the need to run multiple individual commands in the terminal, the repository includes a centralized interactive launcher script.
- On Windows: Simply double-click the run_project.bat file.
- On Linux / macOS: Run the ./run_project.sh script in your terminal.

This automation tool opens an interactive text menu. By entering a simple number (1 through 5), you can instantly execute any part of the project—whether you want to rerun the full machine learning pipeline, launch the Streamlit web app, test the model with a sample compound, or run the automated unit testing suite.

---
Developed as a professional Chemoinformatics portfolio project.

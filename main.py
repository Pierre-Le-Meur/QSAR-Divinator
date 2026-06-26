import os
import numpy as np
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import r2_score, mean_squared_error

# Importing your local modules from the src/ folder
from src.data import load_data
from src.features import mol_to_fp
from src.model import train_model, save_model

def main():
    print("🚀 Starting QSAR Pipeline...")

    # 1. Load and clean chemical data
    print("[1/5] Loading and cleaning chemical data...")
    df = load_data("data/chembl_data.csv")

    # 2. Convert SMILES molecules to molecular descriptors (Fingerprints)
    print("[2/5] Computing Morgan Fingerprints via RDKit...")
    X = np.array([mol_to_fp(m) for m in df["mol"]])
    y = df["measured log solubility in mols per litre"]
    groups = df["scaffold"].values  # Contains Bemis-Murcko scaffold groups

    # 3. Scaffold Split (GroupShuffleSplit)
    # Ensures 20% of entirely distinct chemical families are kept for testing
    gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    train_idx, test_idx = next(gss.split(X, y, groups=groups))

    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    print(f"👉 Dataset Split - Train size: {len(X_train)} | Test size: {len(X_test)}")

    # 4. Train the Random Forest Regressor
    print("[3/5] Training Random Forest Regressor...")
    model = train_model(X_train, y_train)

    # 5. Save the trained model for deployment (predict.py & app.py)
    print("[4/5] Saving trained model to 'models/' directory...")
    os.makedirs("models", exist_ok=True)
    save_model(model, "models/solubility_rf_model.joblib")

    # 6. Evaluate performance on unseen chemical families
    print("[5/5] Evaluating model performance on test set...")
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    # Output final metrics to terminal
    print("\n📊 --- MODEL PERFORMANCE METRICS ---")
    print(f"R² Score (Coefficient of Determination) : {r2:.4f}")
    print(f"RMSE (Root Mean Squared Error)         : {rmse:.4f}")
    print("-------------------------------------")
    print("✨ Pipeline executed successfully. Model is ready for inference!")

if __name__ == "__main__":
    main()
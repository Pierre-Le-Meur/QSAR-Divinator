import argparse
import sys
from rdkit import Chem
from src.features import mol_to_fp
from src.model import load_model

def main():
    # Setup command line arguments
    parser = argparse.ArgumentParser(description="Predict the aqueous solubility of a molecule.")
    parser.add_argument(
        "--smiles", 
        type=str, 
        required=True, 
        help="The SMILES string of the molecule to test (e.g., 'CC(=O)Oc1ccccc1C(=O)O')"
    )
    args = parser.parse_args()

    # 1. Molecule validation via RDKit
    mol = Chem.MolFromSmiles(args.smiles)
    if mol is None:
        print(f"❌ Error: The provided SMILES string is invalid: '{args.smiles}'")
        sys.exit(1)

    # 2. Extract molecular descriptors
    fp = mol_to_fp(mol)
    X_input = [fp]  # Reshape for the model (expects 2D array)

    # 3. Load the saved model checkpoint
    try:
        model = load_model("models/solubility_rf_model.joblib")
    except FileNotFoundError:
        print("❌ Error: Trained model checkpoint not found in 'models/'.")
        print("👉 Please run 'python main.py' first to train and export the model.")
        sys.exit(1)

    # 4. Perform Inference
    prediction = model.predict(X_input)[0]

    # Display prediction results
    print("\n🔬 --- QSAR PREDICTION RESULT ---")
    print(f"Molecular Structure (SMILES) : {args.smiles}")
    print(f"Estimated Aqueous Solubility : {prediction:.2f} log(mol/L)")
    print("---------------------------------")

if __name__ == "__main__":
    main()
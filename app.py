import os
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# Importing local functions
from src.features import mol_to_fp
from src.model import load_model

# 1. Streamlit web page configuration
st.set_page_config(
    page_title="Chemoinformatics - QSAR Solubility",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 Aqueous Solubility Prediction (QSAR)")
st.write(
    "This web application leverages a Machine Learning model (Random Forest Regressor) "
    "trained using a strict **Scaffold Split** strategy to predict the aqueous solubility of novel compounds."
)

# 2. Load model with caching to optimize performance
@st.cache_resource
def get_model():
    model_path = "models/solubility_rf_model.joblib"
    if os.path.exists(model_path):
        return load_model(model_path)
    return None

model = get_model()

# Error handling if model is missing
if model is None:
    st.error("❌ Trained model checkpoint not found in 'models/'.")
    st.info("👉 Please run `python main.py` in your terminal first to generate and save the model.")
else:
    st.divider()

    # 3. Interactive SMILES input text box (Defaults to Aspirin)
    smiles_input = st.text_input(
        "Enter a molecular SMILES string:", 
        value="CC(=O)Oc1ccccc1C(=O)O"
    )

    if smiles_input:
        # Validate chemical structure with RDKit
        mol = Chem.MolFromSmiles(smiles_input)
        
        if mol is None:
            st.error("❌ Invalid SMILES string. Unable to parse chemical structure.")
        else:
            # 4. Display results in a clean 2-column layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("2D Chemical Structure")
                # Render 2D image of the molecule
                img = Draw.MolToImage(mol, size=(300, 300))
                st.image(img, use_container_width=True)
                
            with col2:
                st.subheader("Model Prediction")
                
                # Featurize molecule and make prediction
                fp = mol_to_fp(mol)
                prediction = model.predict([fp])[0]
                
                # Render clean metric display
                st.metric(label="Estimated Solubility", value=f"{prediction:.2f} log(mol/L)")
                
                # Interpret the predicted value for the end user
                if prediction > 0:
                    st.success("💧 Highly soluble compound in water.")
                elif prediction > -2:
                    st.warning("⚠️ Moderately soluble compound.")
                else:
                    st.error("🚫 Low solubility or practically insoluble compound.")

    st.divider()
    st.caption("Powered by RDKit, Scikit-Learn, and Streamlit.")
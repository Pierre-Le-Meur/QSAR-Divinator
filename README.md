🧪 Overview
QSAR-Divination is a cheminformatics machine learning project that predicts the aqueous solubility of small molecules from their chemical structure.
The goal is to build a full QSAR (Quantitative Structure–Activity Relationship) pipeline using RDKit descriptors and classical machine learning models.

---

🎯 Objective
Given a molecular structure (SMILES format), the model predicts a continuous property:
- Aqueous solubility (logS)
- More to come in the future...
This project demonstrates how molecular structure can be mapped into numerical features for predictive modeling in drug discovery.

---

📊 Dataset
The project uses the ESOL dataset, which contains:
→ SMILES strings of molecules
→ Experimental solubility values (logS)
Each molecule is represented as a data point for regression.

---

⚙️ Methodology
1. Molecular Representation
Molecules are processed using RDKit to generate numerical representations.

2. Feature Engineering
Two main approaches are used:
→ Morgan fingerprints (circular fingerprints)
→ Optional physicochemical descriptors (e.g., molecular weight, LogP)
These transform SMILES into fixed-length feature vectors.

3. Machine Learning Models
Several regression models can be trained and compared, such as:
→ Random Forest Regressor
→ Gradient Boosting / XGBoost
→ Linear Regression (baseline)

4. Evaluation Metrics
Model performance is evaluated using:
→ R² score
→ Root Mean Squared Error (RMSE)
→ Mean Absolute Error (MAE)

--- 

🔁 Workflow
SMILES
  ↓
RDKit processing
  ↓
Molecular fingerprints / descriptors
  ↓
Machine Learning model
  ↓
Predicted solubility (logS)

---

🛠️ Installation
Clone the repository and install dependencies:

git clone https://github.com/<your-username>/QSAR-Divination.git
cd QSAR-Divination
pip install -r requirements.txt

---

🚀 Usage
Run the main pipeline:
python src/model.py
Or explore the data and models in Jupyter notebooks:
jupyter notebook notebooks/



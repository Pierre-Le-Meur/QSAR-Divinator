import pandas as pd
from rdkit import Chem

def load_data(path):
    df["mol"] = df["smiles"].apply(Chem.MolFromSmiles)
    return df

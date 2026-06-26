import pandas as pd
from rdkit import Chem
from rdkit.Chem.Scaffolds import MurckoScaffold

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["smiles", "measured log solubility in mols per litre"])
    
    df["mol"] = df["smiles"].apply(Chem.MolFromSmiles)
    df = df.dropna(subset=["mol"])
    
    scaffolds = []
    for i, mol in enumerate(df["mol"]):
        scaffold_smiles = MurckoScaffold.MurckoScaffoldSmiles(mol=mol)
        
        if scaffold_smiles == "":
            scaffolds.append(f"acyclic_{i}")
        else:
            scaffolds.append(scaffold_smiles)
            
    df["scaffold"] = scaffolds
    return df
from rdkit.Chem import AllChem

def mol_to_fp(mol):
    return list(AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048))

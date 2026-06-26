import numpy as np
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)

def mol_to_fp(mol):
    return list(morgan_gen.GetFingerprint(mol))
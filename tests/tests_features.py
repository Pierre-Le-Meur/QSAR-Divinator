import pytest
import numpy as np
from rdkit import Chem
from src.features import mol_to_fp

def test_mol_to_fp_valid_molecule():
    """
    Test that a valid SMILES string (Ethanol) is correctly transformed 
    into a Morgan Fingerprint vector of length 2048.
    """
    # 1. Arrange: Create a valid RDKit molecule object
    smiles = "CCO"  # Ethanol
    mol = Chem.MolFromSmiles(smiles)
    
    # 2. Act: Generate the fingerprint
    fp = mol_to_fp(mol)
    
    # 3. Assert: Check types and dimensions
    assert fp is not None, "Fingerprint should not be None for a valid molecule"
    assert isinstance(fp, np.ndarray) or isinstance(fp, list), "Fingerprint must be a numpy array or a list"
    assert len(fp) == 2048, f"Fingerprint length should be 2048, got {len(fp)}"
    
    # Check that it contains binary-like data (0s or 1s, or counts)
    assert all(val >= 0 for val in fp), "Fingerprint values must be non-negative"


def test_mol_to_fp_invalid_molecule():
    """
    Test that the feature extraction handles None molecules safely 
    or raises the appropriate error.
    """
    # 1. Arrange: An invalid SMILES yields a None object in RDKit
    invalid_smiles = "C=C=C=C=C=C=C=C=C=C"  # Highly unstable/invalid valence structure or typos
    mol = Chem.MolFromSmiles(invalid_smiles)
    
    # 2. Act & Assert
    # If your src.features.mol_to_fp is expected to fail or return None when mol is None:
    with pytest.raises(AttributeError):
        # This will fail because RDKit's GetMorganFingerprintAsBitVect needs a valid Mol object
        mol_to_fp(mol)
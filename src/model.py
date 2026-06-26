import joblib 
from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, path):
    """Sauvegarde le modèle dans un fichier .joblib"""
    joblib.dump(model, path)

def load_model(path):
    """Charge un modèle depuis un fichier .joblib"""
    return joblib.load(path)
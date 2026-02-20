from pathlib import Path
import pickle
import json

from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor

rootPath = Path(__file__).parent
modelPaths = rootPath.parent / "002__model_training" / "models"

def get_feature_names() -> list:
    """
    Charge les noms de colonnes attendus par les modèles.
    """
    with open(modelPaths / 'feature_names.json', "r") as f:
        feature_names = json.load(f)
        return feature_names

def get_column_mapping() -> dict:
    """
    Mapping entre noms Python et noms du dataset d'entraînement.
    """
    return {
        'age': 'Age',
        'gender_male': 'Gender_Male',
        'annual_revenue': 'Annual Income',
        'marital_status_divorced': 'Marital Status_Divorced',
        'marital_status_single': 'Marital Status_Single',
        'number_dependents': 'Number of Dependents',
        'education_level_high_school': 'Education Level_High School',
        'education_level_masters': "Education Level_Master's",
        'education_level_phd': 'Education Level_PhD',
        'occupation_employed': 'Occupation_Employed',
        'occupation_unemployed': 'Occupation_Unemployed',
        'occupation_unknown': 'Occupation_Unknown',
        'health_score': 'Health Score',
        'location_rural': 'Location_Rural',
        'location_suburban': 'Location_Suburban',
        'policy_type_basic': 'Policy Type_Basic',
        'policy_type_comprehensive': 'Policy Type_Comprehensive',
        'previous_claims': 'Previous Claims',
        'vehicle_age': 'Vehicle Age',
        'insurance_duration': 'Insurance Duration',
        'smoking_status_yes': 'Smoking Status_Yes',
        'exercise_frequency_daily': 'Exercise Frequency_Daily',
        'exercise_frequency_monthly': 'Exercise Frequency_Monthly',
        'exercise_frequency_rarely': 'Exercise Frequency_Rarely',
        'property_type_apartment': 'Property Type_Apartment',
        'property_type_condo': 'Property Type_Condo'
    }

def get_linear_model() -> LinearRegression:
    with open(modelPaths / 'LinearReg_Model.pkl', "rb") as f:
        return pickle.load(f)

def get_elasticnet_model() -> ElasticNet:
    with open(modelPaths / 'ElasticNet_Model.pkl', "rb") as f:
        return pickle.load(f)

def get_boosting_model() -> GradientBoostingRegressor:
    with open(modelPaths / 'GradientB_Model.pkl', "rb") as f:
        return pickle.load(f)

def get_adaboost_model() -> AdaBoostRegressor:
    with open(modelPaths / 'AdaBoost_Model.pkl', "rb") as f:
        return pickle.load(f)
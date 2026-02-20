import streamlit as st
from formulaire import get_forms
import model_helper as models
import pandas as pd

from dataclasses import asdict

st.set_page_config(
    page_title="Prédiction de Prime d'Assurance",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Prédicteur de Prime d'Assurance")
st.markdown("""
Cette application utilise des modèles de machine learning pour estimer
le montant de votre prime d'assurance en fonction de vos caractéristiques personnelles.
""")

LINEAR_REGRESSION = "Régression linéaire"
ELASTIC_NET = "ElasticNet"
GRADIENT_BOOSTING = "Gradient Boosting"
ADABOOST = "AdaBoost"

MODEL_MAPPING = {
    LINEAR_REGRESSION: models.get_linear_model,
    ELASTIC_NET: models.get_elasticnet_model,
    GRADIENT_BOOSTING: models.get_boosting_model,
    ADABOOST: models.get_adaboost_model
}

st.subheader("🤖 Choisissez un modèle de prédiction")
selected_model = st.selectbox(
    "Modèle",
    ["--", LINEAR_REGRESSION, ELASTIC_NET, GRADIENT_BOOSTING, ADABOOST]
)

user_input = get_forms()

ml_data = asdict(user_input.convert_to_mlinput())
mlinput = pd.DataFrame([ml_data])

column_mapping = models.get_column_mapping()
mlinput = mlinput.rename(columns=column_mapping)

feature_names = models.get_feature_names()
mlinput = mlinput[feature_names]

if selected_model != "--":
    model = MODEL_MAPPING[selected_model]()
    prediction_value = model.predict(mlinput)[0]

    st.success(f"### 💰 Prédiction : {prediction_value:.2f} $")

    st.info(f"""
    **Modèle utilisé** : {selected_model}

    Le montant estimé de votre prime d'assurance est de **{prediction_value:.2f} $**.
    """)

st.markdown("---")
if st.checkbox("📊 Comparer tous les modèles"):
    st.subheader("Comparaison des prédictions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🔹 Régression Linéaire",
            value=f"{models.get_linear_model().predict(mlinput)[0]:.2f} $"
        )

    with col2:
        st.metric(
            label="🔹 ElasticNet",
            value=f"{models.get_elasticnet_model().predict(mlinput)[0]:.2f} $"
        )

    with col3:
        st.metric(
            label="🔹 Gradient Boosting",
            value=f"{models.get_boosting_model().predict(mlinput)[0]:.2f} $"
        )

    with col4:
        st.metric(
            label="🔹 AdaBoost",
            value=f"{models.get_adaboost_model().predict(mlinput)[0]:.2f} $"
        )

    st.info("""
    **💡 Conseil** : Les différences entre modèles montrent l'incertitude de la prédiction.
    Un écart important peut indiquer un profil atypique.
    """)
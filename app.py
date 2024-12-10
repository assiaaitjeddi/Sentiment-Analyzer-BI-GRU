import streamlit as st
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Charger le modèle et le tokenizer
model = load_model('sentiment model.h5')
tokenizer = joblib.load('text_tokenizer.joblib')

# Classes de prédiction et leurs styles
classes = ['angry', 'fear', 'happy', 'neutral', 'sad', 'surprise']
emoji_map = {
    'angry': '😡',
    'fear': '😨',
    'happy': '😊',
    'neutral': '😐',
    'sad': '😢',
    'surprise': '😲'
}
color_map = {
    'angry': '#FF5733',   # Rouge
    'fear': '#8E44AD',    # Violet
    'happy': '#2ECC71',   # Vert
    'neutral': '#BDC3C7', # Gris
    'sad': '#3498DB',     # Bleu
    'surprise': '#F1C40F' # Jaune
}

# Fonction pour prédire le sentiment
def predict_sentiment(text):
    sequences = tokenizer.texts_to_sequences([text])
    X = pad_sequences(sequences, maxlen=100)
    pred = model.predict(X, verbose=0)
    result = classes[pred.argmax()]
    return result

# Interface Streamlit stylisée
st.set_page_config(page_title="Analyse des Sentiments", page_icon="💡", layout="centered")

# En-tête avec style
st.markdown("""
<div style="background-color: #4CAF50; padding: 10px; border-radius: 10px; text-align: center;">
    <h1 style="color: white; font-size: 2em;">🌟 Analyse des Sentiments 🌟</h1>
    <p style="color: white; font-size: 1.2em;">Découvrez le sentiment d'un texte en quelques secondes grâce à mon modèle d'apprentissage profond.</p>
</div>
""", unsafe_allow_html=True)

# Champ de texte utilisateur avec un emoji
user_input = st.text_area("📝 Entrez votre texte :", "", height=150, placeholder="Tapez un texte ici...")

# Bouton stylisé pour effectuer la prédiction
if st.button("🚀 Prédire le Sentiment"):
    if user_input.strip():
        sentiment = predict_sentiment(user_input)
        emoji = emoji_map[sentiment]
        color = color_map[sentiment]
        st.markdown(f"""
        <div style="background-color: {color}; padding: 15px; border-radius: 10px; text-align: center;">
            <h2 style="color: white;">{emoji} Le sentiment prédit est : <b>{sentiment.capitalize()}</b></h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Veuillez entrer un texte pour effectuer une prédiction.")

# Footer avec informations supplémentaires
st.markdown("""
<hr>
<div style="text-align: center; font-size: 0.9em;">
    <p>📊 Application développée par AIT JEDDI Assia</p>
    <p>✨ Modèle basé sur LSTM pour l'analyse des sentiments.</p>
</div>
""", unsafe_allow_html=True)

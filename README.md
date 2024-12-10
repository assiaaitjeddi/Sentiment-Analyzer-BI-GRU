<h1>🧠 Sentiment Analysis with Neural Networks</h1>

<h2>📌 Description</h2>
<p>
Ce projet utilise des <b>modèles de réseaux de neurones séquentiels</b> tels que <b>RNN</b>, <b>LSTM</b>, et <b>GRU</b> pour effectuer une <b>analyse des sentiments</b>.  
L'objectif est de classer les textes en différentes émotions, notamment :  
</p>
<ul>
  <li>😡 <b>Colère (Angry)</b></li>
  <li>😨 <b>Peur (Fear)</b></li>
  <li>😄 <b>Joie (Happy)</b></li>
  <li>😢 <b>Tristesse (Sad)</b></li>
  <li>😲 <b>Surprise (Surprise)</b></li>
  <li>😐 <b>Neutre (Neutral)</b></li>
</ul>
<p>
Les données proviennent du dataset <a href="https://www.kaggle.com/datasets/mathurinache/goemotions">GoEmotions</a>, un jeu de données riche pour l'analyse des émotions.  
Une interface utilisateur a été créée avec <b>Streamlit</b> pour tester le modèle en temps réel.
</p>

---

<h2>🚀 Fonctionnalités</h2>
<ul>
  <li>🧪 <b>Classification des textes</b> en six émotions principales.</li>
  <li>🧠 Entraînement de modèle avancé : <b>LSTM</b>.</li>
  <li>🔄 <b>Prétraitement des données</b> :
    <ul>
      <li>Suppression des stopwords.</li>
      <li>Lemmatization des textes.</li>
      <li>Nettoyage et tokenization.</li>
    </ul>
  </li>
  <li>⚙️ Gestion des données déséquilibrées grâce à l’<b>upsampling</b>.</li>
  <li>🌐 Interface interactive développée avec <b>Streamlit</b>.</li>
</ul>

---

<h2>📂 Technologies utilisées</h2>
<p>Voici les principales bibliothèques et frameworks utilisés dans ce projet :</p>
<ul>
  <li><b>Python 3.8+</b></li>
  <li><a href="https://streamlit.io/">Streamlit</a> - Pour l'interface utilisateur.</li>
  <li><a href="https://www.tensorflow.org/">TensorFlow/Keras</a> - Pour les modèles de réseaux de neurones.</li>
  <li><a href="https://pandas.pydata.org/">Pandas</a> - Manipulation des données.</li>
  <li><a href="https://numpy.org/">NumPy</a> - Calculs numériques.</li>
  <li><a href="https://plotly.com/python/">Matplotlib & Plotly</a> - Visualisation des résultats.</li>
  <li><a href="https://www.nltk.org/">NLTK</a> - Prétraitement du texte.</li>
  <li><a href="https://scikit-learn.org/">Sklearn</a> - Préparation des données et encodage des labels.</li>
</ul>

---


<h2>📊 Résultats & Visualisations</h2>
<h3>Exemple d'interface utilisateur :</h3>
<img src="images/image.png" alt="Capture d'écran de l'interface" width="600"/><br>
<img src="images/image1.png" alt="Capture d'écran de l'interface" width="600"/>

---

<h2>🧪 Dataset utilisé</h2>
<p>Les données utilisées dans ce projet proviennent de <a href="https://www.kaggle.com/datasets/mathurinache/goemotions">GoEmotions</a>.</p>


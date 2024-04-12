import streamlit as st
import pickle
import time
import sklearn



st.title("Twitter Sentiment Analysis")

model = pickle.load(open('twitter_sentiment_v4.pkl','rb'))

tweet = st.text_input('Enter Tweet')

submit = st.button('Predict Sentiment')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()

    st.write('Prediction time :',round(end-start,2),' seconds')

    if prediction[0] == 'Positive':
        st.write("Predicted sentiment is :", prediction[0], "\U0001F603")

    elif prediction[0] == 'Negative':
        st.write("Predicted sentiment is :", prediction[0], "\U0001F614")

    elif prediction[0] == 'Neutral':
        st.write("Predicted sentiment is :", prediction[0], "\U0001F610")

    else:
        st.write("Predicted sentiment is :", prediction[0], "\U0001F937")

    print(prediction[0])

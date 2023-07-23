import json
import numpy as np
from tensorflow import keras
import colorama
colorama.init()
from colorama import Fore, Style,
import pickle

with open("intents.json") as file:
    data = json.load(file)

def chat():
    model = keras.models.load_model('chat_model')

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open('label_ecoder.pickle', 'rb') as ecn:
        lbl_encoder = pickle.load(ecn)
    max_len = 20

    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end='')
        inp = input()
        if inp.lower() == 'quit':
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen = max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "ChatBot: " + Style.RESET_ALL, np.random.choice(i['responses']))

print(Fore.YELLOW+"Start messaging with the bot (type quit to stop)!"+Style.RESET_ALL)
chat()

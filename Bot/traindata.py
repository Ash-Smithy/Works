import random
import json
import pickle
import numpy as np
from tensorflow import keras


import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())
words = []
classes = []
documents = []
ignore_letters = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words)) #to remove duplicates and sort

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl','wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    #To check if word occurs in the pattern
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

#shuffling
random.shuffle(training)
#training lists to train the neural network
training = np.array(training) 

#splitting the list
train_x = list(training[:,0])
train_y = list(training[:,1])

#Building the model
model = keras.models.Sequential()
model.add(keras.layers.Dense(128, input_shape=(len(train_x[0]),),activation='relu')) #input layer
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(len(train_y[0]), activation='softmax'))

sgd = keras.optimizers.SGD(learning_rate=0.01, weight_decay= 1e-6, momentum=0.9, nesterov=True)
model.compile(loss= 'categorical_crossentropy', optimizer=sgd, metrics= ['accuracy'])

hist = model.fit(np.array(train_x),np.array(train_y),epochs=200, batch_size=5,verbose=1)
model.save('chatbotmodel.h5', hist)
print("done")
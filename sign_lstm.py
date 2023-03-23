from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,Dropout
from tensorflow.keras.callbacks import TensorBoard
import tensorflow as tf
import cv2
import os
import numpy as np
from make_folders import actions,no_sequences,sequence_length,DATA_PATH
# log_dir = os.path.join('Logs')
# tb_callback = TensorBoard(log_dir=log_dir)
# label_map = {label:num for num, label in enumerate(actions)}
# print(label_map)
# sequences, labels = [], []
# for action in actions:
#     for sequence in range(no_sequences):
#         window = []
#         for frame_num in range(sequence_length):
#             res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
#             window.append(res)
#         sequences.append(window)
#         labels.append(label_map[action])
#
#
# X = np.array(sequences)
# y = to_categorical(labels).astype(int)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)
# print(X_train.shape,X_test.shape)
# print(y_train.shape,y_test.shape)
model = Sequential()
model.add(LSTM(128, return_sequences=True, activation='relu', input_shape=(100,1662,2)))
model.add(LSTM(256, return_sequences=True, activation='relu'))
model.add(LSTM(128, return_sequences=False, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
#model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001), loss='categorical_crossentropy', metrics=['categorical_accuracy'])
print(model.summary())
# model.fit(X_train, y_train, epochs=100)
# print(model.summary())

# res=model.predict(X_test)
#
# print(actions[np.argmax(res[0])],"vs")
#
# print(actions[np.argmax(y_test[0])])
#
#
# model.save('keras_lstm.h5')

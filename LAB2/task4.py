from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import tensorflow as tf

class Task4Manager:

    @staticmethod
    def create_and_learn_model(root_folder):
        input_shape = (28, 28, 1)
        num_classes = 10

        def scheduler(epoch, lr):
            if epoch < 5:
                return lr
            else:
                return lr * tf.math.exp(-0.1)

        model = Sequential()
        model.add(Flatten(input_shape=input_shape))

        model.add(Dense(256, activation='relu'))
        model.add(Dense(128, activation='tanh'))
        model.add(Dense(64, activation='sigmoid'))
        model.add(Dropout(0.5))

        model.add(Dense(num_classes, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2(0.01))) # Exit Layer

        callback = tf.keras.callbacks.LearningRateScheduler(scheduler)

        model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Task_4 Model Summary:\n")

        model.summary()

        datagen = ImageDataGenerator(
            rescale=1./255,
            validation_split=0.05
        )

        train_generator = datagen.flow_from_directory(
            r'%s' %root_folder,
            target_size=(28, 28),
            color_mode='grayscale',
            batch_size=32,
            class_mode='sparse',
            subset="training"
        )

        test_generator = datagen.flow_from_directory(
            r'%s' %root_folder,
            target_size=(28, 28),
            color_mode='grayscale',
            batch_size=32,
            class_mode='sparse',
            subset="validation"
        )

        model.fit(train_generator, epochs=10, callbacks=[callback])
        loss, accuracy = model.evaluate(test_generator)
        print(f'Task_4 accuracy: {accuracy:.4f}')    
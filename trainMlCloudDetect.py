import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Dropout, MaxPooling2D

# Define where the images are. Two sub-dirs are Clear and Cloudy (note caps)
dataDir='/home/stellarmate/allskyimages'

datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
train_generator = datagen.flow_from_directory(
        dataDir,
        target_size=(224, 224),
        batch_size=32,
        shuffle=True,
        class_mode='categorical')
test_generator = datagen.flow_from_directory(
        dataDir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical')

model1 = Sequential()
model1.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(100,100,3)))
model1.add(Conv2D(32, (3, 3), activation='relu'))
model1.add(MaxPooling2D(pool_size=(2, 2)))
model1.add(Conv2D(64, (3, 3), activation='relu'))
model1.add(Dropout(0.25))
model1.add(Flatten())
model1.add(Dense(128, activation='relu'))
model1.add(Dropout(0.5))
model1.add(Dense(4, activation='softmax'))
model1.compile(loss=tf.keras.losses.categorical_crossentropy,
              optimizer=tf.keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model1.fit(train_generator, epochs=2)
model1.evaluate(test_generator)

model1.save("mlCloudDetect.keras")

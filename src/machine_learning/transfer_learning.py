import matplotlib.pyplot as plt
import tensorflow as tf

if __name__ == '__main__':
    testing_mp3_file_name = tf.keras.utils.get_file('../data/raw-audio/5_19.mp3')

    print(testing_mp3_file_name)

    _ = plt.plot(testing_mp3_file_name)

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1024), dtype=tf.float32, name='input_embedding'),
        tf.keras.layers.Dense(512, activation='relu'),
    ], name="hello_model")

    model.summary()
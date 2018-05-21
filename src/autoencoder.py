import numpy as np
import tensorflow as tf

def encoder(input_layer):

  enc_1 = tf.layers.dense(inputs = input_layer, units = 2)

  enc_2 = tf.layers.dense(inputs = enc_1, units = 1)

  return enc_2

def decoder(input_layer):

  dec_1 = tf.layers.dense(inputs = input_layer, units = 2)

  dec_2 = tf.layers.dense(inputs = dec_1, units = 4)

  return dec_2

X = tf.placeholder("float32", [None, 4])

encoder_op = encoder(X)

decoder_op = decoder(decoder_op)

y_pred = decoder_op

y_true = X

num_steps = 3000
batch_size = 128
lr = 0.001
display_step = 100

loss = tf.reduce_mean(tf.pow(y_true - y_pred, 2))

optimizer = tf.train.AdamOptimizer(lr).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:

  sess.run(init)

  for i in range(1, num_steps + 1):

    batch_x = np.random.rand(128,4)

    _, l = sess.run([optimizer, loss], feed_dict = {X: batch_x})

    if i % display_step == 0 or i == 1:
      print('Step %i: Minibatch Loss: %f' % (i,l))

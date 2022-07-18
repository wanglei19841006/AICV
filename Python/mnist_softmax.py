

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np 
import sys

import tensorflow as tf 
import input_data

mnist = input_data.read_data_sets("Mnist_data/", one_hot=True)

sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)


tf.initialize_all_variables().run()

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	_, loss_val = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y_:batch_ys})
	print(loss_val)

#test trained model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))



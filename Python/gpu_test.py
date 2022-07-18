import tensorflow as tf
'''
# Test tensorflow
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
out = sess.run(hello)
a = tf.constant(10)
b = tf.constant(32)
sess.run(a+b)

# Test that tensorflow supports GPUs
with tf.device('gpu:0'):
    a = tf.constant(10)
    b = tf.constant(32)
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    sess.run(a+b)
'''

#import tensorflow as tf
#CUDA_VISIBLE_DEVICES="3"
a = tf.constant([1.,2.,3.,4.,5.,6.], shape=[2,3], name='a')
b = tf.constant([1.,2.,3.,4.,5.,6.], shape=[3,2], name='b')
c = tf.matmul(a,b)

#with tf.Session(config= tf.ConfigProto(log_device_placement=True)) as sess:
#    print(sess.run(c))
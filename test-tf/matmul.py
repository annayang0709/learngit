import tensorflow as tf
import numpy as nps


a = tf.constant([[[[221.92527771, 198.44966125, 280.75027466, 197.97703552, 247.86460876, 238.38121033, 240.93908691, 242.23928833, 290.53756714, 262.59194946]]],
    [[[259.05166626, 199.91087341, 285.74609375, 196.49412537, 267.81878662, 241.24752808, 255.80618286, 277.16595459, 294.27633667, 283.67721558]]]])

b = tf.constant([[41, 75, 79, 81, 54, 97, 41, 108, 77, 111], [139,190, 223, 186, 183, 244, 138, 268, 230, 263]])
'''
a = tf.constant([[[[1, 2, 2, 4]]]])
b = tf.constant([[3, 2, 1, 5]])

'''


'''

net_out [[[[ 18.30159569  33.48086548  27.72011566  28.56781387  21.04497337
     32.8461647   16.04844284  39.15698624  28.69630623  40.30340195]]]


 [[[ 17.42982674  25.52663422  27.64196777  28.01275253  24.08052254
     29.59262466  17.56949806  35.83520508  24.25045967  33.40745926]]]]
landmarks [[17 27 26 28 23 32 18 38 25 38]
 [17 28 27 28 21 34 17 37 26 37]]


'''
a1 = tf.constant(np.arange(1,13), shape=[2, 2, 3])
b1 = tf.constant(np.arange(13,25), shape=[2, 3, 2])

#sub = tf.square(tf.subtract(tf.cast(b, tf.float32), tf.cast(a, tf.float32)))
#sum = tf.reduce_sum(sub, axis=3)

#euclidean_loss = tf.reduce_mean(tf.reduce_sum(tf.sqrt(tf.subtract(tf.cast(b, tf.float32), tf.cast(a, tf.float32))), axis=3)/2)
#l = tf.log(euclidean_loss)
'''
with tf.Session() as sess:
    _loss, _l= sess.run([euclidean_loss, l])
    print('loss:', _loss)
    print('log', _l)
    #print('_sub:', _sub)
    #print('sum', _sum)
'''
m = tf.matmul(a1, b1)
with tf.Session() as sess:
    r = sess.run(m)
    print(r)
    print()

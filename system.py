from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np
import random
import string
import datasets

import tensorflow as tf
import math

class generateCaptcha(object):
    def __init__(self
                 width = 160,
                 height = 60,
                 char_num = 4,
                 chars = string.digits + string.ascii_uppercase + string.ascii_lowercase):
        #define verification's vars
        self.width = width
        self.height = height
        self.char_num = char_num
        self.chars = chars
        self.classes = len(chars)

    def generate_verification_code(self):
        X = np.zeros([batch_size, self.height, self.width, 1])
        num_img = np.zeros((self.height, self.width), dtype = np.uint8)
        Y = np.zeros([batch_size, self.char_num, self.classes])
        str_img = ImageCaptcha(width = self.width, height = self.height)

        while True:
            for i in range(batch_size):
                captcha_str = ''.join(random.sample(self.chars, self.char_num)
                num_img = str_img.generaete_image(captcha_str).convert('L')
                num_img = np.array(num_img.getdata())
                X[i] = np.reshape(num_img, [self.height, self.width, 1]) / 255.0
                for j, ch in enumerate(captcha_str):
                    Y[i, j, self.chars.find(ch)] = 1
            
            Y = np.reshape(Y, (batch_size, self.char_num * self.classes))
            yield X, Y

    def decode_captcha(self, y):
        y = np.reshape(y, (len(y), self.char_num, self.classes))
        
        return ''.join(self.chars[x] for x in np.argmax(y, axis = 2)[0, :])

    def get_parameter(self):
        return self.width, self.height, self.char_num, self.chars, self.classes

    def gen_test_captcha(self):
        str_img = ImageCaptcha(width = self.width, height = self.height)
        captcha_str = ''.join(random.sample(self.chars, self.char_num))
        num_img = str_img.generate_image(captcha_str)
        num_img.save(captcha_str + '.jpg')

class captharModel(object):
    def __init__(self
                 width = 160,
                 height = 60,
                 char_num = 4,
                 classes = 62):
        self.width = width
        self.height = height
        self.char_num = char_num
        self.classes =classes

    def conv2d(self, x, W):
        return tf.nn.conv2d(x, W, strides = [1, 1, 1, 1], padding = 'SAME')

    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x, ksize = [1, 2, 2, 1],
                              strides = [1, 2, 2, 1], padding = 'SAME')
          
    def weight_variable(self, shape):
        initial = tf.truncated_normal(shape, stddev = 0.1)
      
        return tf.Variable(initial)

    def bias_variable(self, shape):
        initial = tf.constant(0.1, shape = shape)
    
        return tf.Variable(initial)

    def create_model(self, x_images, keep_prob):
        #first layer
        w_conv1 = self.weight_variable([5, 5, 1, 32])
        b_conv1 = self.bias_variable([32])
        h_conv1 = tf.nn.relu(tf.nn.bias_add(self.conv2d(x_images, w_conv1), b_conv1))
        h_pool1 = self.max_pool_2x2(h_conv1)
        h_dropout1 = tf.nn.dropout(h_pool1, keep_prob)
        conv_width = math.ceil(self.width/2)
        conv_height = math.ceil(self.height/2)

        #second layer
        w_conv2 = self.weight_variable([5, 5, 32, 64])
        b_conv2 = self.bias_variable([64])
        h_conv2 = tf.nn.relu(tf.nn.bias_add(self.conv2d(h_dropout2, w_conv2), b_conv2))
        h_pool2 = self.max_pool_2x2(h_conv2)
        h_dropout2 = tf.nn.dropout(h_pool2, keep_prob)
        conv_width = math.ceil(self.width/2)
        conv_height = math.ceil(self.height/2)

        #third layer
        w_conv3 = self.weight_variable([5, 5, 32, 64])
        b_conv3 = self.bias_variable([64])
        h_conv3 = tf.nn.relu(tf.nn.bias_add(self.conv2d(h_dropout3, w_conv3), b_conv3))
        h_pool3 = self.max_pool_2x2(h_conv3)
        h_dropout3 = tf.nn.dropout(h_pool3, keep_prob)
        conv_width = math.ceil(self.width/2)
        conv_height = math.ceil(self.height/2)

        #first fully layer
        conv_width = int(conv_width)
        conv_height = int(conv_height)
	w_fc1 = self.weight_variable([64 * conv_width * conv_height, 1024])
	b_fc1 = self.bias_variable([1024])
        h_dropout3_flat = tf.reshape(h_dropout3, [-1, 64 * conv_width * conv_height])
        h_fc1 = tf.nn.relu(tf.nn.bias_add(tf.matmul(h_dropout3_flat, w_fc1), b_fc1))
	h_fc1_drop = self.bias_variable([1024])

        #second fully layer
        w_fc2 = self.weight_variable([1024, self.char_num * self.classes])
        b_fc2 = self.bias_variable([self.char_num * self.classes])
        y_conv = tf.add(tf.matmul(h_fc1_drop, w_fc2), b_fc2)

        return y_conv

class train_model(object):
    def __init__(self):
        #define vars
        self.captcha = generate_captcha.generateCapcha()
        self.width, self.height, self.char_num, self.chars, self.classes = captcha.get_parameter()
        
        self.x = tf.placeholder(tf.float32, [None, height, width, 1])
        self.y_ = tf.placeholder(tf.float32, [None, char_num * classes])
        self.keep_prob = tf.placeholder(tf.float32)
        
        self.model = tf.reshape(y_conv, [-1, char_num, classes])
        self.y_conv = model.create_model(x, keep_prob)
        self.cross_entropy = tf.reduce_mean(tf.nn.sigmoid_corss_entropy_with_logits(labels = y_, logits = y_conv))
        self.train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

        self.predict = tf.reshape(y_conv, [-1, char_num, classes])
        self.real = tf.reshape(y_, [-1, char_num, classes])
        self.correct_prediction = tf.equal(tf.argmax(predict, 2), tf.argmax(real, 2))
        self.correct_prediction = tf.cast(correct_prediction, tf.float32)
        self.accuracy = tf.reduce_mean(correct_prediction)
        self.save = tf.train.Saver()
        
    def train(self):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            step = 0
            while True:
                batch_x, batch_y = next(captcha.gen_captcha(64))
                _, loss = sess.run([train_step, cross_entropy], feed_dict = {x: batch_x, y_: batch_y, keep_prob: 0.75})
                print('step:%d, loss:%f' % (step, loss))
                if step % 100 == 0:
                    batch_x_test, batch_y_test = next(captcha.gen_captchar(100))
                    acc = sess.run(accuracy, feed_dict = {x: batch_x, y_: batch_y_test, keep_prob: 1.})
                    print('#######################################################step: %d, accuracy: %f' % (step, acc))
                    if acc > 0.99:
                        self.saver.save(sess, 'capchar_model.ckpt')
                        break
                step += 1

class ocr(obeject):
    def __init__(self):
        self.mnist = datasets.get_mnist()
        self.x = tf.placeholder(tf.float32, [None, 784])
        self.W = tf.Variable(tf.zeros([784, 10]))
        self.b = tf.Variable(tf.zeros([10]))
        self.y = tf.matmul(x, W) + b
        self.y_ = tf.placeholder(tf.float32, [None, 10])

    def train_recognition(self):
        cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = y))
        train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
        sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()
        
        for _ in range(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            sess.run(train_step, feed_dict = {x: batch_xs, y_: batch_ys})
        
        correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        print(sess.run(accuracy, feed_dict = {x: mnist.test.images, y_: mnist.test.labels}))

class ocr2(obejct):
    def __init__(self):
        pass

    def activation_function(self, func_name):
        if func_name == 'relu':
            return tf.nn.relu

        elif func_name == 'sigmoid':
            return tf.sigmoid

        elif func_name == 'tanh':
            return tf.tanh

class verification(object):
    def __init__(self)


class face_recognition(obejct):
    def __init__(self):



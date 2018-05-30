from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

def get_mnist():
    return input_data.read_data_sets('MNIST_data', one_hot = True)

def get_cifar10():
    

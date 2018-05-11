# coding:UTF-8
# http://blog.csdn.net/baixiaozhe/article/details/54409966
import numpy as np
import tensorflow as tf
from accurancyTest import getCatData

# 定义weight,随机生成
def weight_variable(shape):
    initial=tf.truncted_normal(shape,stddev=0.1)
    return tf.Variable(initial)
# 定义bias,常量0.1
def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
# 定义卷积移动步长strides[0],[3]的1是默认值,
# 中间两个1代表padding时在x方向运动一步，y方向运动一步，padding采用的方式是SAME
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')


train_x, test_x, train_y, test_y= getCatData()



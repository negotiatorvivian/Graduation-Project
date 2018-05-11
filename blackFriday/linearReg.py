# coding: utf-8
from sklearn import preprocessing
from sklearn import linear_model
import pandas as pd
import numpy as np
import tensorflow as tf

def LinearRegr(train_x, train_y,test_x,test_y):

    # sklearn做回归 --很差
    reg = linear_model.LinearRegression()
    reg.fit(train_x,train_y)
    W = reg.coef_
    b = reg.intercept_
    print("Coefficients of sklearn:W=%s,b=%f" % (W, b))
    test_x_m = np.asmatrix(test_x)
    w =np.asmatrix(W).T
    y = test_x_m *w+b
    print (y[0:20])
    print (test_y[0:20])

    # 用tensorflow做回归 --一样很差
    scaler = preprocessing.StandardScaler().fit(train_x)
    print (scaler.mean_,scaler.scale_)
    x_data_standard = tf.cast(scaler.transform(train_x), tf.float32)

    W = tf.Variable(tf.zeros([7,1]))
    b = tf.Variable(tf.zeros([1,1]))
    y = tf.matmul(x_data_standard,W)+b

    loss = tf.reduce_mean(tf.square(y-train_y.reshape(-1,1)))/2
    optimizer = tf.train.GradientDescentOptimizer(0.05)
    train = optimizer.minimize(loss)

    init = tf.initialize_all_variables()

    sess = tf.Session()
    sess.run(init)
    for step in range(300):
        sess.run(train)
        #if step %10 == 0:
            # print step,sess.run(W).flatten(),sess.run(b).flatten()

    # print "w = %s,b = %s" % (sess.run(W).flatten() / scaler.scale_,sess.run(b).flatten()-np.dot(scaler.mean_/scaler.scale_,sess.run(W)))

    W1 = sess.run(W).flatten() / scaler.scale_
    b1 = sess.run(b).flatten() - np.dot(scaler.mean_ / scaler.scale_, sess.run(W))
    test_x_m = np.asmatrix(test_x)
    w =np.asmatrix(W1).T
    y1 = test_x_m *w+b1
    print (y1[0:20])
    print (test_y[0:20])
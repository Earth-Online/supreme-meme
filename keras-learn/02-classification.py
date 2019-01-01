#coding:utf-8
import numpy as np
np.random.seed(1337) # reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential # 顺序模型
from keras.layers import Dense, Activation # 全连接层 激活层
from keras.optimizers import RMSprop
#import matplotlib.pyplot as plt

# load data
# X shape (60,000 28x28=784), y shape (60,000, )
(X_, Y_),(_X, _Y) = mnist.load_data()

# pre-processing data
# 25s 600 40ms/step
X_ = (X_.reshape(X_.shape[0], -1)/255)[:2000] # 取数据形状[0]=28 使其/255 得到 0~1
Y_ = (np_utils.to_categorical(Y_, num_classes=10))[:2000] # for traning 10个长度

_X = (_X.reshape(_X.shape[0], -1)/255)[:200] 
_Y = (np_utils.to_categorical(_Y, num_classes=10))[:200]  # for test

# ANN
model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax')
])

# choose loss function and optimizing method
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(loss='categorical_crossentropy',optimizer=rmsprop,metrics=['accuracy'],)

# loss 函数 (wx+b)^2

# traning
print("traning ----")
model.fit(X_, Y_, epochs=2, batch_size=32) # 批处理32个数据 大+小=2

# test
print("\ntesting ----")
cost, accuracy = model.evaluate(_X, _Y)
print("test cost:",cost)
print("test accuracy:",accuracy)

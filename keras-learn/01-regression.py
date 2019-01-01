#coding:utf-8
import numpy as np
np.random.seed(1337) # reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# gen data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X) # randomize data
Y = 0.5*X+2 + np.random.normal(0, 0.05, (200,))
# plot data
plt.scatter(X, Y)
plt.show()

X_ , Y_ = X[:160],Y[:160] # for traning
_X , _Y = X[160:],Y[160:] # for test
# ANN
model = Sequential([
    Dense(output_dim=1, input_dim=1),
])
'''model.add'''

# choose loss function and optimizing method
model.compile(loss='mse',optimizer='sgd') # 二次方误差，乱序训练优化
# loss 函数 (wx+b)^2

# traning
print("traning ----")
for step in range(301):
    cost = model.train_on_batch(X_, Y_) # cost 一批数据的loss情况
    if step % 100 == 0:
        print("traning cost: ",cost)
# test
print("\ntesting ----")
cost = model.evaluate(_X, _Y, batch_size=40)
print("test cost:",cost)
W, b = model.layers[0].get_weights()
print("weights=%s\nbiases=%s"%(W,b))

#plotting the prediction
Y_p = model.predict(_X)
plt.scatter(_X, _Y)
plt.plot(_X, Y_p)
plt.show()
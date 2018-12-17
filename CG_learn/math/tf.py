# http://dev.earthonline.tk:9999/?token=710c1ce32c8b7fbce4f3d2eb3cf9fcdad3a37efeba688344

import tensorflow as tf
# 一维向量
# 二维矩阵
with tf.Session():
	tf.constant([1.0, 1.0, 1.0, 1.0])
	np.full(4, 2.0)
	# 向量相加
	output = tf.add(:constant, :constant)
	output = input1 + input2
	result = output.eval()
	# 填充操作
	tf.constant(1.0, shape=[4])
	# 矩阵相加
	''' [1, 2, 3]
		[4, 5, 6]'''
	tf.constant(1.0, shape=[2, 3])
	tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32), (2, 3)))
	# 矩阵相乘
	input_features = tf.constant(np.reshape([1, 0, 0, 1], (1, 4)).astype(np.float32))
	weights = tf.constant(np.random.randn(4, 2).astype(np.float32))
	output = tf.matmul(input_features, weights)
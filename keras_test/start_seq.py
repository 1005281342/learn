import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential(
    [Dense(32, input_shape=(100,)),
     Activation('relu'),
     Dense(10),
     Activation('softmax'),
     ])

# 多分类问题
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# 生成虚拟数据
data = np.random.random((1000, 100))
print(data.shape)
labels = np.random.randint(10, size=(1000, 1))

# 将标签转换为分类的 one-hot 编码
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# 训练模型，以 32 个样本为一个 batch 进行迭代
model.fit(data, one_hot_labels, epochs=10, batch_size=32)

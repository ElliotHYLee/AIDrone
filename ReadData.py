import numpy as np
import pandas as pd
#from sklearn import preprocessing
from sklearn.preprocessing import minmax_scale
def readData():
    data = pd.read_csv('OUTPUT.TXT', sep=" ", header=None)
    data = np.array(data)
    data = data[:, 1:16]
    print data


    print data.shape
    #data = minmax_scale(data, (0, 1))
    gyro = data[:, 0:3]
    acc = data[:, 3:6]
    mag = data[:, 6:9]
    euler = data[:9:12]
    #x = data[:, [0, 10]]
    x = data[:,0:12]
    print x.shape
    print x

    x = minmax_scale(x)



    y = data[:, 12:14]
    print y
    print np.max(y)
    print np.min(y)

    y = minmax_scale(y)



    train_x = x[10:7000, :]
    train_y = y[10:7000, :]
    test_x = x[7001:10001, :]
    test_y = y[7001:10001, :]


    return train_x, train_y, test_x, test_y

from ReadData import *
from Model import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
def train():
    trainX, trainY, testX, testY = readData()

    # Train ==========================
    input_dim = 12
    model = getModel(input_dim)
    model.fit(trainX, trainY, nb_epoch=4000, batch_size=6000, verbose=1,  shuffle=True, validation_split=0.2)

    predict = model.predict(testX)
    testY = minmax_scale(testY, (1213, 1287))
    testY = np.rint(testY)
    predict = minmax_scale(predict, (1213, 1287))
    predict = np.rint(predict)

    rmse = np.sqrt((np.asarray((np.subtract(predict, testY))) ** 2).mean())
    print 'data len: %d rmse=%f' %(len(testY), rmse)

    plt.figure()
    plt.plot(testY, 'r')
    plt.plot(predict, 'b')
    plt.show()

if __name__ == "__main__":
    train()

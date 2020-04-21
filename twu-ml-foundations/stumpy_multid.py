from numpy import *
import requests


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def getdata(url):
    content = requests.get(url).content
    content = content.decode('utf-8')
    content = content.split("\n")
    x = []
    y = []
    # print(content[:-1])
    for line in content[:-1]:  # 最后一个是“ ”
        data = line.split(' ')
        y.append(int(data[-1]))  # 最后一列是+/-1
        x1 = data[1:-1]
        for i in range(len(x1)):
            x1[i] = float(x1[i])
        x.append(x1)
    return array(x), array(y)


def h(x, s, theta):
    if s == 1:
        return sign(x-theta)
    else:
        return -sign(x-theta)


def error(x, y, s, theta, dimension):
    errors = 0
    for i in range(len(x)):
        if y[i] != h(x[i][dimension], s, theta):
            errors += 1
    return errors/len(x)


def stump(url):
    x, y = getdata(url)
    dimensions = len(x[0])
    ss = [-1, 1]
    Ein = 1
    best_s = 1
    best_theta = 0
    best_dim = 0
    for dim in range(dimensions):
        thetas = sort(x[:, dim])
        for theta in thetas:
            for s in ss:
                E = error(x, y, s, theta, dim)
                if E < Ein:
                    Ein = E
                    best_s = s
                    best_theta = theta
                    best_dim = dim
    return Ein, best_s, best_theta, best_dim


def main():
    train_url = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw2_train.dat"
    test_url = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw2_test.dat"
    Ein, s, theta, dim = stump(train_url)
    testx, testy = getdata(test_url)
    Eout = error(testx, testy, s, theta, dim)
    print("Ein is", Ein)
    print("Eout is", Eout)


if __name__ == '__main__':
    main()

from numpy import *


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def data(N, noise):
    x = []
    y = []
    for i in range(N):
        xi = random.uniform(-1, 1)
        prob = random.uniform(0, 1)
        if prob < noise:
            yi = -sign(xi)
        else:
            yi = sign(xi)
        x.append(xi)
        y.append(yi)
    return array(x), array(y)


def h(x, s, theta):
    if s == 1:
        return sign(x-theta)
    else:
        return -sign(x-theta)


def error(x, y, s, theta):
    errors = 0
    for i in range(len(x)):
        if y[i] != h(x[i], s, theta):
            errors += 1
    # print(errors/len(x))
    return errors/len(x)


def computeEout(s, theta):
    if s == 1:
        return 0.5+0.3*(abs(theta)-1)
    else:
        return 0.5-0.3*(abs(theta)-1)


def stump(N, noise):
    x, y = data(N, noise)
    thetas = sort(x)
    ss = [1, -1]
    Ein = 1
    best_s = 1
    best_theta = 0
    for theta in thetas:
        for s in ss:
            E = error(x, y, s, theta)
            if E < Ein:
                Ein = E
                best_s = s
                best_theta = theta
    # index, = where(thetas == best_theta)
    # if index[0] == 0:
    #     best_theta = (-1 + best_theta) / 2
    # else:
    #     best_theta = (thetas[index[0] - 1] + best_theta) / 2
    Eout = computeEout(best_s, best_theta)
    # print(Ein)
    return Ein, Eout


def main():
    times = 5000
    N = 20
    noise = 0.2
    Ein_total = 0
    Eout_total = 0
    for i in range(times):
        Ein, Eout = stump(N, noise)
        Ein_total += Ein
        Eout_total += Eout
    print("Ein is", Ein_total/times)
    print("Eout is", Eout_total/times)


if __name__ == '__main__':
    main()
def h(th0, th1, x):
    return th0 + th1 * x

def diff(alp, yarr, xarr, th0, th1, idx):
    sum = 0.0
    for i, y in enumerate(yarr):
        sum += ((h(th0, th1, xarr[i]) - y) * idx * xarr[i])
    return sum * alp / len(yarr)

def cost(yarr, xarr, th0, th1):
    sum = 0.0
    for i, y in enumerate(yarr):
        sum += (h(th0, th1, xarr[i]) - y) ** 2
    return sum / (2 * len(yarr))

def get_hypothesis(yarr, xarr, epsilon, max_iter):
    alp = 0.01
    th0 = 0.0
    th1 = 1.0

    new_cost = cost(yarr, xarr, th0, th1)
    iter = 0
    while ((new_cost > epsilon) and (iter < max_iter)):
        th0, th1 = th0 - diff(alp, yarr, xarr, th0, th1, 0),\
            th1 - diff(alp, yarr, xarr, th0, th1, 1)
        new_cost = cost(yarr, xarr, th0, th1)
        iter += 1
        print 'iteration ' + str(iter) + ': th0=' \
            + str(th0) + ', th1=' + str(th1) + ', cost=' + str(new_cost)
    return th0, th1

if __name__ == "__main__":
    xarr = [1,2,3,4,5,6,7,8,9,10]
    yarr = [2,4,6,8,10,12,14,16,18,20]

    th0, th1 = get_hypothesis(yarr, xarr, 0.0001, 100)
    print "hypothesis: " + str(th0) + " + x * " + str(th1)




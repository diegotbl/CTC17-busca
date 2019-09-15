from random import uniform, randint
from math import exp, pow

def quad(x, y):
    return (pow(x,2) + pow(y,2))

def J(neightor):
    x = neightor[0]
    y = neightor[1]
    return 4*exp(-quad(x, y)) + exp(-quad(x-5, y-5)) + exp(-quad(x-5, y+5)) + exp(-quad(x+5, y-5)) + exp(-quad(x+5, y+5))

def temperature_schedule(i):
    T_0 = 5.0
    Beta = 0.5
    return T_0/(1+Beta*i)

def random_neighbor(theta):
    k = uniform(-2.5, 2.5)
    l = uniform(-2.5, 2.5)
    return (theta[0]+k, theta[1]+l)


def simulated_annealing(theta):
    i = 0
    maximum = theta
    while True:
        T = temperature_schedule(i)
        if T <= 0.00001:
            if J(maximum) <= J(theta):

                return theta
            return maximum
        neighbor = random_neighbor(theta)
        deltaE = J(neighbor) - J(theta)
        if deltaE > 0.0:
            theta = neighbor
        else:
            r = uniform(0.0, 1.0)
            if r <= exp(deltaE/T):
                theta = neighbor
        i = i+1

if __name__ == "__main__":
    min = 0
    max = 10
    for i in range(min, max):
        x = uniform(-15.0, 15.0)
        y = uniform(-15.0, 15.0)
        theta = (x,y)
        print(theta)
        maximum = simulated_annealing(theta)
        print("{0}, {1}".format(maximum, J(maximum)))
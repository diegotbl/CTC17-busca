from random import uniform, randint
from math import exp
from math import pow

def quad(x, y):
    return (pow(x,2) + pow(y,2))

def J(neightor):
    x = neightor[0]
    y = neightor[1]
    return 4*exp(-quad(x, y)) + exp(-quad(x-5, y-5)) + exp(-quad(x-5, y+5)) + exp(-quad(x+5, y-5)) + exp(-quad(x+5, y+5))

def temperature_schedule(i, option):
    if option == 1:
        T_0 = 5.0
        Beta = 0.05
        return T_0/(1+Beta*i)
    else:
        T_0 = 5
        Beta = 0.01
        return T_0*pow(Beta, i)

def random_neighbor(theta):
    k = randint(1, 4)
    if k == 1:
        return (theta[0]+0.1, theta[1])
    elif k == 2:
        return (theta[0], theta[1]+ 0.1)
    elif k == 3:
        return (theta[0] - 0.1, theta[1])
    else:
        return (theta[0] , theta[1]- 0.1)


def simulated_annealing(theta):
    i = 0
    while True:
        T = temperature_schedule(i, 1)
        #print(T)
        if T <= 0.00001:
            return theta
        neighbor = random_neighbor(theta)

        deltaE = J(neighbor) - J(theta)
        #print(J(neighbor))
        #print(J(theta))
        #print(deltaE)
        #print(neighbor)
        #print(theta)
        if deltaE > 0.0:
            theta = neighbor
        else:
            r = uniform(0.0, 1.0)
            if r <= exp(deltaE/T):
                theta = neighbor
        i = i+1

        #print(theta)


if __name__ == "__main__":
    theta = (-2,4)
    print(simulated_annealing(theta))
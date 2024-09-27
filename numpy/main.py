
import numpy as np
import matplotlib.pyplot as plt
# import scipy.integrate as integrate
# import matplotlib.pyplot as plt
#
# # def cornerFunc(numpyArr):
# #     return np.array([numpyArr[0][0],numpyArr[0][-1],numpyArr[-1][0],numpyArr[-1][-1]]).reshape(2,2)
# #
# # def oddFunc(numpyArr):
# #
# #     return numpyArray[::2,::2]
# # [1, 2], [3, 4],[5,6]]
# # numpyArray = np.array(arr)
# # print(oddFunc(numpyArray))
# # print(cornerFunc(numpyArray))
#
# start= float(input("enter start:"))
# end= float(input("enter end:"))
# points= int(input("enter number of points:"))
# equ=input("enter equation:")
#
# x=np.linspace(start,end,points)
# y=eval(equ)
# print(x)
# print(y)
#
# #
# # plt.plot(x,y)
# # plt.show()
#
# def derivative(x,y):
#     deriv=(y[1:]-y[0:-1])/(x[1:]-x[0:-1])
#     deriva=np.append(deriv,deriv[-1])
#     return deriva
#
# def zeroCrossing(x,y):
#     changingY= y[:-1] * y[1:]
#     changingY = np.append(changingY, changingY[-1])
#     crossingY=y[changingY <= 0]
#     crossingX= x[changingY <= 0]
#     return crossingX,crossingY
#     # plt.plot(x, y)
#     # plt.plot(crossingX, crossingY,'ro')
#     # plt.show()
#
# def minMax(y,x,deriv):
#     changing= deriv[:-1] * deriv[1:]
#     changing = np.append(changing, changing[-1])
#     minMaxDeriv=y[changing <= 0]
#     X= x[changing <= 0]
#     return X,minMaxDeriv
#     # plt.plot(X, minMaxDeriv,'bo')
#
#
# deriv=derivative(x,y)
# f,m=zeroCrossing(x,y)
# l,n=minMax(y,x,deriv)
# plt.plot(x,y)
# plt.plot(f,m,'ro')
# plt.plot(l,n,'bo')
# # plt.show()
#
# # zeroCrossing(x,y)
# der= derivative(x,y)
# print(der)
# #
# plt.plot(x,der)
# # plt.show()
# #
# integ= integrate.cumtrapz(y,x,initial=0)
# plt.plot(x,integ)
# plt.show()
#
# # number = int(input("enter number:"))
# # x=np.arange(number)
# # # x = x[::2]
# # # y=np.array([])
# # while True:
# #     x=x[::2]
# #     x=x[-1::-1]
# #     if len(x)<2:
# #         break
# # print(x)


# def bernouli(p, size):
#     x = np.random.random(size)
#     success= x <= p
#     failure= x>p
#     x[success]=1
#     x[failure]=0
#     return x
#
# print(bernouli(0.3, 5))
#
# def binomial(n,p,size):
#     distr=bernouli(p, (size,n))
#     # row2 = bernouli(p, n)
#     # row3 = bernouli(p, n)
#     #
#     # np.vstack(row1,row2,row3)
#     return np.sum(distr,axis=1)
#
# print(binomial(5,0.3,3))
#
# def poisson(lambd,size):
#     n=1000
#     p=lambd/n
#     return binomial(n, p, size)
#
# print(poisson(8,5))
#
# def uniform(a,b,size):
#     x=np.random.random(size)
#     x=x*(b-a)
#     x=x+3
#     return x
#
# print(uniform(3,20,5))


def bernouli(p, size):
    x = np.random.random(size)
    success= x <= p
    failure= x>p
    x[success]=1
    x[failure]=0
    return x

# print(bernouli(0.3, 5))

def binomial(n,p,size):
    distr=bernouli(p, (size,n))
    # row2 = bernouli(p, n)
    # row3 = bernouli(p, n)
    #
    # np.vstack(row1,row2,row3)
    return np.sum(distr,axis=1)

# print(binomial(5,0.3,3))

def poisson(lambd,size):
    n=1000
    p=lambd/n
    return binomial(n, p, size)

# print(poisson(8,5))

def uniform(a,b,size):
    x=np.random.random(size)
    x=x*(b-a)
    x=x+3
    return x

# print(uniform(3,20,5))

myBernoulliArr = bernoulli(0.3, 1000)
bernouliArr=np.random.binomial(size=1000, n=1, p= 0.3)

myBinomialArr = binomial(5, 0.3, 1000)
binomialArr=np.random.binomial(size=1000, n=5, p= 0.3)

myPoissonArr = poisson(8, 1000)
poissonArr = np.random.poisson(lam=2, size=1000 )

myUniformArr = uniform(3, 20, 1000)
uniformArr= np.random.uniform(low=3, high=20,size=1000)

meanBernoulli= np.mean(bernoulli)
stdBernoulli= np.std(bernoulli)

meanBinomial = np.mean(binomial)
stdBinomial=np.std(binomial)

meanPoisson= np.mean(poisson)
stdPoisson= np.std(poisson)

meanUniform = np.mean(uniform)
stdUniform= np.std(uniform)

# # Plot histograms
# plt.figure(figsize=(12, 8))
#
# plt.subplot(2, 2, 1)
# plt.hist(bernoulliArr, bins=20, color='blue', alpha=0.7)
# # plt.title(f'Bernoulli Distribution\nMean: {meanBernoulli:.2f}, Std: {stdBernoulli:.2f}')
#
# plt.subplot(2, 2, 2)
# plt.hist(binomialArr, bins=20, color='green', alpha=0.7)
# # plt.title(f'Binomial Distribution\nMean: {meanBinomial:.2f}, Std: {stdBinomial:.2f}')
#
# plt.subplot(2, 2, 3)
# plt.hist(poissonArr, bins=20, color='red', alpha=0.7)
# # plt.title(f'Poisson Distribution\nMean: {meanPoisson:.2f}, Std: {stdPoisson:.2f}')
#
# plt.subplot(2, 2, 4)
# plt.hist(uniformArr, bins=20, color='purple', alpha=0.7)
# # plt.title(f'Uniform Distribution\nMean: {meanUniform:.2f}, Std: {stdUniform:.2f}')
#
# plt.tight_layout()
# plt.show()

plt.hist(myBernoulliArr, bins='auto', alpha=0.5, label='My Bernoulli')
plt.hist(bernouliArr, bins='auto', alpha=0.5, label='Numpy Bernoulli')
plt.legend()
plt.show()


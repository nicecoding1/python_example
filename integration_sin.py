import numpy as np 
import matplotlib.pyplot as plt
import math

dx = 0.1
xvals = []
yvals = []

# 적분 근사화 함수 
def integral_approximation(f, a, b): 
    return (b-a)*np.mean(f)

# 적분 f(x) = sin(x)
def f(x): 
    global xvals, yvals
    y = math.sin(x)
    xvals.append(x)
    yvals.append(y)
    return y

# 적분의 범위 정의 
a = 0 
b = 1

# 함수 값 생성 
x_range = np.arange(a, b, dx) 
fx = np.vectorize(f)(x_range)

# 근사 적분 
approx = integral_approximation(fx, a, b) 
print(approx)

plt.plot(xvals, yvals)
plt.fill_between(xvals[:], yvals[:], alpha=0.2)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()
plt.show()  

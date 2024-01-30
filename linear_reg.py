import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([2,5,3,6,4,7,5,8,4,7,2,8,5])
y = np.array([99,60,80,65,60,62,65,59,75,99,55,65,60])

def co_eff(x,y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    
    ss_xy = np.sum(y*x) - n*m_y*m_x
    ss_xx = np.sum(x*x) - n*m_x*m_x
    
    m = ss_xy / ss_xx
    c = m_y - m_x*m
    
    return (c,m)

b = co_eff(x,y)
print(b)

def plot_regression_line(x,y,b):
    
    plt.scatter(x,y,s = 30)
    
    y_pre = b[0] + b[1]*x
    
    plt.plot(x,y_pre)
    
    plt.show()
    plt.xlabel('x')
    plt.ylabel('y')
    
plot_regression_line(x,y,b)



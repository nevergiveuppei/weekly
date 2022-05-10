
# Purpose: use gradient descent mothod to optimize a linera modle solution 
# find b and w in the linear model: y = b + w*x_data 
# loss_function: L = sum_nn((y_data-(b + w*x_data))**2)

import numpy as np
import matplotlib.pyplot as plt

x_data = [338, 333, 328, 207, 226, 25, 179, 60, 208, 606]
y_data = [640, 633, 619, 393, 428, 27, 193, 66, 226, 1591]

# define hyper-parameters
b = -120 # bias
w = -4 # weight
lr = 1 # learning rate
iteration = 100000 # iteration

# store initial values for plotting
b_history = [b]
w_history = [w]

lr_b = 0
lr_w = 0

# iterations
for ii in range(iteration):
    b_grad = 0.0
    w_grad = 0.0
    for nn in range(len(x_data)):
        b_grad = b_grad - 2.0*(y_data[nn]-b-w*x_data[nn])
        w_grad = w_grad - 2.0*(y_data[nn]-b-w*x_data[nn])*x_data[nn]    
    lr_b = lr_b + b_grad**2
    lr_w = lr_w + w_grad**2
    # update hyper-parameters: b and w
    b = b - lr/np.sqrt(lr_b)*b_grad
    w = w - lr/np.sqrt(lr_w)*w_grad
    # store parameters for plotting
    b_history.append(b)
    w_history.append(w)

# contour map plotting
x = np.arange(-200, -100, 1) # bias_axis 
y = np.arange(-5, 5, 0.1) # weight_axis
Z = np.zeros((len(x),len(y)))
X, Y = np.meshgrid(x,y)
for ii in range(len(x)):
    for jj in range(len(y)):
        b = x[ii]
        w = y[jj]
        Z[jj][ii] = 0 
        for nn in range(len(x_data)):
            Z[jj][ii] = Z[jj][ii] + (y_data[nn]-b-w*x_data[nn])**2 # the contour lines of loss function values
        Z[jj][ii] = Z[jj][ii]/len(x_data)
        
plt.contourf(x,y,Z, 50, alpha=0.5, cmap=plt.cm.jet)
plt.plot([-188.4],[2.67], "x", ms=12, markeredgewidth=3, color="orange")
plt.plot(b_history, w_history, "o-", ms=3, lw=1.5, color="black")
plt.xlim(-200,-100)
plt.ylim(-5,5)
plt.xlabel(r"$b$", fontsize=16)
plt.ylabel(r"$w$", fontsize=16)
plt.show()


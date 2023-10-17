import numpy as np
import matplotlib.pyplot as plt

def rumus_sigmoid(x):
    return 1/ (1+np.exp(-x))

# data 
x = np.linspace(-5, 5, 100)
y = rumus_sigmoid(x)

plt.plot(x,y)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Sigmoid Activation Function')
plt.grid(True) # ada kotak kotaknya
plt.show()

# Semakin jauh range-nya, semakin tegak fungsi aktivasinya
# (yang menuju ke 0 dan 1)
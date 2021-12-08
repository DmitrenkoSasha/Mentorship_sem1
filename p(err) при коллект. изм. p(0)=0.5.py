import numpy as np
import matplotlib.pyplot as plt
    
a = np.arange(0, np.pi/4, 0.05) # Искусственные точки по оси х
A = []
p_Err = []
for i in range(len(a)):
    A= 0.5*np.arccos(np.cos(2*a)**3)
    p_Err = (np.sin(np.pi/4-a)**6+3*(np.sin(np.pi/4-a)**4)*(np.cos(np.pi/4-a))**2)  # Это уже для инд.

#print('min(p_Err) = ', min(p_Err))
                  
plt.plot(a, A, color = 'red', label='$\\alpha$ между $\\Psi(0), \\Psi(1)$')
plt.plot(a, 0.5*np.sin(np.pi/4-A)**2+0.5*np.cos(np.pi/4+A)**2, color = 'blue', label='p(err) ')

plt.xlabel("$\\alpha$, rad")
plt.ylabel('')
plt.legend()
plt.title(r"Зависимость p_err($\alpha$) при коллективном измерении")
plt.show()


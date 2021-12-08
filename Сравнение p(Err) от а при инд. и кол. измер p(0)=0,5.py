import numpy as np
import matplotlib.pyplot as plt
    
a = np.arange(0, np.pi/4, 0.02) # Искусственные точки по оси х
A = []
p_Err = []
for i in range(len(a)):
    A= 0.5*np.arccos(np.cos(2*a)**3)
    p_Err.append(np.sin(np.pi/4-a[i])**6+3*(np.sin(np.pi/4-a[i])**4)*(np.cos(np.pi/4-a[i]))**2)

#print('min(p_Err) = ', max(p_Err))
                  
plt.plot(a, np.sin(np.pi/4-a)**6+3*(np.sin(np.pi/4-a)**4)*(np.cos(np.pi/4-a))**2, color = 'red', label='p(err) при инд. изм. ')
plt.plot(a, 0.5*(np.cos(np.pi/4+A)**2+np.sin(np.pi/4-A)**2), color = 'blue', label='p(err) при коллект. изм. ')

plt.xlabel("$\\alpha$, rad")
plt.ylabel("p_err")
plt.legend()
plt.title(r"Сравнение p_err($\alpha$) при индивидуальных и коллективных измерениях")
plt.show()

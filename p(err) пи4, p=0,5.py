import numpy as np
import matplotlib.pyplot as plt
    
a = np.arange(0, np.pi/2, 0.01) # Искусственные точки по оси х
plt.plot(a, 0.5*(np.cos(np.pi/4+a)**2+np.sin(np.pi/4-a)**2), color = 'red', label='минимум ошибки при угле $\dfrac{\pi}{4}$')

plt.xlabel("alf, rad")
plt.ylabel("p(err)")
plt.legend()
plt.title(r"Зависимость p_err(alf) в одном измерении")
plt.show()

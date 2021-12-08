from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = axes3d.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
i = np.arange(0, np.pi/4, 0.01)
j = np.arange(0, 1/2, 0.00633)
alfa = np.meshgrid(i, i)
p = np.meshgrid(j, j)
beta=[]  # Для коллектив
beta1=[]  # Для индивид
Alpha = []

for i in range(len(alfa)):
        for j in range(len(alfa)):
            Alpha.append(0.5*np.arccos(np.cos(2*alfa[i])**3))
            beta.append(0.5*np.arctan(np.tan(2*Alpha[j+i*len(alfa)])/(-2*p[j]+1)))
            beta1.append(0.5*np.arctan(np.tan(2*alfa[i])/(-2*p[j]+1)))
            ax.plot_wireframe(alfa[i], p[j], beta[j+i*len(alfa)], rstride=10, cstride=10, color = 'blue', label = 'коллект. измерения')
            ax.plot_wireframe(alfa[i], p[j], beta1[j+i*len(alfa)], rstride=10, cstride=10, color = 'red', label = 'инд. измерения')


plt.xlabel("$\\alpha$, rad")
plt.ylabel("p($\psi_0$)")
plt.legend()
plt.title(r"Зависимость beta($\psi_0, \alpha$)")
plt.show()

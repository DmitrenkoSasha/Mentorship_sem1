from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = axes3d.Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
i = np.arange(0, np.pi/4, 0.01)
j = np.arange(0, 1/2, 0.00633)
alpha = np.meshgrid(i, i)
p = np.meshgrid(j, j)
beta=[]# Для коллект. измерения
beta1 = []# Для инд. измерения
p_Err = []
p_Err1 = []
Alpha = []  # Угол м/у Пси0, Пси1

for i in range(2):
    for j in range(2):
        Alpha.append(0.5*np.arccos(np.cos(2*alpha[i])**3))
        beta.append(0.5*np.arctan(np.tan(2*Alpha[j+i*len(alpha)])/(-2*p[j]+1)))  
        beta1.append(0.5*np.arctan(np.tan(2*alpha[i])/(-2*p[j]+1)))  
        p_Err.append((1-p[j])*np.sin(beta[j+len(alpha)*i]-Alpha[j+i*len(alpha)])**2+p[j]*np.cos(beta[j+len(alpha)*i]+Alpha[j+i*len(alpha)])**2)
        p_Err1.append((1-p[j])*np.sin(beta1[j+len(alpha)*i]-alpha[i])**2+p[j]*np.cos(beta1[j+len(alpha)*i]+alpha[i])**2)
        ax.plot_wireframe(alpha[i], p[j], p_Err[j+len(alpha)*i], rstride=10, cstride=10, color = 'blue', label = 'коллект. измерения')
        ax.plot_wireframe(alpha[i], p[j], p_Err1[j+len(alpha)*i], rstride=10, cstride=10, color = 'red', label = 'инд. измерения')

        
plt.xlabel("$\\alpha$, rad")
plt.ylabel("p$(\psi_0)$")
#ax.zlabel("beta, rad")
plt.legend()
plt.title(r"Зависимость p_Err($\psi_0, \alpha$)")
plt.show()

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
beta=[]
p_err = []

for i in range(len(alfa)):
    for j in range(len(alfa)):
        beta.append(0.5*np.arctan(np.tan(2*alfa[i])/(-2*p[j]+1)))
        p_err.append((1-p[j])*np.sin(beta[j+len(alfa)*i]-alfa[i])**2+p[j]*np.cos(beta[j+len(alfa)*i]+alfa[i])**2)
        ax.plot_wireframe(alfa[i], p[j], p_err[j+len(alfa)*i], rstride=10, cstride=10)

plt.xlabel("$\\alpha$, rad")
plt.ylabel("p$(\psi_0)$")
#plt.zlabel("beta, rad")
plt.legend()
plt.title(r"Зависимость p_err($\psi_0, \alpha$)")
plt.show()

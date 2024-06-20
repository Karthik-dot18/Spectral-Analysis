import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

file = open('aspcap_parameters_and_erros_1000.csv', 'r')

data = file.readlines()
l = len(data)
col=[]



for i in range(2,l):

    col.append(data[i].strip().split(","))

ra=[]
dec=[]
teff = []
teff_err = []
logg = []
logg_err = []
m_h = []
m_h_err = []
alpha_m = []
alpha_m_err = []
glon = []
glat = []

for i in range(len(col)):
    ra.append(float(col[i][1]))
    dec.append(float(col[i][2]))
    teff.append(float(col[i][7]))
    teff_err.append(float(col[i][8]))
    logg.append(float(col[i][9]))
    logg_err.append(float(col[i][10]))
    teff_err.append(float(col[i][8]))
    m_h.append(float(col[i][11]))
    m_h_err.append(float(col[i][12]))
    alpha_m.append(float(col[i][13]))
    alpha_m_err.append(float(col[i][14]))
    glon.append(float(col[i][3]))
    glat.append(float(col[i][4]))


#print(len(m_h))


filter_indices = [i for i, mh in enumerate(m_h) if mh >= -1000]

ra = [ra[i] for i in filter_indices]
dec = [dec[i] for i in filter_indices]
teff = [teff[i] for i in filter_indices]
logg = [logg[i] for i in filter_indices]
m_h = [m_h[i] for i in filter_indices]
glon = [glon[i] for i in filter_indices]
glat = [glat[i] for i in filter_indices]
teff_err = [teff_err[i] for i in filter_indices]
logg_err = [logg_err[i] for i in filter_indices]
m_h_err = [m_h_err[i] for i in filter_indices]
alpha_m = [alpha_m[i] for i in filter_indices]
alpha_m_err = [alpha_m_err[i] for i in filter_indices]

for i in range(len(glon)):
    if glon[i] > 180 :
        glon[i] = -360 + glon[i]

'''def get_point_color(metallicity):
    if -0.88 <= metallicity < 0.32:
        return 'blue'  # Color for the range -2.5 to -1 
    elif -1.5 <= metallicity <= 0:
        return 'green'  # Color for the range -1 to 1
    else:
        return 'red'  # Default color for other values'''




def plot_3d_scatter(x, y, z, xlabel, ylabel, zlabel, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    
    
    #colors = [get_point_color(m) for m in z]

    ax.scatter(x, y, z, marker='o',s=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    #ax.legend()
    plt.title(title)
    plt.show()

'''def plot_3d_scatter(x, y, z, xlabel, ylabel, zlabel, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, marker='o')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.title(title)
    plt.show()'''

def plot_2d_scatter(x, y, xlabel, ylabel, title):
    fig = plt.figure()
    #colors = [get_point_color(teff_val) for teff_val in y]
    plt.scatter(x, y, marker='o',s=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.title(title)
    #plt.grid(True)
    plt.show()

print(len(glat))
print(len(glon))
print(len(m_h))

# Plot Teff vs Glat and Glon
#plot_3d_scatter(glat, glon, teff, 'Glat', 'Glon', 'Teff', 'Variation of Teff')

# Plot Metallicity vs Glat and Glon
plot_3d_scatter(glat, glon, m_h, 'Glat', 'Glon', 'Metallicity', 'Variation of Metallicity')

# Plot Teff vs logg
#plot_2d_scatter(logg_err_selected, teff_err_selected, 'Log g', 'Teff', 'Teff vs Log g')

plot_2d_scatter(glat, m_h, 'Glat','metallicity', 'metallicity vs Glat')
plot_2d_scatter(glon, m_h, 'Glon','metallicity', 'metallicity vs Glon')


plt.scatter(glat,m_h,marker='o',s=2)
plt.title("Metallicity vs Glat")
plt.xlabel("Glat")
plt.ylabel("Metallicity")
plt.xlim([-7,17])
plt.show()


file.close()
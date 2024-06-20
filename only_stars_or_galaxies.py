import matplotlib.pyplot as plt

file = open('only_stars_or_galaxies.csv', 'r')

data = file.readlines()
l = len(data)
col=[]

for i in range(2,l):

    col.append(data[i].strip().split(","))

ra=[]
dec=[]
g=[]

for i in range(len(col)):
    ra.append(float(col[i][1]))
    dec.append(float(col[i][2]))
    g.append(float(col[i][3]))

plt.plot(dec,ra,'*')
plt.xlabel('dec')
plt.ylabel('RA')
plt.grid()
plt.title('RA vs dec')
#plt.xlim(15,15.1)
#plt.ylim(185,185.07)
plt.show()

file.close()
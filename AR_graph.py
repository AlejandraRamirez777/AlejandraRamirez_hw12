import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("advection.txt", usecols = 0)
A = np.genfromtxt("advection.txt", usecols = 1)


#plt.plot(x[:160],A[:160], c = "g")
#print x[161]
plt.ylim(-0.5,1)
plt.xlim(-3,3)
plt.title("Progresion de onda en el tiempo")
plt.ylabel("Amplitud")
plt.xlabel("Posicion")


end = np.shape(x)
#print end
a = 0
c = 159

while(c<end[0]):
    
    plt.plot(x[a:c],A[a:c])
    a += 159
    c +=159
    #print c
    

#plt.savefig("ProgressT.png")

#plt.plot(x,A)
plt.show()

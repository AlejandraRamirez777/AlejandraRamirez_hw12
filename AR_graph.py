import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("advection.txt", usecols = 0)
A = np.genfromtxt("advection.txt", usecols = 1)


#plt.plot(x[:157],A[:157], c = "g", label = "Inicial")
#plt.plot(x[158:317], A[158:317],  c = "y", label = "Snapshot 1")
#print x[318]
plt.ylim(0.00,1)
plt.xlim(-2.05,2.05)
plt.title("Progresion de onda en el tiempo")
plt.ylabel("Amplitud")
plt.xlabel("Posicion")



end = np.shape(x)
#print end
a = 0
c = 162
k=1



while(c<end[0]):
    
    if(k == 1):
        plt.plot(x[a:c],A[a:c], label = "Inicial")
        plt.legend(loc = 2)
        a += 159
        c +=159
        k +=1
    
    else:
        plt.plot(x[a:c],A[a:c], label = "Snapshot " + str(k-1))
        plt.legend(loc = 2)
        a += 159
        c +=159
        k +=1
    

plt.savefig("graph.png")

#plt.plot(x,A)
#plt.show()

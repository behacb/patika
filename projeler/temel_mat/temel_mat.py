
#Lineer cebir
import numpy as np
 
# iki diziyi carpma islemi
x = [1, 2, 3]
y = [4, 5, 6]
sonuc = []
for i in range(len(x)):
    sonuc.append(x[i] * y[i])
 
# lineer cebir ile
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print x * y
# sonuc array([ 4, 10, 18])

#Matrislerde toplama
import numpy as np
 
# iki diziyi carpma islemi
x = [1, 2, 3]
y = [4, 5, 6]
sonuc = []
for i in range(len(x)):
    sonuc.append(x[i] * y[i])
 
# lineer cebir ile
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print x * y
# sonuc array([ 4, 10, 18])

#Matrislerde çarpma
import numpy as np
 
y = np.array([1,2,3])
x = np.array([2,3,4])
 
print  y * x
 
# sonuc
# y * x = [2, 6, 12]
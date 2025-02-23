import matplotlib.pyplot as plt
import numpy as np
datos = np.random.randn(30)
plt.hist(datos, bins=30, edgecolor='black', color='skyblue')  # 'bins' define el número de intervalos
plt.title('Histograma de datos aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

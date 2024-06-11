import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV original
df = pd.read_csv('recursos.csv')

# Eliminar la última columna
df = df.iloc[:, :-1]

# Guardar el nuevo archivo CSV sin la última columna
df.to_csv('recursos_corregidos.csv')

# Leer los datos desde el archivo CSV corregido
df = pd.read_csv('recursos_corregidos.csv')

# Convertir la columna 'Tiempo' a formato de fecha y hora
df['Tiempo'] = pd.to_datetime(df['Tiempo'])
# Convertir los tiempos a minutos
df['Tiempo'] = df['Tiempo'].apply(
    lambda x: x.hour * 60 + x.minute + x.second / 60)

# Configurar la gráfica
plt.figure(figsize=(10, 5))

# Graficar el consumo de memoria
plt.plot(df['Tiempo'], df['Memoria(%)'], color='blue', label='Memoria(%)')

# Graficar el uso de CPU
plt.plot(df['Tiempo'], df['CPU(%)'], color='red', label='CPU(%)')

# Etiquetas y título
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Uso (%)')
plt.title('Consumo de Memoria y CPU a lo largo del tiempo')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.xlim(df['Tiempo'].min(), df['Tiempo'].max())
plt.ylim(0, 100)
plt.tight_layout()

# Mostrar la gráfica
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
# leemos el archivo
df = pd.read_csv('recursos_corregidos.csv')

# Convertimos la coulmna de tiempo a formato de fecha y hora
df['Tiempo'] = pd.to_datetime(df['Tiempo'])
# pasamos los timepos a minutos
df['Tiempo'] = df['Tiempo'].apply(
    lambda x: x.hour * 60 + x.minute + x.second / 60)

# Ajustamos el ta;anos de la figura a mostrar
plt.figure(figsize=(10, 5))

# Grafica del consumo de memoria
plt.plot(df['Tiempo'], df['Memoria(%)'], color='blue', label='Memoria(%)')
# Grafica del uso de CPU
plt.plot(df['Tiempo'], df['CPU(%)'], color='red', label='CPU(%)')

# aJUSTES PARA UNA MERJOR VISUALIZACION
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Uso (%)')
plt.title('Consumo de Memoria y CPU a lo largo del tiempo')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.xlim(df['Tiempo'].min(), df['Tiempo'].max())
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

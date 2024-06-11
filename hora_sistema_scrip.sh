# Creamos el archivo donde se almacenarán los valores de la hora del sistema
touch save_hour.txt

# Esta función estará encargada de guardar la hora en el archivo creado anteriormente
save_hour() {
    date +%H:%M:%S >> save_hour.txt
}
# Función para ejecutar el bucle en segundo plano
ejecutar_en_background() {
    i=0
    # Mientras i sea menor que el número total de iteraciones,
    # se ejecutará la función save_hour cada 5 segundos
    while [ $i -lt 120 ]; do # se hace que solo se ejecute 2 min
        save_hour
        sleep 5
        i=$((i+1))
    done
}

# Ejecutamos la funcion en segundo plano
ejecutar_en_background &

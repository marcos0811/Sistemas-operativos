# creamos el archvio donde se almacenara los valores de timepo, menoria y cpu
touch recursos.csv

#  creamos la cabecera del archivo como el timepo, menoria y cpu
echo "Tiempo,Memoria(%),CPU(%)" > recursos.csv

# Función para obtener la información de memoria y CPU
obtener_estadisticas() {
    tiempo=$(date "+%Y-%m-%d %H:%M:%S")
    memoria=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2}')
    cpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "$tiempo,$memoria,$cpu" >> recursos.csv
}

echo -n "Ingrese el intervalo de N (en segundos): "
read N

ejecutar_en_background() {
    i=0 # Se incia la vairable en o
    while [ $i -lt 120 ]; do # se hace que se itere solo 2 min  
        obtener_estadisticas
        sleep $N
        i=$((i+1))
    done
}

# hacemos que se ejecute el scrip ens egundo plano
ejecutar_en_background &


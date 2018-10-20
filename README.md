# GetDataWS

Script en python para descargar datos de un servicio web

## Configuración

```
pip install pandas 

echo 'export PATH=$PATH:$HOME/GetDataWS/' >> /home/cloudera/.bashrc
source $HOME/.bashrc
```

## Ejemplo

```
get_data.sh \
    --dir data \
    --item ListaEESSPrecio \
    --timestamp \
    --clean \
    https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/

get_data.sh \
    --name ccaa \
    --dir data \
    --format csv \
    --header \
    https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/Listados/ComunidadesAutonomas/
```

## Requirements
requests
```
pip istall requests
```

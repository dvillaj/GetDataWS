#!/bin/bash

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

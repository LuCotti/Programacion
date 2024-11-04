#!/bin/bash
echo "Creamos la estructura de carpetas."
sudo mkdir -p /Examenes-UTN/{alumno_{1..3}/parcial_{1..3},profesores}
echo "La mostramos mediante tree."
tree /Examenes-UTN/

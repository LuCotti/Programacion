#!/bin/bash
DISCO=$(sudo fdisk -l | grep "10 G" | awk '{print $2}' | sed 's/://g')
echo "Entro al fdisk y creo todas las particiones."
sudo fdisk $DISCO << EOF
n
p
1

+1G
n
p
2

+1G
n
p
3

+1G
n
e

+7166M
n

+1G
n

+1G
n

+1G
n

+1G
n

+1G
n

+1G
n

+1014M
w
EOF
sudo partprobe $DISCO
echo "Muestro las particiones."
sudo fdisk -l $DISCO
echo "Formateo las particiones con ext4."
sudo fdisk -l $DISCO | grep Linux | awk '{print "sudo mkfs.ext4 "$1}' | bash
# sudo mkfs -t ext4 /dev/sdc1
# sudo mkfs -t ext4 /dev/sdc2
# sudo mkfs -t ext4 /dev/sdc3
# sudo mkfs -t ext4 /dev/sdc5
# sudo mkfs -t ext4 /dev/sdc6
# sudo mkfs -t ext4 /dev/sdc7
# sudo mkfs -t ext4 /dev/sdc8
# sudo mkfs -t ext4 /dev/sdc9
# sudo mkfs -t ext4 /dev/sdc10
# sudo mkfs -t ext4 /dev/sdc11
echo "Monto las particiones en las carpetas correspondientes."
sudo mount ${DISCO}1 /Examenes-UTN/alumno_1/parcial_1
sudo mount ${DISCO}2 /Examenes-UTN/alumno_1/parcial_2
sudo mount ${DISCO}3 /Examenes-UTN/alumno_1/parcial_3
sudo mount ${DISCO}5 /Examenes-UTN/alumno_2/parcial_1
sudo mount ${DISCO}6 /Examenes-UTN/alumno_2/parcial_2
sudo mount ${DISCO}7 /Examenes-UTN/alumno_2/parcial_3
sudo mount ${DISCO}8 /Examenes-UTN/alumno_3/parcial_1
sudo mount ${DISCO}9 /Examenes-UTN/alumno_3/parcial_2
sudo mount ${DISCO}10 /Examenes-UTN/alumno_3/parcial_3
sudo mount ${DISCO}11 /Examenes-UTN/profesores
echo "Añado la información al archivo fstab."
echo "${DISCO}1    /Examenes-UTN/alumno_1/parcial_1    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}2    /Examenes-UTN/alumno_1/parcial_2    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}3    /Examenes-UTN/alumno_1/parcial_3    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}5    /Examenes-UTN/alumno_2/parcial_1    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}6    /Examenes-UTN/alumno_2/parcial_2    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}7    /Examenes-UTN/alumno_2/parcial_3    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}8    /Examenes-UTN/alumno_3/parcial_1    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}9    /Examenes-UTN/alumno_3/parcial_2    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}10   /Examenes-UTN/alumno_3/parcial_3    ext4    defaults    0    0" | sudo tee -a /etc/fstab
echo "${DISCO}11   /Examenes-UTN/profesores            ext4    defaults    0    0" | sudo tee -a /etc/fstab





# TERMINAR LO SIGUIENTE (IMAGEN GUARDADA EN CARPETA PARCIAL)
# FLAG_EXISTE_FSTAB=''
# FLAG_EXISTE_FSTAB=$(grep -i exam /etc/fstab)
# if [ "$FLAG_EXISTE_FSTAB" -ne ""]; then
#     echo "ya esta"
#     exit 1
# else:
#     echo "no esta cargado"
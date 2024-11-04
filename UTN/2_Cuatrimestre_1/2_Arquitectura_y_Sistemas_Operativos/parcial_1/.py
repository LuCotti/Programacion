print(0 % 3 + 1)
print(1 % 3 + 1)
print(2 % 3 + 1)
print(3 % 3 + 1)
print(4 % 3 + 1)
print(5 % 3 + 1)
print(6 % 3 + 1)
print(7 % 3 + 1)
print(8 % 3 + 1)
print(9 % 3 + 1)
print(0 % 3 + 1)
print(11 % 3 + 1)



'''sudo mount /dev/sdc1 Examenes-UTN/alumno_1/parcial_1
sudo mount /dev/sdc2 Examenes-UTN/alumno_1/parcial_2
sudo mount /dev/sdc3 Examenes-UTN/alumno_1/parcial_3
sudo mount /dev/sdc5 Examenes-UTN/alumno_2/parcial_1
sudo mount /dev/sdc6 Examenes-UTN/alumno_2/parcial_2
sudo mount /dev/sdc7 Examenes-UTN/alumno_2/parcial_3
sudo mount /dev/sdc8 Examenes-UTN/alumno_3/parcial_1
sudo mount /dev/sdc9 Examenes-UTN/alumno_3/parcial_2
sudo mount /dev/sdc10 Examenes-UTN/alumno_3/parcial_3
sudo mount /dev/sdc11 Examenes-UTN/profesores


for i in {1..10}; do
    sudo mount $DISCOi Examenes-UTN/alumno_((i - 1) / 3 + i)
done

'''
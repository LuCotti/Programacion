// /*OPERADORES COMPARATIVOS*/

// let numero1 = "0";
// let numero2 = 1;

// document.write(numero1 == numero2);
// document.write(" SEPARO ");
// document.write(numero1 != numero2);
// document.write(" SEPARO ");
// document.write(numero1 === numero2);
// document.write(" SEPARO ");
// document.write(numero1 !== numero2);
// document.write(" SEPARO ");

// let numero3 = 3;
// let numero4 = 4;

// document.write(numero3 < numero4);
// document.write(" SEPARO ");
// document.write(numero3 > numero4);
// document.write(" SEPARO <br>");

// let edad = prompt("¿Cuántos años tenés?");

// edad = parseInt(edad);

// alert("Te faltan " + (edad + 60) + " años para morir");

// // ARRAYS ASOCIATIVOS

// let pc = {
//     nombre: "LuchoPC",
//     procesador: "64 bits",
//     sistema: "Windows 10",
//     espacio: "256 GB"
// }

// let frase = `Nombre de la PC: ${pc["nombre"]} <br>
//              Procesador de la PC: ${pc["procesador"]} <br>
//              Sistema operativo: ${pc["sistema"]} <br>
//              Espacio total en disco: ${pc["espacio"]}`

// document.write(frase + "<br>");



// BUCLES------------------------------------------------------

// for (let i = 0; i <=30; i++) {
//     if (i >= 11) {
//         break;
//     }
//     if (i == 1 || i == 3 || i == 5 || i == 7 || i == 9) {
//         continue;
//     }
//     document.write(i + "<br>");
// }

// document.write("<br><br><br><br>");

let ropa = ["Remera", "Pantalón", "Zapatillas", "Medias", "Boxer"];

for (let prenda in ropa) {
    document.write(prenda + "<br>");
}

document.write("<br><br>");

for (let prenda of ropa) {
    document.write(prenda + "<br>");
}



// let array1 = ["Matías", "Agustín", "Tomás"];
// let array2 = ["Rocío", "Camila", array1, "Cristina", "Estela", "F", "F", "F", "F", "F", "F", "F", "F", "F"];

// forMateo:
// for (vuelta in array2) {
//     if (vuelta == 2) {
//         for (vuelta of array1) {
//             document.write(vuelta + "<br>");
//             continue forMateo;
//         }
//     } else if (array2[vuelta] == "F") {
//         break;
//     } else {
//         document.write(array2[vuelta] + "<br>");
//     }
// }
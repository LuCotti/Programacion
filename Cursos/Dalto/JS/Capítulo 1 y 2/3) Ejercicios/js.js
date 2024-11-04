let free = false;

const validarCliente = (edad, hora) => {
    edad = prompt("¿Edad?");
    if (edad < 18) {
        alert("No, nene, andá a tomar la mamadera.");
    } else {
        hora = prompt("¿Tenés hora, capo?");
        if (hora >= 2 && hora <= 7 && free == false) {
            alert("Pasá gratis nomás, total mañana renuncio.")
            free = true;
        } else {
            alert(`La entrada son 500 dólares a las ${hora}:00 hs.`);
        }
    }
}

validarCliente();
validarCliente();
validarCliente();
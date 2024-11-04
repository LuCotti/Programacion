const guardarInfo = (materia) => {
    let materias = {
        lengua: ["Perez", "Ezequiel", "Gabriel", "Mario"],
        matematica: ["Rodriguez", "Pedro", "Ezequiel", "Gabriel"],
        fisica: ["Hernández", "Mario", "Pedro", "Ezequiel"],
        quimica: ["Dalto", "Gabriel", "Mario", "Pedro"]
    }
    if (materias[materia]) {
        return [materia, materias[materia]];
    } else {
        return materias;
    }
}


const obtenerInfo = (materia) => {
    let info = guardarInfo(materia);
    if (info !== false ) {
        let profesor = info[1][0];
        let alumnos = info[1];
        alumnos.shift();
        document.write(`<b>Materia: </b>${info[0]}<br><b>Profesor: </b>${profesor}<br><b>Alumnos inscriptos: </b>${alumnos}<br><br>`);
    } else {
        document.write(`<b style="color:red">ESCRIBÍ BIEN HIJO DE PUTAAAAAA!!!!!!!!!</b><br><br>`);
    }
}

obtenerInfo("lengua");
obtenerInfo("matematica");
obtenerInfo("fisica");
obtenerInfo("quimica");
document.write("<br><br>");


const cantidadDeClases = (alumno) => {
    let informacion = guardarInfo();
    let total = 0;
    for (info in informacion) {
        if (informacion[info].includes(alumno)) {
            total++;
        }
    }
    document.write (`${alumno} se encuentra en ${total} clases.<br>`);
}

cantidadDeClases("Pedro");
cantidadDeClases("Ezequiel");
cantidadDeClases("Gabriel");
cantidadDeClases("Mario");
document.write("<br><br>");


const infoPersonal = (alumno) => {
    let informacion = guardarInfo();
    let clasesPresentes = [];
    let profesores = [];
    for (info in informacion) {
        if (informacion[info].includes(alumno)) {
            clasesPresentes.push(" " + info);
            profesores.push(" " + informacion[info][0]);
        }
    }
    document.write(`${alumno} se encuentra en las siguientes clases: ${clasesPresentes}.<br>
                    Sus respectivos profesores son: ${profesores}.<br><br>`);
}

infoPersonal("Pedro");
infoPersonal("Ezequiel");
infoPersonal("Gabriel");
infoPersonal("Mario");

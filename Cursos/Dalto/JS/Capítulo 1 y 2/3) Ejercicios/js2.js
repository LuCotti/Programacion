let cantidad = prompt("¿Cuántos alumnos son?");

let alumnosTotales = [];

for (i = 0; i < cantidad; i++) {
    alumnosTotales[i] = [prompt("Nombre del alumno" + (i+1)), 0];
}

const tomarLista = (nombre, p) => {
    let presencia = prompt(nombre);
    if (presencia == "p" || presencia == "P") {
        alumnosTotales[p][1]++;
    }
}

for (i = 0; i < 10; i++) {
    for (alumno in alumnosTotales) {
        tomarLista(alumnosTotales[alumno][0], alumno);
    }
}

for (alumno in alumnosTotales) {
    let resultado = `${alumnosTotales[alumno][0]}:<br>
    Presentes: ${alumnosTotales[alumno][1]}<br>
    Ausentes: ${10 - alumnosTotales[alumno][1]}<br><br>`;

    if (10 - alumnosTotales[alumno][1] > 3) {
        resultado += "<b style = 'color: red'>SE QUEDÓ LIBRE</b><br><br>";
    }
    document.write(resultado);
}

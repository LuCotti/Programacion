let materias = {
    lengua: ["Perez", "Ezequiel", "Gabriel", "Mario"],
    matematica: ["Rodriguez", "Pedro", "Ezequiel", "Gabriel"],
    fisica: ["Hernández", "Mario", "Pedro", "Ezequiel"],
    quimica: ["Dalto", "Gabriel", "Mario", "Pedro"]
}


const inscribir = (alumno, materia) => {
    let personas = materias[materia];
    if (personas.length >= 21) {
        document.write(`Lo siento ${alumno}, Las clases de ${materia} se encuentran llenas.<br>`);
    } else {
        personas.push(alumno);
        if (materia == "lengua") {
            materias = {
                lengua: personas,
                matematica: materias['matematica'],
                fisica: materias['fisica'],
                quimica: materias['quimica']
            }
        } else if (materia == "matematica") {
            materias = {
                lengua: materias['lengua'],
                matematica: personas,
                fisica: materias['fisica'],
                quimica: materias['quimica']
            }
        } else if (materia == "fisica") {
            materias = {
                lengua: materias['lengua'],
                matematica: materias['matematica'],
                fisica: personas,
                quimica: materias['quimica']
            }
        } else if (materia == "quimica") {
            materias = {
                lengua: materias['lengua'],
                matematica: materias['matematica'],
                fisica: materias['fisica'],
                quimica: personas
            }
        }
        document.write("Inscripción realizada con éxito.<br>");
    }
}

inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
inscribir("José", "lengua");
document.write(materias['lengua'] + "<br><br>")
document.write("Último alumno inscripto: " + materias["lengua"]["20"]);
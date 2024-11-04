// VALIDAR ENTERO
function validarEntero(texto){
    let field = document.getElementById(texto);
    let valueInt = parseInt(field.value);

    if(!Number.isInteger(valueInt)){
        alert("No es un entero");
    } else{
        field.value = valueInt;
    }
}

// COMPROBAR IGUALDAD
function comprobarClave(){
    let clave1 = document.form.clave1.value;
    let clave2 = document.form.clave2.value;

    if(clave1 == clave2){
        alert("Las claves coinciden");
    } else {
        alert("Las claves son distintas");
    }
}

// CONTAR CARACTERES
function contar(){
    document.forms[0].caracteres.value = document.forms[0].texto2.value.length;
}

// RELOJ
function mueveReloj(){
    let momentoActual = new Date();
    let hora = momentoActual.getHours();
    let minuto = momentoActual.getMinutes();
    let segundo = momentoActual.getSeconds();

    let str_segundo = new String (segundo)
    if(str_segundo.length == 1){
        segundo = "0" + segundo;
    }

    let str_minuto = new String (minuto)
    if(str_minuto.length == 1){
        minuto = "0" + minuto;
    }

    let str_hora = new String (hora)
    if(str_hora.length == 1){
        hora = "0" + hora;
    }

    let horaImprimible = hora + " : " + minuto + " : " + segundo;
    document.form.reloj.value = horaImprimible;

    setTimeout("mueveReloj()",1000);
}
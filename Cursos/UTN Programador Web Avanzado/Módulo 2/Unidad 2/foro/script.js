function validarObligatorios(){
    let nombre = document.forms[0].nombre.value;
    let apellido = document.forms[0].apellido.value;
    let password1 = document.forms[0].password1.value;
    let password2 = document.forms[0].password2.value;
    if(nombre == ""){
        alert("El campo 'Nombre' es obligatorio");
    }
    if(apellido == ""){
        alert("El campo 'Apellido' es obligatorio");
    }
    if(password1 == ""){
        alert("El campo 'Password' es obligatorio");
    }
    if(password2 == ""){
        alert("El campo 'Repetir password' es obligatorio");
    }
}

function validarNumero(telefono){
    let campo = document.getElementById('telefono');
    let entero = parseInt(campo.value);

    if(!Number.isInteger(entero)){
        alert("El valor ingresado debe ser numérico")
    }
}

function validarIgualdad(){
    let password1 = document.form.password1.value;
    let password2 = document.form.password2.value;
    if(password1 != password2){
        alert("Las contraseñas no coinciden");
    }
}
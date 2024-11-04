class App {
    constructor (descargas, puntuacion, peso) {
        this.descargas = descargas;
        this.puntuacion = puntuacion;
        this.peso = peso;
        this.info = `Cantidad de descargas: ${this.descargas}
Puntuación: ${this.puntuacion} / 5 estrellas
Peso: ${this.peso}`;
        this.instalada = false;
        this.abierta = false;
    }
    verInfo() {
        alert(this.info);
    }
    descargar() {
        if (!this.instalada) {
        alert("Descargando...");
        alert("Instalando...");
        alert("La aplicación fue instalada correctamente.");
        this.instalada = true;
        } else {
            alert("Esta aplicación ya fue instalada.");
        }
    }
    abrir() {
        if (this.instalada) {
            if (!this.abierta) {
                alert("Bienvenido a WhatsApp!");
            } else {
                alert("Ya estás navegando en WhatsApp.");
            }
            this.abierta = true;
        } else {
            alert("Primero se debe instalar la aplicación.");
        }
    }
    cerrar() {
        if (this.instalada) {
            if (this.abierta) {
                alert("La aplicación fue cerrrada.");
                this.abierta = false;
            } else {
                alert("Primero se debe abrir la aplicación.");
            }
        } else {
            alert("Primero se debe instalar la aplicación.");
        }
    }
    desinstalar() {
        if (this.instalada) {
            let confirmacion = prompt("¿Está seguro que desea desinstalar WhatsApp?");
            if (confirmacion === "si" || confirmacion === "SI" || confirmacion === "Si") {
                alert("Desinstalando aplicación...");
                alert("La aplicación fue desinstalada correctamente.");
                this.instalada = false;
            }
        } else {
            alert("Primero se debe instalar la aplicación.");
        }
    }
}

const whatsapp = new App (50690, 4.7, "259 MB");

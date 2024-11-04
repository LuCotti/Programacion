class Celular {
    constructor (color, peso, pantalla, camara, ram) {
        this.color = color;
        this.peso = peso;
        this.pantalla = pantalla;
        this.camara = camara;
        this.ram = ram;
        this.encendido = false;
        this.grabando = false;
        this.info = `<a href="Problema A.html">Volver</a><br>
                    Color: ${this.color}<br>
                    Peso: ${this.peso}<br>
                    Resolución de pantalla: ${this.pantalla}<br>
                    Resolución de cámara: ${this.camara}<br>
                    Espacio total de memoria ram: ${this.ram}<br>`;
    }
    encenderApagar() {
        if (!this.encendido) {
            alert("Dispositivo encendido.");
            this.encendido = true;
        } else {
            alert("Apagando sistema...");
            this.encendido = false;
        }
    }
    reiniciar() {
        if (this.encendido) {
            alert("Reiniciando sistema...");
        } else {
            alert("El dispositivo se encuentra apagado.");
        }
    }
    sacarFoto() {
        if (this.encendido) {
            if (!this.grabando) {
                alert("*Foto*");
            } else {
                alert("No se puede sacar fotos mientras se graba.");
            }
        } else {
            alert("El dispositivo se encuentra apagado.")
        }
    }
    grabar() {
        if (this.encendido) {
            if (!this.grabando) {
                alert("Grabando...");
                this.grabando = true;
            } else {
                alert("La grabación ya fue iniciada.");
            }
        } else {
            alert("El dispositivo se encuentra apagado.");
        }
    }
    detenerGrabacion() {
        if (this.encendido) {
            if (this.grabando) {
                alert("Video guardado.");
                this.grabando = false;
            } else {
                alert("Primero se debe iniciar la grabación.");
            }
        } else {
            alert("El dispositivo se encuentra apagado.");
        }
    }
}

const TCL = new Celular("Azul", "87 g", "420 p", "5 Mpx", "1 GB")

class CelularAltaGama extends Celular {
    constructor (color, peso, pantalla, camara, ram, camara2) {
        super (color, peso, pantalla, camara, ram);
        this.camara2 = camara2;
    }
    grabarLento() {
        if (this.encendido) {
            if (!this.grabando) {
                alert("Grabando lento...");
                this.grabando = true;
            } else {
                alert("La grabación ya fue iniciada.");
            }
        } else {
            alert("El dispositivo se encuentra apagado.");
        }
    }
    reconocimientoFacial() {
        if (this.encendido) {
            alert("Jeta reconocida");
        } else {
            alert("El dispositivo se encuentra apagado.");
        }
    }
    infoAltaGama() {
        document.write(this.info + `Resolución de cámara frontal: ${this.camara2}<br>`);
    }
}

const celular1 = new CelularAltaGama("Negro", "300 g", "1080 p", "100 Mpx", "16 GB", "50 Mpx")




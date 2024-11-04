class Animal {
    constructor (especie, edad, color) {
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Especie: ${this.especie}.<br>
                    Edad: ${this.edad} años.<br>
                    Color: ${this.color}.<br><br>`
    }
    verInfo() {
        document.write(this.info);
    }
}

class Perro extends Animal {
    constructor (especie, edad, color, raza) {
        super (especie, edad, color);
        this.raza = raza;
    }

    ladrar() {
        document.write("¡RAWR!");
    }

    set setRaza(newName) {
        this.raza = newName;
    }

    get getRaza() {
        return this.raza;
    }
}

const perro = new Perro("perro", 8, "gris", "Caniche");
const gato = new Animal("gato", 4, "naranja");
const mosquito = new Animal("mosquito", 0.24, "negro");

// document.write(perro.info);
// document.write(gato.info);
// document.write(mosquito.info);

perro.verInfo();
gato.verInfo();
mosquito.verInfo();

perro.ladrar();

perro.setRaza = "Rottweiler";

document.write("<br><br>Nueva raza: " + perro.getRaza);
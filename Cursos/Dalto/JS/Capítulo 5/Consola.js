console.time();
let A = prompt("¿Querés un assert?");
console.assert(A === "No" || A === "NO" || A === "no" || A === "");
if (A === "") {
    console.error("Error: texto en blanco.");
}

setTimeout(() => {
    let B = prompt("¿Desea limpiar la consola?");
    if (B === "si" || B === "Si" || B === "SI") {
    console.warn("¡Guarda que si la limpiás te hackean los nazis!");
    setTimeout(() => {
        let C = prompt("¿ENTONCES LA LIMPIÁS?");
        if (C === "si" || C === "Si" || C === "SI") {
            console.clear();
        }
    }, 2000);
}
}, 2000);

console.timeLog();

console.table(["Nacho","Pedro","Cleopatra","Pitacio"]);
console.dir(["Nacho","Pedro","Cleopatra","Pitacio"]);

console.group("Grupo abierto");
console.log("Somos del grupo abierto.");
console.log("Somos del grupo abierto.");
console.log("Somos del grupo abierto.");
console.log("Somos del grupo abierto.");
console.log("Somos del grupo abierto.");
console.groupEnd();
console.groupCollapsed("Grupo cerrado");
console.log("Somos del grupo cerrado.");
console.log("Somos del grupo cerrado.");
console.log("Somos del grupo cerrado.");
console.log("Somos del grupo cerrado.");
console.log("Somos del grupo cerrado.");
console.groupEnd();

console.timeEnd();
console.log("");
console.log("");
console.log("");
console.log("");
console.log("");
console.log("%cHOLA", "background: #000; color: #fff; padding: 10px 20px; letter-spacing: 0;");
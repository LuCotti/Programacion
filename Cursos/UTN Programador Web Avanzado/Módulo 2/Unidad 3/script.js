function obtenerDatos(){
    return new Promise ((resolve, reject) =>{
        setTimeout (() =>{
            const datos = {nombre: "Juan", edad: 25};
            resolve(datos);
            reject (new Error ("error al obtener los datos"))
        }, 1500)
    })
}

async function procesarDatos(){
    try{
        const datos = await obtenerDatos();
        console.log("Datos recibidos: ", datos);
    } catch (error){
        console.log("Error: ", error.message);
    }
}

procesarDatos();
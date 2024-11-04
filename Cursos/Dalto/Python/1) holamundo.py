print('Hola mundo')
nombre = 'Luciano'
saludo = f'Hola {nombre}, ¿Cómo estás?' # f al principio para concatenar cualquier tipo de dato.
print(saludo)

nom = 'Luciano'
apellido = 'Cotti'
edad = 22
mensaje = f'''Nombre: {nom}
Apellido: {apellido}
Edad: {edad}''' # Comillas triples para textos de múltiples líneas.
print(mensaje)

print('ombre' in mensaje) # Devuelve True ya que lo encuentra en la variable 'mensaje'.
print('ombre' not in mensaje) # Devuelve False.


del nom # Devuelve un error ya que se elimina la variable 'nom'.
print(nom)

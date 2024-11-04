'''
Crea una clase CuentaBancaria con los siguientes atributos:
titular:
saldo:

Incluye métodos:
• depositar(cantidad): agrega la cantidad al saldo
• extraer(cantidad): resta la cantidad al saldo, si hay suficiente dinero. De
lo contrario, imprimir "saldo insuficiente".
• mostrar_saldo()

Caso de uso: crear una cuenta a Daniel con $1000
Después depositar $500
Extraer $200
Mostrar saldo
'''
# Definición de la clase
class CuentaBancaria:
    # Atributos
    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.saldo = saldo
    
    # Métodos
    def depositar(self, cantidad: int) -> int:
        self.saldo += cantidad
        return self.saldo
    
    def extraer(self, cantidad: int) -> (int | None):
        if cantidad > self.saldo:
            return print('Saldo insuficiente.')
        else:
            self.saldo -= cantidad
            return self.saldo
    
    def mostrar_saldo(self) -> None:
        print(f'Saldo disponible: ${self.saldo}')

cuenta_daniel = CuentaBancaria('Daniel', 1000)
# cuenta_daniel.depositar(500)
# cuenta_daniel.extraer(200)
# cuenta_daniel.mostrar_saldo()



# Función para mostrar el menú
def mostrar_menu():
    menu = '''
1. Depositar dinero.
2. Extraer dinero.
3. Mostrar saldo disponible.
4. Salir.
    '''
    while True:
        print(menu)
        opcion_ingresada = input('Ingrese una de las opciones anteriores: ')
        
        match opcion_ingresada:
            case '1':
                monto_a_depositar = int(input('Ingrese el monto a depositar: '))
                cuenta_daniel.depositar(monto_a_depositar)
            case '2':
                monto_a_extraer = int(input('Ingrese el monto a extraer: '))
                cuenta_daniel.extraer(monto_a_extraer)
            case '3':
                cuenta_daniel.mostrar_saldo()
            case '4':
                break
            case _:
                print('La opción ingresada no existe.')

mostrar_menu()

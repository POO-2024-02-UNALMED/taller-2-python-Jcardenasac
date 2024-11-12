class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ("verde", "negro", "amarillo", "rojo", "blanco"):
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo  
        self.registro = registro

    def cambiarRegistro(self, nuevoregistro):
        self.registro = nuevoregistro
    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    def __init__(self, modelo, asientos, marca, color, registro, motor):
        self.modelo = modelo
        self.asientos = asientos
        self.marca = marca
        self.color = color
        self.registro = registro
        self.motor = motor

    def cantidadAsientos(self):
        contador = 0
        for elemento in self.asientos:
            if isinstance(elemento, Asiento):
                contador += 1
        return contador

    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):
            for i in self.Asientos:
                if i is not None:
                    if self.registro != i.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

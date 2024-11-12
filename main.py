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
    def __init__(self, modelo, precio, asientos, marca, motor, color, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.color = color
        self.registro = registro
      

    def cantidadAsientos(self):
        contador = 0
        for elemento in self.asientos:
            if isinstance(elemento, Asiento):
                contador += 1
        return contador

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
           return "Las piezas no son originales"
    
        for asiento in self.asientos:
           if asiento is not None and asiento.registro != self.registro:
               return "Las piezas no son originales"
    
        return "Auto original"

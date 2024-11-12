class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ("verde", "negro", "amarillo", "rojo", "blanco"):
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, registro, tipo):
        self.numeroCilindros = numeroCilindros
        self.registro = registro
        self.tipo = tipo

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

    def verificarIntegridad(self) -> str:
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != self.motor.registro:
                    return "Las piezas no son originales"
                elif asiento.registro != self.registro:
                    return "Las piezas no son originales"
                elif self.registro != self.motor.registro:
                    return "Las piezas no son originales"
        return "Auto original"

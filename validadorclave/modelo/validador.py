# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._logitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._logitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(char.isupper() for char in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(char.isdigit() for char in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str)-> bool:
        especiales = {'@', '_', '#' , '$', '%'}
        return any(char in especiales for char in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("ReglaValidacionGanimedes: La clave debe tener una longitud de mas de 8 caracteres.")
        if not self._contiene_mayuscula(clave):
            raise ValueError("ReglaValidacionGanimedes: La clave debe contener al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise ValueError("ReglaValidacionGanimedes: La clave debe contener al menos una letra minúscula.")
        if not self._contiene_numero (clave):
            raise ValueError("ReglaValidacionGanimedes: La clave debe contener al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise ValueError("ReglaValidacionGanimedes: La clave debe contener al menos uno de los caracteres especiales @, _, #, $, %.")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for char in clave if char.isupper())
        total_letras = len(clave)
        return mayusculas >= 2 and mayusculas < total_letras

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("ReglaValidacionCalisto: La clave debe tener una longitud de más de 6 caracteres.")
        if not self._contiene_numero(clave):
            raise ValueError("ReglaValidacionCalisto: La clave debe contener al menos un número.")
        if not self.contiene_calisto(clave):
            raise ValueError("ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula.")
        return True

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

    def validar_calve(clave: str, reglas: list):
        for regla in reglas:
            validador = Validador(clave)
            pass




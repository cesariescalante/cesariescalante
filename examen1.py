"""1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

class Persona:
    def __int__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = "peruana"

    def cumpleanios(self):
        self.edad +=1


persona = Persona(48)

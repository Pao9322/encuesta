class Pregunta:
    """
    Clase que representa una pregunta.

    Atributos:
    - enunciado (str): Texto que describe la pregunta.
    - ayuda (str): Descripción adicional opcional para la pregunta.
    - es_requerida (bool): Indica si la pregunta es obligatoria (True) o no (False).
    - alternativas (list): Lista de objetos de tipo Alternativa asociados a la pregunta.
    """

    def __init__(self, enunciado, ayuda=None, es_requerida=False):
        """
        Inicia una nueva instancia de la clase Pregunta.

        Parámetros:
        - enunciado (str): Texto que describe la pregunta.
        - ayuda (str, opcional): Descripción adicional opcional para la pregunta.
        - es_requerida (bool): Indica si la pregunta es obligatoria (True) o no (False).
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = []

    def agregar_alternativa(self, alternativa):
        """
        Agrega una alternativa a la lista de alternativas de la pregunta.

        Parámetros:
        - alternativa: Objeto de tipo Alternativa a agregar.
        """
        self.alternativas.append(alternativa)

    def mostrar_pregunta(self):
        """
        Muestra la información de la pregunta, incluyendo sus alternativas.

        Nota: Este método asume que las alternativas tienen un método mostrar_alternativa().
        """
        print(f"Enunciado: {self.enunciado}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        print("Alternativas:")
        for alternativa in self.alternativas:
            alternativa.mostrar_alternativa()
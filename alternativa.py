class Alternativa:
    """
    Clase que representa una alternativa.

    Atributos:
    - contenido (str): Texto que describe el contenido de la alternativa.
    - ayuda (str, opcional): Descripción adicional opcional para la alternativa.
    """

    def __init__(self, contenido, ayuda=None):
        """
        Inicia una nueva instancia de la clase Alternativa.

        Parámetros:
        - contenido (str): Texto que describe el contenido de la alternativa.
        - ayuda (str, opcional): Descripción adicional opcional para la alternativa.
        """
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar_alternativa(self):
        """
        Muestra la información de la alternativa.

        Imprime el contenido de la alternativa y, si está disponible, su ayuda.
        """
        print(f"Contenido: {self.contenido}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")


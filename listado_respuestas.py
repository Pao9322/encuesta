class ListadoRespuestas:
    """
    Clase que representa un listado de respuestas asociado a un usuario.

    Atributos:
    - usuario (Usuario): Usuario asociado al listado de respuestas.
    - respuestas (list): Lista que almacena las respuestas asociadas al usuario.

    Métodos:
    - agregar_respuesta(respuesta): Método para agregar una respuesta al listado.

    """

    def __init__(self, usuario, respuestas=None):
        """
        Inicia una nueva instancia de la clase ListadoRespuestas.

        Parámetros:
        - usuario (Usuario): Usuario asociado al listado de respuestas.
        - respuestas (list, opcional): Lista de respuestas inicial. Por defecto, es una lista vacía.
        """
        self.usuario = usuario
        self.respuestas = [] if respuestas is None else respuestas

    def agregar_respuesta(self, respuesta):
        """
        Agrega una respuesta al listado de respuestas.

        Parámetros:
        - respuesta: Respuesta a ser agregada al listado.
        """
        self.respuestas.append(respuesta)
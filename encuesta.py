class Encuesta:
    """
    Clase que representa una encuesta.

    Atributos:
    - nombre (str): Nombre de la encuesta.
    - preguntas (list): Lista de preguntas asociadas a la encuesta.
    - listados_respuestas (list): Lista de listados de respuestas asociados a la encuesta.
    """

    def __init__(self, nombre):
        """
        Inicializa una nueva instancia de la clase Encuesta.

        Parámetros:
        - nombre (str): Nombre de la encuesta.
        """
        self.nombre = nombre
        self.preguntas = []
        self.listados_respuestas = []

    def agregar_pregunta(self, pregunta):
        """
        Agrega una pregunta a la lista de preguntas de la encuesta.

        Parámetros:
        - pregunta: Objeto de tipo Pregunta a agregar.
        """
        self.preguntas.append(pregunta)

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la lista de listados de respuestas de la encuesta.

        Parámetros:
        - listado_respuestas: Objeto de tipo ListadoRespuestas a agregar.
        """
        self.listados_respuestas.append(listado_respuestas)

    def mostrar_encuesta(self):
        """
        Muestra la información de la encuesta, incluyendo sus preguntas.

        Este método asume que las preguntas tienen un método mostrar_pregunta().
        """
        print(f"Nombre de la Encuesta: {self.nombre}")
        print("Preguntas:")
        for pregunta in self.preguntas:
            pregunta.mostrar_pregunta()


class EncuestaEdadLimitada(Encuesta):
    """
    Clase que representa una encuesta limitada por edad, heredada de la clase Encuesta.

    Atributos:
    - nombre (str): Nombre de la encuesta.
    - edad_minima (int): Edad mínima.
    - edad_maxima (int): Edad máxima.
    """

    def __init__(self, nombre, edad_minima, edad_maxima):
        """
        Inicializa una nueva instancia de la clase EncuestaEdadLimitada.

        Parámetros:
        - nombre (str): Nombre de la encuesta.
        - edad_minima (int): Edad mínima permitida.
        - edad_maxima (int): Edad máxima permitida.
        """
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la lista de listados de respuestas
        solo si el usuario cumple con las restricciones de edad.

        Parámetros:
        - listado_respuestas: Objeto de tipo ListadoRespuestas a agregar.
        """
        usuario = listado_respuestas.usuario
        if self.edad_minima <= usuario.edad <= self.edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)


class EncuestaRegionLimitada(Encuesta):
    """
    Clase que representa una encuesta limitada por región, heredada de la clase Encuesta.

    Atributos:
    - nombre (str): Nombre de la encuesta.
    - lista_regiones (list): Lista de regiones permitidas para participar en la encuesta.
    """

    def __init__(self, nombre, lista_regiones):
        """
        Inicializa una nueva instancia de la clase EncuestaRegionLimitada.

        Parámetros:
        - nombre (str): Nombre de la encuesta.
        - lista_regiones (list): Lista de regiones permitidas.
        """
        super().__init__(nombre)
        self.lista_regiones = lista_regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un listado de respuestas a la lista de listados de respuestas
        solo si el usuario pertenece a una región permitida.

        Parámetros:
        - listado_respuestas: Objeto de tipo ListadoRespuestas a agregar.
        """
        usuario = listado_respuestas.usuario
        if usuario.region in self.lista_regiones:
            super().agregar_listado_respuestas(listado_respuestas)
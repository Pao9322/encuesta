
class Usuario:
    """
    Clase que representa a un usuario.

    Atributos:
    - correo (str): Correo electrónico del usuario.
    - edad (int): Edad del usuario.
    - region (int): Región del usuario.

    Métodos:
    - contestar_encuesta(encuesta): Método para contestar una encuesta y generar un listado de respuestas.

    """

    def __init__(self, correo, edad, region):
        """
        Inicia una nueva instancia de la clase Usuario.

        Parámetros:
        - correo (str): Correo electrónico del usuario.
        - edad (int): Edad del usuario.
        - region (int): Región del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta):
        """
        Contesta una encuesta y genera un listado de respuestas asociado al usuario.

        Parámetros:
        - encuesta (Encuesta): Objeto de la clase Encuesta a ser contestado.

        Retorna:
        - listado_respuestas (ListadoRespuestas): Listado de respuestas generado por el usuario.
        """
        listado_respuestas = ListadoRespuestas(usuario=self)
        encuesta.agregar_listado_respuestas(listado_respuestas)
        return listado_respuestas
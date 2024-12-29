import psycopg2
from abc import ABC, abstractmethod


class BaseDeDatosMeta(type):
    """Se asegura que exista solo una instancia de la base de datos"""

    __instances = None

    def __call__(cls, *args, **kwargs):
        if cls.__instances is None:
            instance = super().__call__(*args, **kwargs)
            cls.__instances = instance
        return cls.__instances


class BaseDeDatos(metaclass=BaseDeDatosMeta):
    """Maneja la conexión con la base de datos instanciada."""

    def __init__(self):
        try:
            self.conexion = psycopg2.connect( host="localhost",
            database="empresas",
            user="postgres",
            password="base1606"
        )
            print("Conexión exitosa")
        except Exception as ex:
            print(ex)

    def obtener_un_elemento(self, consulta, valores=None):
        """Devuelve un elemento de la base de datos según la consulta realizada"""
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, valores)
                return cursor.fetchone()
        except Exception as ex:
            return f"{ex} Error en la consulta: {consulta}. No se pudo obtener el elemento de la base de datos."

    def obtener_elementos(self, consulta, valores=None):
        """Devuelve uno o más elementos de la base de datos según la consulta realizada"""
        try:
            with self.conexion.cursor() as cursor:
                if valores:
                    cursor.execute(consulta, valores)
                else:
                    cursor.execute(consulta)
                return cursor.fetchall()
        except Exception as ex:
            return f'{ex} Error en la consulta: "{consulta}". No se pudieron obtener los elementos de la base de datos.'
     
        
    def consulta(self, consulta, valores):
        """Permite realizar consultas a la base de datos."""
        try:
            # Usar 'with' para asegurar que el cursor se cierre automáticamente
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, valores)
                self.conexion.commit()
        except Exception as ex:
            self.conexion.rollback()  # Rollback en caso de error
            return f"{ex} Error en la consulta: {consulta}."

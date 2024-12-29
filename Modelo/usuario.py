
class Usuario:
    def __init__(self, datos):
       self.__legajo = datos[0]
       self.__dni_personal = datos[1]
       self.__nombre = datos[2]
       self.__apellido = datos[3]
       self.__jerarquia = datos[4]
       self.__fecha_nacimiento = datos[5]
       self.__correo_electronico = datos[6]
       self.__telefono = datos[7]
       self.__usuario = datos[8]
       self.__contrasena = datos[9]
      
      
# GETTERS 
    def get_legajo(self):
        return self.__legajo
    def get_dni_personal(self):
        return self.__dni_personal       
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_jerarquia(self):
        return self.__jerarquia
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def get_correo_electronico(self):
        return self.__correo_electronico
    def get_telefono(self):
        return self.__telefono
    def get_usuario(self):
        return self.__usuario
    def get_contrasena(self):
        return self.__contrasena
    
# SETTERS
    def set_legajo(self,valor):
        self.__legajo = valor
    def set_dni_personal(self,valor):
        self.__dni_personal = valor    
    def set_nombre(self,valor):
        self.__nombre = valor
    def set_apellido(self,valor):
        self.__apellido = valor
    def set_jerarquia(self,valor):
        self.__jerarquia = valor
    def set_fecha_nacimiento(self,valor):
        self.__fecha_nacimiento = valor
    def set_correo_electronico(self,valor):
        self.__correo_electronico = valor
    def set_telefono(self,valor):
        self.__telefono = valor
    def set_usuario(self,valor):
        self.__usuario = valor
    def set_contrasena(self,valor):
        self.__contrasena = valor
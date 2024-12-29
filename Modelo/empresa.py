class Empresa:
    def __init__(self,datos):
       self.__nro_habilitacion = datos[0]
       self.__nombre = datos[1]
       self.__tipo_empresa = datos[2]
       self.__cuit = datos[3]
       self.__direccion = datos[4]
       self.__telefono = datos[5]
       self.__email = datos[6]
       self.__nombre_apoderado = datos[7]
       self.__dni_apoderado = datos[8]
       self.__legajo = datos[9]


# GETTERS 
    def get_nro_habilitacion(self):
        return self.__nro_habilitacion
    def get_nombre(self):
        return self.__nombre      
    def get_tipo_empresa(self):
        return self.__tipo_empresa
    def get_cuit(self):
        return self.__cuit
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    def get_nombre_apoderado(self):
        return self.__nombre_apoderado
    def get_dni_apoderado(self):
        return self.__dni_apoderado
    def get_legajo(self):
        return self.__legajo
    
# SETTERS
    def set_nro_habilitacion(self,valor):
        self.__nro_habilitacion = valor
    def set_nombre(self,valor):
        self.__nombre = valor    
    def set_tipo_empresa(self,valor):
        self.__tipo_empresa = valor
    def set_cuit(self,valor):
        self.__cuit = valor
    def set_direccion(self,valor):
        self.__direccion = valor
    def set_telefono(self,valor):
        self.__telefono = valor
    def set_email(self,valor):
        self.__email = valor
    def set_nombre_apoderado(self,valor):
        self.__nombre_apoderado = valor
    def set_dni_apoderado(self,valor):
        self.__dni_apoderado = valor
    def set_legajo(self,valor):
        self.__legajo = valor
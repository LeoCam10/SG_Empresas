import sys
sys.path.append('C://Users//camus//Desktop//SG_Empresas-main//Modelo')
from base_de_datos import BaseDeDatos



class UsuarioDAO:
    def __init__(self):
        self.base = BaseDeDatos()

    def agregar_usuario(self, legajo, dni_personal, nombre, apellido, jerarquia, fecha_nacimiento, correo_electronico, telefono, usuario, contrasena):
        consulta = '''
        INSERT INTO public."personal"
        (legajo, dni_personal, nombre, apellido, jerarquia, fecha_nacimiento, correo_electronico, telefono, usuario, contrasena)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        valores = (legajo, dni_personal, nombre, apellido, jerarquia, fecha_nacimiento, correo_electronico, telefono, usuario, contrasena)
        self.base.consulta(consulta, valores)
        print (f"Se agregó a la base de datos un usuario con el DNI {dni_personal}")

    def eliminar_usuario(self, dni_personal):
        consulta = '''
        DELETE FROM public."personal" WHERE dni_personal = %s;
        ''' 
        valores = (dni_personal,)
        self.base.consulta(consulta, valores)
        print(f"Se dio la baja al usuario con el dni {dni_personal}")

    def modificar_usuario(self, legajo, dni_personal, nombre, apellido, jerarquia, fecha_nacimiento, correo_electronico, telefono, usuario, contrasena):
        consulta = '''UPDATE public."personal" SET legajo = %s, dni_personal = %s, nombre= %s, apellido = %s ,jerarquia = %s, fecha_nacimiento = %s, correo_electronico= %s, telefono = %s,usuario = %s, contrasena = %s  WHERE dni_personal = %s;'''
        valores = (legajo, dni_personal, nombre, apellido, jerarquia, fecha_nacimiento, correo_electronico, telefono, usuario, contrasena,dni_personal)
        self.base.consulta(consulta, valores)
        print(f"Se modificaron los datos del usuario con el dni {dni_personal}")
    
    def obtener_personal(self, dni_personal):
        consulta = '''SELECT * FROM public."personal" WHERE dni_personal = %s;'''
        valores = (dni_personal,)
        resultado = self.base.obtener_un_elemento(consulta,valores)
        print(f'los datos del usuario {dni_personal}')
        print(resultado)
        
    def obtener_todo_personal(self,valores = None):
        consulta = '''SELECT * FROM public."personal"''' 
        resultado = self.base.obtener_elementos(consulta,valores)
        print(resultado)
        print('Se obtuvieron todos los valores de la tabla') 
   
    def login_usuario(self,usuario, contrasena):
        consulta = '''SELECT usuario, contrasena FROM public."personal" WHERE usuario = %s;''' 
        valores = (usuario,)
        resultado = self.base.obtener_un_elemento(consulta, valores)
        if resultado[1] == contrasena:
            print('Ingreso valido')
        else:
            print('Ingreso invalido')
        
           
objeto = UsuarioDAO()
objeto.login_usuario('leocam10','sipa2025')


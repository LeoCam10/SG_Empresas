import sys
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Modelo")

from Modelo.usuarioDAO import UsuarioDAO
from Modelo.usuario import Usuario
from Controlador.controlador_ventana_principal import Controlar_ventana_principal
from Visual.ventana_inicio_sesion import Ventana_inicio_sesion

class Controlador_inicio_sesion:
    def __init__(self):
        self.__vista = Ventana_inicio_sesion(self)
        self.__vista.show()
        
        
    def validar_entrada(self):
        usuario_dao = UsuarioDAO()
        self.usuario =  self.__vista.label_ingreso_usuario.text()
        self.contrasena =self.__vista.label_ingreso_contrasena.text()
        print(f'llegue a capturar el nombre {self.usuario}')  
        print(f'llegue a capturar el nombre {self.contrasena}') 
        
        resultado = usuario_dao.obtener_personal_usuario(self.usuario)
        print(resultado)
        
    
       
        valido = usuario_dao.login_usuario(self.usuario,self.contrasena)
        print(valido)
        if valido:
                self.usuario_logueado = Usuario(resultado)
                self.inicio = Controlar_ventana_principal(self,"leonardo")
                return self.__vista.close()
        else:
            print(f'error al iniciar sesion')

            
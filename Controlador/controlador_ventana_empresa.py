from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import sys
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
import Controlador.controlador_ventana_eliminar_empresa
from Visual.ventana_empresa import Ventana_empresa
#from Visual.ventana_inicio_sesion import Ventana_inicio_sesion
import Controlador.controlador_ventana_modificar_empresa
import Controlador.controlador_ventana_agregar_empresa
import Controlador.controlador_ventana_eliminar_empresa

class Controlador_ventana_empresa:
    def __init__(self,controlador):
        self.__vista = Ventana_empresa()
        self.__vista.boton_alta_empresa.clicked.connect(self.abrir_ingreso_empresa)
        self.__vista.boton_baja_empresa.clicked.connect(self.abrir_eliminar_empresa)
        self.__vista.boton_modificacion_empresa.clicked.connect(self.abrir_modificar_empresa)
        
    def abrir_ingreso_empresa(self):
        self.ventana_agregar_empresa = Controlador.controlador_ventana_agregar_empresa.Controlador_ventana_agregar_empresa(self)
        
    def abrir_eliminar_empresa(self):
        self.ventana_eliminar_empresa = Controlador.controlador_ventana_eliminar_empresa.Controlador_ventana_eliminar_empresa(self)
        
    def abrir_modificar_empresa(self):
        self.ventana_modificar_empresa = Controlador.controlador_ventana_modificar_empresa.Controlador_ventana_modificar_empresa(self)
    
    def obtener_vista(self):
        return self.__vista     
    
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import sys
import os
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Modelo")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Modelo.empresaDAO import EmpresaDAO
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
        self.cargar_datos_empresa()
        
    def cargar_datos_empresa(self):
        empresas = EmpresaDAO()
        datos = empresas.obtener_empresas()
                   
        self.__vista.tabla_empresa.setRowCount(0)  # Limpia la tabla antes de llenarla
        for fila_num, fila_datos in enumerate(datos):
            self.__vista.tabla_empresa.insertRow(fila_num)
            for columna_num, dato in enumerate(fila_datos):
                self.__vista.tabla_empresa.setItem(fila_num, columna_num, QTableWidgetItem(str(dato)))

        
    def abrir_ingreso_empresa(self):
        self.ventana_agregar_empresa = Controlador.controlador_ventana_agregar_empresa.Controlador_ventana_agregar_empresa(self)
        
    def abrir_eliminar_empresa(self):
        self.ventana_eliminar_empresa = Controlador.controlador_ventana_eliminar_empresa.Controlador_ventana_eliminar_empresa(self)
        
    def abrir_modificar_empresa(self):
        self.ventana_modificar_empresa = Controlador.controlador_ventana_modificar_empresa.Controlador_ventana_modificar_empresa(self)
    
    def obtener_vista(self):
        return self.__vista     
    
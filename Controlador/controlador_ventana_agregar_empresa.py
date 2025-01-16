from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import sys
import os
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Visual.ventana_agregar_empresa import Ventana_agregar_empresa
from Modelo.empresaDAO import EmpresaDAO
#from Visual.ventana_inicio_sesion import Ventana_inicio_sesion
#import Controlador.controlador_inicio_sesion


class Controlador_ventana_agregar_empresa:
    def __init__(self,controlador):
        self.__vista = Ventana_agregar_empresa(self)
        self.__vista.show()
                
    def validar_entrada(self):
        
        # Captura los datos de cada campo
        self.habilitacion = self.__vista.ingreso_habilitacion_empresa.text()
        self.nombre_empresa = self.__vista.ingreso_nombre_empresa.text()
        self.tipo_empresa = self.__vista.ingreso_tipo_empresa.currentText()
        self.cuit = self.__vista.ingreso_cuit_empresa.text()
        self.direccion = self.__vista.ingreso_direccion_empresa.text()
        self.telefono = self.__vista.ingreso_telefono_empresa.text()
        self.email = self.__vista.ingreso_email_empresa.text()
        self.nombre_apoderado = self.__vista.ingreso_nombre_apoderado.text()
        self.dni_apoderado = self.__vista.ingreso_dni_apoderado.text()
            
       # print(f'{habilitacion} {tipo_empresa} {dni_apoderado} {dni_apoderado} {email} {telefono}')
        
        empresa = EmpresaDAO()
        tipos_empresa = empresa.obtener_tipo_empresas()
        empresas_existentes = empresa.obtener_empresas()
        self.validar_ingreso_habilitaciones = True
        for tipo in empresas_existentes:
            if tipo[0] == self.habilitacion:
                self.validar_entrada_habilitaciones = False
                break
        if not self.validar_entrada:
            self.__vista.error_ingreso_habilitacion_empresa.setText('La empresa ya se encuentra registrada')
            QTimer.singleShot(3000, lambda :self.__vista.error_ingreso_habilitacion_empresa.setVisible(False))
            
                
        
        
        self.ingreso_tipo = None
        for orden,tipo in enumerate(tipos_empresa):
            if tipo[1] == self.tipo_empresa:
                self.ingreso_tipo = tipo[0]
                print(f'el ingreso del tipo es {self.ingreso_tipo}')
                break 
        empresa.agregar_empresa(self.habilitacion,self.nombre_empresa,self.ingreso_tipo,self.cuit,self.direccion,self.telefono,self.email,self.nombre_apoderado,int(self.dni_apoderado),6619)
        
        

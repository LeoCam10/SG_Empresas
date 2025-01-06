from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import sys
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
from Visual.ventana_modificar_empresa import Ventana_modificar_empresa
#from Visual.ventana_inicio_sesion import Ventana_inicio_sesion
#import Controlador.controlador_inicio_sesion


class Controlador_ventana_modificar_empresa:
    def __init__(self,controlador):
        self.__vista = Ventana_modificar_empresa()
        self.__vista.show()
        
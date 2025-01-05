import sys
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
from Visual.ventana_principal import Ventana_Principal
from Visual.ventana_inicio_sesion import Ventana_inicio_sesion
import Controlador.controlador_inicio_sesion


class Controlar_ventana_principal:
    def __init__(self,controlador, nombre):
        self.__vista = Ventana_Principal(self,"leonardo")
        self.__vista.show()
        self.__vista.label_horizonta_arriba_4.clicked.connect(self.cerrar_sesion)
        
        
    def cerrar_sesion(self):
        self.ventana = Controlador.controlador_inicio_sesion.Controlador_inicio_sesion()
        self.__vista.close()
        
       
        

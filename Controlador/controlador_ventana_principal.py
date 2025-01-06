

import sys
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Controlador")
sys.path.append(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual")
from Visual.ventana_principal import Ventana_Principal
from Visual.ventana_inicio_sesion import Ventana_inicio_sesion
from Visual.ventana_empresa import Ventana_empresa
import Controlador.controlador_inicio_sesion
import Controlador.controlador_ventana_empresa


class Controlador_ventana_principal:
    def __init__(self,controlador, nombre):
        self.__vista = Ventana_Principal(self,"leonardo")
        self.__vista.show()
        self.__vista.label_horizonta_arriba_4.clicked.connect(self.cerrar_sesion)
        self.__vista.boton_primer_contenedor_bajo_1.clicked.connect(self.cambio_a_personal)
        
    
    def cambio_a_personal(self):     
        self.controlador_ventana_empresa = Controlador.controlador_ventana_empresa.Controlador_ventana_empresa(self)   
        self.vista_empresa = self.controlador_ventana_empresa.obtener_vista()
        self.__vista.stacked_layout.addWidget(self.vista_empresa)
        self.__vista.stacked_layout.setCurrentWidget(self.vista_empresa)
        

    def cerrar_sesion(self):
        self.ventana = Controlador.controlador_inicio_sesion.Controlador_inicio_sesion()
        self.__vista.close()
        
       
        

         
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
class Ventana_empresa(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Ventana Empresas')
        self.setFixedSize(1200,600)
        self.contenedor_principal = QHBoxLayout()
        self.contenedor_1 = QVBoxLayout()
        self.contenedor_2= QVBoxLayout()
      
        self.tabla_empresa = QTableWidget()
        self.tabla_empresa.setColumnCount(10)
        self.tabla_empresa.setRowCount(10)
        self.tabla_empresa.setHorizontalHeaderLabels(['nro_habilitacion', 'nombre', 'tipo_empresa', 'cuit', 'direccion', 'telefono', 'email', 'nombre_apoderado', 'dni_apoderado', 'legajo'])
        
        self.boton_alta_empresa = QPushButton()
        self.boton_alta_empresa.setFixedSize(180,150)
        self.boton_alta_empresa.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_alta_empresa = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\alta")).scaled(QSize(170,120))
        #self.boton_alta_empresa.clicked.connect(self.ventana_agregar_usuario)
        self.boton_alta_empresa.setIcon(QIcon(self.imagen_boton_alta_empresa))
        self.boton_alta_empresa.setIconSize(self.boton_alta_empresa.size())
        
        self.label_boton_alta_empresa = QLabel("Alta")
        self.label_boton_alta_empresa.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_boton_alta_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_boton_alta_empresa.setFixedSize(180,50)
        self.contenedor_alta_empresa= QVBoxLayout()
        self.contenedor_alta_empresa.setSpacing(0)
        self.contenedor_alta_empresa.addWidget(self.boton_alta_empresa,alignment=Qt.AlignmentFlag.AlignCenter)
        self.contenedor_alta_empresa.addWidget(self.label_boton_alta_empresa)
        self.contenedor_alta_empresa.setContentsMargins(0,0,0,0)
        
        
        
        self.boton_baja_empresa = QPushButton()
        self.boton_baja_empresa.setFixedSize(180,150)
        self.boton_baja_empresa.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        #self.boton_primer_contenedor_bajo_2.clicked.connect((lambda: self.cambiar_pantalla(2)))
        self.imagen_boton_baja_empresa = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\baja")).scaled(QSize(170,120))
        self.boton_baja_empresa.setIcon(QIcon(self.imagen_boton_baja_empresa))
        self.boton_baja_empresa.setIconSize(self.boton_baja_empresa.size())
                                                        
        self.label_boton_baja_empresa = QLabel("Baja")
        self.label_boton_baja_empresa.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_boton_baja_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_boton_baja_empresa.setFixedSize(180,50)
        self.contenedor_baja_empresa = QVBoxLayout()
        self.contenedor_baja_empresa.setSpacing(0)
        self.contenedor_baja_empresa.addWidget(self.boton_baja_empresa,alignment=Qt.AlignmentFlag.AlignCenter)
        self.contenedor_baja_empresa.addWidget(self.label_boton_baja_empresa)
        
        #######################################################################################33
        self.boton_modificacion_empresa = QPushButton()
        self.boton_modificacion_empresa.setFixedSize(180,150)
        self.boton_modificacion_empresa.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_modificacion_empresa = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\modificacion")).scaled(QSize(170,120))
       # self.boton_primer_contenedor_bajo_3.clicked.connect((lambda: self.cambiar_pantalla(3)))
        self.boton_modificacion_empresa.setIcon(QIcon(self.imagen_boton_modificacion_empresa))
        self.boton_modificacion_empresa.setIconSize(self.boton_modificacion_empresa.size())
        
        self.label_boton_modificacion_empresa = QLabel("Modificacion")
        self.label_boton_modificacion_empresa.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_boton_modificacion_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_boton_modificacion_empresa.setFixedSize(180,50)
        self.contenedor_modifcacion_empresa = QVBoxLayout()
        self.contenedor_modifcacion_empresa.addWidget(self.boton_modificacion_empresa,alignment=Qt.AlignmentFlag.AlignCenter)
        self.contenedor_modifcacion_empresa.addWidget(self.label_boton_modificacion_empresa)
        self.contenedor_modifcacion_empresa.setSpacing(0)
        self.contenedor_modifcacion_empresa.setContentsMargins(0, 0, 0, 0)
        
        self.contenedor_1.addWidget(self.tabla_empresa)
        self.contenedor_2.addLayout(self.contenedor_alta_empresa)
        self.contenedor_2.addLayout(self.contenedor_baja_empresa)
        self.contenedor_2.addLayout(self.contenedor_modifcacion_empresa)
        self.contenedor_2.setContentsMargins(0,0,0,0)
        self.contenedor_principal = QHBoxLayout()
        self.contenedor_principal.addLayout(self.contenedor_1)
        self.contenedor_principal.addLayout(self.contenedor_2)
        self.pantalla_central = QWidget()
        self.pantalla_central.setLayout(self.contenedor_principal)
        self.setCentralWidget(self.pantalla_central)
            

        
            
        
           
 
        
app  = QApplication([])
window = Ventana_empresa()
window.show()
app.exec()
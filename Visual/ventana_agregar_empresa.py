from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Ventana_agregar_usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(' ')
        self.setFixedSize(600,600)
        self.contenedor_principal = QVBoxLayout()
        self.formulario = QFormLayout()
        self.titulo = QLabel("Complete el formulario")
        self.espacio = QLabel()
        self.habilitacion_empresa = QLabel('Habilitacion')
        self.ingreso_habilitacion_empresa = QLineEdit()
        self.ingreso_habilitacion_empresa.setPlaceholderText('Ingrese la habilitacion')
        self.ingreso_habilitacion_empresa.setFixedWidth(240)
        self.ingreso_habilitacion_empresa.setFixedHeight(40)
        
        self.contenedor_nombre_tipo = QHBoxLayout()
        self.nombre_empresa = QLabel('Nombre')
        self.nombre_empresa.setFixedWidth(240)
        self.tipo_empresa = QLabel('Tipo')
        self.tipo_empresa.setFixedWidth(240)
        self.contenedor_nombre_tipo.addWidget(self.nombre_empresa)
        self.contenedor_nombre_tipo.addWidget(self.tipo_empresa)
        
        self.contenedor_ingreso_nombre_tipo= QHBoxLayout()
        self.ingreso_nombre_empresa = QLineEdit()
        self.ingreso_nombre_empresa.setPlaceholderText('Ingrese el nombre ')
        self.ingreso_nombre_empresa.setFixedWidth(240)
        self.ingreso_nombre_empresa.setFixedHeight(40)
        self.ingreso_tipo_empresa = QGroupBox() 
        self.contenedor_ingreso_nombre_tipo.addWidget(self.ingreso_nombre_empresa)
        self.contenedor_ingreso_nombre_tipo.addWidget(self.ingreso_tipo_empresa)
        
        self.contenedor_cuit_direccion = QHBoxLayout()
        self.cuit_empresa = QLabel('Cuit')
        self.cuit_empresa.setFixedWidth(240)
        self.direccion_empresa = QLabel('Direccion')
        self.direccion_empresa.setFixedWidth(240)
        self.contenedor_cuit_direccion.addWidget(self.cuit_empresa)
        self.contenedor_cuit_direccion.addWidget(self.direccion_empresa)
        
        self.contenedor_ingreso_cuit_direccion= QHBoxLayout()
        self.ingreso_cuit_empresa = QLineEdit()
        self.ingreso_cuit_empresa.setPlaceholderText('Ingrese el cuit ')
        self.ingreso_cuit_empresa.setFixedWidth(240)
        self.ingreso_cuit_empresa.setFixedHeight(40)
        self.ingreso_direccion_empresa = QLineEdit()
        self.ingreso_direccion_empresa.setPlaceholderText('Ingrese la direccion ')
        self.ingreso_direccion_empresa.setFixedWidth(240)
        self.ingreso_direccion_empresa.setFixedHeight(40)
        self.contenedor_ingreso_cuit_direccion.addWidget(self.ingreso_cuit_empresa)
        self.contenedor_ingreso_cuit_direccion.addWidget(self.ingreso_direccion_empresa)
        
        
        self.contenedor_telefono_email = QHBoxLayout()
        self.telefono_empresa = QLabel('Telefono')
        self.telefono_empresa.setFixedWidth(240)
        self.email_empresa = QLabel('Email')
        self.email_empresa.setFixedWidth(240)
        self.contenedor_telefono_email.addWidget(self.telefono_empresa)
        self.contenedor_telefono_email.addWidget(self.email_empresa)
        
        self.contenedor_ingreso_telefono_email= QHBoxLayout()
        self.ingreso_telefono_empresa = QLineEdit()
        self.ingreso_telefono_empresa.setPlaceholderText('Ingrese el telefono ')
        self.ingreso_telefono_empresa.setFixedWidth(240)
        self.ingreso_telefono_empresa.setFixedHeight(40)
        self.ingreso_email_empresa = QLineEdit()
        self.ingreso_email_empresa.setPlaceholderText('Ingrese el email ')
        self.ingreso_email_empresa.setFixedWidth(240)
        self.ingreso_email_empresa.setFixedHeight(40)
        self.contenedor_ingreso_telefono_email.addWidget(self.ingreso_telefono_empresa)
        self.contenedor_ingreso_telefono_email.addWidget(self.ingreso_email_empresa)
        
        self.contenedor_apoderado_dni = QHBoxLayout()
        self.nombre_apoderado = QLabel('Nombre Apoderado')
        self.nombre_apoderado.setFixedWidth(240)
        self.dni_apoderado = QLabel('Dni Apoderado')
        self.dni_apoderado.setFixedWidth(240)
        self.contenedor_apoderado_dni.addWidget(self.nombre_apoderado)
        self.contenedor_apoderado_dni.addWidget(self.dni_apoderado)
        
        self.contenedor_ingreso_apoderado_dni= QHBoxLayout()
        self.ingreso_nombre_apoderado = QLineEdit()
        self.ingreso_nombre_apoderado.setPlaceholderText('Ingrese el nombre del apoderado ')
        self.ingreso_nombre_apoderado.setFixedWidth(240)
        self.ingreso_nombre_apoderado.setFixedHeight(40)
        self.ingreso_dni_apoderado= QLineEdit()
        self.ingreso_dni_apoderado.setPlaceholderText('Ingrese el email ')
        self.ingreso_dni_apoderado.setFixedWidth(240)
        self.ingreso_dni_apoderado.setFixedHeight(40)
        self.contenedor_ingreso_apoderado_dni.addWidget(self.ingreso_nombre_apoderado)
        self.contenedor_ingreso_apoderado_dni.addWidget(self.ingreso_dni_apoderado)
        
        self.contenedor_boton_validar_ingreso = QHBoxLayout()
        self.boton_validar_ingreso = QPushButton('Registrar',self)
        self.boton_validar_ingreso.setFixedSize(300,50)    
        #self.boton_iniciar_sesion.clicked.connect(controlador.validar_entrada)  
        self.boton_validar_ingreso.setStyleSheet("background: #3391df;color: white;font-size: 18px;padding: 10px 20px")
        self.contenedor_boton_validar_ingreso.addWidget(self.boton_validar_ingreso,alignment=Qt.AlignmentFlag.AlignCenter )
        
        
        self.formulario.addRow(self.titulo)
        self.formulario.addRow(self.espacio)
      
        self.formulario.addRow(self.habilitacion_empresa)
        self.formulario.addRow(self.ingreso_habilitacion_empresa)
        
        
        self.formulario.addRow(self.contenedor_nombre_tipo)
        self.formulario.addRow(self.contenedor_ingreso_nombre_tipo)
   
        self.formulario.addRow(self.contenedor_cuit_direccion)
        self.formulario.addRow(self.contenedor_ingreso_cuit_direccion)
 
        self.formulario.addRow(self.contenedor_telefono_email)
        self.formulario.addRow(self.contenedor_ingreso_telefono_email)
  
        self.formulario.addRow(self.contenedor_apoderado_dni)
        self.formulario.addRow(self.contenedor_ingreso_apoderado_dni)
        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.contenedor_boton_validar_ingreso)
        
        
        
        
        self.contenedor_principal.addLayout(self.formulario)
        self.pantalla_principal = QWidget()
        self.pantalla_principal.setStyleSheet('background: black ; color : white; font-size: 20px;')
        self.pantalla_principal.setLayout(self.contenedor_principal)
        self.setCentralWidget(self.pantalla_principal)
 
 
 
                
app  = QApplication([])
window = Ventana_agregar_usuario()
window.show()
app.exec()
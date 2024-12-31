from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *




class Ventana_inicio_sesion(QMainWindow):
    def __init__(self,controlador):
        super().__init__()
        
        
        self.setWindowTitle("Estacion de Salvamento, Incedio y Proteccion Ambiental CRIV")
        self.setFixedSize(1200,600)
        alto = self.frameGeometry().height()
        ancho = self.frameGeometry().width()
                
            
        self.label_bomberos = QLabel(self)
        self.label_bomberos.setPixmap(QPixmap(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\imagen_sipa"))
        self.label_bomberos.setFixedHeight(alto-60)
        self.label_bomberos.setFixedWidth(ancho//2) 
        self.label_bomberos.setScaledContents(True)
     
        
        self.label_bienvenido = QLabel('¡Te damos la bienvenida!')
        self.label_bienvenido.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_bienvenido.setStyleSheet("color :#050200; font-size : 30px ;margin: 0px; padding: 0px  ")
        self.label_bienvenido.setFixedHeight(50)
        self.label_bienvenido.setFixedWidth(600)
        self.label_usuario =  QLabel('Usuario')
        self.label_usuario.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_usuario.setStyleSheet("color :#a9a7a7; font-size : 25px ;margin: 0px; padding: 0px")
        self.label_usuario.setFixedHeight(27)
        #self.label_usuario.setFixedSize(350,35)
        self.label_ingreso_usuario = QLineEdit('leocam10')
        self.label_ingreso_usuario.setStyleSheet("background: #d7d0b7; color : #a9a7a7; font-size : 25px ; border:none ")
        self.label_ingreso_usuario.setAlignment(Qt.AlignmentFlag.AlignLeft )
        #self.label_ingreso_usuario.setFixedHeight(30)
        self.label_ingreso_usuario.setFixedSize(300,30)
        self.label_ingreso_usuario.setPlaceholderText('Ingresá tu usuario')
        self.label_contrasena =  QLabel('Contraseña')
        self.label_contrasena.setAlignment(Qt.AlignmentFlag.AlignLeft )
        self.label_contrasena.setStyleSheet("color :#a9a7a7; font-size : 25px  ") 
        self.label_contrasena.setFixedHeight(27)  
        #self.label_contrasena.setFixedSize(385,35)
        self.label_ingreso_contrasena = QLineEdit('sipa2025')
        self.label_ingreso_contrasena.setStyleSheet("background: #d7d0b7;color :#a9a7a7; font-size : 25px  ;border:none  ")
        self.label_ingreso_contrasena.setAlignment(Qt.AlignmentFlag.AlignLeft )
        self.label_ingreso_contrasena.setPlaceholderText('Ingresá tu contraseña')
        self.label_ingreso_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        #self.label_ingreso_contrasena.setFixedHeight(30)   
        self.label_ingreso_contrasena.setFixedSize(300,30)    
        self.label_olvido_contrasena = QLabel(' ¿Olvidaste tu contraseña?')
        self.label_olvido_contrasena.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_olvido_contrasena.setStyleSheet("color :#cf0606 ;font-size : 25px ") 
        self.label_olvido_contrasena.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.label_olvido_contrasena.setFixedHeight(35)
        #self.label_olvido_contrasena.setFixedSize(520,35) 
        self.boton_iniciar_sesion = QPushButton('Iniciar sesión',self)
        self.boton_iniciar_sesion.setFixedSize(300,50)    
        self.boton_iniciar_sesion.clicked.connect(controlador.validar_entrada)   

        self.boton_iniciar_sesion.setStyleSheet("background: #3391df;color: white;font-size: 18px;padding: 10px 20px")                            
         
        self.label_leyenda = QLabel('      Consultá acerca de las empresas, sus vencimientos, caracteristicas de trabajo y personal interviniente.', self)
        self.label_leyenda.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    spread: pad,
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #666666,
                    stop: 0.5 #8c8c8c,
                    stop: 1 #b5b5b5);
                color: white;             /* Color del texto */
                font-size: 18px;          /* Tamaño del texto */               
            }
        """)
        self.label_leyenda.setFixedHeight(60)
        
        self.contenedor_imagen= QVBoxLayout()
        self.contenedor_login= QVBoxLayout()
        self.contenedor_vertical = QVBoxLayout()
        self.contenedor_horizontal = QHBoxLayout()  
       # self.espacio = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        #self.contenedor_login.addSpacerItem(self.espacio)
        # Ajustar los márgenes del layout (izquierda, arriba, derecha, abajo)
        #self.spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        # Ajustar márgenes y espaciado
        self.contenedor_login.setContentsMargins(150, 0, 0, 0) 
        # Márgenes: izquierda, arriba, derecha, abajo
        #self.contenedor_login.setSpacing(0)  # Sin espacio entre widgets

        
        self.contenedor_login.addWidget(self.label_bienvenido)
        self.contenedor_login.addWidget(self.label_usuario)
        self.contenedor_login.addWidget(self.label_ingreso_usuario)
        self.contenedor_login.addWidget(self.label_contrasena)
        self.contenedor_login.addWidget(self.label_ingreso_contrasena)
        self.contenedor_login.addWidget(self.label_olvido_contrasena)
        self.contenedor_login.addWidget(self.boton_iniciar_sesion)
        #self.contenedor_login.addItem(self.spacer)
        
        
        self.contenedor_horizontal.addWidget(self.label_bomberos)
        self.contenedor_horizontal.addLayout(self.contenedor_login)
        self.contenedor_vertical.addLayout(self.contenedor_horizontal)
        self.contenedor_vertical.addWidget(self.label_leyenda)
        self.contenedor_vertical.setContentsMargins(0,0,0,0)
        
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.contenedor_vertical)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet(""" QWidget {
                background: #d7d0b7""")
"""        
app = QApplication([])
window = Ventana_inicio_sesion()
window.show()
app.exec()
"""
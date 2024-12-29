from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Ventana_Principal(QMainWindow):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.setWindowTitle('Ventana Principal')
        self.setFixedSize(1200,600)
        
        self.alto = self.frameGeometry().height()
        self.ancho = self.frameGeometry().width()
        
    
        self.label_horizonta_arriba_1 = QLabel(self.nombre)
        self.label_horizonta_arriba_1.setFixedSize(700,60)
        self.label_horizonta_arriba_1.setStyleSheet('background-color: #FFFFFF; border: none; color: black; font-size: 30px; ')
        
        self.label_horizonta_arriba_5= QPushButton()
        self.label_horizonta_arriba_5.setFixedSize(60,50)
        
        self.imagen_horizonta_arriba_5 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\usuario")).scaled((QSize(58,48)))
        self.label_horizonta_arriba_5.setIcon(QIcon(self.imagen_horizonta_arriba_5))
        self.label_horizonta_arriba_5.setIconSize(self.label_horizonta_arriba_5.size())
        
        self.label_horizonta_arriba_2= QPushButton()
        self.label_horizonta_arriba_2.setFixedSize(60,50)
        self.imagen_horizonta_arriba_2 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\inicio")).scaled(QSize(58,48))
        self.label_horizonta_arriba_2.setStyleSheet(""" QPushButton:hover {  border: 3px solid blue}  """)
        self.label_horizonta_arriba_2.setIcon(QIcon(self.imagen_horizonta_arriba_2))
        self.label_horizonta_arriba_2.setIconSize(self.label_horizonta_arriba_2.size())
        
        self.label_horizonta_arriba_3= QPushButton()
        self.label_horizonta_arriba_3.setFixedSize(60,50)
        self.imagen_horizonta_arriba_3 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\reglamento")).scaled(QSize(58,48))
        self.label_horizonta_arriba_3.setStyleSheet(""" QPushButton:hover {  border: 3px solid blue}  """) 
        self.label_horizonta_arriba_3.setIcon(QIcon(self.imagen_horizonta_arriba_3))
        self.label_horizonta_arriba_3.setIconSize(self.label_horizonta_arriba_3.size())
       
        self.label_horizonta_arriba_4= QPushButton()
        self.label_horizonta_arriba_4.setFixedSize(60,50)
        self.imagen_horizonta_arriba_4 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\salir")).scaled(QSize(58,48))
        self.label_horizonta_arriba_4.setStyleSheet(""" QPushButton:hover {  border: 3px solid blue}  """)
        self.label_horizonta_arriba_4.setIcon(QIcon(self.imagen_horizonta_arriba_4))
        self.label_horizonta_arriba_4.setIconSize(self.label_horizonta_arriba_4.size())
    
        self.contenedor_horizontal_arriba = QHBoxLayout()
        self.contenedor_horizontal_arriba.addWidget(self.label_horizonta_arriba_5)
        self.contenedor_horizontal_arriba.addWidget(self.label_horizonta_arriba_1)
        self.contenedor_horizontal_arriba.addWidget(self.label_horizonta_arriba_2)
        self.contenedor_horizontal_arriba.addWidget(self.label_horizonta_arriba_3)
        self.contenedor_horizontal_arriba.addWidget(self.label_horizonta_arriba_4)
        self.contenedor_horizontal_arriba.setContentsMargins(0,0,0,0)
        
        
        self.label_horizontal_medio_1 = QLabel()
        self.label_horizontal_medio_1.setPixmap(QPixmap(r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\gestor"))
        self.label_horizontal_medio_1.setFixedSize(self.ancho,100)
        self.label_horizontal_medio_1.setScaledContents(True)
        self.contenedor_horizontal_media = QHBoxLayout()
        self.contenedor_horizontal_media.addWidget(self.label_horizontal_medio_1)
        self.contenedor_horizontal_media.setContentsMargins(0,0,0,0)
        
        #############################
        self.boton_primer_contenedor_bajo_1 = QPushButton()
        self.boton_primer_contenedor_bajo_1.setFixedSize(180,150)
        self.boton_primer_contenedor_bajo_1.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_primer_contenedor_bajo_1 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\empresas")).scaled(QSize(170,120))
        self.boton_primer_contenedor_bajo_1.setIcon(QIcon(self.imagen_boton_primer_contenedor_bajo_1))
        self.boton_primer_contenedor_bajo_1.setIconSize(self.boton_primer_contenedor_bajo_1.size())
        
        self.label_primer_contenedor_bajo_1 = QLabel("Empresas")
        self.label_primer_contenedor_bajo_1.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_primer_contenedor_bajo_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_primer_contenedor_bajo_1.setFixedSize(180,50)
        self.primer_contenedor_bajo_1 = QVBoxLayout()
        self.primer_contenedor_bajo_1.setSpacing(0)
        self.primer_contenedor_bajo_1.addWidget(self.boton_primer_contenedor_bajo_1,alignment=Qt.AlignmentFlag.AlignCenter)
        self.primer_contenedor_bajo_1.addWidget(self.label_primer_contenedor_bajo_1)
        
        
        
        self.boton_primer_contenedor_bajo_2 = QPushButton()
        self.boton_primer_contenedor_bajo_2.setFixedSize(180,150)
        self.boton_primer_contenedor_bajo_2.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_primer_contenedor_bajo_2 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\vencimientos")).scaled(QSize(170,120))
        self.boton_primer_contenedor_bajo_2.setIcon(QIcon(self.imagen_boton_primer_contenedor_bajo_2))
        self.boton_primer_contenedor_bajo_2.setIconSize(self.boton_primer_contenedor_bajo_1.size())
                                                        
        self.label_primer_contenedor_bajo_2 = QLabel("Vencimientos")
        self.label_primer_contenedor_bajo_2.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_primer_contenedor_bajo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_primer_contenedor_bajo_2.setFixedSize(180,50)
        self.primer_contenedor_bajo_2 = QVBoxLayout()
        self.primer_contenedor_bajo_2.setSpacing(0)
        self.primer_contenedor_bajo_2.addWidget(self.boton_primer_contenedor_bajo_2,alignment=Qt.AlignmentFlag.AlignCenter)
        self.primer_contenedor_bajo_2.addWidget(self.label_primer_contenedor_bajo_2)
        
        self.boton_primer_contenedor_bajo_3 = QPushButton()
        self.boton_primer_contenedor_bajo_3.setFixedSize(180,150)
        self.boton_primer_contenedor_bajo_3.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_primer_contenedor_bajo_3 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\historial")).scaled(QSize(170,120))
        self.boton_primer_contenedor_bajo_3.setIcon(QIcon(self.imagen_boton_primer_contenedor_bajo_3))
        self.boton_primer_contenedor_bajo_3.setIconSize(self.boton_primer_contenedor_bajo_3.size())
        
        self.label_primer_contenedor_bajo_3 = QLabel("Historial")
        self.label_primer_contenedor_bajo_3.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_primer_contenedor_bajo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_primer_contenedor_bajo_3.setFixedSize(180,50)
        self.primer_contenedor_bajo_3 = QVBoxLayout()
        self.primer_contenedor_bajo_3.addWidget(self.boton_primer_contenedor_bajo_3,alignment=Qt.AlignmentFlag.AlignCenter)
        self.primer_contenedor_bajo_3.addWidget(self.label_primer_contenedor_bajo_3)
        self.primer_contenedor_bajo_3.setSpacing(0)
        self.primer_contenedor_bajo_3.setContentsMargins(0, 0, 0, 0)
        
  
        self.primer_contenedor_bajo = QHBoxLayout()
        self.primer_contenedor_bajo.addLayout(self.primer_contenedor_bajo_1)
        self.primer_contenedor_bajo.addLayout(self.primer_contenedor_bajo_2)
        self.primer_contenedor_bajo.addLayout(self.primer_contenedor_bajo_3)
        
        self.boton_segundo_contenedor_bajo_1 = QPushButton()
        self.boton_segundo_contenedor_bajo_1.setFixedSize(180,150)
        self.boton_segundo_contenedor_bajo_1.setStyleSheet("""QPushButton { background: white; padding: 0px} QPushButton:hover {  border: 3px solid blue}  """)
        self.imagen_boton_segundo_contenedor_bajo_1 = QPixmap((r"C:\Users\camus\Desktop\SG_Empresas-main\Visual\Imagenes\personal")).scaled(QSize(170,120))
        self.boton_segundo_contenedor_bajo_1.setIcon(QIcon(self.imagen_boton_segundo_contenedor_bajo_1))
        self.boton_segundo_contenedor_bajo_1.setIconSize(self.boton_segundo_contenedor_bajo_1.size())
        
        self.label_segundo_contenedor_bajo_1 = QLabel("Personal")
        self.label_segundo_contenedor_bajo_1.setStyleSheet('color : white;background: black; font-size : 25px')
        self.label_segundo_contenedor_bajo_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_segundo_contenedor_bajo_1.setFixedSize(180,50)
        self.segundo_contenedor_bajo_1 = QVBoxLayout()
        self.segundo_contenedor_bajo_1.setSpacing(0)
        self.segundo_contenedor_bajo_1.addWidget(self.boton_segundo_contenedor_bajo_1,alignment=Qt.AlignmentFlag.AlignCenter)
        self.segundo_contenedor_bajo_1.addWidget(self.label_segundo_contenedor_bajo_1)
        
        self.segundo_contenedor_bajo = QHBoxLayout()
        self.segundo_contenedor_bajo.setSpacing(0)
        self.segundo_contenedor_bajo.addLayout(self.segundo_contenedor_bajo_1)
        
        self.contenedor_bajo = QVBoxLayout()
        self.contenedor_bajo.setContentsMargins(10,10,10,10)       
        self.contenedor_bajo.addLayout(self.primer_contenedor_bajo)
        self.contenedor_bajo.addLayout(self.segundo_contenedor_bajo)
      
          
        #############################
        
        self.contenedor_principal= QVBoxLayout()
        self.contenedor_principal.addLayout(self.contenedor_horizontal_arriba)
        self.contenedor_principal.addLayout(self.contenedor_horizontal_media)
        self.contenedor_principal.addLayout(self.contenedor_bajo)
        self.contenedor_principal.setContentsMargins(0,10,0,20)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.contenedor_principal)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet(""" QWidget {
                background-color: #FFFFFF; border: none }""")
           
app = QApplication([])
window = Ventana_Principal('Leonardo')
window.show()
app.exec()
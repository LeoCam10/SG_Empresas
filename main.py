
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *



from Controlador.controlador_inicio_sesion import Controlador_inicio_sesion
from Modelo.usuarioDAO import UsuarioDAO


app = QApplication([])
ventana = Controlador_inicio_sesion()
app.exec()
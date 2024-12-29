import sys
sys.path.append('C://Users//camus//Desktop//SG_Empresas-main//Modelo')
from base_de_datos import BaseDeDatos

class empresaDao:
    def __init__(self):
        self.base = BaseDeDatos()
        
    def agregar_empresa(self,nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo):
        consulta = '''INSERT INTO public.empresa (nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        valores = (nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo)
        self.base.consulta(consulta, valores)
        print(f'se agrego la empresa {nombre} a la base de datos')

    def eliminar_empresa(self, nro_habilitacion):
        consulta = '''
        DELETE FROM public.empresa WHERE nro_habilitacion = %s; 
        '''
        valores = (nro_habilitacion,)
        self.base.consulta(consulta,valores)
        print(f'se eliminar la empresa {nro_habilitacion} de la base de datos')
     
    def modficar_empresa(self,nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo):
        consulta = '''
        UPDATE public.empresa
	    SET nro_habilitacion=%s, nombre=%s, tipo_empresa=%s, cuit=%s, direccion=%s, telefono=%s, email=%s, nombre_apoderado=%s, dni_apoderado=%s, legajo=%s
	    WHERE nro_habilitacion=%s;
        '''  
        valores = (nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo,nro_habilitacion)
        self.base.consulta(consulta,valores)
        print(f'se modifico correctamente la empresa {nombre} en la base de datos')   
        
    def obtener_empresa(self, nro_habilitacion):
        consulta = '''
        SELECT * FROM public.empresa WHERE nro_habilitacion = %s ;
        '''
        valores = (nro_habilitacion,) 
        resultado =self.base.obtener_un_elemento(consulta,valores)
        print(resultado)
        
    def obtener_empresas(self):
        consulta = '''
        SELECT * FROM public.empresa;
        '''
        resultado =self.base.obtener_elementos(consulta,valores=None)
        print(resultado)
        
empresa = empresaDao()
#empresa.agregar_empresa('A-42', 'Amarras S.A', 1, '30-67030271-3', 'AV. LAS TONINAS N°887 - COMODORO RIVADAVIA - PROVINCIA DEL CHUBUT', '0297-6239058', 'osvaldonunez@amarras.com.ar', 'NUÑEZ NORBERTO OSVALDO', 25011157, 6619)
#empresa.eliminar_empresa('A-42')
#empresa.modficar_empresa('A-42', 'Amarras S.R.L', 1, '30-67030271-3', 'AV. LAS TONINAS N°887 - COMODORO RIVADAVIA - PROVINCIA DEL CHUBUT', '0297-6239058', 'osvaldonunez@amarras.com.ar', 'NUÑEZ NORBERTO OSVALDO', 25011157, 6619)
#empresa.obtener_empresa('A-42')
#empresa.obtener_empresas()

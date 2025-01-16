import sys
sys.path.append('C://Users//camus//Desktop//SG_Empresas-main//Modelo')
from base_de_datos import BaseDeDatos

class EmpresaDAO:
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

        return resultado
    
    def obtener_tipo_empresas(self):
        consulta = '''
        SELECT * FROM public.tipo_empresa;
        '''
        resultado =self.base.obtener_elementos(consulta,valores=None)
        return resultado
    
empresa = EmpresaDAO()
empres = empresa.obtener_tipo_empresas()
print(empres)
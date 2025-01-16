import sys
from datetime import date
sys.path.append('C://Users//camus//Desktop//SG_Empresas-main//Modelo')
from base_de_datos import BaseDeDatos

class VencimientoDAO:
    def __init__(self):
        self.base = BaseDeDatos()
        
    def agregar_vencimiento(self,nro_habilitacion, certificado, fecha_validez, fecha_inicio_primera, fecha_fin_primera, funcionario_firma_primera, fecha_inicio_segunda, fecha_fin_segunda, funcionario_firma_segunda, observaciones_trabajo, legajo, inspeccion_primera, inspeccion_segunda):
        consulta = '''INSERT INTO public.vencimiento_empresa (nro_habilitacion, certificado, fecha_validez, fecha_inicio_primera, fecha_fin_primera, funcionario_firma_primera, fecha_inicio_segunda, fecha_fin_segunda, funcionario_firma_segunda, observaciones_trabajo, legajo, inspeccion_primera, inspeccion_segunda)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)'''
        valores = (nro_habilitacion, certificado, fecha_validez, fecha_inicio_primera, fecha_fin_primera, funcionario_firma_primera, fecha_inicio_segunda, fecha_fin_segunda, funcionario_firma_segunda, observaciones_trabajo, legajo, inspeccion_primera, inspeccion_segunda)
        self.base.consulta(consulta, valores)
        print(f'se agrego la empresa {certificado} a la base de datos')

    def eliminar_vencimiento(self, nro_habilitacion):
        consulta = '''
        DELETE FROM public.empresa WHERE nro_habilitacion = %s; 
        '''
        valores = (nro_habilitacion,)
        self.base.consulta(consulta,valores)
        print(f'se eliminar la empresa {nro_habilitacion} de la base de datos')
     
    def modficar_vencimiento(self,nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo):
        consulta = '''
        UPDATE public.empresa
	    SET nro_habilitacion=%s, nombre=%s, tipo_empresa=%s, cuit=%s, direccion=%s, telefono=%s, email=%s, nombre_apoderado=%s, dni_apoderado=%s, legajo=%s
	    WHERE nro_habilitacion=%s;
        '''  
        valores = (nro_habilitacion, nombre, tipo_empresa, cuit, direccion, telefono, email, nombre_apoderado, dni_apoderado, legajo,nro_habilitacion)
        self.base.consulta(consulta,valores)
        print(f'se modifico correctamente la empresa {nombre} en la base de datos')   
        
    def obtener_vencimiento(self, nro_habilitacion):
        consulta = '''
        SELECT * FROM public.empresa WHERE nro_habilitacion = %s ;
        '''
        valores = (nro_habilitacion,) 
        resultado =self.base.obtener_un_elemento(consulta,valores)
        print(resultado)
        
    def obtener_vencimientos(self):
        consulta = '''
        SELECT DISTINCT * FROM public.vencimiento_empresa;
        '''
        resultado =self.base.obtener_elementos(consulta,valores=None)
        return resultado
        
vencimiento = VencimientoDAO()
vencimiento.agregar_vencimiento("A-41","CE-2024-86605511-APN-DPSN#PNA"	, date(2027,8,13),	date(2025,5,13),	date(2025,11,3)	," ",	date(2026,5,13)	,date(2026,11,13)	," "," ",	6619	,True	, False)
#empresa.agregar_empresa('A-42', 'Amarras S.A', 1, '30-67030271-3', 'AV. LAS TONINAS N°887 - COMODORO RIVADAVIA - PROVINCIA DEL CHUBUT', '0297-6239058', 'osvaldonunez@amarras.com.ar', 'NUÑEZ NORBERTO OSVALDO', 25011157, 6619)
#empresa.eliminar_empresa('A-42')
#empresa.modficar_empresa('A-42', 'Amarras S.R.L', 1, '30-67030271-3', 'AV. LAS TONINAS N°887 - COMODORO RIVADAVIA - PROVINCIA DEL CHUBUT', '0297-6239058', 'osvaldonunez@amarras.com.ar', 'NUÑEZ NORBERTO OSVALDO', 25011157, 6619)
#empresa.obtener_empresa('A-42')
#empresa.obtener_empresas()

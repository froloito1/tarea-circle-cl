def validate_user(username, password):
    # Datos de usuario (en una aplicación real, esto estaría en una base de datos)
    users = {
        "luz": "123",
        "luz2": "1234"
    }

    if username in users and users[username] == password:
        return True
    else:
        return False
def validate_Create_user(cedula,nombre,apellido,direccion,telefono,username):
    # Datos de usuario (en una aplicación real, esto estaría en una base de datos)
        if username=="luz":
           if cedula=="" or nombre=="" or apellido=="" or direccion=="" or telefono=="":
                   return False
           else: 
                   if direccion=="suiza":return False
                   else: return True
        else: return False
def calcularServiciosConIva(higieneOral,ortodoncia):
    iva= (higieneOral+ortodoncia)*0.19
    valor=(higieneOral+ortodoncia)+iva
    if valor==357 :return True
    else :return False

def calcularServiciosSinIva(higieneOral,ortodoncia):
    valor=(higieneOral+ortodoncia)
    if valor==300:return True
    else : return False    

        

import login

def test_validate_user():
    # Caso de prueba válido
    assert login.validate_user("luz", "123") == True

    # Caso de prueba inválido (contraseña incorrecta)
    assert login.validate_user("luz2", "1234") == True

    # Caso de prueba inválido (usuario no existente)
    assert login.validate_user("luz3", "123") == False
    
def test_validate_Create_user():
    # Caso de prueba username existe
    assert login.validate_Create_user("12345","luz eliana","valencia","junin","123456789","luz") == True

    # Caso de prueba username existe (usuario incorrecto)
    assert login.validate_Create_user("12345","luz eliana","valencia","junin","123456789","luz1") == False
    
     # Caso de prueba cedula vacia
    assert login.validate_Create_user("","luz eliana","valencia","junin","123456789","luz") == False
    
     # Caso de prueba nombre vacio
    assert login.validate_Create_user("12345","","valencia","junin","123456789","luz") == False
    
    # Caso de prueba apellido vacio
    assert login.validate_Create_user("12345","luz eliana","","junin","123456789","luz") == False
    
    # Caso de prueba direccion incorrecta
    assert login.validate_Create_user("12345","luz eliana","valencia","suiza","123456789","luz") == True
    
    # Caso de prueba apellido vacio
    assert login.validate_Create_user("12345","luz eliana","valencia","junin","123456789","luz") == True

   
#if __name__=='__login__':
 #       test_validate_user()
 #       test_validate_Create_user()
        
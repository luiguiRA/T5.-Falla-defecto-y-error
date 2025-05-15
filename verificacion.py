usuarios = {
    "usuario1": "contrasena123",
    "admin": "adminpass"
}

def iniciar_sesion():
    intentos_restantes = 3

    while intentos_restantes > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # CORRECCIÓN del FALLO 1:
        # Se reemplaza el operador 'or' por 'and' para asegurar que:
        # 1. El usuario exista
        # 2. La contraseña coincida con la del usuario correspondiente
        if usuario in usuarios and usuarios.get(usuario) == contrasena:
            print("Inicio de sesión exitoso.")
            return True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

    # CORRECCIÓN del FALLO 2:
    # Se agrega un mensaje claro al usuario cuando ha agotado todos los intentos
    print("Acceso denegado. Ha superado el número máximo de intentos.")
    return False


iniciar_sesion()

usuarios = {
    "usuario1": "contrasena123",
    "admin": "adminpass"
}

def iniciar_sesion():
    intentos_restantes = 3

    while intentos_restantes > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # FALLO 1 (intencional):
        # DEFECTO: Usamos 'or' en lugar de 'and'. Esto permite el acceso si EITHER usuario o contraseña coinciden.
        # ERROR: Si el usuario es correcto pero la contraseña no lo es, se concede acceso.
        # FALLO: El sistema permite entrar a alguien con contraseña incorrecta.
        if usuario in usuarios or usuarios.get(usuario) == contrasena:
            print("Inicio de sesión exitoso.")
            return True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

    # FALLO 2 (intencional):
    # DEFECTO: El mensaje de acceso denegado no se imprime si se fallan los 3 intentos.
    # ERROR: El flujo llega al final de la función sin mostrar el mensaje al usuario.
    # FALLO: El usuario no sabe que el acceso fue definitivamente denegado.
    # Solución sería imprimir aquí un mensaje claro, pero está omitido a propósito.
    return False


iniciar_sesion()

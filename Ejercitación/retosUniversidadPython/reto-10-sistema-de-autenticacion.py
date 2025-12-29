USUARIO_CORRECTO = "admin"
PASSWORD_CORRECTO = "1234"

usuario = input("Usuario: ").strip()
password = input("Password: ").strip()

print((usuario == USUARIO_CORRECTO) and (password == PASSWORD_CORRECTO))
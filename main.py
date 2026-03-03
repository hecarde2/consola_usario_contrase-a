print("Bienvenido/a")
nombre_de_usuario = input("escriba su nombre de usuario: ")
contrasena = input("escriba una contraseña: ")

if len(contrasena) >= 8 and \
 any(letra.isupper() for letra in contrasena) and \
 any(letra.isdigit for letra in contrasena) and \
 any(letra in "@$-_*+" for letra in contrasena):
   print("usuario creado")
 
else:
    print(" La contraseña debe tener:")
    print("- Mínimo 8 caracteres")
    print("- Al menos una mayúscula")
    print("- Al menos un número")
    print("- Al menos un carácter especial (@, *, +)")


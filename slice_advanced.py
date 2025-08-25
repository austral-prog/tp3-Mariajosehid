def slice_advanced():
    texto = "Hello World!"
    texto = texto.lower()

    nombre = texto [4] + texto [5] + texto [4] + texto [-3] + texto [-1]
    print(nombre)

    texto = "1234567890"
    texto = texto.lower()

    nombre = texto [4] + texto [6] + texto [8] + texto [9]
    print(nombre)

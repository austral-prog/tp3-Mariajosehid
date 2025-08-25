def slice_simple():
    texto = "Awesome"
    texto = texto.lower()

    nombre = texto [0:3]
    print(nombre)

    nombre = texto [2:5]
    print(nombre)

    nombre = texto [0:4] + texto [-3:]
    print(nombre)

slice_simple()
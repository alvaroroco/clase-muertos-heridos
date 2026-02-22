from random import randint


def generar_num_aleatorio():
    num_aleatorio = "".join(str(randint(0, 9)) for _ in range(4))
    return num_aleatorio


def pedir_numero():
    while True:
        num_introducido = input("Por favor, introduce un número de 4 dígitos: ")
        if num_introducido.isnumeric() and len(num_introducido) == 4:
            return num_introducido

        print("El número introducido no es válido\n")


def calcular_muertos_heridos(num_pensado: str, num_usuario: str) -> tuple[bool, str]:
    if num_pensado == num_usuario:
        return True, "MMMM"

    muertos_heridos = ["V", "V", "V", "V"]
    for i in range(4):
        if num_pensado[i] == num_usuario[i]:
            muertos_heridos[i] = "M"
        elif num_usuario[i] in num_pensado[:i] + num_pensado[i + 1 :]:
            muertos_heridos[i] = "H"

    return False, "".join(muertos_heridos)


if __name__ == "__main__":
    intentos = 0
    ganador = False
    num_pensado = generar_num_aleatorio()

    while not ganador:
        intentos += 1
        num_usuario = pedir_numero()
        ganador, muertos_heridos = calcular_muertos_heridos(num_pensado, num_usuario)

        if not ganador:
            print(f"¡Incorrecto!\nTus muertos y heridos son: {muertos_heridos}")

    print(f"¡Enhorabuena! Lo has acertado en {intentos} intentos")

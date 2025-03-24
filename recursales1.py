
jugadores = [
    
]


def menu():
    print("\n TONREO DE TENIS ")
    print("1. Registrar jugador")
    print("2. Registrar puntos de sets ganados")
    print("3. Leaderboard")
    print("4. Salir")


def registrado():
    nombre = input("Nombre del jugador: ")
    
    # Verifica si el nombre ya existe
    if any(jugador["nombre"].lower() == nombre.lower() for jugador in jugadores):
        print(f" El jugador '{nombre}' ya existe, elige otro nombre.")
    else:
        jugadores.append({"nombre": nombre, "puntos": 0})
        print(f" El jugador '{nombre}' ha sido registrado.")


def asignar_puntos():
    nombre = input("Nombre del jugador al que se le asignan los puntos: ")
    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre.lower():
            puntos = int(input("Sets ganados a registrar: "))
            jugador["puntos"] += puntos
            print(f"{puntos} puntos registrados a '{nombre}'.")
            return
    print(f" '{nombre}' no existe, elige otro jugador.")


def tabla():
    if not jugadores:
        print(" Aun no existe jugadores registrados.")
        return
    
    print("\n Leaderborad:")
    orden = sorted(jugadores, key=lambda x: x["puntos"], reverse=True)
    
    for srs, jugador in enumerate(orden, start=1):
        print(f"{srs}. {jugador['nombre']} - {jugador['puntos']} puntos")


def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            registrado()
        elif opcion == "2":
            asignar_puntos()
        elif opcion == "3":
            tabla()
        elif opcion == "4":
            print(" ¡Hasta luego! vuelve pronto")
            break
        else:
            print("Opcion no valida, intenta usar otra.")


if __name__ == "__main__":
    main()

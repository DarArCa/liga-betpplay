def registrar_partido(torneo):
    if not torneo["equipos"]:
        print("No hay equipos registrados para jugar un partido.")
        return torneo

    equipo1 = input("Ingrese el nombre del primer equipo: ").strip()
    equipo2 = input("Ingrese el nombre del segundo equipo: ").strip()

    if equipo1 not in torneo["equipos"] or equipo2 not in torneo["equipos"]:
        print("Uno o ambos equipos no existen.")
        return torneo

    if equipo1 == equipo2:
        print("Un equipo no puede jugar contra sí mismo.")
        return torneo

    try:
        goles1 = int(input(f"Goles de {equipo1}: "))
        goles2 = int(input(f"Goles de {equipo2}: "))
    except ValueError:
        print("Error: Ingresa valores numéricos para los goles.")
        return torneo

    torneo["equipos"][equipo1]["goles_favor"] += goles1
    torneo["equipos"][equipo1]["goles_contra"] += goles2
    torneo["equipos"][equipo2]["goles_favor"] += goles2
    torneo["equipos"][equipo2]["goles_contra"] += goles1

    if goles1 > goles2:
        torneo["equipos"][equipo1]["puntos"] += 3
    elif goles1 < goles2:
        torneo["equipos"][equipo2]["puntos"] += 3
    else:
        torneo["equipos"][equipo1]["puntos"] += 1
        torneo["equipos"][equipo2]["puntos"] += 1

    print(f"Partido registrado: {equipo1} {goles1} - {goles2} {equipo2}")
    return torneo

def mostrar_tabla_posiciones(torneo):
    print("\nTabla de Posiciones:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Equipo", "Puntos", "GF", "GC"))
    for equipo, datos in sorted(torneo["equipos"].items(), key=lambda x: x[1]["puntos"], reverse=True):
        print(f"{equipo:<20} {datos['puntos']:<10} {datos['goles_favor']:<10} {datos['goles_contra']:<10}")

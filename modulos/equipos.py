def agregar_equipo(torneo):
    """Agrega un equipo al torneo si no existe ya."""
    nombre = input("Ingrese el nombre del equipo: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    
    if nombre in torneo['equipos']:
        print("Error: El equipo ya existe.")
        return
    
    torneo['equipos'][nombre] = {
        "puntos": 0,
        "goles_favor": 0,
        "goles_contra": 0,
        "jugadores": [],
        "cuerpo_tecnico": [],
        "cuerpo_medico": []
    }
    print(f"Equipo '{nombre}' agregado correctamente.")

def ver_equipos(torneo):
    """Muestra la lista de equipos registrados en el torneo."""
    equipos = list(torneo['equipos'].keys())
    if not equipos:
        print("No hay equipos registrados.")
        return
    
    print("\nEquipos Registrados:")
    for equipo in equipos:
        print(f"- {equipo}")

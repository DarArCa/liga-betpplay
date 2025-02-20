from modulos.menus import menu_principal
from modulos.equipos import agregar_equipo, ver_equipos
from modulos.partidos import registrar_partido, mostrar_tabla_posiciones
from modulos.datos import cargar_datos, guardar_datos
#en ese entonces caundo hice el codigo, no sabiamos manejar excepciones, por eso si hay algun error es por esto
#sin decirle mentiras en la tabla de posiciones me ayude con chatgpt, dicen que vale mas ser honesto que otra cosa
def main():
    torneo = cargar_datos()
    
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            agregar_equipo(torneo)
        elif opcion == "2":
            ver_equipos(torneo)
        elif opcion == "3":
            registrar_partido(torneo)
        elif opcion == "4":
            mostrar_tabla_posiciones(torneo)
        elif opcion == "5":
            guardar_datos(torneo)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

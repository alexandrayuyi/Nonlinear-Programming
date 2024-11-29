import ConRestricciones
import LagrangeV2
import ProblemasMasGrandes 
import Gradiente

def Menu()-> str:
    return """\t\t\t\t
        +------------------------------------------------+
        |          PROGRAMACION NO LINEAL - Menu         |
        +------------------------------------------------+
        | 1. Ejercicio No.1 -> Metodo Lagrange           |
        | 2. Ejercicio No.2 -> Metodo ConRestriccion     |
        | 3. Ejercicio No.3 -> Metodo Gradiente          |
        | 4. Ejercicio No.4 -> Metodo ProblemasMasGrande |
        | 5. Salir                                       |
        +------------------------------------------------+
        """


if __name__ == "__main__":
    band=True
    while(band):
        print(Menu())
        try:
            event = float(input("\t\t ⚜ Seleccionar una Opcion: "))
            match event:
                case 1: 
                    print("\n \t")
                    LagrangeV2.Sample()
                case 2: 
                    print("\n \t")
                    ConRestricciones.Sample()
                case 3:
                    print("\n \t")
                    Gradiente.Sample()
                case 4:
                    print("\n \t")
                    ProblemasMasGrandes.Sample()
                case _: 
                    band=False
        except: 
            print("\n\t ⚠ ERROR..Reintentar!! ⚠ ")
            ...
        ...

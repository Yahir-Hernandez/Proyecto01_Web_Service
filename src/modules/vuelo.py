
class Vuelo():

    """
    Clase que crea un objeto para el vuelo
    """
    def __init__(self, origen, destino, hrorigen, hrdestino, ciudadOr, ciudadDes):

        self.origen = origen
        self.destino = destino 
        self.hrorigen = hrorigen
        self.hrdestino = hrdestino 
        self.ciudadOr = ciudadOr 
        self.ciudadDes = ciudadDes

    def __str__(self):
        print()
        print()
        return (f"Aereopuerto de origen:  {self.origen}\n"
                f"Aereopuerto de destino: {self.destino}\n" 
                f"Hora de la Ciudad de Origen: {self.hrorigen}\n"
                f"Hora de la Ciudad de Destino: {self.hrdestino}\n"
                f"Ciudad de Origen: {self.ciudadOr}\n"
                f"Ciudad de Destino: {self.ciudadDes}"
                )
        




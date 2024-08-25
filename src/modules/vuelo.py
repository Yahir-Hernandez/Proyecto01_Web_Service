
class Vuelo():

    """
    Clase que crea un objeto para el vuelo
    """
    def __init__(self, origen, destino, hrorigen, hrdestino, ciudadOr, ciudadDes, iataorigen, iatadestino, iata):

        self.origen = origen
        self.destino = destino 
        self.hrorigen = hrorigen
        self.hrdestino = hrdestino 
        self.ciudadOr = ciudadOr 
        self.ciudadDes = ciudadDes
        self.iataorigen = iataorigen
        self.iatadestino = iatadestino
        self.iata = iata

    def __str__(self):
        print()
        print()
        return (f"Aereopuerto de origen:  {self.origen}\n"
                f"Aereopuerto de destino: {self.destino}\n" 
                f"Fecha y hora de la Ciudad de Origen: {self.hrorigen}\n"
                f"Fecha y hora de la Ciudad de Destino: {self.hrdestino}\n"
                f"Ciudad de Origen: {self.ciudadOr}\n"
                f"Ciudad de Destino: {self.ciudadDes}\n"
                f"IATA de la Ciudad de Origen: {self.iataorigen}\n"
                f"IATA de la Ciudad de Destino: {self.iatadestino}\n"
                f"==================================================\n"
                f"IATA de vuelo: {self.iata}"
                )
    
    def getAereoOrigen(self):
        return self.origen
    
    def getAereoDest(self):
        return self.destino
    
    def gethrorigen(self):
        return self.hrorigen
    
    def gethrdesttino(self):
        return self.hrdestino
    
    def getciudadOr(self):
        return self.ciudadOr
    
    def getIataorigen(self):
        return self.iataorigen
    
    def getIatadestino(self):
        return self.iatadestino

    def getIata(self):
        return self.iata





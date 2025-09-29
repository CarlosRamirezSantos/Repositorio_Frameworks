'''En esta clase hacer toda la gestion del log'''
from datetime import datetime
import logging

fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"{fecha}_heroes_villanos.log"


logging.basicConfig(filename= nombre_fichero, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')






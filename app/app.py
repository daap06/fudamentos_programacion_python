
from service.info_Aves import informacion_aves
from service.generar_pagina import generar_pagina
# import os


def app():
    # direct = os.getcwdb()
    # print("Directorio actual", direct)
    
    informacion_aves()
    generar_pagina()
    

if __name__ == "__main__":
    app()
    
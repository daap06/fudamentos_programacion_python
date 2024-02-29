
from service.info_Aves import informacion_aves
from service.generar_pagina import generar_pagina

def app():
    informacion_aves()
    generar_pagina()
    

if __name__ == "__main__":
    app()
    
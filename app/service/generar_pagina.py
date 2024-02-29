
from string import Template
from .info_Aves import informacion_aves

def generar_pagina(): 
    """
    generar_pagina: inserta información obtenida de una api en un html, en caso de ser positiva la respuesta.

    Toma el template.html lee sus datos y generar desde esa base otro html con la información obtenida de la api.
    Al finalizar imprime en la terminal "pagina generada con éxito."
    """
    with open('template.html', 'r') as f:
        template_html = f.read()

    pagina_web = Template(template_html).substitute(body=informacion_aves())

    with open('aves_chile.html', 'w') as f:
        f.write(pagina_web)
    


print("Pagina generada exitosamente.")
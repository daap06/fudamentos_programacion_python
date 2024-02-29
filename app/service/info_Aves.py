from .get_request import request_get


data = request_get('https://aves.ninjas.cl/api/birds')
if data is None:
    exit()

def informacion_aves():
    """
    En caso de no existir errores, obtiene la información requerida de un api.

    Mediante un bucle for se insertan etiquetas html y su contenido sera el obtenido de la api.
    retorna un str."
    """
    
    global data
    dato_html = '<div class="container"><div class="row">'
    for dato in data[:6]:
        nombre_espanol = dato['name']['spanish']
        nombre_ingles = dato['name']['english']
        imagen = dato['images']['main']
        # dato_html += f'<div><h2>{nombre_espanol} / {nombre_ingles}</h2><img src="{imagen}" alt="{nombre_espanol} / {nombre_ingles}"/></div>'
        dato_html += f"""<div class="col mt-4">
                            <div class="card" style="width: 18rem; display: inline-block;">
                                <img src="{imagen}" class="card-img-top" alt="{nombre_espanol} / {nombre_ingles}">
                                <div class="card-body">
                                    <h5 class="card-title">{nombre_espanol} / {nombre_ingles}</h5>
                                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                                        additional content. This content is a little bit longer.</p>
                                </div>
                            </div>
                        </div>"""
    dato_html += '</div></div>'
    return dato_html


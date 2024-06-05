def contar_categorias(idiomas, eventos, tecnicas, extensao):
    return contar_horas_idiomas(idiomas) + contar_horas_eventos(eventos) + contar_horas_tecnicas(tecnicas) + contar_horas_extensao(extensao)


def contar_horas_idiomas(idiomas: int):
    if idiomas >= 40:
        return 40
    return idiomas


def contar_horas_eventos(eventos:int):
    if eventos > 40:
        return 40

    return eventos


def contar_horas_tecnicas(tecnicas:int):
    if tecnicas > 20:
        return 20

    return tecnicas


def contar_horas_extensao(extensao:int):
    if extensao > 80:
        return 80

    return extensao
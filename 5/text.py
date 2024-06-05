from funcao import *


def test_contar_horas_idiomas_menor_que_limite():
    result = contar_horas_idiomas(10)
    assert result == 10


def test_contar_horas_idiomas_maior_que_limite():
    result = contar_horas_idiomas(45)
    assert result == 40


def test_contar_horas_eventos_maior_que_limite():
    result = contar_horas_eventos(45)
    assert result == 40


def test_contar_horas_eventos_menor_que_limite():
    result = contar_horas_eventos(10)
    assert result == 10


def test_contar_horas_extensao_menor_que_limite():
    result = contar_horas_extensao(70)
    assert result == 70


def test_contar_horas_extensao_maior_que_limite():
    result = contar_horas_extensao(90)
    assert result == 80


def test_contar_horas_tecnicas_maior_que_limite():
    result = contar_horas_tecnicas(30)
    assert result == 20


def test_contar_horas_tecnicas_menor_que_limite():
    result = contar_horas_extensao(15)
    assert result == 15


def test_contar_categorias():
    result = contar_categorias(15, 15, 15, 15)
    assert result == 60

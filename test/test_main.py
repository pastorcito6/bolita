import pytest

from main import calcular_area_triangulo

def test_calcular_area_triangulo():
    #resultado obtenido (real)
    actual_result = calcular_area_triangulo(13.1, 3.85)

    #assert (estamos asegurando o vericando) que el resultado obtenido sea igual al resultado esperado
    #que el expected result sea igual al actual result
    assert actual_result == pytest.approx(19.5, abs=0.01)
import pytest
from cine import Pelicula

def test_vender_entradas_suficientes():
    pelicula = Pelicula("Test Movie", 10, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Test Movie. Total: $40"
    assert pelicula.asientos_disponibles == 5 
def test_vender_entradas_insuficientes():
    pelicula = Pelicula("Test Movie", 3, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3
def test_vender_cero_entradas():
    pelicula = Pelicula("Test Movie", 10, 8)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test Movie. Total: $0"
    assert pelicula.asientos_disponibles == 10 


from ejercicio01.Ejercicio01 import promedio
import pytest

@pytest.mark.parametrize (
    "input_nota1,input_nota2,input_nota3,expected_prom",
    [
        (10,5,6,6.5),
        (9,6,7,7.1)
        
    ]
    
)
def test_promedios_ok(input_nota1, input_nota2, input_nota3, expected_prom):
    assert promedio(input_nota1, input_nota2, input_nota3) == expected_prom
    
@pytest.mark.parametrize (
    "input_nota1,input_nota2,input_nota3,expected_prom",
    [
        (1,5,6,6.5),
        (9,3,7,7.1)
        
    ]
    
)
def test_promedios_not_ok(input_nota1, input_nota2, input_nota3, expected_prom):
    assert promedio(input_nota1, input_nota2, input_nota3) != expected_prom
    
from leilao.dominio import Usuario, Leilao, LanceInvalido
from leilao.excecoes import LanceInvalido

import pytest


@pytest.fixture
def vini():
    return Usuario('Vini', 100.00)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subitrair_valor_da_carteira_quando_tiver_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)
    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_vlr_menor_que_a_vlr_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)
    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_vlr_igual_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)
    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_vlr_maior_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 150.0)

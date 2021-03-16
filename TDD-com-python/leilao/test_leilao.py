from unittest import TestCase
from dominio import Usuario, Lance, Leilao
# python -m unittest src/leilao/test_avaliador.py


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.00)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_menor_e_menor_ordem_crescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 160.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        menor_valor = 150.00
        maior_valor = 160.00

        self.assertEqual(menor_valor, self.leilao.menor_lance)
        self.assertEqual(maior_valor, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('Yuri')
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_maior_menor_quando_3_lance(self):
        with self.assertRaises(ValueError):
            vini = Usuario('Vini')
            yuri = Usuario('Yuri')
            lance_do_yuri = Lance(yuri, 100.0)
            lance_do_vini = Lance(vini, 190.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)
            self.leilao.propoe(lance_do_vini)

            menor_valor = 100.00
            maior_valor = 190.00

            self.assertEqual(menor_valor, self.leilao.menor_lance)
            self.assertEqual(maior_valor, self.leilao.maior_lance)

    def test_deve_retornar_mesmo_quando_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        menor_valor = 150.00
        maior_valor = 150.00

        self.assertEqual(menor_valor, self.leilao.menor_lance)
        self.assertEqual(maior_valor, self.leilao.maior_lance)

    # se o leilao nao tiver lance, deve premitir propor um lance
    def test_deve_premitir_um_lance_nao_exitir(self):
        self.leilao.propoe(self.lance_do_gui)

        qnt_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, qnt_de_lances_recebido)
        
    # se o ultimo ususario for diferente , deve premitir propor o lance
    def test_deve_premitir_um_lance_caso_usuario_for_diferente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        qnt_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, qnt_de_lances_recebido)

    # se o ultimo usuario for mesmo, nao deve permitir propor o lance
    def test_nao_deve_premitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
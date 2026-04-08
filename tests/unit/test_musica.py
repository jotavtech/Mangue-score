# testes da classe Musica - validação de entrada
import pytest
from src.models.musica import Musica


class TestValidacaoMusica:
    # testes de validação - RN007 e RN008

    def test_titulo_vazio_deve_lancar_erro(self):
        # RN007 - título vazio tem que dar erro
        with pytest.raises(ValueError, match="Título deve ter pelo menos 3 caracteres"):
            Musica(titulo="", artista="Chico Science", caracteristicas=["percussão forte"])

    def test_titulo_menor_que_3_caracteres_deve_lancar_erro(self):
        # RN007 - título muito curto tbm dá erro
        with pytest.raises(ValueError, match="Título deve ter pelo menos 3 caracteres"):
            Musica(titulo="AB", artista="Chico Science", caracteristicas=["percussão forte"])

    def test_artista_vazio_deve_lancar_erro(self):
        # RN007 - artista vazio não pode
        with pytest.raises(ValueError, match="Artista deve ter pelo menos 3 caracteres"):
            Musica(titulo="Maracatu Atômico", artista="", caracteristicas=["percussão forte"])

    def test_artista_menor_que_3_caracteres_deve_lancar_erro(self):
        # RN007 - artista curto demais
        with pytest.raises(ValueError, match="Artista deve ter pelo menos 3 caracteres"):
            Musica(titulo="Maracatu Atômico", artista="AB", caracteristicas=["percussão forte"])

    def test_caracteristicas_vazia_deve_lancar_erro(self):
        # RN008 - sem características não dá
        with pytest.raises(ValueError, match="Lista de características não pode ser vazia"):
            Musica(titulo="Maracatu Atômico", artista="Chico Science", caracteristicas=[])

    def test_caracteristica_string_vazia_deve_lancar_erro(self):
        # RN008 - característica vazia na lista não pode
        with pytest.raises(ValueError, match="Cada característica deve ser uma string não vazia"):
            Musica(
                titulo="Maracatu Atômico",
                artista="Chico Science",
                caracteristicas=["percussão forte", ""],
            )

    def test_criacao_musica_valida(self):
        # criação normal tem que funcionar
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science",
            caracteristicas=["percussão forte", "guitarra funk/rock", "letras sociais/críticas"],
        )
        assert musica.titulo == "Maracatu Atômico"
        assert musica.artista == "Chico Science"


class TestIdentificacaoElementos:
    # testes da RN001 - identificação de elementos

    def test_possui_caracteristica_manguebeat(self):
        # verifica se identifica característica mangue corretamente
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "sertanejo raiz"],
        )
        assert musica.possui_caracteristica_manguebeat("percussão forte") is True
        assert musica.possui_caracteristica_manguebeat("sertanejo raiz") is False

    def test_contar_caracteristicas_manguebeat(self):
        # conta certinho as características mangue (3 das 4)
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "sertanejo raiz",
            ],
        )
        assert musica.contar_caracteristicas_manguebeat() == 3

    def test_tem_elementos_manguebeat_com_3_caracteristicas(self):
        # RN001 - com 3 características é mangue
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
            ],
        )
        assert musica.tem_elementos_manguebeat() is True

    def test_tem_elementos_manguebeat_com_menos_de_3(self):
        # RN001 - menos de 3 não tem DNA mangue suficiente
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
        )
        assert musica.tem_elementos_manguebeat() is False


class TestIdentificacaoArtistas:
    # testes de identificação dos artistas

    def test_artista_fundador(self):
        # Chico Science é fundador
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=["percussão forte"],
        )
        assert musica.is_artista_manguebeat_fundador() is True
        assert musica.is_artista_manguebeat() is True

    def test_artista_influenciado(self):
        # Siba é dos influenciados
        musica = Musica(
            titulo="Fuloresta",
            artista="Siba e A Fuloresta",
            caracteristicas=["percussão forte"],
        )
        assert musica.is_artista_manguebeat_influenciado() is True
        assert musica.is_artista_manguebeat() is True

    def test_artista_nao_manguebeat(self):
        # artista pop não é mangue
        musica = Musica(
            titulo="Musica Pop",
            artista="Lady Gaga",
            caracteristicas=["percussão forte"],
        )
        assert musica.is_artista_manguebeat() is False


class TestGeneros:
    # testes de gêneros divergentes

    def test_genero_divergente(self):
        # sertanejo é gênero estranho pro mangue
        musica = Musica(
            titulo="Música Sertaneja",
            artista="Dupla Sertaneja",
            caracteristicas=["percussão forte"],
            genero_principal="sertanejo",
        )
        assert musica.is_genero_divergente() is True

    def test_genero_nao_divergente(self):
        # rock combina com mangue
        musica = Musica(
            titulo="Rock Song",
            artista="Rock Band",
            caracteristicas=["percussão forte"],
            genero_principal="rock",
        )
        assert musica.is_genero_divergente() is False

# testes do calculador de score - todas as RNs
import pytest
from src.models.musica import Musica
from src.services.manguescore_calculator import MangueScoreCalculator


class TestPontuacaoCaracteristicas:
    # RN002 - pontuação das características

    def test_pontuacao_base_10_pontos(self):
        # característica normal vale 10
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["guitarra funk/rock"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_score_base() == 10

    def test_pontuacao_essencial_15_pontos(self):
        # essencial vale 15
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_score_base() == 15

    def test_pontuacao_mista(self):
        # mistura de essencial e normal: 15 + 10 + 15 = 40
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "guitarra funk/rock", "letras sociais/críticas"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_score_base() == 40

    def test_caracteristica_nao_manguebeat_nao_conta(self):
        # característica que não é mangue não conta ponto
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "voz aguda", "solo de piano"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_score_base() == 15


class TestBonusArtista:
    # RN004 - bônus por artista

    def test_bonus_fundador_30_pontos(self):
        # fundador ganha 30 pts
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=["percussão forte"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_bonus_artista() == 30

    def test_bonus_influenciado_15_pontos(self):
        # influenciado ganha 15 pts
        musica = Musica(
            titulo="Fuloresta",
            artista="Siba",
            caracteristicas=["percussão forte"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_bonus_artista() == 15

    def test_sem_bonus_artista_comum(self):
        # artista comum não ganha nada
        musica = Musica(
            titulo="Pop Song",
            artista="Taylor Swift",
            caracteristicas=["percussão forte"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_bonus_artista() == 0


class TestPenalidadeGenero:
    # RN005 - penalidade de gênero

    def test_penalidade_genero_divergente(self):
        # gênero estranho sem compensação leva penalidade
        musica = Musica(
            titulo="Música Sertaneja",
            artista="Dupla",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
            genero_principal="sertanejo",
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_penalidade_genero() == -10

    def test_sem_penalidade_com_compensacao(self):
        # muitas características compensam o gênero ruim
        musica = Musica(
            titulo="Música Sertaneja",
            artista="Dupla",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "elementos eletrônicos",
                "regionalismo nordestino",
            ],
            genero_principal="sertanejo",
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_penalidade_genero() == 0

    def test_sem_penalidade_genero_adequado(self):
        # rock não tem penalidade
        musica = Musica(
            titulo="Rock Song",
            artista="Rock Band",
            caracteristicas=["percussão forte"],
            genero_principal="rock",
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_penalidade_genero() == 0


class TestMangueScoreFinal:
    # RN003 e RN006 - score final

    def test_score_base_somente(self):
        # só o base: 15 + 10 = 25
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_manguescore() == 25

    def test_score_com_bonus(self):
        # com bônus de fundador: 40 + 30 = 70
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=["percussão forte", "guitarra funk/rock", "letras sociais/críticas"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_manguescore() == 70

    def test_score_com_penalidade(self):
        # com penalidade: 25 - 10 = 15
        musica = Musica(
            titulo="Música",
            artista="Artista",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
            genero_principal="sertanejo",
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_manguescore() == 15

    def test_score_com_bonus_e_penalidade(self):
        # bônus e penalidade juntos: 15 + 30 - 10 = 35
        musica = Musica(
            titulo="Música",
            artista="Chico Science",
            caracteristicas=["percussão forte"],
            genero_principal="sertanejo",
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.calcular_manguescore() == 35

    def test_limite_minimo_score_acima(self):
        # RN006 - acima de 50 é mangue: 15+10+15+10+30 = 80
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "elementos eletrônicos",
            ],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.is_manguebeat() is True

    def test_limite_minimo_score_abaixo(self):
        # RN006 - 25 <= 50 não é mangue
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.is_manguebeat() is False


class TestClassificacao:
    # testes da classificação personalizada

    def test_classificacao_nao_manguebeat(self):
        # menos de 50 não entra
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=["percussão forte"],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.get_classificacao() == "Não Manguebeat"

    def test_classificacao_bronze(self):
        # entre 51-69 é bronze: 15+10+15+10+10 = 60
        musica = Musica(
            titulo="Teste",
            artista="Artista",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "elementos eletrônicos",
                "regionalismo nordestino",
            ],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.get_classificacao() == "Bronze"

    def test_classificacao_prata(self):
        # entre 70-89 é prata: 15+10+15+10+30 = 80
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "elementos eletrônicos",
            ],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.get_classificacao() == "Prata"

    def test_classificacao_ouro(self):
        # 90+ é ouro: 15+10+15+10+10+10+30 = 100
        musica = Musica(
            titulo="Da Lama Ao Caos",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=[
                "percussão forte",
                "guitarra funk/rock",
                "letras sociais/críticas",
                "elementos eletrônicos",
                "regionalismo nordestino",
                "referências urbanas",
            ],
        )
        calculator = MangueScoreCalculator(musica)
        assert calculator.get_classificacao() == "Ouro"


class TestDetalhamento:
    # testa o retorno do detalhamento

    def test_get_detalhamento(self):
        # verifica se o dict vem completo
        musica = Musica(
            titulo="Maracatu Atômico",
            artista="Chico Science & Nação Zumbi",
            caracteristicas=["percussão forte", "guitarra funk/rock"],
        )
        calculator = MangueScoreCalculator(musica)
        detalhamento = calculator.get_detalhamento()

        assert detalhamento["titulo"] == "Maracatu Atômico"
        assert detalhamento["artista"] == "Chico Science & Nação Zumbi"
        assert detalhamento["score_base"] == 25
        assert detalhamento["bonus_artista"] == 30
        assert detalhamento["penalidade_genero"] == 0
        assert detalhamento["score_final"] == 55
        assert detalhamento["classificacao"] == "Bronze"
        assert detalhamento["is_manguebeat"] is True
        assert detalhamento["caracteristicas_manguebeat"] == 2

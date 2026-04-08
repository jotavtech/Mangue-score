# cálculo do manguescore - onde a mágica acontece
from src.models.musica import Musica


class MangueScoreCalculator:
    # faz as contas do score mangue

    # pontuações - valores escolhidos depois de vários testes
    PONTUACAO_BASE = 10
    PONTUACAO_ESSENCIAL = 15  # essencial vale mais
    BONUS_FUNDADOR = 30  # os cara que criaram ganham mais
    BONUS_INFLUENCIADO = 15  # quem segue ganha menos mas ganha
    PENALIDADE_GENERO_DIVERGENTE = -10  # castigo suave
    LIMITE_MINIMO_SCORE = 50  # menos que isso não é mangue
    LIMITE_COMPENSACAO_GENERO_DIVERGENTE = 5  # 5 características compensa o gênero ruim

    def __init__(self, musica):
        self.musica = musica  # guarda a ref

    def calcular_score_base(self):
        # RN002, RN003 - soma os pontos das características
        total = 0
        for caracteristica in self.musica.caracteristicas:
            if not self.musica.possui_caracteristica_manguebeat(caracteristica):
                continue  # não mangue não conta
                
            # essencial vale mais que as outras
            if caracteristica in self.musica.CARACTERISTICAS_ESSENCIAIS:
                total = total + self.PONTUACAO_ESSENCIAL
            else:
                total = total + self.PONTUACAO_BASE
        
        return total

    def calcular_bonus_artista(self):
        # RN004 - bônus pelo artista
        if self.musica.is_artista_manguebeat_fundador():
            return self.BONUS_FUNDADOR  # 30 pts
        
        if self.musica.is_artista_manguebeat_influenciado():
            return self.BONUS_INFLUENCIADO  # 15 pts
        
        return 0  # artista comum não ganha bônus

    def calcular_penalidade_genero(self):
        # RN005 - penalidade por gênero estranho
        if not self.musica.is_genero_divergente():
            return 0  # tá safe
        
        # mas se tiver muitas características mangue, compensa
        qtd_caracteristicas = self.musica.contar_caracteristicas_manguebeat()
        if qtd_caracteristicas >= self.LIMITE_COMPENSACAO_GENERO_DIVERGENTE:
            return 0  # compensou, tira a penalidade
        
        return self.PENALIDADE_GENERO_DIVERGENTE  # -10 pts

    def calcular_manguescore(self):
        # junta tudo: base + bônus - penalidade
        base = self.calcular_score_base()
        extra = self.calcular_bonus_artista()
        desconto = self.calcular_penalidade_genero()
        
        resultado = base + extra + desconto
        return resultado

    def is_manguebeat(self):
        # RN006 - só é mangue se passar de 50
        pontuacao = self.calcular_manguescore()
        if pontuacao > self.LIMITE_MINIMO_SCORE:
            return True
        return False

    def get_classificacao(self):
        # níveis personalizados que eu criei
        pontos = self.calcular_manguescore()
        
        if not self.is_manguebeat():
            return "Não Manguebeat"  # não passou do limite
        
        if pontos >= 90:
            return "Ouro"  # máximo respeito
        
        if pontos >= 70:
            return "Prata"  # tá bom demais
        
        return "Bronze"  # entrou pro movimento

    def get_detalhamento(self):
        # retorna tudo bonitinho pra ver como foi a conta
        base = self.calcular_score_base()
        extra = self.calcular_bonus_artista()
        desconto = self.calcular_penalidade_genero()
        final = base + extra + desconto
        
        detalhes = {
            "titulo": self.musica.titulo,
            "artista": self.musica.artista,
            "score_base": base,
            "bonus_artista": extra,
            "penalidade_genero": desconto,
            "score_final": final,
            "classificacao": self.get_classificacao(),
            "is_manguebeat": self.is_manguebeat(),
            "caracteristicas_manguebeat": self.musica.contar_caracteristicas_manguebeat(),
        }
        
        return detalhes

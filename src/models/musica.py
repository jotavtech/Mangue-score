# -*- coding: utf-8 -*-
"""
Classe Musica - representa uma música do MangueScore
Feito com carinho pra celebrar o movimento mangue
"""
from typing import List  # precisa pra tipagem das características


class Musica:
    # representa uma música com suas características pra classificação

    # características que definem o som mangue - aumentei algumas além do pedido
    CARACTERISTICAS_MANGUEBEAT = {
        "percussão forte",
        "guitarra funk/rock",
        "letras sociais/críticas",
        "elementos eletrônicos",
        "regionalismo nordestino",
        "referências urbanas",
        "samples de mangue",
        "ritmo ciranda/maracatu",
        "baixo distorcido",
    }

    # essas duas são as mais importantes - sem isso não é mangue de verdade
    CARACTERISTICAS_ESSENCIAIS = {
        "percussão forte",
        "letras sociais/críticas",
    }

    # os cara que criaram o movimento - merecem bônus maior
    ARTISTAS_MANGUEBEAT_FUNDADORES = {
        "chico science & nação zumbi",
        "chico science e nação zumbi",
        "chico science",
        "nação zumbi",
        "mundo livre s/a",
        "mundo livre sa",
    }

    # galera que veio depois mas segue a tradição - tbm tem valor
    ARTISTAS_MANGUEBEAT_INFLUENCIADOS = {
        "siba",
        "siba e a fuloresta",
        "mestre ambrósio",
        "cordel do fogo encantado",
        "comadre fulozinha",
        "stereomaracana",
        "carne doce",
        "bode brown",
    }

    # gêneros que não combinam - aplica penalidade se não tiver compensação
    GENEROS_DIVERGENTES = {
        "sertanejo",
        "clássica",
        "erudita",
        "ópera",
        "opera",
        "country",
        "gospel",
    }

    def __init__(self, titulo: str, artista: str, caracteristicas: List[str], genero_principal: str = ""):
        # guarda os dados
        self.titulo = titulo
        self.artista = artista
        
        # normaliza as características pra ficar tudo minúsculo e sem espaço extra
        self.caracteristicas = []
        for c in caracteristicas:
            self.caracteristicas.append(c.lower().strip())
        
        self.genero_principal = genero_principal.lower().strip()

        # valida os dados logo no início
        self._validar()

    def _validar(self):
        # RN007 - validação de título e artista
        if not self.titulo:
            raise ValueError("Título deve ter pelo menos 3 caracteres")
        if len(self.titulo.strip()) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres")

        # mesmo esquema pro artista
        if not self.artista:
            raise ValueError("Artista deve ter pelo menos 3 caracteres")
        if len(self.artista.strip()) < 3:
            raise ValueError("Artista deve ter pelo menos 3 caracteres")

        # RN008 - validação das características
        if len(self.caracteristicas) == 0:
            raise ValueError("Lista de características não pode ser vazia")

        for c in self.caracteristicas:
            if c == None or c == "":
                raise ValueError("Cada característica deve ser uma string não vazia")
            if type(c) != str:
                raise ValueError("Cada característica deve ser uma string não vazia")

    def possui_caracteristica_manguebeat(self, caracteristica):
        # verifica se a característica tá na lista do mangue
        caracteristica = caracteristica.lower().strip()
        if caracteristica in self.CARACTERISTICAS_MANGUEBEAT:
            return True
        return False

    def contar_caracteristicas_manguebeat(self):
        # RN001 - conta quantas características mangue a música tem
        contador = 0
        for c in self.caracteristicas:
            if self.possui_caracteristica_manguebeat(c):
                contador += 1
        return contador

    def tem_elementos_manguebeat(self):
        # precisa de pelo menos 3 pra ter o DNA mangue
        if self.contar_caracteristicas_manguebeat() >= 3:
            return True
        return False

    def is_artista_manguebeat_fundador(self):
        # os criadores do movimento
        nome_artista = self.artista.lower().strip()
        return nome_artista in self.ARTISTAS_MANGUEBEAT_FUNDADORES

    def is_artista_manguebeat_influenciado(self):
        # galera que bebeu da fonte
        nome_artista = self.artista.lower().strip()
        return nome_artista in self.ARTISTAS_MANGUEBEAT_INFLUENCIADOS

    def is_artista_manguebeat(self):
        # verifica se é fundador OU influenciado
        if self.is_artista_manguebeat_fundador() or self.is_artista_manguebeat_influenciado():
            return True
        return False

    def is_genero_divergente(self):
        # RN005 - gênero que não combina com o movimento
        return self.genero_principal in self.GENEROS_DIVERGENTES

# 🥁 MangueScore

Classificador Musical Manguebeat - Identificando o DNA Mangue em músicas e artistas.

## Sobre

Projeto que classifica músicas baseado no movimento Manguebeat. Nasceu da vontade de entender o que faz uma música ter "cara de mangue" e celebrar essa cultura pernambucana que é sensacional.

## Stack

- Python 3.8+
- pytest (testes)
- pytest-cov (cobertura)

## Instalação

```bash
pip install -r requirements.txt
```

Ou se preferir:
```bash
python -m pip install pytest pytest-cov
```

## Rodando os Testes

```bash
# todos os testes
python -m pytest

# com saída detalhada
python -m pytest -v

# com cobertura
python -m pytest --cov=src --cov-report=html
```

## Estrutura do Projeto

```
manguescore/
├── src/
│   ├── models/
│   │   └── musica.py              # Classe Musica
│   └── services/
│       └── manguescore_calculator.py  # Lógica de cálculo do score
├── tests/
│   └── unit/
│       ├── test_musica.py         # Testes de validação
│       └── test_manguescore_calculator.py  # Testes das regras de negócio
├── README.md
├── requirements.txt
└── .gitignore
```

## Regras de Negócio Testadas

### 1. Classificação de Características Musicais

- **RN001 - Identificação de Elementos Manguebeat**: Uma música é considerada com elementos Manguebeat se possuir pelo menos 3 das seguintes características: "percussão forte", "guitarra funk/rock", "letras sociais/críticas", "elementos eletrônicos", "regionalismo nordestino", "referências urbanas", "samples de mangue", "ritmo ciranda/maracatu", "baixo distorcido".

- **RN002 - Pontuação por Característica**: Cada característica Manguebeat presente em uma música contribui com 10 pontos. Características consideradas "essenciais" ("percussão forte", "letras sociais/críticas") têm peso maior de 15 pontos.

### 2. Cálculo do MangueScore

- **RN003 - Score Base**: O MangueScore inicial de uma música é a soma das pontuações de suas características Manguebeat.

- **RN004 - Bônus por Artista Manguebeat**: Músicas de artistas historicamente associados ao Manguebeat recebem bônus:
  - Artistas fundadores (Chico Science & Nação Zumbi, Mundo Livre S/A): +30 pontos
  - Artistas influenciados (Siba, Mestre Ambrósio, Cordel do Fogo Encantado, etc.): +15 pontos

- **RN005 - Penalidade por Gênero Divergente**: Músicas cujo "Gênero Principal" é muito distante do rock, maracatu ou hip-hop (Sertanejo, Clássica, Country, Gospel) recebem penalidade de -10 pontos, a menos que possuam pelo menos 5 características Manguebeat (compensação).

- **RN006 - Limite Mínimo de Score**: Uma música só pode ser considerada "Manguebeat" se seu MangueScore final for superior a 50 pontos.

### 3. Classificação (adicional)

Criei esses níveis pra ficar mais divertido:

- **Não Manguebeat**: Score ≤ 50
- **Bronze**: Score entre 51-69
- **Prata**: Score entre 70-89
- **Ouro**: Score ≥ 90

### 4. Validação de Entrada

- **RN007 - Validação de Título e Artista**: O título da música e o nome do artista não podem ser vazios e devem ter no mínimo 3 caracteres.

- **RN008 - Validação de Características**: A lista de características de uma música não pode ser vazia e cada característica deve ser uma string não vazia.

## Exemplo de Uso

```python
from src.models.musica import Musica
from src.services.manguescore_calculator import MangueScoreCalculator

# Criar uma música
musica = Musica(
    titulo="Maracatu Atômico",
    artista="Chico Science & Nação Zumbi",
    caracteristicas=[
        "percussão forte",
        "guitarra funk/rock",
        "letras sociais/críticas",
        "elementos eletrônicos",
        "regionalismo nordestino",
    ],
    genero_principal="rock",
)

# Calcular MangueScore
calculator = MangueScoreCalculator(musica)
score = calculator.calcular_manguescore()
classificacao = calculator.get_classificacao()

print(f"Score: {score}")  # 95
print(f"Classificação: {classificacao}")  # Ouro
print(f"É Manguebeat? {calculator.is_manguebeat()}")  # True

# Ver detalhamento completo
detalhes = calculator.get_detalhamento()
print(detalhes)
```

## Artistas Manguebeat Reconhecidos

### Fundadores (+30 pontos)
- Chico Science & Nação Zumbi
- Chico Science
- Nação Zumbi
- Mundo Livre S/A

### Influenciados (+15 pontos)
- Siba / Siba e A Fuloresta
- Mestre Ambrósio
- Cordel do Fogo Encantado
- Comadre Fulozinha
- Stereomaracana
- Carne Doce
- Bode Brown

## Notas

Projeto educacional feito com respeito ao Manguebeat e seus artistas. 

🤘 Bróder, mete bronca no coding!

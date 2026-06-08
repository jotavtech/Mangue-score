# language: pt
Funcionalidade: Navegacao pela pagina de servicos do gov.br
  Como um cidadao brasileiro
  Quero navegar pela pagina de servicos
  Para conhecer os servicos disponibilizados pelo Governo Federal

  Cenario: Acessar a pagina de servicos
    Dado que eu acesso a pagina de servicos do gov.br
    Entao o endereco da pagina deve conter "/servicos"
    E devo visualizar o titulo da pagina

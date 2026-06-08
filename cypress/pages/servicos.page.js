// Page Object da pagina de Servicos do gov.br.

class ServicosPage {
  // ----- Seletores -----
  get campoBusca() {
    return cy.get('#govbr-busca-input');
  }

  get titulo() {
    // Primeiro titulo visivel da pagina (ignora cabecalhos ocultos)
    return cy.get('h1, h2').filter(':visible').first();
  }

  // ----- Acoes -----
  acessar() {
    cy.visit('/pt-br/servicos');
    cy.aceitarCookies();
    return this;
  }

  // ----- Validacoes -----
  validarUrlServicos() {
    cy.url().should('include', '/servicos');
    return this;
  }
}

export default new ServicosPage();

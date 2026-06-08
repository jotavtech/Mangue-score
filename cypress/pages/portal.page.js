// Page Object da pagina inicial do Portal gov.br.
// Centraliza seletores e acoes da home, evitando duplicacao nos steps.

class PortalPage {
  // ----- Seletores -----
  // O campo de busca do gov.br e um autocomplete (Algolia). O <input>
  // real possui o id "searchtext-input" (o "#govbr-busca-input" e apenas
  // o container externo, sem ser editavel).
  get campoBusca() {
    return cy.get('#searchtext-input');
  }

  get menuNavegacao() {
    // Filtra apenas elementos visiveis para ignorar menus de acessibilidade
    // ocultos (ex.: nav.govbr-skip-menu, que e position:fixed e invisivel).
    return cy.get('header, nav, [role="navigation"]').filter(':visible').first();
  }

  get secaoServicos() {
    return cy.contains(/servi[cç]os/i);
  }

  // ----- Acoes -----
  acessar() {
    cy.visit('/');
    cy.aceitarCookies();
    return this;
  }

  validarCarregamento() {
    cy.get('body').should('be.visible');
    this.campoBusca.should('exist');
    return this;
  }
}

export default new PortalPage();

// Page Object responsavel pela funcionalidade de busca/pesquisa do gov.br.
// A busca do portal e implementada com o componente de autocomplete da
// Algolia (classes "aa-*"). O input real e #searchtext-input e o envio e
// feito pelo botao .aa-SubmitButton, que navega para /pt-br/search.

import PortalPage from './portal.page';

class PesquisaPage {
  // ----- Seletores -----
  get campoBusca() {
    return PortalPage.campoBusca; // #searchtext-input
  }

  get botaoSubmit() {
    return cy.get('.aa-SubmitButton');
  }

  // ----- Acoes -----
  pesquisar(termo) {
    // Garante que o autocomplete esteja pronto antes de interagir
    this.campoBusca.should('be.visible').and('not.be.disabled').click().clear();
    this.campoBusca.type(termo);
    this.botaoSubmit.first().click();
    return this;
  }

  submeterBuscaVazia() {
    this.campoBusca.should('be.visible').clear();
    this.botaoSubmit.first().click();
    return this;
  }

  // ----- Validacoes -----
  validarPaginaDeResultados() {
    // Apos a busca o portal navega para a pagina de resultados
    // (ex.: /pt-br/search?...&SearchableText=<termo>).
    cy.url().should('match', /search|busca|searchabletext|consulta|q=/i);
    return this;
  }
}

export default new PesquisaPage();

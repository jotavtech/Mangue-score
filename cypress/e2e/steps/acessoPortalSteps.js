import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';
import PortalPage from '../../pages/portal.page';

// Passo compartilhado: acessa a home do gov.br (usado por varios cenarios)
Given('que eu acesso a pagina inicial do Portal gov.br', () => {
  PortalPage.acessar();
});

Then('o titulo da pagina deve conter {string}', (texto) => {
  cy.title().should('match', new RegExp(texto, 'i'));
});

// Passo compartilhado: valida que o campo de busca esta visivel
Then('o campo de busca deve estar visivel', () => {
  PortalPage.campoBusca.should('be.visible');
});

Then('devo visualizar o menu de navegacao', () => {
  PortalPage.menuNavegacao.should('exist').and('be.visible');
});

Then('devo visualizar a secao de servicos', () => {
  PortalPage.secaoServicos.should('exist');
});

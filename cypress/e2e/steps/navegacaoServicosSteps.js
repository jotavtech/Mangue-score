import { Given, Then } from '@badeball/cypress-cucumber-preprocessor';
import ServicosPage from '../../pages/servicos.page';

Given('que eu acesso a pagina de servicos do gov.br', () => {
  ServicosPage.acessar();
});

Then('o endereco da pagina deve conter {string}', (trecho) => {
  cy.url().should('include', trecho);
});

Then('devo visualizar o titulo da pagina', () => {
  ServicosPage.titulo.should('be.visible');
});

import { When, Then } from '@badeball/cypress-cucumber-preprocessor';
import PesquisaPage from '../../pages/pesquisa.page';

When('eu pesquiso pelo termo {string}', (termo) => {
  PesquisaPage.pesquisar(termo);
});

When('eu submeto a busca sem informar um termo', () => {
  PesquisaPage.submeterBuscaVazia();
});

Then('a pagina de resultados deve ser exibida', () => {
  PesquisaPage.validarPaginaDeResultados();
});

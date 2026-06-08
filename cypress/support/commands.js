// ***********************************************
// Comandos customizados reutilizaveis nos testes.
// ***********************************************

/**
 * Aceita o banner de cookies do gov.br caso ele esteja presente.
 *
 * Importante: a busca e restrita a elementos <button> DENTRO de um
 * container de cookies. Nunca clica em links (<a>) genericos, para
 * evitar navegar para fora do site (ex.: redes sociais no rodape).
 * E tolerante: nao falha o teste quando o banner nao aparece.
 */
Cypress.Commands.add('aceitarCookies', () => {
  cy.get('body').then(($body) => {
    const $botoes = $body
      .find(
        '.br-cookiebar button, [class*="cookiebar"] button, [id*="cookie"] button, [class*="cookie"] button'
      )
      .filter((_, el) =>
        /aceitar|aceito|concordo|entendi/i.test(el.textContent || '')
      );

    if ($botoes.length > 0) {
      cy.wrap($botoes.first()).click({ force: true });
    }
  });
});

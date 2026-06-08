// ***********************************************************
// Arquivo de suporte carregado automaticamente antes de cada
// arquivo de teste (spec). Importa os comandos customizados.
// ***********************************************************
import './commands';

// Sites governamentais podem disparar erros de JavaScript de
// terceiros (analytics, libs externas, etc.) que nao afetam o
// objetivo do teste. Evitamos que esses erros derrubem a suite.
Cypress.on('uncaught:exception', () => {
  return false;
});

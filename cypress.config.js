const { defineConfig } = require('cypress');
const createBundler = require('@bahmutov/cypress-esbuild-preprocessor');
const {
  addCucumberPreprocessorPlugin,
} = require('@badeball/cypress-cucumber-preprocessor');
const {
  createEsbuildPlugin,
} = require('@badeball/cypress-cucumber-preprocessor/esbuild');

module.exports = defineConfig({
  e2e: {
    // Site governamental publico utilizado como alvo dos testes
    baseUrl: 'https://www.gov.br',
    specPattern: 'cypress/e2e/features/**/*.feature',
    supportFile: 'cypress/support/e2e.js',
    fixturesFolder: 'cypress/fixtures',
    defaultCommandTimeout: 15000,
    pageLoadTimeout: 90000,
    requestTimeout: 15000,
    chromeWebSecurity: false,
    video: true,
    videosFolder: 'cypress/videos',
    screenshotsFolder: 'cypress/screenshots',
    retries: {
      runMode: 2,
      openMode: 0,
    },
    async setupNodeEvents(on, config) {
      // Habilita o pre-processador do Cucumber/Gherkin
      await addCucumberPreprocessorPlugin(on, config);

      // Empacota os steps com esbuild
      on(
        'file:preprocessor',
        createBundler({
          plugins: [createEsbuildPlugin(config)],
        })
      );

      // Retorna a config para que o Cypress aplique os ajustes do plugin
      return config;
    },
  },
});

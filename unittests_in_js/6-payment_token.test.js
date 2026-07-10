const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', function () {
  it('should return a resolved promise with the correct object when success is true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // Indique à Mocha que le test asynchrone est terminé
      })
      .catch((err) => {
        done(err); // Transmet l'erreur à Mocha si quelque chose se passe mal
      });
  });
});

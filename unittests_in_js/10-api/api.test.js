const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865/cart/';

  it('Correct status code when :id is a number?', (done) => {
    request.get(`${baseUrl}12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('Correct status code when :id is NOT a number (=> 404)?', (done) => {
    request.get(`${baseUrl}hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments page', () => {
  const url = 'http://localhost:7865/available_payments';

  it('Correct status code and deep equal object?', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      // Utilisation de JSON.parse pour lire la chaîne retournée par le serveur
      // et de deep.equal pour comparer le contenu des objets
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('Login', () => {
  const url = 'http://localhost:7865/login';

  it('Correct status code and result message?', (done) => {
    // Configuration de la requête POST avec Request
    const options = {
      url: url,
      json: true,
      body: {
        userName: 'Betty'
      }
    };

    request.post(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});

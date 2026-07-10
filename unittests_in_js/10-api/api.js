const express = require('express');

const app = express();
const port = 7865;

// Middleware crucial pour parser le JSON du body de la requête POST
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

// Nouvelle route GET : Retourne un objet JSON
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// Nouvelle route POST : Récupère userName dans le body
app.post('/login', (req, res) => {
  const userName = req.body.userName;
  res.send(`Welcome ${userName}`);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;

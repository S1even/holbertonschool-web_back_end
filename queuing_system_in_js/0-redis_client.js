import redis from 'redis';

// Création du client Redis (se connecte par défaut à 127.0.0.1:6379)
const client = redis.createClient();

// Écoute de l'événement de connexion réussie
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Écoute de l'événement d'erreur
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

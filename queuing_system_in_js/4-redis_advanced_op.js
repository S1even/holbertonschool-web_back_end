import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const hashKey = 'HolbertonSchools';

// Création du Hash avec de multiples champs (hset)
// On utilise redis.print comme callback pour afficher le "Reply: 1"
client.hset(hashKey, 'Portland', 50, redis.print);
client.hset(hashKey, 'Seattle', 80, redis.print);
client.hset(hashKey, 'New York', 20, redis.print);
client.hset(hashKey, 'Bogota', 20, redis.print);
client.hset(hashKey, 'Cali', 40, redis.print);
client.hset(hashKey, 'Paris', 2, redis.print);

// Récupération et affichage de tout le Hash (hgetall)
client.hgetall(hashKey, (err, object) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(object);
});

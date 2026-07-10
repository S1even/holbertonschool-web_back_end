import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Fonction pour définir une nouvelle valeur
function setNewSchool(schoolName, value) {
  // redis.print est un callback natif de la librairie qui affiche "Reply: OK" si tout s'est bien passé
  client.set(schoolName, value, redis.print);
}

// Fonction pour afficher une valeur existante
function displaySchoolValue(schoolName) {
  // On utilise un callback (err, reply) pour récupérer la donnée de manière asynchrone
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(reply);
  });
}

// Appels demandés à la fin du fichier
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

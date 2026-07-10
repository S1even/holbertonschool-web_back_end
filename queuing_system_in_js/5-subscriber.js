import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const CHANNEL = 'holberton school channel';

// On s'abonne au canal
client.subscribe(CHANNEL);

// On écoute les messages entrants sur les canaux auxquels on est abonné
client.on('message', (channel, message) => {
  if (channel === CHANNEL) {
    console.log(message);
    
    // Si le message est "KILL_SERVER", on se désabonne et on quitte
    if (message === 'KILL_SERVER') {
      client.unsubscribe(CHANNEL);
      client.quit();
    }
  }
});

import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // On indique que le job commence (0 sur 100)
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Si le numéro est blacklisté, on fait échouer le job en passant une Error à done()
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Si tout va bien, on avance à 50%
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
  // On termine le job avec succès
  done();
}

const queue = kue.createQueue();

// On écoute la file d'attente avec une concurrence de 2 (2 jobs à la fois)
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

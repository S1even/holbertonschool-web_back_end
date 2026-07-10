import kue from 'kue';

// Initialisation de la file d'attente avec Kue
const queue = kue.createQueue();

// Fonction qui simule l'envoi de la notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Le processeur écoute la file 'push_notification_code'
// Il traite un travail (job) à la fois et prend un callback 'done'
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  
  // Exécution de l'action
  sendNotification(phoneNumber, message);
  
  // On valide la tâche pour indiquer à Kue qu'elle est "completed"
  done();
});

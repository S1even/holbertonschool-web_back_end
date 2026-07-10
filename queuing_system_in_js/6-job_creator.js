import kue from 'kue';

// Initialisation de la file d'attente avec Kue
const queue = kue.createQueue();

// Création des données de la tâche (le numéro et le message)
const jobData = {
  phoneNumber: '0612345678',
  message: 'This is the code to verify your account'
};

// Création de la tâche dans la file 'push_notification_code'
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Écoute de l'événement de succès de la tâche
job.on('complete', () => {
  console.log('Notification job completed');
});

// Écoute de l'événement d'échec de la tâche
job.on('failed', () => {
  console.log('Notification job failed');
});

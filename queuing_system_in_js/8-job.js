export default function createPushNotificationsJobs(jobs, queue) {
  // Vérification de sécurité : est-ce bien un tableau ?
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Boucle pour créer un job pour chaque élément
  jobs.forEach((jobData) => {
    // Création de la tâche dans la file 'push_notification_code_3'
    const job = queue.create('push_notification_code_3', jobData);

    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Écoute des événements de la tâche
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

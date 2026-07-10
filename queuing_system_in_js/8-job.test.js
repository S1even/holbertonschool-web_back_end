import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Avant de lancer les tests de ce bloc, on passe Kue en mode test
  before(() => {
    queue.testMode.enter();
  });

  // Après chaque test, on vide la file d'attente en mémoire pour repartir à zéro
  afterEach(() => {
    queue.testMode.clear();
  });

  // Une fois tous les tests terminés, on quitte le mode test
  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    // On passe un Number ou un String au lieu d'un Array pour forcer l'erreur
    expect(() => createPushNotificationsJobs('Not an array', queue)).to.throw(
      Error,
      'Jobs is not an array'
    );
  });

  it('create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);

    // On vérifie que 2 jobs ont bien été mis dans la file d'attente de test
    expect(queue.testMode.jobs.length).to.equal(2);
    
    // On vérifie le type et le contenu du premier job généré
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });

    // On vérifie le contenu du second job généré
    expect(queue.testMode.jobs[1].data).to.deep.equal({
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    });
  });
});

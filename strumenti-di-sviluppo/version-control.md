# Strumenti di sviluppo - Gestione delle versioni

## Sistemi di controllo delle versioni

I **Version Control System** sono sistemi che gestiscono _repository_ di codice sorgente, tengono traccia delle modifiche effettuate, consentono l'accesso concorrente e gestiscono _tag_ e _branch_ del progetto.

Sono basati su architetture client-server, lo sviluppatore scarica i file dal server, li modifica e invia le modifiche al server. Ogni volta che si apportano modifiche ad un file il sistema gli assegna un **version number** che distingue ciascuna versione.

Il primo VCS è CVS (Concurrent Versioning System) nato nel 1990 con molti limiti. Nel 2000 nasce SVN (Subversion), orientato al codice C e limitato ai file sorgente.
Dallo sviluppo del kernel Linux nel 2005 nasce Git che ora rappresenta lo standard.

### Operazioni fondamentali

1. __import__: aggiunta di un progetto software al repository
2. __checkout__: prelevamento di una copia dal repository e copia in locale
3. __commit__: invio delle modifiche locali al server remoto
4. __update__: scaricamento delle modifiche remote in locale

E' possibile fare il checkout di qualsiasi versione precedente per spostarsi avanti e indietro nella storia delle versioni. La versione corrente (predefinita per il checkout) viene detta __HEAD__.

### Sincronizzazione

Ci sono 2 possibili approcci nella gestione dei problemi di sincronizzazione delle modifiche da parte di 2 o più sviluppatori che operano contemporaneamente:

1. **Locking pessimistico**: quando uno sviluppatore effettua il checkout acquisisce il lock sulla cartella e i checkout vengono impediti finché questo non rilascia il lock.
2. **Locking ottimistico**: la gestione dei conflitti è rimandata nel momento del commit, se è presente un conflitto non risolvibile automaticamente il commit viene bloccato.

Ci sono 4 scenari possibili quando si esegue un update su un repository locale:

1. _unchanged and current_: nessuna azione da eseguire.
2. _locally changed and current_: non vengono effettuate operazioni ma è necessario fare il commit delle modifiche
3. _unchanged and out-of-date_: la versione aggiornata viene scaricata.
4. _locally changed and out-of-date_: è necessaria l'operazione di **merge**, la versione aggiornata viene scaricata, se il merge può essere fatto automaticamente viene eseguito dal VCS, altrimenti si chiede all'utente di fornire una soluzione manuale e segnalare l'operazione come _resolved_ per poi fare il commit.

### TAGS & Branches

Un tag è un nome che viene assegnato a una versione del progetto per etichettare un determinato stato e recuperare la versione più facilmente in futuro.

Un branch è una linea parallela di sviluppo, tipicamente si creano più branches quando è necessario sviluppare nuove funzionalità, risolvere bug o in generale effettuare modifiche invasive sul codice senza intaccare il normale sviluppo (che continua sul master).

## Linee guida

1. Mettere sotto controllo di versione solo i file non riproducibili, ignorando i file di build e di configurazione dell'IDE
2. Per gestire i classpath è preferibile utilizzare sistemi di costruzione del codice che gestiscano autonomamente le dipendenze o includerle in una cartella `lib/` versionata.
3. Effettuare commit frequenti
4. Effettuare update frequenti
5. Cercare di effettuare commit quando il codice si trova in uno stato stabile
6. Creare tag per le versioni significative

## GIT

Git utlizza un approccio distribuito: ogni client agisce da server. Questo consente di effettuare modifiche in locale, anche in assenza di rete e inviare successivamente le modifiche al server remoto. Per fare ciò si rende necessario introdurre le operazioni di **push** e **pull** che servono per inviare/prelevare il codice dal repository remoto.

I file nella directory di lavoro possono assumere 3 stati:

- Commited: file non modificato
- Modified: file modificato o nuovo
- Staged: file modificato e contrassegnato come pronto per un commit

I file e le directory da ignorare in GIT possono essere indicati nel file `.gitignore` contenuto nella cartella principale del repository.

Git utilizza un hash di 42 caratteri per indicare i numeri di versione, questi contrassegnano l'intero repository e non la versione dei singoli file.

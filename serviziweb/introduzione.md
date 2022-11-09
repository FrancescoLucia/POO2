# Servizi Web

Un'applicazione distribuita è composta da moduli che girano su macchine diverse e comunicano attraverso messaggi scambiati via rete.

2 moduli fondamentali:

- __Applicativo di frontend__: riguarda l'interazione con l'utente finale, schermi, interfaccia
- __Applicativo di backend__: riguarda i servizi applicativi offerti (al frontend) e l'interazione con il DBMS. Può essere suddiviso in __microservizi__.

## Operazioni CRUD

Sono operazioni tipiche relative alla persistenza di una classe nel database. 4 operazioni

- __Create__
- __Retrieve__
- __Update__
- __Delete__

## Remote Procedure Call

Il problema principale è come far comunicare i moduli atraverso la rete, la comunicazione è chiamata Remote Procedure Call (RPC).

Anche per le RPC è necessario stabilire un protocollo di comunicazione e un formato per la serializzazione degli oggetti.

I moduli backend espongono __API__, in particolare Web API.

Un __DTO - Data Transfer Object__ è un oggetto creato ad hoc per la serializzazione, differente dall'oggetto nel modello.

### SOAP - Simple Object Access Protocol

Lo standard (ormai superato) dei protocolli RPC.

I messaggi sono scambiati con HTTP in formato XML. Il messaggio è chiamato _busta SOAP_ ed è formato da un header contenente metadati e un body con informazioni sull'azione da eseguire e i parametri (o il risultato dell'azione nel caso della risposta).

SOAP è orientato alle azioni, le cihamate assumono nomi simili alle chiamate di procedure in Java (es. `getStudenti`, `updateStudente`).

Utilizza solo il metodo POST e pertanto non effettua caching delle richieste.

I vantaggi sono le estensioni di XML e la possibilità di validare la richiesta con il DTD. Lo svantaggio principale è la verbosità dei messaggi.

Un altro vantaggio di SOAP è il __Web Services Description Language__ (WSDL): formato per la documentazione dell'API, insieme all' __Universal Description Discovery and Integration__ (UDDI): standard per la costruzione di repository e motori di ricerca per web services.

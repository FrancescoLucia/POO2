# API REST

REST è l'acronimo di __Representational State Transfer__

## Caratteristiche

Si tratta di uno stile di programmazione di web api divenuto uno standard di fatto.

A differenza di SOAP l'idea di REST è di strutturare gli endpoint non con l'obiettivo di eseguire sottoprogrammi ma di accedere a risorse (tipicamente nel dbms).

Le api rest sono comunque basate su HTTP ma utilizzano come standard di serializzazione dati il formato JSON, molto più snello e orientato anch'esso agli oggetti.

## URI

Gli endpoint sono organizzati come un filesystem virtuale. I nomi sono plurali se si riferiscono agli oggetti di una collezione, singolari se si riferiscono ad un oggetto singolo.

Esempi:

- `/studenti`
- `/esami`
- `/studenti/1234` studente con matricola 1234
- `/studenti/1234/esami`
- `/studenti/1234/esami/pp/insegnamento` insegnamento associato all'esame pp dello studente 1234

Gli URI possono riferirsi sia a proprietà e risorse reali che virtuali (ovvero calcolate dinamicamente).

## Richieste

A differenza di SOAP (che utilizza solo il metodo POST), il protocollo REST utilizza tutti e 4 i protocolli principali (GET, POST, PUT, DELETE).

- Una richiesta di tipo GET serve per ottenere lo stato degli oggetti a cui ci si riferisce attraverso l'URI, il formato predefinito della risposta è la serializzazione dell'oggetto in JSON. Quando il server vuole restituire lo stato dell'oggetto parzialmente (eliminando alcune proprietà o arricchendolo con proprietà calcolate) utilizza un DTO.
- Una richiesta POST aggiunge nuove risorse inviando nel corpo della richiesta la risorsa da aggiungere in formato json.
- In maniera simile lavora il metodo PUT procedendo all'aggiornamento della risorsa
- Il metodo DELETE elimina risorse esistenti

La query string nello standard REST viene utilizzata al solo scopo di filtrare il risultato di una richiesta GET, es: `GET /studenti?anno=2`.

I metodi PUT e DELETE sono idempotenti, ovvero esecuzioni ripetute danno gli stessi risultati, POST no, ogni ripetizione aggiunge nuovi dati clonati.

### Operazioni non CRUD

Gli URI che fanno riferimento a esecuzioni di metodi sono caratterizzati da verbi e possono utilizzare sia GET che POST (più frequente).

Es. `POST /utenti/login`, `POST /conti/conto123/effettuaBonifico`

Convenzionalmente per separare versioni diverse della stessa API e mantenerle entrambe senza causare la rottura dei client che utilizzano la veccchia versione si antepone il nome di versione agli endpoint.

Es. `GET /v1/studenti` , `GET /v2/studenti`

## Test e Documentazione

REST non ha uno standard per la documentazione. Esiste uno standard di fatto chiamato __OpenAPI__ e basato su __Swagger__.

Swagger è uno strumento per generare documentazione a partire da un'API REST in json e fornisce un'interfaccia in HTML per l'interrogazione rapida delle API.

Gli strumenti di test degli endpoint sono essenziali durante lo sviluppo in quanto spesso lo sviluppo del/dei frontend non è parallelo a quello del backend. Un tool che permette di effettuare richieste alle API è postman.

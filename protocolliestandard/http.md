# Protocollo HTTP

Il protocollo nasce nel 1991, attualmente la vesione 1.1 è supportata da tutti i browser, dal 2015 esiste la HTTP/2.

Il concetto principale del protocollo HTTP è la __transazione__, una transazione è uno scambio di messagi tra client e server:

- apertura connessione
- il client invia una richiesta
- il server invia una risposta
- chiusura connessione

Il protocollo non è orientato alle connessioni, questo significa che per ogni nuova transazione ci sarà una connessione differente e le transazioni sono tra di loro indipendenti.

## Struttura dei messaggi

La struttura generale e comune sia a richiesta che risposta è:

```
<linea iniziale>
<intestazioni opzionali>...
<intestazione>:<valore>
<intestazione>:<valore>
<linea vuota>
<corpo, opzionale>
```
### Intestazioni

Contengono metainformazioni sulla richiesta o risposta, ad esempio lo User-Agent (il sistema utilizzato), il Referer, il Content-Type e altre informazioni opzionali

### Richiesta

Nella richiesta la linea iniziale contiene il percorso della risorsa a cui si vuole accedere. Il corpo è vuoto o contiene parametri della richiesta.

La linea iniziale ha il formato: `<metodo> <percorso> HTTP/1.0`

I metodi di HTTP 1.0 sono  GET e POST

__GET__ è il metodo standard, il corpo della richiesta è vuoto e i parametri sono passati nella querystring

Es. `GET /bollo.php?targa=A123 HTTP/1.0`

__POST__ è utilizzato per comunicare con i servizi, i parametri sono passati nel corpo della richiesta e quindi sono nascosti, questo consente di bypassare il limite di lunghezza delle querystring.

es.

```
POST /bollo.php HTTP/1.0

targa=A123
```

### Risposta

Nella risposta la linea iniziale contiene l'esito della richiesta. Il corpo contiene il contenuto della risposta se previsto.

La riga iniziale ha il formato: `HTTP/1.0 <codice numerico> <descrizione>`

Classi di codici:

- 1xx: messaggio informativo
- 2xx: richiesta esaudita con successo
- 3xx: redirect
- 4xx: errore lato client
- 5xx: errore lato server

Esempi di codici

- 200 ok
- 201 Created
- 202 Accepted
- 301 Moved Permanently
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal server error
- 503 Service Unavailable

## Autenticazione e autorizzazione

L'autenticazione è la procedura secondo la quale l'utente si identifica al server fornendo delle credenziali che il server confronterà nel proprio archivio (solitamente un db).

L'autorizzazione è la possibilità di un utente appartenente ad una determinata classe di utenti di eseguire un'operazione o accedere ad una risorsa.

## HTTP 1.1

### Novità e miglioramenti introdotti

#### Connessioni persistenti

Con l'http 1.1 sulla stessa connessione TCP possono avvenire più transazioni, la connessione viene chiusa o dal server dopo un certo timeout, o dal client con l'intestazione `Connection: close`.

#### Host Virtuali

IP e porta non bastano ad identificare un server, questo consente ai provider di utilizzare lo stesso ip e indirizzare la connessione su più server, il client deve specificare l'intestazione __Host__ con il nome del server.

#### Autenticazione Digest

Nell'autenticazione le password non vengono trasmesse, il server invia al browser una stringa __nonce__ (number used once) e il browser risponde con il nome utente e un valore crittografato basato su utente, password, percorso e nonce, il server confronta questo valore con quello calcolato e stabilisce se l'autenticazione è valida.

Il meccanismo non è sicuro perché la richiesta è intercettabile.

#### SSL

__Secure Socket Layer__ è un protocollo di trasporto che utilizza un meccanismo a chiave pubblica per crittografare tutti i messaggi trasmessi. un server HTTP gestisce le richieste HTTPS sulla porta 443.

#### Metodi di accesso aggiuntivi

HTTP 1.0 introduce una serie di metodi di accesso aggiuntivi per facilitare le operazioni sulle risorse:

1. PUT
2. DELETE
3. OPTIONS
4. TRACE
5. UPGRADE

Per la gestione del caching si differiscono i metodi in __idempotendi__ e __non idempotenti__. Un metodo si dice idempotente se esecuzioni successive di una richiesta producono risultati identici alla prima.

Sono metodi idempotenti GET, PUT e DELETE.

I metodi per i quali è consentito il caching sono GET e HEAD, nessuno degli attori coinvolti nelle richieste effettua caching dei metodi POST, PUT o DELETE.

Un problema da gestire è l'invio ripetuto di richieste (per esempio perché l'utente clicca due volte sul pulsante o ricarica una pagina erroneamente o perché la vista non risponde) che può causare duplicazioni di dati o errori lato server.

## HTTP/2

Supportato dal 97% dei client ma solo il 50% dei server.

La principale novità è che in un'unica connessione è possibile caricare più risorse in parallelo e il server può restituire dati anche non richiesti. Ad esempio se il client richiede una pagina html il server può restituire autonomamente la pagina e le risorse (jpg, css, js) ad essa collegate.

L'utilizzo a priori di HTTP/2 non è consigliato per la mancata copertura del 100% dei client ma può essere utile nella comunicazione tra microservizi di backend.

## Stato e Sessioni

### Cookies

Uno dei meccanismi per ovviare al problema di mancanza di stato di HTTP sono i cookies, si tratta di coppie chiave valore che il server aggiunge alla risposta. Il client (se accetta il cookie) si impegna a restituirlo con le successive richieste per consentire al server di collegarle alle precedenti.

#### Intestazioni

- __Set-Cookie__ intestazione inviata dal server
- __Cookie__ intestazione del client nella richiesta

Un cookie è associato ad un URI ed è valido per tutti gli URI che contengono come prefisso quello a cui è associato.

Un cookie può avere validità di sessione (finchè non viene chiusa la tab) o una scadenza nel tempo (anche infinita).

### Tokens

Per gestire le autenticazioni si utilizzano i token

#### Bearer Token

Viene inviato dal server a seguito dell'autenticazione di un client, il server aggiunge all'intestazione (o come attributo) il token (una stringa), che autorizza chiunque la invii nella richiesta ad accedere come l'utente autenticato.

Questo risolve il problema dell'autenticazione ma non dell'autorizzazione, poiché il server non riesce a risalire all'utente e ai suoi permessi.

#### JWT - Json Web Token

I JWT risolvono questo problema, i token sono stringhe crittografate di un oggetto json contenente informazioni sull'utente.

## XSS - Cross Site Scripting

Tecnica di attacco che sfrutta gli input non sicuri che vengono poi mostrati in una pagina. Immettendo in un input del codice html o javascript il server lo inserisce nella pagina e questo viene eseguito.

In questo modo è possibile creare dei link (sfruttando parametri passati come get) che eseguono nella pagina codice javascript proveniente da altri domini. Uno script eseguito in questo modo può accedere a cookie, intestazioni e informazioni sulle richieste e può risalire a informazioni sensibili per l'utente a partire da questi.

L'attacco può essere anche persistente se la porzione di codice malevolo viene memorizzata nel DB (ad esempio in un social network o forum) e viene automaticamente eseguita sui client di tutti gli utenti che visitano la pagina anche senza necessità che si clicchi su link.

### Protezioni

Il primo e fondamentale rimedio per questo tipo di attacco è la sanificazione degli input che consiste nel rimuovere tag e keywords pericolose riconosciute come codice eseguibile.

Una seconda forma di protezione è offerta dai browser:

#### Same Origin Policy

Definiamo come Origin di una richiesta la parte del referer che corrisponde a protocollo dominio e porta, es. [https, www.unibas.it, 80]

La Same Origin Policy è un insieme di regole che bloccano le richieste Cross Origin originate da Javascript. __Il browser effettua la richiesta ma ne blocca l'accesso alla rispota__.

Questo viene effettuato a livello di richiesta con l'intestazione `Origin: <origine>` del browser.

Per gli scopi di sviluppo e in generale per le nuove architetture basate su microservizi e separazione tra backend (con api) e frontend questo meccanismo costituisce un problema.

Lo standard per controllare le richieste cross origin è il __CORS - Cross Origin Resource Sharing__.

Le richieste XO possono essere effettuate aggiungendo al server 2 richieste http:

- Access-Control-Allow-Origin: \<origin\>
- Access-Control-Allow-Credentials: true

Ogni richiesta eseguita viene confrontata con quelle indicate nella prima intestazione e se è presente viene accettata correttamente e la prima intestazione viene restituita anche nella risposta.

La seconda intestazione serve per esporre i cookie in una richiesta XO (cosa di default disabilitata dal browser).

#### Richieste di Preflight

Il browser non può sapere se una richiesta XO verrà bloccata finché non la effettua, per velocizzae le cose esistono richieste di preflight, attraverso il metodo OPTIONS consentono di effettuare richieste molto leggere per verificare se il server risponde positivamente ad una richiesta XO.

__NON C'E' PREFLIGHT PER LE RICHIESTE GET__
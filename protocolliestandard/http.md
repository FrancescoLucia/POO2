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


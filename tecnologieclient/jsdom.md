# Javascript nel browser

Il __Document Object Model__ è la piattaforma e l'interfaccia che consente a programmi e scripts di accedere dinamicamente e aggiornare i contenuti, la struttura e lo stile di un documento. Il DOM del browser viene chiamato __BOM__.

In generale il DOM è sia la struttura dei dati (equivalente dell'infoset in XML) sia una API per manipolare l'albero.

Le API del DOM sono fondamentali per costruire applicazioni _rich client_ in javascript. Infatti il modello e controllo sviluppati in javascript girano sul client e modificano la vista (attraverso le API del DOM), scritta in html e css.

L'oggetto `window` del BOM permette l'accesso ad informazioni sulla finestra del browser (es. `innerHeight` e `innerWidth`). L'oggetto `window.screen` consente invece di accedere ai parametri dello schermo: `height`, `width`, `availHeight`, `availWidth`.

Javascript può accedere ad una serie di informazioni e interazioni con la finestra del browser es. `window.navigator`, `window.location` (uri), `window.location.assign("")`, `window.alert`, `window.confirm`, `window.prompt`, gli ultimi 3 servono per aprire finestre di interazione con l'utente.

L'oggetto `document` rappresenta la radice del DOM. Attraverso di esso è possibile recuperare, modificare, eliminare e aggiungere nodi. Contiene una serie di metadati accessibili come proprietà:

- `document.lastModified`
- `document.title`
- `document.URL`
- `document.baseURI`
- `document.domain`
- `document.referrer`
- `document.cookie`
- `document.readyState`

I tipi di nodi sono:

- ELEMENT_NODE
- ATTRIBUTE_NODE (deprecato)
- TEXT_NODE
- COMMENT_NODE
- DOCUMENT_NODE
- DOCUMENT_TYPE_NODE

Le proprietà `innerText` e `innerHTML` consentono di modificare rispettivamente il contenuto testuale e il contenuto HTML di un nodo. Per modificare una proprietà di stile di un nodo `n` è possibile usare la sintassi `n.style.proprieta = valore`.

Per la ricerca dei nodi esistono diverse funzioni, le più utilizzate:

- `document.getElementById(id)` seleziona gli elementi con un determinato id
- `document.getElementsByTagName(name)` restitusice una HTMLCollection (lista)
- `document.getElementsByClassName(classe)`
- `document.querySelectorAll(selector)` ricerca sulla base del selettore css

Esistono alcune collezioni predefinite nel dom:

- `document.forms`
- `document.images`
- `document.anchors`
- `document.scripts`

Ogni elemento in HTML può essere sorgente di evento e il DOM prevede la registrazione di un gestore di eventi per ognuno.

Esempi di eventi sono: onclick, onload, onmouseover, onchange, onsubmit, onkeyup/down/press.

Esistono 3 modi per registrare un gestore di un evento:

1. Utilizzare la proprietà evento nel codice js: `nodo.onclick = funzione()`
2. Dichiarare il gestore direttamente come attributo in html:<br>
`<button type="button" onclick="funzione()">`
3. Tramite una istruzione esplicita di sottoscrizione:<br>
`nodo.addEventListener(event, funzione)`.

E' possibile modificare il DOM seguendo 2 approcci:

1. Modificare i nodi esistenti, gestire la dinamicità agendo sull'attributo display dei nodi per visualizzarli/nasconderli
2. Creare ed eliminare nodi quando necessario (più efficace quando è necessario gestire collezioni dinamiche). Metodi `appendChild()` e `removeChild()`

## Local Storage e Session storage

Il browser dispone di strutture dati per memorizzare informazioni. La differenza tra local storage e session storage è che il secondo è volatile (viene eliminato alla chiusura del browser).

Si tratta di mappe chiave valore, per memorizzare un dato si utilizza la sintassi `localStorage.setItem(chiave, valore)`, per recuperarlo `localStorage.getItem(chiave)`.
Lo spazio è limitato a 5MB per il localstorage, per il sessionstorage l'unico limite è la quantità di RAM assegnata dal OS.

## Chiamare API

La funzione standard per effettuare richieste HTTP con Javascript dal browser è la funzione `fetch()`. E' una funzione asincrona che restituisce una promise.

Esempio di chiamata fetch con logging della risposta:

```js
fetch("http://example.com").then( 
    (response) => response.json()).then( 
    (data) => console.log(data));
```

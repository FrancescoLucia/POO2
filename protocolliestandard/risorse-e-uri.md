# Risorse e URI

## MIME Types

Acronimo di __Multipurpose Internet Mail Extensions__

Sono stringhe per la descrizione del formato delle risorse, utili nelle pagine html o nelle richieste così come nella posta elettronica.

Ogni volta che client e server scambiano risorse indicano nel messaggio il MIME type.

Il browser gestisce le risorse ricevute in base al MIME type di queste

Es.

- text application/msword
- image image/gif
- messagge application/json

## URI

__Uniform Resource Identifier__

Modo per rappresentare indirizzi: _\<protocollo\>:\<indirizzo\>_

Protocolli:

- http/s
- mailto
- ftp
- file

Forma generica di un url HTTP

`http://<server>[:<porta>][/<percorso>][?<query>]`

La querystring è una lista di coppia `nome=valore` separate dalla `&`.

## Richieste

- Richieste dell'utente (inoltrate attraverso il browser o client)
- Richieste di collegamenti (click su link da pagina html)
- Richieste implicite (richieste del browser per renderizzare elementi come immagini o css)

__REFERER__: URI della pagina da cui si origina una richiesta HTTP. Parametro bloccato da alcuni browser per motivi di privacy perché consentirebbe ai server di ricostruire parzialmente o completamente la cronologia dell'utente.

## File System

Il file system di un server http è virtuale. L'organizzazione non corrisponde all'organizzazione dei file sul disco, la root `/` può essere montata su una qualsiasi cartella del disco, es. `/home/sito/` o `F:\sito\`, dalla radice è visibile tutto il contenuto della cartella.

E' possibile montare altre porzioni del filesystem attraverso alias, ad esempio si potrebbe montare la cartella `C:\Users\utente\` in `/utente`.

Il meccanismo dell'alias viene utilizzato anche nelle applicazioni e questo è il motivo principale per il quale _un URL non corrisponde necessariamente ad una risorsa fisica_ ma può essere il punto di accesso per una risorsa generata dinamicamente da un componente software.
# Tecnologie Lato Client - HTML

La prima versione di HTML esce nel giugno '93 per opera di Tim Berners Lee e Dave Ragget, basato su DTD di SGML, il padre di XML.

L'HTML risulta da subito meno restrittivo di xml, i numerosi problemi che questa libertà causava (dovuti alle varie implementazioni dei browser) richiesero una standardizzazione che inizialmente prevedeva vincoli molto rigidi (XHTML gennaio 2000).

Attualmente lo standard riconosciuto e supportato da tutti i browser è l'HTML5 che non deve essere necessariamente un documento XML ben formattato ma deve essere coercibile in XML. Infatti è il browser stesso che si occupa di tradurre un HTML5 nel XML equivalente e correggere eventuali errori.

In HTML5 è convenzionale introdurre una netta separazione tra struttura e stile (che deve essere gestito attraverso fogli CSS). 

## Elementi

La struttura di base di un documento HTML5 è:

```html
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <title>Titolo</title>
        <!-- Metadati della pagina-->
    </head>
    <body>
        <!-- Corpo della pagina-->
    </body>
</html>
```

2 tipi di elementi

- Block level elements: elementi di blocco, i relativi riquadri cominciano sempre una nuova linea. Es. titoli, div, tabelle, liste, paragrafi
- inline elements: elementi i cui relativi riquadri possono essere disposti lungo la stessa linea. es. testo, span, immagini, link

Il browser contiene un __foglio di stile standard__ che utilizza per tutti gli elementi che non hanno altre regole CSS specificate.

## Attributi

- __id__: identificatore univoco per un elemento
- __class__: utile per dare regole di stili a più elementi
- __lang__: lingua del contenuto (di solito applicata al tag html)

Le metainformazioni contenute nell'HEAD sono utilizzate per specificare intestazioni HTTP relative alla pagina o per aiutare i motori di ricerca nell'indicizzazione.

```html
<meta name="author" content="Autore" />
<meta name="keywords" content="prova, html,..." />
```

> Gli appunti non sono completi, ho tralasciato le parti di sintassi e i tag

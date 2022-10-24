# CSS

__Cascading Style Sheets__, nasce con l'boettivo di specificare caratteristiche di formattazione per i riquadri di una pagina XHTML.

Il CSS è basato su __regole__, una regola deve contenere un riferimento al riquadro da formattare (__selettore__), una lista di __dichiarazioni__ composte da una __proprietà__ e il __valore__ da attribuirgli.

```css
h2 {
    color: green;
    font-size: 14px;
}
```

Sintassi: `<selettore> { <proprietà>: <valore>; altraProprieta: valore;}`

I commenti in CSS si delimitano con `/* */`

Per fare riferimento ad un URI esiste una sintassi particolare: `url("sfondo.jpg")`

## Selettori

Un selettore è un indicatore dell'elemento (o insieme di elementi) html a cui applicare le regole di stile contenute tra parentesi quadre. Esistono diversi modi per selezionare un elemento:

### Selettori semplici

- Nome dell'elemento (tag): es. `img { border: 1px; }`
- In base all'attributo id:
<br>es. volendo selezionare un div `<div id="esempio">` la sintassi css è `#esempio {}` o `div#esempio {}`
- In base all'attributo classe: `.nomeclasse { }` o `p.nomeclasse {} `, il primo seleziona tutti gli elementi che hanno la classe `nomeclasse`, il secondo solamente i paragrafi.

### Pseudo-classi

Le pseudoclassi sono selettori utili per classificare elementi dinamicamente in base a condizioni che si  verificano a livello di azioni che l'utente compie sull'interfaccia.

Sintassi: `<selettore>:<pseudo classe>`. Ad esempio se si vuole indicare un comportamento per i link quando vengono attraversati dal mouse si può utilizzare la classe _hover_:

```css
a:hover {
    color: red;
}
```

### Selettori contestuali

Sono selettori che consentono di distinguere gli elementi in base alla loro posizione nel DOM, costituiti da un selettore ordinario e un __contesto__: `<contesto> <selettore semplice>`.

La sintassi funziona se tra questi due elementi è presente lo spazio, in caso ci sia la virgola invece questa vale come OR logico, ovvero seleziona entrambi gli elementi separati dalla virgola.

```css
div p {} /* seleziona i paragrafi all'interno di un div */
div#main img {} /* seleziona le immagini all'interno di un paragrafo con id main */
p span.prova {} /* seleziona gli span con classe prova all'interno di un paragrafo */
h2.titolo, p {} /* seleziona gli h2 di classe titolo E tutti i paragrafi */
```

Lo spazio seleziona gli elementi "all'interno di", il `>` seleziona gli elementi direttamente figli del contesto: es. `div.home > p` seleziona solo il paragrafo direttamente figlio del div.home.

## Lunghezze

- Unità assolute: in, cm, mm, pt
- Unità relative: em, rem, ex, vh, vw, px
- Percentuali
- Parole chiave: es. small, x-small

px è la dimensione in pixels, dipende dalla risoluzione dello schermo. emè la dimensione del font del riquadro ad eccezione del font-size relativo alla dimensione del font per il riquadro del padre.

rem è la dimensione del font dell'elemento body.

vh è l'altezza del viewport, vw è la larghezza del viewport.

Ogni browser ha una dimensione predefinita assegnata a ciascuna delle parole chiave:

- xx-small
- x-small
- small
- medium
- large
- x-large
- xx-large

## Colori

I colori si rappresentano in codifica RGB o con le keywords standard di HTML. Un colore RGB è una stringa che contiene le codifiche esadecimali dei livelli di rosso verde e blu: `#<rr><gg><bb>` es `#FF000` è il rosso.

## Box Model

Ad ogni elemento HTML corrisponde un riquadro, questo è articolato in vari spazi:

- content
- padding
- border
- margin

![](boxmodel.png)

Le proprietà relative ai margini sono: `margin-top`, `margin-bottom`, `margin-left` e `margin-right`.

Così come le proprietà relative al padding: `padding-top`, `padding-bottom`, `padding-left`, `padding-right`.

Dei bordi possiamo impostare la larghezza (border-width), il colore (border-color) e lo stile (border-style).

Per l'attributo `margin` è possibile impostare il valore `auto` che centra il box orizzontalmente rispetto al padre.

Di default la dimensione di un box è data da width/height + padding + border.

Per disabilitare queto comportamento è possibile aggiungere la regole `box-sizing: border-box` che rende la dimensione dipendente solo da width e height, il padding e i bordi vengono considerati interni.

Solitamente questa viene impostata come opzione di default perché rende più semplice ragionare sulle dimensioni dei riquadri.

## Semantica delle regole CSS

### Ereditarietà

Alcune proprietà CSS sono ereditate dai predecessori (ad esempio il font), altre no (es. sfondo). Per sapere se una proprietà è ereditata _inherit_ consultare lo [standard](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)

### Cascata

Il meccanismo nasce per l'integrazione sulla stessa pagina di fogli di stile diversi. Le dichiarazioni hanno regole di precedenza e si applicano in cascata.

Il qualificatore per dare priorità massima ad una dichiarazione è `!important`.

```css
p { font-size: 1.5em !important }
```

__Algoritmo per la priorità__:

- Trova tutti i valori per una proprietà
- Ordina rispetto all'origine, in ordine:
  - utente !important
  - autore !important
  - autore
  - utente
  - standard
- Ordina rispetto alla specificità partendo dai più specifici
  - id
  - classe
  - nome
  - ...
- ordina per ordine di comparizione nel file css (le ultime prima)


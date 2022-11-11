# Programmazione Web - J2EE

Lo sviluppo web in java lato server richiede __J2EE__, inizialmente Java 2 Enterprise Edition, dal 2017 Jakarta Enterprise Edition.

## Server applicativo

Il server di riferimento per i backend in Java è Tomcat, progetto open source in ascolto di default sulla porta 8080. E' in grado di servire anche file statici ma per una questione di prestazioni viene di solito utilizzato in accoppiata con un server HTTP standard. Quest'ultimo funzionerà da intermediario, quando gli sarà richiesta una risorsa statica la restituirà direttamente, quando la risorsa richiederà esecuzione del codice Java, il lavoro sarà passato al server tomcat.

## Java Server Pages

Tecnologia attualmente poco utilizzata, è una pagina in cui sono mischiati codice HTML e codice Java tradotta automaticamente dal server in un servlet equivalente.

```html
<html>
    <body>
        <% 
            String nome = request.getParameter("nome");
            session.setAttribute("nome", nome);
        %>
        <p>Benvenuto <%= nome %></p>
    </body>
</html>
```

## Struttura delle applicazioni

Una applicazione J2EE è una cartella che deve avere una struttura definita ed essere visibile sul filesystem virtuale. 

La radice del filesysem virtuale corrisponde a una cartella chiamata _webapps_.

E' necessario che tutte le applicazioni seguano la struttura standard per essere correttamente supportate dal server tomcat.

### Organizzazione dei file

- Cartella radice con pagine jsp, html, css e immagini
- Cartella __WEB-INF__ contenente il file __web.xml__
- Cartella WEB-INF/classes contenente servlet e componenti
- cartella WEB-INF/lib con le librerie necessarie

La struttura della cartella viene solitamente generata dall'IDE nell'operazione di build. Convenzionalmente, anche se è possibile configurare il server per avere librerie condivise tra applicazioni, si preferisce incorporare con ogni applicazione una copia delle librerie necessarie in modod da evitare problemi con le versioni.

Tomcat ha una cartella `/lib` nella quale sono contenute le librerie comuni a tutti i progetti e le librerie `servlet-api.jar` e `jsp-api.jar`, non incluse in J2SE necessarie per lo sviluppo di applicazioni web.

### WAR

I Web Application Archive sono archivi compressi con estensione .war e un'organizzazione di file e cartelle standard. I contenitori possono decomprimere e installare le applicazioni fornitegli sottoforma di file war.

### Deployment Descriptor

Il file __web.xml__ è un descrittore di parametri di configurazione. Attraverso questo file è possibile specificare parametri che occorrono al server per il deployment dell'applicazione.

Es. nomi e uri per servlet, timeout ecc...

Se è vuoto il contenitore assegnerà dei valori di default.

Gli elementi devono comparire nel seguente ordine:

- display-name
- description
- servlet
- servlet-mapping
- error-page

Ogni applicazione ha un nome (_context path_) che corrisponde al nome della cartella in cui è contenuta.

## Deployment

Le applicazioni web per essere rese operative devono subire un processo di deployment. Questo differisce in base al server e all'applicazione, solitamente consiste nella copia dei file sul server, la configurazione di alcuni parametri, l'avvio di alcuni servizi. I parametri relativi alla configurazione vengono specificati nel file __Context Descriptor__ di norma chiamato _context.xml_.

Lo standard di deployment per le applicazioni web su Tomcat prevede la copia del file .war nella cartella webapps. A questo punto il server riconosce la presenza del nuovo file e installa l'applicazione, in particolare decomprime il war in una cartella omonima, assegna un context path, utilizza il context descriptor per il deployment o ne crea uno standard.

Una applicazione può essere messa in stato di _stop_ ovvero spenta o rimossa con l'azione _undeploy_. Il __reload__ consente di reinizializzarne i componenti senza doverla rimuovere e reinstallare.

Per ovviare ai problemi di lentezza della procedura di deployment standard Tomcat offre una modalità alternativa che consiste nel creare un alias fornendo un descrittore di contesto in cui è indicata la posizione della cartella eseguibile da recuperare.
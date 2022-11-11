# Servlet

Un servlet è una classe Java orientata alla comunicazione client server in grado di gestire richieste dai metodi principali.

Due package:

- `javax.servlet` per i servlet generici
- `javax.servlet.http` per i servlet http

L'interfaccia è `Servlet`, i servlet generici estendono la classe astratta `GenericServlet`, i servlet http estendono `HttpServlet`.

Il ciclo di vita dei servlet è gestito unicamente dal contenitore. Lo sviluppatore implementa metodi di servizio che saranno chiamati dal contenitore alla ricezione di una richiesta.

I metodi da implementare per gestire le principali richieste http sono `doGet()`, `doPost()`, `doPut()` e `doDelete()`. Le implementazioni ereditate sono vuote.

Tutti i metodi prendono come parametri un oggetto `HttpServletRequest` e un `HttpServletResponse`.

## Ciclo di vita

Il ciclo di vita di un servlet prevede 3 fasi:

1. Inizializzazione (creazione delle istanze del servlet)
2. Servizio (istanze in funzione che gestiscono le richieste)
3. Distruzione (istanza distrutte dal garbage collector)

Il contenitore solitamente crea un'unica istana del servlet quando l'applicazione viene avviata ed esegue il metodo `init()`. Il servlet gestisce le richieste creando un thread per ogni nuova richiesta. Il thread chiama il metodo `service()` e il metodo service chiama il metodo necessario in base al tipo di richiesta.

Quando il server viene spento o viene spenta l'applicazione il contenitore chiama il metodo `destroy()` e distrugge l'istanza del servlet.

## Richieste 

Nella gestione delle richieste i servlet hanno a disposizione metodi per accedere ad alcuni parametri. Una richiesta contiene una mappa di parametri forniti nella querystring ai quali si può accedere con il metodo `String getParameter(String nomeParametro)` o `String[] getParameterValues(String nome)`.

La richiesta può anche accedere a:

- informazioni sul client
- informazioni sul metodo
- informazioni sull'URI
- informazioni sulle intestazioni http

## Risposte

Un oggetto risposta consente di specificare le intestazioni http da inviare e il corpo del messaggio. Le intestazioni si impostano con i metodi `setHeader(String nome, String valore)` o `addHeader(String nome, String valore)`, l'intestazione fondamentale (e la prima da inserire) è il content type, impostabile con il metodo `response.setContentType("text/html")`.

Per scrivere il corpo della risposta è necessario ottenere un oggetto PrintWriter con il metodo `response.getWriter()` e successivamente scrivervi le righe del corpo.

## Context

L'oggetto `javax.servlet.ServletContext` rappresenta il contesto nel quale il servlet viene eseguito, può essere recuperato con il metodo `getServletContext()`. Il context consente la comunicazione tra servlet e contenitore e consente di manipolare gli attributi dell'applicazione con il metodo `getAttribute(String chiave)`, `setAttribute(String chiave, Object obj)` e `removeAttribute(String chiave)`.

Il context risulta l'unica soluzione in caso di redirectm infatti i servlet chiedono al contenitore di effettuare l'inoltro della richiesta verso un altro servlet. Il compito è gestito dal __Request Dispatchet__, il cui riferimento può essere ottenuto con il metodo `getRequestDispatchet(String uri)` del ServletContext. Il dispatchet a sua volta ha un metodo `forward` che prende come parametri la richiesta e la ripsosta elaborata fino a quel momento e le inoltra al servlet di competenza.

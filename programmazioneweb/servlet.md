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

## Filtri

Un filtro è un servlet speciale che intercetta richieste e risposte da e verso altri servlet. Si utilizza un filtro per modificare una risposta prima di inviarla al client o per controllare determinate caratteristiche della richiesta e decidere se procedere con l'inoltro al servlet (tipico caso l'autorizzazione del client).

Anche i filtri devono essere definiti nel deployment descriptor e devono rispondere ad un url-pattern. Un url-pattern può essere associato a più filtri, e in questo caso questi verranno chiamati in cascata secondo l'ordine con il quale soo dichiarati nel file `web.xml`.

L'interfaccia da implementare per creare un filtro è `javax.servlet.Filter`, contenente 3 metodi: `init()`, `destroy()` e `doFilter()`, il terzo prende come parametri una richiesta, una risposta, e una `FilterChain`.

```java
public class Filtro implements Filter {
    public void init(FilterConfig config) throws ServletException {}
    public void destroy() {}
    public void doFilter(ServletRequest request, ServletResponse response,
                        FilterChain chain) throws IOException, ServletException {
        chain.doFilter(reques, response); // necessario per inoltrare la richiesta
    }
}
```
Esempio dichiarazione di un filtro in _web.xml_:

```xml
<filter>
    <filter-name>FiltroAutorizzazione</filter-name>
    <filter-class>it.unibas.FiltroAutorizzazione</filter-class>
</filter>
<filter-mapping>
    <filter-name>FiltroAutorizzazione</filter-name>
    <url-pattern>*</url-patern>
</filter-mapping>
```

## Security Context

La sicurezza in una webapp viene gestita nel package `javax.security.enterprise` di J2EE. Una classe di interfaccia `SecuriyContext` viene istanziata dal contenitore.

L'oggetto fornisce accesso al __principal__ con il metodo `Principal getPrincipal()`

### Principal

Il principal è un oggetto che consente di sapere se un utente è autenticato e risalire ai suoi permessi e ai suoi dati. Il metodo `String getName()` consente di conoscere il nome dell'utente autenticato e resituisce `null` in caso di mancata autenticazione.

## Eventi dell'applicazione

Alcuni tipi di eventi che un'applicazione web potrebbe registrare:

- Creazione dell'applicazione
- Rimozione dell'applicazione
- Modifiche alla mappa dell'applicazione

I primi due sono intercettabili implementando l'interfaccia `javax.servlet.ServletContextListener` tramite i metodi `contextInitialized()` e `contextDestroyed()`. Per monitorare le modifiche alla mappa è necessario implementare l'interfaccia `javax.servlet.ServletContextAttributesListener` e utilizzare i metodi `attributeAdded()`, `attributeRemoved()`, `attributeReplaced()`.

Gli eventi vanno registrati nel deployment descriptor sotto il tag `<listener>` specificandone la `<listener-class>`.
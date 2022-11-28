# Jersey

Jersey è un progetto open source della Eclipse Foundation, implementazione di riferimento dello standard JAX-RS.

Si integra nativamente con il server applicativo GlassFish di Eclipse ma è possibile utilizzarlo anche in container più leggeri.

Il modulo principale contiene solo l'implementazione dello standard, le altre funzionalità vengono fornite con una serie di estensioni tra le quali quelle per il supporto alla validazione o alla dependency injection.

Il modulo per la DI è HK2, l'estensione per la CDI è WELD.

## Weld

Weld gestisce la Dependency Injection. Le classi da iniettare sono quelle contenenti una _bean defining annotation_, che, come nello standard è principalmente una tra:

- @ApplicationScoped
- @RequestScoped

E' presente anche l'annotazione @SessionScoped inutile nel caso di backend stateless.

Per una questione di prestazioni ogni modulo dovrebbe dichiarare se contiene bean gestiti utilizzando un file `WEB-INF/beans.xml` e l'opzione _bean-discovery-mode_ con valori `annotated` (di default) o `all` (analisi di tutte le classi, sconsigliato).

Un utilizzo tipico è la necessità di istanziare un service per le risorse, Jersey mette a disposizione la sintassi con le annotazioni già vista in JAX-RS: `@RequestScoped`, `@ApplicationScoped` e `@Inject`.

## Elementi di un'applicazione jersey

### Punto di ingresso

Il traffico sul server deve essere intercettato da un servlet di Jersey che estende la classe `jakarta.wsrs.core.Application`.

Un approccio consiste nel dichiarare il punto di ingresso nel file _web.xml_.

Un altro nel creare una classe Applicazione che estenda Application e contenga l'annotazione `@ApplicationPath("prefisso")` per la quale è possibile specificare il prefisso di tutte le API dell'applicazione.

All'avvio il contenitore istanzierà tutti i componenti annotati, in particolare quelli aventi le annotazioni `@Path` e `@Provider`, anche nelle librerie esterne.

E' possibile sovrascrivere i metodi `getClass` e `getSingletons` per registrarne altri manualmente.

### Modello

I bean del modello sono java bean classici ma a differenza delle applicazioni desktop in questo caso è essenziale rendere un'entità facilmente identificabile. Per questo ogni bean avrà una proprietà `long id` autogenerata in fase di salvataggio e che servirà per identificare univocamente l'oggetto nelle successive operazioni.

I __DTO__ saranno essenziali nella serializzazione del modello, specialmente in casi di associazioni bidirezionali o liste nidificate. Le risorse dovrebbero lavorare esclusivamente con DTO sia in ingresso che in uscita e i service avranno il compito di convertirli nei bean del modello.

Per le conversioni tra modello e DTO si utilizzeranno delle librerie basate sulla riflessione. Un esempio è la classe `Mapper` basata sulla libreria `modelmapper` che offre 3 metodi statici `map` per la conversione di oggetti.

#### Caricamento pigro dei dati

Nell'esempio della media pesata non bisognerebbe restituire la lista degli esami per ogni studente che viene restituito. Allora sarà necessario esporre un'API per risalire agli esami dello studente, del tipo `/{idStudente}/esami`.

### Validazione dell'id

L'id non può essere validato in fase di creazione da parte del client e neanche in fase di creazione dell'oggetto sul server poichè il compito di assegnare un id spetta allo strato di persistenza. Per questo nel DTO non è prevista una verifica del campo id che verrà invece convalidato nel singolo metodo del service quando sarà necessario eseguire operazioni sull'oggetto.

In molti casi il client vorrebbe chiamare dei metodi su un oggetto subito dopo averlo creato, perciò è pratica comune che il metodo CRUD di salvataggio di un oggetto restituisca `long id` mentre per l'aggioramento questo non è necessario.

## DAO

Nelle applicazioni web, considerato il meccanismo del caricamento pigro dei dati e l'interazione nei casi reali con un DBMS, esiste un DAO per ogni entità e contiene vari metodi CRUD.

Per il DAO non verrà utilizzata da dependency injection ma un singleton `DAOFactory` con il compito di fabbricare le istanze dei dao sulla base della tecnologia scelta tramite una costante.

Per il DAO mock verrà utilizzato un Repository Mock: un singleton con una serie di proprietà rappresentanti lo stato del mock sul quale lavoreranno i singoli DAO. Il repository mantiene una proprietà `long prossimoId` che sarà utile per assegnare un id ad ogni nuova entità inserita.

Per evitare la scrittura di molto codice ci sarà una classe generica `RepositoryGenericoMock` che esporrà vari metodi di accesso generici per le operazioni CRUD e una classe `DAOGenericoMock` .


## Protezione delle risorse

Per l'autenticazione nel modello ci sarà una classe per gli utenti, generalmente questa contiene i campi username e password ed eventualmente i ruoli.

Nel processo di autenticazione il client fornsice le credenziali dell'utente, il server verifica le credenziali e in caso di successo restituisce un token. Il client dovrà poi restituire il token in tutte le richieste successive per essere autorizzato con l'intestazione `Authorization: Bearer <token>`

Il server quando riceve una richiesta contenente un token nell'intestazione deve validare il token (verificare che sia firmato correttamente e che non sia scaduto), estrarre l'username, caricare l'oggetto Utente dal DAO e verificare i suoi permessi, poi inserire le informazioni utili nel SecurityContext.

## Filtri

I filtri consentono di definire alcune operazioni che andrebbero svolte prima di eseguire il codice della risorsa o dopo averlo eseguito. Consentono di effettuare controlli di sicurezza senza duplicare il codice per ogni risorsa.

JAX-RS offre varie categorie di filtri, specifici per tipologia di operazione. Ad ogni tipologia corrisponde un'interfaccia da implementare.

Tutti i filtri devono essere annotati con `@Provider`.

### ContainerRequestFilter

L'interfaccia richiede di implementare il metodo `filter(ContainerRequestContext req)` che consente l'accesso alle informazioni della richiesta.

Il filtro viene eseguito prima di eseguire una risorsa. Nel caso in cui sia necessario interrompere la richiesta viene messo a disposizione il metodo `abortWith`.

### ContainerResponseFilter

Analogo del precedente ma invocato dopo aver eseguito la risorsa. Il metodo filter accetta come parametro anche un `ContainerResponseContext`.

In generale per ogni risorsa possono essere eseguiti vari filtri in serie, per stabilire l'ordine di esecuzione è necessario inserire l'annotazione `@Priority(<valore>` specificando un valore numerico che rappresenta la priorità del filtro.

I filtri di richiesta vengono eseguiti solo se la risorsa esiste, per bypassare questo controllo il filtro deve essere annotato con `@PreMatching`.

### Filtri Cors

In caso di richieste cross origin si realizza un ContainerResponseFilter per verificare se l'origine fa parte di quelle consentite (comunemente specificate in un array), in questo caso si aggiungono le intestazioni HTTP: `Access-Control-Allow-Origin` e `Access-Control-Allow-Methods`.

### Altre tipologie di filtri:

- `ExceptionMapper`: invocati quando si verifica un'eccezione
- `ParamConverterProvider`: convertitori personalizzati per i QueryParam

## Linee guida sui TEST

1. I test sula modello rimangono identici a quelli previsti con applicazioni Desktop e Console
2. I servizi vanno trattati come moduli di logica applicativa e per ogni servizio è previsto un test JUnit che esegue i casi CRUD facendo asserzioni sui risultati.
3. I test sulle risorse vanno eseguiti con strumenti che semplificano il lavoro come PostMan o SwaggerUI.

La libreria swagger si occupa anche di generare la documentazione in formato JSON scandendo automaticamente le risorse. La documentazione può essere estesa/personalizata con opportune annotazioni.

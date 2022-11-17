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

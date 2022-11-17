# JAX-RS

Un framework per la creazione di applicazioni web J2EE fornisce uno scheletro di applicazione web con un servlet principale che intercetta tutte le richieste e gestisce/genera tutti i componenti necessari sulla base di annotazioni scritte dal programmatore.

E' fondamentale il concetto di __bean gestito__: il programmatore predispone il codice ma sarà il framework a istanziare le risorse necessarie e chiamare i metodi che il programmatore ha definito sulla base di quello che avviene nell'applicazione.

I principali framework per lo sviluppo backend in Java sono Jersey, REST Easy, RESTlet e Spring Boot. Dei quali il primo e l'ultimo occupano la maggior fetta di mercato.

I framework forniscono solitamente anche servizi per la validazione dei bean e per la dependency injection.

JAX-RS, acronimo inizialmente di __Java API for RESTful Web Services__, ora __Jakarta RESTful Web Services__ è uno standard per i framework orientati allo sviluppo di API REST. Definisce le interfacce dei componenti e le annotazioni standard da utilizzare.

Il framework Jersey è l'implementazione di riferimento dello standard.

## Elementi di un'app JAX-RS

- Resources
- Services
- Providers
- Modello
- DAO
- DTO

### Resource

Le resource sono le classi responsabili della gestione di richieste e risposte. Ogni classe resource gestisce le richieste per una risorsa, ogni metodo gestisce un endpoint.

#### Annotazioni principali per le risorse

__@Path__: può essere applicata alla classe e al metodo e associa un URI alla risorsa (classe) o un URI di un endpoint al metodo che lo gestisce. Es. `@Path("/studenti")` sulla classe, `@Path("{idStudente}/mediaPesata")` sul metodo.

__@GET__, __@POST__, __@PUT__, __@DELETE__: associano il metodo HTTP al metodo che gestisce un endpoint

__@Produces(MediaType)__: consente di specificare il formato della serializzazione, il formato standard per REST è `MediaType.JSON`.

__@Consumes(MediaType)__: analogo del precedente per le richieste con corpo.

#### Binding dei parametri

Per recuperare parti dell'URI o della query string o intestazioni passate con la richiesta esistono annoazioni specifiche:

__@PathParam("id")__: prende il parametro `{id}` nel Path. (es. /studenti/{id}/media)

__@QueryParam("id")__: prende il valore di _id_ passato nella querystring

__@HeaderParam("id")__: prende il valore dell'intestazione _id_

__@CookieParam("id")__: prende il valore del cookie con nome _id_

Esempio di risorsa CRUD

```java
@Path("/studenti") @Produces(MediaType.APPLICATION_JSON)
public class RisorsaStudenti {
    @GET
    public List<StudenteDTO> getAll() {...}
    @GET @Path("/{id}")
    public StudenteDTO get(@PathParam("id") long id) {...}
    @POST @Consumes(MediaType.APPLICATION_JSON)
    public long add(StudenteDTO s) {...}
    @DELETE @Path("/{id}")
    public void delete(@PathParam("id") long id) {...}
}
```

Modello e DAO e DTO sono componenti ordinari.

### Services

Sono operatori utilizzati dalle resources per costruire le risposte. Le Resource infatti sono convenzionalmente senza stato e si occupano solo di gestire richieste e produrre risposte. La logica applicativa si trova nei services che sono perciò modulari e riutilizzabili.

L'operatore __@Provider__ ha lo scopo di selezionare un componente in modo che sia _scoperto_ dal framework nell'analisi del classpath. Un utilizzo classico sono le classi per i filtri.

## Dependency Injection

La dependency injection è una alternativa alla __service location__ per applicazioni in cui la quantità di componenti renda difficile quest'ultima.

Si chiamerà _client_ il componente che intende acquisire riferimenti di un altro componente, chiamato _server_ (nulla a che vedere con architetture client-server di rete).

La dependency injection prevede che il componente client debba soltanto dichiararli e utilizzarli senza localizzarli esplicitamente. Sarà un terzo componente esterno, detto __contenitore__ o __contesto__ a localizzare, creare e _iniettare_ i componenti richiesti dal client.

Tutti i bean oggetto di injection devono essere gestiti dal framework che deve controllarne il ciclo di vita.

La tecnica prende il nome di __inversione del controllo__ e il fenomeno va sotto il nome di __Hollywood principle__ (il framework dirà al componente "don't call me, I will call you").

In questo modo il componente ha codice molto più pulito in quanto dichiara semplicemente i componenti che intende utilizzare e sarà poi compito del framework acquisirli.

> Il framework non può iniettare bean che non gestisce

### Scope di un bean gestito

Lo scope è l'ambito di visibilità e il ciclo di vita di un bean, stabilisce quindi la politica di creazione e iniezione. 2 scope:

1. Application scope: unica istanza per tutta l'applicazione (simile al concetto di singleton)
2. Request scope: un'istanza del bean per ogni richiesta

Lo standard per le DI è pensato per essere utilizzato in qualsiasi tipologia di applicazione. Uno standard specifico __Context Dependency Injection__ include alcune annotazioni specifiche per la programmazione web.

### Jakarta Context Dependency Injection

E' l'implementazione di riferimento dello standard controllata da Eclipse.

Per indicare al framework i punti di iniezione si utilizza l'annotazione __@Inject__ applicata a proprietà, metodi o costruttori.

es `@Inject ServiceStudenti serviceStudenti`

Per gli scope esistono le annoazioni `@ApplicationScoped` o `@RequestScoped` da applicare ai bean gestiti.

L'annotazione `@Context` viene utilizzata per iniettare in una risorsa il riferimento ad un elemento collegato al contesto dell'applicazione web. Caso tipico è l'iniezione del security context: `@Context SecurityContext context` utilizzato per risalire al Principal e recuperarne l'identità.

Elementi iniettabili:

- SecurityContext
- ServletContext
- HttpServletRequest
- HttpServletResponse
- HttpHeaders
- UriInfo
- ServletConfig
- Providers, Configuration...

## Bean validation

Lo standard per la validazione dei valori in Java è __Jakarta Bean Validation__, Hibernate Validation è l'implementazione di riferimento.

Anche in questo caso il framework fornisce una serie di annotazioni per definire vincoli sui valori delle proprietà. La convalida può essere innescata manualmente o automaticamente dal framework che solleva eccezioni in caso di violazioni.

Principali annotazioni:

- __@NotNull__ 
- __@NotEmpty__ (stringa o collezione)
- __@NotBlank__ (stringa)
- __@Positive, @PositiveOrZero__ (numero)
- __@Negative, @NegativeOrZero__ (numero)
- __@Min(value=m)__ (numero)
- __@Max(value=m)__ (numero)
- __@AssertTrue__ (boolean)
- __@Size(min=m, max=M)__ (stringa o collezione)
- __@Email__
- __@Past, @PastOrPresent__ (date)
- __@Future, @FutureOrPresent__ (date)

Le annotazioni possono essere posizionate in corrispondenza di proprietà o parametri dei metodi ed è possibile er ognuna aggiungere un messaggio di errore.

```java
@NotNull(message="Non deve essere vuoto") String nome;
```

L'annotazione __@Valid__ associata ad un riferimento ad un bean con vincoli di validità innesca la validazione dei vincoli nella classe (richiede che il bean sia valido).

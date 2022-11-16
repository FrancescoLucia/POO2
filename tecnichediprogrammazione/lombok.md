# Lombok

Uno degli svantaggi di Java è l'eccessiva verbosità. Project Lombok è una libreria opensource nata per snellire lascrittura di codice Java.

Fornisce una serie di annotazioni che verranno elaborate dal preprocessore che le sostituirà con parti di codice prima di sottoporre la classe al compilatore.

Ad esempio l'annotazione `@Getter` inserisce implicitamente tutti i metodi getter per le proprietà della classe.

Per questa ragione è fondamentale il supporto degli IDE che devono gestire l'autocompletamento di metodi che non esistono (perchè implicitamente dichiarati nelle annotazioni lombok). Attualmente gli IDE principali lo supportano.

## Annotazioni

- @Getter
- @Setter
- @ToString
- @EqualsAndHashCode (sulla base di tutte le proprietà, di default)
- @NoArgsConstructor
- @AllArgsConstructor
- @RequiredArgsConstructor (solo le proprietà final)
- @Slf4j (crea un oggetto logger `log` )
- @Data (ToString, EqualsHashCode, Getter, Setter e RequiredArgsConstructor)
- @Value (oggetti immutabili con proprietà tutte final, ToString, Equals..., Getter, RequiredArgsConstructor)
- @NotNull (genera una guardia se la proprietà diventa null solleva NullPointerException)

### Proprietà delle annotazioni
Le annotazioni hanno proprietà che controllano il funzionamento e vengono inserite nel costruttore dell'annotazione. Es.` @ToString(callSuper=[call | skip| warn], of = {lista-dei-campi}, ...)`

Sulle proprietà della classe è possibile inserire annotazioni per includerle/escluderle es. `@ToString.Include` o `@EqualsHashCode.Exclude`.

## Pattern Builder

Il __Builder__ è un design pattern che risolve il problema della creazione di un oggetti con molte proprietà di cui alcune hanno valori di default.

Una soluzione potrebbe essere creare un costruttore vuoto e implementare tutti i metodi setter per le proprietà. Soluzione verbosa.

Un'altra è creare molti costruttori con argomenti uno per ogni variante di argomenti non nulli. Anche questa complessa e verbosa.

Il pattern builder risolve il problema tramite un oggetto esterno con un metodo `build()` e procedure per impostare le proprietà utilizzabili con uno stile conversazionale.

### Dichiarazione

```java
@Builder
public class Utente {
    private String nomeUtente;
    private String password;
    private String nome;
    @Builder.Default
    private String dipartimento = "Staff";
    @Builder.Default
    private String ruolo = "Utente";
}
```

### Utilizzo

```java
Utente u1 = Utente.builder()
                .nomeUtente("u1@email.it")
                .password("passowrd")
                .nome("Utente uno")
                .build();
Utente u2 = Utente.builder()
                .nomeUtente("u2@email.it")
                .password("password2")
                .nome("Utente due")
                .dipartimento("IT")
                .ruolo("Admin")
                .build();
                
```

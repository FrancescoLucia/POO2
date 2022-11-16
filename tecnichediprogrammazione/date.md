# Gestione delle date da Java 8

A partire da java 8 viene introdotto il package `java.time` che risolve alcuni problemi dovuti a scelte superate nella gestione delle date e semplifica il tutto prendendo spunto dalla piattaforma .NET.

Le classi per la gestione delle date sono `LocalDate`, `LocalTime` e `LocalDateTime`. 

`LocalDate` permette di creare una data con il metodo statico `of(<anno>, <mese>, <giorno>)`. A differenza della gestione con Calenadar la numerazione dei mesi è a base 1 e il comportamento di default non è permissivo: il costruttore solleva `java.time.DateTimeException`. Per ottenere la data attuale: `LocalDate.now()`.

`LocalTime` offre il metodo statico `of(<ore>,<minuti>,<secondi>)`, supera il limite di Calendar di non poter rappresentare solo orari.

Tutti gli oggetti del package hanno un metodo `format(<formatter>)` che prende come parametro un oggetto della classe `java.time.format.DateTimeFormatter`.

Per costruirlo è necessario specificare pattern e localizzazione: `DateTimeFormatter.of(<pattern>).withLocale(<locale>)`.

Il pattern però non è localizzato, l'alternativa è richiedere la stampa localizzata con il metodo `ofLocalizedDate` che accetta un `FormatStyle` che può assumere come valor `FULL`, `LONG`, `MEDIUM` e `SHORT`.

```java
LocalDate d = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofLocalizedDate(FormatStyle.MEDIUM).withLocale(Locale.US);
System.out.println("Data odierna: " + d.format(formatter));
```

Un `LocalDateTIme` è composto da un LocalDate e un LocalTime: `LocalDateTime.of(<localDate>, <localTime>)`.

Per accedere a parti della data mette a disposizione metodi predefiniti:

- `getDayOfMonth()`
- `getMonth()`
- `getYear()`
- `getHour()`
- `getMinute()`
- `getSecond()`

Tutte le classi del package offrono metodi per aggiungere o sottrarre intervalli di tempo:

- `plusMonths()`
- `plusDays()`
- `plusWeeks()`
- `plusYears()`
- ...

# Java e HTTP

Il package `java.net` offre un'interfaccia per la comunicazione a basso livello e una per la comunicazione ad alto livello.

## Socket

Le socket sono canali di comunicazione tra server e client.

Il client apre una connessione con un oggetto `java.net.Socket` e invia richieste con un OutputStream.

__Client__

```java
Socket socket = new Socket("localhost", 8080);
PrintWriter richiesta = new PrintWriter(socket.getOutputStream());
richiesta.println("Hello");
richiesta.flush(); // Ripulisci il buffer
BufferedReader risposta = new BufferedReader(new InputStreamReader(socket.getInputStream()));
String linea;
while ((linea = risposta.readLine()) != null) {
    System.out.println(linea);
}
socket.close();
```

__Server__

```java
ServerSocket serverSocket = new ServerSocket(8080);
Socket socket = serverSocket.accept(); // Bloccante fino alla richiesta
BufferedReader flusso = new BufferedReader(new InputStreamReader(socket.getInputStream()));
String richiesta = flusso.readLine();

PrintWriter risposta = new PrintWriter(socket.getOutputStream());
risposta.println("Echo:" +richiesta);
risposta.flush();
socket.close();
```

Le socket sono utlizzate quando si ha necessità di creare connessioni molto veloci e poco strutturate, ad esempio in un videogioco multiplayer o una chat istantanea. In generale per i casi standard sono poco utilizzate.

## HttpURLConnection

Classe astratta URLConnection e classe HttpURLConnection

Esempio di utilizzo

```java
HttpURLConnection urlConnection = null;
        try {
            URL url = new URL("http://www.google.it");
            urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.setRequestMethod("GET");
            urlConnection.setConnectTimeout(10000);
            urlConnection.setDoOutput(true);
            PrintWriter writer = new PrintWriter(urlConnection.getOutputStream());
            writer.write("q=Ciao");
            writer.flush();
            urlConnection.connect();
            InputStream risposta = urlConnection.getInputStream();
        } catch (IOException e) {
        } finally {
            urlConnection.disconnect(); // chiudo la connessione nel finally
        }
```

Una libreria alternativa è Apache HttpClient
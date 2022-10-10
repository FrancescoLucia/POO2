# Protocolli e standard - Introduzione alle reti di calcolatori

## Architettura Client - Server

E' un'architettura utilizzata nelle applicazioni distribuite. Il server è il sistema che offre i servizi e i client sono i sistemi che li utilizzano.

## Reti

Una rete di calcolatori è un insieme di calcolatori collegati fisicamente in grado di condividere risorse e servizi e di scambiarsi messaggi.

### Collegamenti e topologie

1. Collegamenti in rame
2. Fibra ottica
3. Ponti radio (Wi-Fi, 3G, 4G, 5G, bluetooth...)

#### Livello di distribuzione

- LAN - Local Area Network (1km)
- MAN - Metropolitan Area Network (100km)
- WAN - Wide Area Network (1000km)
- GAN - Global Area Network (10000km)
- PAN - Personal Area Network (10mt)
- BAN - Body Area Network (1mt)

#### Modalità di connessione

1. Commutazione di circuito
2. Commutazione di pacchetto

#### Protocolli

Un protocollo è un insieme di regole per la comunicazione tra calcolatori

**Protocollo TCP/IP**: ad ogni macchina è associato un indirizzo IP:

- IPv4: 32 bit, $2^{32}$ macchine collegabili
- IPv6: 128 bit, 340 miliardi di miliardi di miliardi di macchine collegabili

L'IPv4 è strutturato in 2 parti, l'identificatore della rete (NET ID) e l'identificatore del calcolatore (HOST, ultime due cifre).

La subnet mask è il numero che specifica quale parte dei numeri di un IP contiene il NET ID. 

#### DNS

- **Domain Name System**: servizio che associa un nome ad un IP
- **Domain Name Server**: macchina che offre il servizio
  
## Servizi internet

1. smtp: invio posta elettronica
2. pop/imap: ricezione posta elettronica
3. http: trasferimento risorse web
4. ssh: terminale remoto
5. ftp: trasferimento file

Data la possibilità di un server di offrire più servizi contemporaneamente, questi sono in ascolto su una __porta__.

## Pila TCP/IP

La comunicazione avviene  attraverso lo scambio di messaggi ad alto livello e ogni strato della rete si rivolge a quello inferiore (nella trasmissione, a quello superiore nella ricezione).

### Livelli:

1. Livello di trasporto: TCP
    - Orientato alla connessione, affidabile
    - Il messaggio è diviso in datagrammi (pacchetti)
2. Livello di rete: IP
    - Commutazione di pacchetto, non affidabile
    - Instradamento (routing) dei pacchetti verso la destinazione
3. Livello fisico
    - Vari protocolli (in base alla tecnologia di trasmissione)

import os

FILES = (
    'protocolliestandard/introduzione.md',
    'protocolliestandard/architettura.md',
    'protocolliestandard/risorse-e-uri.md',
    'protocolliestandard/http.md',
    'protocolliestandard/java-http.md',
    'tecnologieclient/html.md',
    'tecnologieclient/css.md',
    'tecnologieclient/jsdom.md',
    'tecnologieclient/aspettimetodologici.md',
    'serviziweb/introduzione.md',
    'serviziweb/rest.md',

    'programmazioneweb/introduzione.md',
    'programmazioneweb/servlet.md',
    'tecnichediprogrammazione/date.md',
    'tecnichediprogrammazione/lombok.md',
    'serviziweb/jaxrs.md',
    'serviziweb/jersey.md',
    
)

DESTINATION = "appunti.pdf"

if __name__ == "__main__":
    comando = "pandoc "
    for file in FILES:
        comando += file + " "
    comando += f" -o {DESTINATION}"
    print(f"Eseguo comando: {comando}")
    result = os.system(comando)
    os.system("clear")
    if result == 0:
        print("--- PDF creato ---")
    else:
        print("********** ERRORE NEL CREARE IL FILE ****************")
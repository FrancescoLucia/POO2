import os

FILES = (
    'protocolliestandard/introduzione.md',
    'protocolliestandard/architettura.md',
    'protocolliestandard/risorse-e-uri.md',
    'protocolliestandard/http.md',
    'protocolliestandard/java-http.md',
    
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
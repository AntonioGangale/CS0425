
import requests

def test_http_verb(method, url):
    """
    Esegue una singola richiesta HTTP con un verbo specifico e stampa il risultato.
    """
    print(f'\n--- Test con verbo: {method.upper()} ---')
    
    try:
        #Usa il metodo generico requests.request()
        #Per POST e PUT, inviamo un body vuoto (json={}) per simulare una richiesta valida
        if method.upper() in ['POST', 'PUT']:
            response = requests.request(method.upper(), url, json={}, timeout=3)
        else:
            response = requests.request(method.upper(), url, timeout=3)
        
        print(f'Risposta: {response.status_code} {response.reason}')
        
        #Un codice 200 OK per PUT o DELETE può indicare una configurazione debole
        if response.status_code == 200 and method.upper() in ['PUT', 'DELETE']:
            print("==> ATTENZIONE! Il server ha risposto 200 OK a una richiesta potenzialmente pericolosa.")
            
    except requests.exceptions.ConnectionError:
        print(f'ERRORE: Impossibile connettersi a {url}. Controlla l\'IP e la rete.')
        return False #Restituisce False per fermare il ciclo
    except Exception as e:
        print(f'È avvenuto un errore inaspettato: {e}')
    
    return True #Restituisce True per continuare il ciclo

#Inizio dello script
if __name__ == '__main__':
    #Lista dei verbi HTTP da testare
    http_verbs = ['GET', 'POST', 'PUT', 'DELETE']

    target_ip = input('Digita l\'indirizzo IP del target (es. 192.168.20.10): ')
    target_path = input('Digita il percorso della risorsa (es. /index.php o /mutillidae/): ')

    full_url = f'http://{target_ip.strip("/")}/{target_path.strip("/")}'

    print(f'\n{"="*50}')
    print(f'Inizio la scansione dei verbi su: {full_url}')
    print(f'{"="*50}')

    #Ciclo che scorre ogni verbo nella nostra lista
    for verb in http_verbs:
        #Se la funzione restituisce False (errore di connessione), interrompiamo il ciclo
        if not test_http_verb(verb, full_url):
            break

    print(f'\n{"="*50}')
    print('Scansione completata.')

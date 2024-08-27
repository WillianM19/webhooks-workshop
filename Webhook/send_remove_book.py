import requests
import json

def send_remove_book(title):
    url = "http://localhost:5001/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "title": title
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print("Resposta do servidor:", response.json())
        else:
            print("Erro:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar a solicitação: {e}")

if __name__ == "__main__":
    # Exemplo de título do livro a ser removido
    send_remove_book("Livro")

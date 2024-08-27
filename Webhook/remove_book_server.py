from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests

BOOK_SERVER_URL = 'http://localhost:5000/update-books'

class RemoveBookServerHandler(BaseHTTPRequestHandler):
    def get_books_from_server(self):
        try:
            response = requests.get('http://localhost:5000/books')
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro ao obter lista de livros: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Erro ao conectar ao servidor de livros: {e}")
            return []

    def do_POST(self):
        print("Recebendo solicitação para remover livro...")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            book_title = data.get('title')

            if not book_title:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Título do livro não fornecido"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                print("Erro: Título do livro não fornecido")
                return

            books = self.get_books_from_server()

            # Busca e remoção do livro
            initial_count = len(books)
            books = [book for book in books if book["title"] != book_title]

            if len(books) < initial_count:
                # Envia a lista atualizada de volta para o servidor `book_server`
                response = requests.post(BOOK_SERVER_URL, json={"books": books})
                if response.status_code == 200:
                    print(f"Livro removido: {book_title}")
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {"status": "success", "message": f"Livro '{book_title}' removido com sucesso"}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                else:
                    print(f"Erro ao atualizar lista de livros: {response.status_code}")
                    self.send_response(500)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {"status": "error", "message": "Erro ao atualizar lista de livros"}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                print(f"Livro não encontrado: {book_title}")
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Livro não encontrado"}
                self.wfile.write(json.dumps(response).encode('utf-8'))

        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "error", "message": "Erro ao decodificar JSON"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            print("Erro ao decodificar JSON")

def run(server_class=HTTPServer, handler_class=RemoveBookServerHandler, port=5001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

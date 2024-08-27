from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RemoveBookServerHandler(BaseHTTPRequestHandler):
    books = []  # Lista para armazenar os livros
    
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

            # Busca e remoção do livro
            initial_count = len(self.books)
            self.books = [book for book in self.books if book["title"] != book_title]

            if len(self.books) < initial_count:
                print(f"Livro removido: {book_title}")
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "success", "message": f"Livro '{book_title}' removido com sucesso"}
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

# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 2000 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            # Читаем HTML-файл
            with open("contacts.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            # Устанавливаем код ответа и заголовки
            self.send_response(200)
            self.send_header("Content-type", "text/html")  # Изменено на text/html
            self.end_headers()

            # Отправляем содержимое HTML-файла в ответ
            self.wfile.write(bytes(html_content, "utf-8"))
        except FileNotFoundError:
            # Если файл не найден, отправляем код 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1>")

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")

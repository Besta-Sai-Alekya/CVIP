from http.server import HTTPServer, BaseHTTPRequestHandler

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Clock</title>
</head>
<body>
    <div id="clock" style="font-size: 48px;"></div>
    <button onclick="toggleFormat()">Toggle Format</button>
    <script>
        var is24HourFormat = false;

        function updateClock() {
            var now = new Date();
            var hours = now.getHours();
            var minutes = String(now.getMinutes()).padStart(2, '0');
            var seconds = String(now.getSeconds()).padStart(2, '0');
            var ampm = '';

            if (!is24HourFormat) {
                hours = hours % 12 || 12;
                ampm = hours >= 12 ? ' PM' : ' AM';
            }

            document.getElementById('clock').textContent = hours + ':' + minutes + ':' + seconds + ampm;
        }

        function toggleFormat() {
            is24HourFormat = !is24HourFormat;
            updateClock();
        }

        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""

class ClockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, ClockHandler)
    print("Server started at localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

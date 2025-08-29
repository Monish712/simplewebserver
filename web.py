from http.server import HTTPServer, BaseHTTPRequestHandler

content = """<html>
<head>
    <title>Web application</title>
    <body>
        <table border="1" align="center" cellpadding="10" cellspacing="10">
            <caption><h1>List of protocols in TCP/IP protocol suite</h1></caption>
            <tr>
                <th>s.no</th><th>names</th><th>protocol</th>
            </tr>
            <tr>
                <td>1</td><td>Application layer</td><td>http,ftp</td>
            </tr>
            <tr>
            <td>2</td><td>transport layer</td><td>tcp & udp</td>
            </tr>
            <tr>
                <td>3</td><td>network layer</td><td>ipv4/ipv6</td>
                </tr>
                <tr>
                    <td>4</td><td>Link layer</td><td>ethernet</td>
                </tr>
        </table>
        
    </body>
</head>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>LAPTOP CONFIGURATION</title>
    </head>
    <body>
        <h2>Umabharathi P</h2>
        <h2>REFERENCE NO:26018686</h2>
        <table border="1" cellpadding="6" cellspacing="4">
    
    <tr bgcolor="lime">
        <th>1</th>
        <th>Device name</th>
        <td>TL15-53M-G2</td>
     </tr>  
     <tr>
        <th>2</th>
        <th>Processor</th>
        <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
     </tr>
     <tr>
        <th>3</th>
        <th>Installed RAM</th>
        <td>16.0 GB (15.7 GB usable)</td>
     </tr>
     <tr>
        <th>4</th>
        <th>Graphics Code</th>
        <td>Intel(R) Graphics (128 MB)</td>
     </tr>
     <tr>
        <th>5</th>
        <th>Storage</th>
        <td>116 GB of 477 GB used</td>
     </tr>
     <tr>
        <th>6</th>
        <th>Device ID</th>
        <td>42EA92B2-A404-4FC8-B5D2-539CCA8C895E</td>
    </tr>
    <tr>
        <th>7</th>
        <th>Product ID</th>
        <td>00342-42954-11692-AAOEM</td>
    </tr>
    <tr>
        <th>8</th>
        <th>System type</th>
        <td>64-bit operating system, x64-based processor</td>
    </tr>
    <tr>
        <th>9</th>
        <th>Pen and touch</th>
        <td>No pen or touch input is available for this display</td>
    </tr>            
   </table
  </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# import required Python modules
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import datetime
import pandas as pd

# define webserver and port the service is provided
hostName = "localhost"
serverPort = 8080

# define webserver class
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """response to HTTP GET request"""

        # define character set
        characterSet = "utf-8"

        # define response type
        self.send_response(200)

        # define HTTP header
        self.send_header("Content-type", "text/html;charset=UTF-8")
        self.end_headers()

        # calculate current date
        datum = datetime.date.today()
        datumStr = datum.strftime("%d.%m.%Y")

        # define HTML content with inline CSS
        content = [
            "<html>\n",
            "<head>\n",
            "<title>Titel</title>\n",
            #"<link rel=\"stylesheet\" type=\"text/css\" href=\"http://localhost:8080/farbschema.css\"/>",
            "</head>\n",
            "<body>\n",
            "<style>\n",
            ".fahrplan {border: 0px;}\n",
            ".fahrplan thead {background-color: blue; color: white; text-align: left}\n",
            ".fahrplan tbody {background-color: white;}\n",
            ".fahrplan th {padding: 5px; padding-left: 5px; text-align: left}\n",
            ".fahrplan td {padding: 5px; padding-left: 5px; text-align: left}\n",
            ".fahrplan tr:nth-child(even) {background-color: #EEEFFF;}\n",
            ".fahrplan tr:hover {background: silver; cursor: pointer;}\n",
            "</style>\n",
            #"<p>Request: %s</p>" % self.path,
            "<h1>Fahrplanauskunft Freiburg (Breisgau) Hbf am " + datumStr + "</h1>\n",
            "<hr>\n"
        ]

        # define data file with train schedule
        datendatei = "abfahrtstafel.csv"

        # define read mode
        modusLesen = "r"

        try:
            # read data file using built-in Pandas function
            inhalt = pd.read_csv(datendatei, delimiter=";")

            # convert the content into an HTML table
            tabelle = inhalt.to_html(classes='fahrplan')

            # extend the content list
            content.extend(tabelle)
            content.append("\n")
            content.append("<hr>\n")

        except IOError:
            # print error message: cannot open file
            print("Kann", datendatei, "nicht oeffnen")

        # extend content: end of body, and html content
        content.append("</body>\n")
        content.append("</html>\n")

        # output content
        for line in content:
            self.wfile.write(bytes(line, characterSet))

if __name__ == "__main__":
    # define web server
    webServer = HTTPServer((hostName, serverPort), MyServer)

    # output status message: web server started
    print("Server started http://%s:%s" % (hostName, serverPort))

    # start web server, and run it forever ...
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        # ... unless CTRL+C is pressed to stop the server
        pass

    # close web server
    webServer.server_close()

    # output status message: web server stopped
    print("Server stopped.")

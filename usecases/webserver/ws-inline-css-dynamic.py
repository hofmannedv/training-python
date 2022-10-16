# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# import required Python modules
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
import pandas as pd
import re

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

        # determine the current date
        datum = datetime.date.today()
        datumStr = datum.strftime("%d.%m.%Y")

        # determine the current time
        zeitpunkt = datetime.datetime.now()
        zeitpunktStr = zeitpunkt.strftime("%H:%M")

        # define HTML content with inline CSS
        content = [
            "<html>\n",
            "<head>\n",
            "<title>Fahrplanauskunft</title>\n",
            #"<link rel=\"stylesheet\" type=\"text/css\" href=\"http://localhost:8080/farbschema.css\"/>",
            "</head>\n",
            "<body>\n",
            "<style>\n",
            ".fahrplan {all: unset}\n",
            ".fahrplan table, tbody, thead, th, td {border:none;}\n",
            ".fahrplan thead {background-color: darkblue; color: white; text-align: left;}\n",
            ".fahrplan tbody {background-color: white;}\n",
            ".fahrplan th {padding: 5px; padding-left: 5px; text-align: left; text-transform: capitalize;}\n",
            ".fahrplan td {padding: 5px; padding-left: 5px; text-align: left}\n",
            ".fahrplan tr:nth-child(even) {background-color: #EEEFFF;}\n",
            ".fahrplan tr:hover {background: silver; cursor: pointer;}\n",
            ".schnellzug {color: red; font-weight: bold;}\n",
            ".flixtrain {color: darkgreen; font-weight: bold;}\n",
            "</style>\n",
            #"<p>Request: %s</p>" % self.path,
            "<h1>Fahrplanauskunft Freiburg (Breisgau) Hbf am %s um %s </h1>\n" % (datumStr, zeitpunktStr),
            "<hr>\n"
        ]

        # define data file with train schedule as csv file
        datendatei = "abfahrtstafel.csv"

        # define read mode
        modusLesen = "r"

        try:
            # read data file using built-in Pandas function
            inhalt = pd.read_csv(datendatei, delimiter=";")

            # sort values by the departure time column
            inhalt.sort_values(by=['zeitpunkt'], inplace=True)

            # filter by time: remove all entries from the past
            inhalt = inhalt[inhalt["zeitpunkt"] >= zeitpunktStr]

            # convert the content into an HTML table
            # - apply CSS class fahrplan
            # - do not show index column
            tabelle = inhalt.to_html(classes='fahrplan', index=False)

            # optimize generated HTML output table
            # - remove unnecessary spaces, and tabulators using a RegEx pattern
            muster = re.compile("\s{2,}")
            tabelle = re.sub(muster, r"", tabelle)

            # - remove leading spaces, and tabulators between ">", and cell content
            muster = re.compile("(>)\s(\S)")
            tabelle = re.sub(muster, r"\1\2", tabelle)

            # - remove trailing spaces, and tabulators between cell content, and "<"
            muster = re.compile("(\S)\s(<)")
            tabelle = re.sub(muster, r"\1\2", tabelle)

            # - add linebreak after each </tr>, </thead>, and </tbody> tag
            muster = re.compile("</(tr|thead|tbody)>")
            tabelle = re.sub(muster, r"</\1>\n", tabelle)

            # - add linebreak before each <tr>, <thead>, and <tbody> tag
            muster = re.compile("<(tr|thead|tbody)>")
            tabelle = re.sub(muster, r"\n<\1>", tabelle)

            # emphasize international, and high-speed trains (IC, ICE,
            # EC, TGV, NJ) in red
            muster = re.compile("(IC|ICE|EC|TGV|NJ)(\d+)");
            tabelle = re.sub(muster, r'<span class="schnellzug">\1\2</span>', tabelle)

            # emphasize trains from FLIXTRANS in dark-green
            muster = re.compile("<td>(FLIX)</td>");
            tabelle = re.sub(muster, r'<td><span class="flixtrain">\1</span></td>', tabelle)
            #print(tabelle)

            # right-align text in the right-most column
            muster = re.compile("<td>(\d+)(</td></tr>)");
            tabelle = re.sub(muster, r'<td style="text-align: right;">\1\2', tabelle)

            #print(tabelle)

             # extend the content list
            content.extend(tabelle)
            content.append("\n")
            content.append("<hr>\n")

        except IOError:
            # print error message: cannot open file
            print("Cannot open data file: ", datendatei)

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

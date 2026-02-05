#70 Python File Write
Wr = open("index.html","w")
Wr.write("<!doctype html>"
         "<head>"
         "<title>Document</title>"
         "</head>"
         "<body>"
         "<h1>Pro Zaman</h1>"
        "</body>"
         "</html>")
Wr = open("hablu.text","w")
Wr.write("Created and Write this text")
Wr = open("test.text","a")
Wr.write("This is another Text.")
Wr.write("This is another Text in new line.  \n")

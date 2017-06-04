from flask import Flask, request

app = Flask(__name__)

flag=0

def Activar():
  global flag
  print "Hola Mundo!"
  flag=1

def Desactivar():
  global flag 
  print "Adios Mundo!"  
  flag=0

@app.route('/')
def main():
    return """<html>
                   <head>
                      <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
                      <script>
                           $(document).ready(function(){

                                $('#btnSend').click(function(){

                                    $.ajax({
                                      type: 'POST',
                                      url: '/process',
                                      success: function(data){
                                        alert(data);
                                      }
                                    });
                                });

                           });
                      </script>
                   </head>
                   <body>
 
                    <input type="button" id="btnSend" value="process">
                    </body>
                   </html>"""


@app.route('/process', methods=['POST'])
def view_do_something():

    if request.method == 'POST' and flag == 0:
        #your database process here
        Activar()
        return "OK"
    elif request.method == 'POST' and flag == 1:
        Desactivar()
        return "unOK"
if __name__ == '__main__':
    app.run(debug = True)
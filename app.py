from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] ='thisIsMySecret' 

socketIo = SocketIO(app)

@app.route('/')
def index():
    return "Hey man"

@socketIo.on('message')
def handleMessage(message):
    print(message)
    send(message, broadcast=True)

if (__name__ == "__main__"):
    socketIo.run(app)
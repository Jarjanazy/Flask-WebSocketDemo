from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] ='thisIsMySecret' 


socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('message')
def handleMessage(message):
    print(message)
    send(message, broadcast=True)

if (__name__ == "__main__"):
    socketio.run(app)
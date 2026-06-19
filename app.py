import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Создаем приложение
app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins="*")

# Главная страница - она будет отдавать твою игру
@app.route('/')
def index():
    return render_template('index.html')

# Когда игрок заходит в игру
@socketio.on('connect')
def handle_connect():
    print("Игрок подключился")

# Когда игрок стреляет, сервер сообщает об этом другому игроку
@socketio.on('shoot')
def handle_shoot(data):
    # broadcast=True отправит это сообщение всем остальным игрокам
    emit('enemy_shoot', data, broadcast=True)

# Запуск сервера
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
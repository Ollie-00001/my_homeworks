from flask import Flask
from blueprints.masters.routes import masters_bp
from blueprints.appointments.routes import appointments_bp

#Создание экземпляра приложения Flask
app = Flask(__name__)

#Отключаем ASCII
app.config['JSON_AS_ASCII'] = False

# Регистрация блюпринтов
app.register_blueprint(masters_bp)
app.register_blueprint(appointments_bp)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import pyrebase
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


# Configuração do Firebase
firebaseConfig = {
    'apiKey': "AIzaSyDtskjYrVh9xAfs_bU1hJN-mesGARSDTDA",
    'authDomain': "keep-8fc35.firebaseapp.com",
    'databaseURL': "https://keep-8fc35-default-rtdb.firebaseio.com",
    'projectId': "keep-8fc35",
    'storageBucket': "keep-8fc35.firebasestorage.app",
    'messagingSenderId': "1057223168049",
    'appId': "1:1057223168049:web:35d9fa9303999762aac510",
    'measurementId': "G-36J4XV7CMD"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")

        if not email:
            return jsonify({"mensagem": "Email não fornecido", "status": "erro"}), 400
        
        if not senha:
            return jsonify({"mensagem": "Senha não fornecida", "status": "erro"}), 400

        user = auth.sign_in_with_email_and_password(email, senha)
        token = user["idToken"]

        return jsonify({
            "mensagem": "Login realizado com sucesso!",
            "data": {"token": token},
            "status": "sucesso"
        }), 200

    except Exception as e:
        return jsonify({
            "mensagem": "Email ou senha inválidos",
            "status": "erro",
            "detalhe": str(e)
        }), 401


@app.route('/cadastrarnovo', methods=['POST'])
def cadastrar_novo():
    try:
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")
        repet = data.get("repet")

        if not email:
            return jsonify({"mensagem": "Email não fornecido ou incorreto", "status": "erro"}), 400
        
        if not senha:
            return jsonify({"mensagem": "Senha não fornecido ou incorreta", "status": "erro"}), 400
        
        if not repet:
            return jsonify({"mensagem": "Senha não fornecido ou diferente", "status": "erro"}), 400

        auth.create_user_with_email_and_password(email, senha)

        return jsonify({"mensagem": "Usuário criado com sucesso"}), 200

    except Exception as e:
        return jsonify({"mensagem": "Não foi possível criar o usuário", "detalhe": str(e)}), 400


@app.route('/recuperarsenha', methods=['POST'])
def recuperar_senha():
    try:
        data = request.get_json()
        email = data.get("email")

        if not email:
            return jsonify({"mensagem": "Email não fornecido", "status": "erro"}), 400

        auth.send_password_reset_email(email)

        return jsonify({"mensagem": "Email de recuperação enviado com sucesso"}), 200

    except Exception as e:
        return jsonify({
            "mensagem": "Não foi possível enviar o email",
            "detalhe": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)

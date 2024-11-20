from flask import Flask, jsonify

app = Flask(__name__)

# Rota de exemplo
@app.route('/')
def home():
    return jsonify({"message": "API accessible via IPv6!"})

# Configurando o servidor para escutar no IPv6
if __name__ == '__main__':
    # '::' faz o servidor escutar em todos os endereços disponíveis, incluindo IPv6.
    app.run(debug=True, host='::', port=5000)

from app import app
from users import view

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, ssl_context=('cert.pem', 'key.pem'))

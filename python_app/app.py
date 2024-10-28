from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler

# Create a Flask application
app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Home route
@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return "Welcome to the Flask logging app!"

# Example route that triggers an error
@app.route('/error')
def error():
    app.logger.error('This is a test error')
    raise Exception("This is a test error.")

# Log all incoming requests
@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.path}")
# Log errors
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Error occurred: {str(e)}")
    return jsonify({"error": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

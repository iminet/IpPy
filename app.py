from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def get_ip():
    # Try to get IP from X-Forwarded-For if behind proxy
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For'].split(',')[0].strip()
    else:
        ip = request.remote_addr
    
    ip = ip.split(':')[0]

    # Get user agent
    user_agent = request.headers.get('User-Agent', 'Unknown')

    # Get current time in ISO format with timezone info (UTC)
    timestamp = datetime.now().isoformat()

    return jsonify({ 'status': 'OK', 'ip': ip, 'user_agent': user_agent, 'timestamp': timestamp } )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

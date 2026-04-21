import os
import uuid
from flask import Flask, request, jsonify, send_from_directory
from runner import run_python_code

app = Flask(__name__, static_folder='static', static_url_path='')

# Đảm bảo thư mục sandbox tồn tại
SANDBOX_DIR = os.path.join(os.path.dirname(__file__), 'sandbox')
os.makedirs(SANDBOX_DIR, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '').strip()
    if not code:
        return jsonify({'output': 'Error: No code provided'}), 400

    # Tạo file tạm để lưu code
    filename = f"{uuid.uuid4().hex}.py"
    filepath = os.path.join(SANDBOX_DIR, filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)

        # Chạy code với giới hạn thời gian (timeout) và bộ nhớ
        output, error = run_python_code(
            filepath,
            timeout=5,          # giới hạn 5 giây
            memory_limit_mb=128 # giới hạn 128MB RAM (chỉ hoạt động trên Linux)
        )

        if error:
            return jsonify({'output': error})
        return jsonify({'output': output})

    except Exception as e:
        return jsonify({'output': f'Server Error: {str(e)}'})
    finally:
        # Dọn dẹp file tạm
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

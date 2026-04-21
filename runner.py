import subprocess
import resource
import platform

def set_memory_limit(memory_mb):
    """Đặt giới hạn bộ nhớ (chỉ hoạt động trên Linux/Unix)"""
    if platform.system() != 'Windows':
        memory_bytes = memory_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))

def run_python_code(filepath, timeout=5, memory_limit_mb=128):
    """
    Chạy file Python trong subprocess với giới hạn thời gian và bộ nhớ.
    Trả về (stdout, stderr)
    """
    try:
        # Sử dụng preexec_fn để set giới hạn bộ nhớ trước khi chạy process con
        def set_limits():
            if platform.system() != 'Windows':
                resource.setrlimit(resource.RLIMIT_AS, (memory_limit_mb * 1024 * 1024, -1))
                # Có thể thêm CPU time limit nếu muốn
                # resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout))

        proc = subprocess.run(
            ['python3', '-I', filepath],  # -I để chạy ở isolated mode (không load site-packages)
            capture_output=True,
            text=True,
            timeout=timeout,
            preexec_fn=set_limits if platform.system() != 'Windows' else None,
            cwd='/tmp'  # đổi thư mục làm việc để tránh truy cập file hệ thống
        )
        return proc.stdout, proc.stderr

    except subprocess.TimeoutExpired:
        return '', f'Error: Timeout ({timeout}s) exceeded'
    except Exception as e:
        return '', f'Error: {str(e)}'

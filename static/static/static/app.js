const outputDiv = document.getElementById('output');
const codeInput = document.getElementById('codeInput');
const runBtn = document.getElementById('runBtn');
const clearBtn = document.getElementById('clearBtn');

// Gửi code đến server
async function runCode() {
  const code = codeInput.value.trim();
  if (!code) {
    appendOutput('Error: No code to run\n');
    return;
  }

  appendOutput(`> Running...\n`);
  runBtn.disabled = true;

  try {
    const response = await fetch('/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    });

    const data = await response.json();
    appendOutput(data.output + '\n');
    appendOutput('> ');
  } catch (err) {
    appendOutput(`Network Error: ${err.message}\n> `);
  } finally {
    runBtn.disabled = false;
  }
}

// Thêm nội dung vào terminal
function appendOutput(text) {
  outputDiv.innerText += text;
  // Tự động scroll xuống cuối
  const terminal = document.getElementById('terminal');
  terminal.scrollTop = terminal.scrollHeight;
}

// Xóa màn hình terminal
function clearTerminal() {
  outputDiv.innerText = '> ';
  codeInput.value = '';
}

// Sự kiện
runBtn.addEventListener('click', runCode);
clearBtn.addEventListener('click', clearTerminal);

// Ctrl+Enter để chạy
codeInput.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.key === 'Enter') {
    e.preventDefault();
    runCode();
  }
});

// Khởi tạo
outputDiv.innerText = '> ';

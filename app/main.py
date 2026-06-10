from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        message="Hello from CI/CD demo!",
        author="your-name",
        version="1.0.0",
    )


@app.get("/health")
def health():
    """健康检查接口，给部署后的冒烟测试用。"""
    return jsonify(status="ok")


if __name__ == "__main__":
    # 生产环境用 gunicorn，这里只是为了本地直接 python app/main.py 启动
    app.run(host="0.0.0.0", port=5000, debug=True)

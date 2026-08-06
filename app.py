from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>GitOps Demo</h1>
    <h2>Deployment using GitHub Actions + Argo CD</h2>
    <p>Hello from Kubernetes!</p>
    """

@app.route("/health")
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Testing'

@app.route('/test')
def test():
    return 'Test endpoint'

if __name__ == "__main__":
    app.run()

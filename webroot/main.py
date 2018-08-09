from flask import Flask, render_template
import argparse

app = Flask(__name__)

@app.route('/')
def home():
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--local", type=bool, default=False)
  args = parser.parse_args()

  endpoint = "http://localhost:7777/" if args.local else "http://23.97.186.93:8080/"

  return render_template('index.html', endpoint=endpoint)

if __name__ == '__main__':  
  app.run(host='127.0.0.1', port=5000)
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['POST', 'GET'])
def test():
    with open('./emails.txt', 'r') as file:
        emails = list()
        page = int(str(request.args.get('page'))) - 1
        print(page)
        file.readline()
        for i in range((page+1)*20):
            if i >= page*20:
                emails.append(file.readline().split(',')[0])
            else:
                file.readline()
        temp = json.dumps(emails)
        print(len(temp))
        return str(temp)


@app.route('/search', methods=['POST', 'GET'])
def search():
    word = str(request.args.get('word'))
    with open('./emails2.txt', 'r') as file:
        emails = file.read().split(' ')
        result = list(filter(lambda x: word in x, emails))
        return json.dumps(result)


if __name__ == '__main__':
    app.run(port=8050, host='localhost')
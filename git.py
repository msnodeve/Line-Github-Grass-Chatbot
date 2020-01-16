from flask import Flask, make_response, request, jsonify
import requests, time
from bs4 import BeautifulSoup

import db

app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def webhook():
    req = request.get_json(force=True)
    print(req)
    method = req.get("queryResult").get("outputContexts")[0].get("parameters").get("work")
    print(method)

    if method == "등록":
        result = db.signUpUser(getIdentity(req), getUserId(req))
        print(str(result))
        return make_response(jsonify({'fulfillmentText': getUserId(req) + "님! 환영~^^"}))
    elif method == "사용자수":
        result = db.getUsers()
        users = ""
        for i in result:
            users += i[0] + "님\n"
        users += "총 " + str(len(result)) + "명이 사용중 입니다!"
        return make_response(jsonify({'fulfillmentText': users}))
    elif method == "잔디그래프":
        result = db.getUser(getIdentity(req))
        url = "https://ghchart.rshah.org/" + result[0][0]
        print(url)
        userCommitFromGithub("test")
        return make_response(jsonify({'fulfillmentText': url}))
    elif method == "커밋횟수":
        result = db.getUser(getIdentity(req))
        commit = userCommitFromGithub(result[0][0])
        response = result[0][0] + "님 금일 커밋 회수는 " + str(commit) + "입니다."
        return make_response(jsonify({'fulfillmentText': response}))


def userCommitFromGithub(userId):
    ti = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    request = requests.get('https://github.com/' + userId)
    soup = BeautifulSoup(request.content, 'html.parser')
    attr = {"class": "day", "data-date": ti}
    data = soup.find_all("rect", attrs=attr)
    return data[0].get('data-count')


# def viewGlass(req):
#     req = request.get_json(force=True)
#     identity = getIdentity()
#     #DB에 있는 아이디랑 접속 아이디랑 비교
#     url =  "https://ghchart.rshah.org/" + identity


def getIdentity(req):
    identity = req.get("originalDetectIntentRequest").get("payload").get("data").get("source").get("userId")
    return identity


def getUserId(req):
    userId = req.get("queryResult").get("outputContexts")[0].get("parameters").get("id")
    return userId


if __name__ == '__main__':
    app.run(debug=True)

    # elif method == "잔디조회":
    #     #잔디가져오기
    # elif method == "커밋횟수":
    #     #커밋횟수 가져오기

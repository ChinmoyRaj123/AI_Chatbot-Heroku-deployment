from chatbot_run import chatbot_response
from scrape import google_response
from flask import Flask, render_template, request

app= Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def getBotResponse():
    user_input= request.args.get('msg')
    user_input = user_input.lower()
    if len(user_input)>1:
        word_check = user_input.split(" ")[0]
        if (word_check == "google"):
            ques = user_input.split(' ', 1)[1]
            ans= google_response(ques)
        else:
            ans = chatbot_response(user_input)
    else:
        ans = "Please enter a valid query"
    return ans



if __name__ == "__main__":
    app.run(threaded=False)

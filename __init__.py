from flask import Flask, jsonify, request
import ChatGPT
import constants

app = Flask(__name__)

@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():

    if request.method == "GET":
        if request.args.get('hub.verify_token') == constants.VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
          return "Invalid verification token"

    data=request.get_json()
    message=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    if message is not None:
        res = ChatGPT.get_response(message)
        res=res.replace("\\n","\\\n")
        res=res.replace("\\","")
        f = open("text.txt", "w")
        f.write(res)
        f.close()

        return jsonify({"status": "success"}, 200)

if __name__ == "__main__":
  app.run(debug=True)
  
# idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
# timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
# telephoneNumberClient=data['entry'][0]['changes'][0]['value']['messages'][0]['from']

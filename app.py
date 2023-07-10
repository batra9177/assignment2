from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def joke():
    if request.method == 'GET':
        joke = ["I invented a new word! Plagiarism!",
                "Whoever invented the knock-knock joke should get a no bell prize.",
                "If two vegans are having an argument, is it still considered beef?",
                "This furniture store keeps emailing me, all I wanted was one night stand!",
                "I never wanted to believe that my Dad was stealing from his job as a road worker. But when I got home, all the signs were there.",
                "Reversing the car: \'Ah, this takes me back\'",
                "Nurse: Doctor, there's a patient that says he's invisible. Doctor: Well, tell him I can't see him right now!",
                "I used to be addicted to the hokey pokey, but I turned myself around.", "When do doctors get angry? When they run out of patients.",
                "A steak pun is a rare medium well done."]
        rng = np.random.default_rng(12345)
        random_number = rng.integers(low=0, high=9)
        selected_joke = joke[random_number]

        data = {
            "joke": selected_joke
        }

        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

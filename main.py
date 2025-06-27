import replicate
from flask import Flask, request, jsonify

app = Flask(__name__)

import os
replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")

    output = replicate.run(
        "stability-ai/stable-diffusion",
        input={"prompt": prompt}
    )

    return jsonify({"image": output[0]})

app.run(host="0.0.0.0", port=8080)

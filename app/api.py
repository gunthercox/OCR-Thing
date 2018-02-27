from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
from io import BytesIO
import base64


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    request_json = request.get_json(force=True)
    image_string = request_json.get('image')

    if not image_string:
        return jsonify(
            error={
                'image': 'This field is required.'
            }
        ), 400

    image = Image.open(BytesIO(base64.urlsafe_b64decode(image_string)))

    image_data = pytesseract.image_to_data(
        image,
        lang='eng',
        output_type=pytesseract.Output.DICT
    )

    print(image_data)

    return jsonify(image_data)

from flask import Flask, request, jsonify
from ocr_tamil.ocr import OCR

app = Flask(__name__)

ocr = OCR(detect=True)

@app.route('/ocr', methods=['POST'])
def recognize_text():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image file'}), 400
        image = request.files['image']
        texts = ocr.predict(image)
        return jsonify({'text': ' '.join(texts[0])})

if __name__ == '__main__':
    app.run(debug=True)
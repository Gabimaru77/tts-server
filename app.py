from flask import Flask, request, send_file
from gTTS import gTTS
import io

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
def text_to_speech():
    text = request.args.get('text', '')
    lang = request.args.get('lang', 'ar')
    if not text:
        return {"error": "No text provided"}, 400
    tts = gTTS(text=text, lang=lang)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return send_file(fp, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, render_template, jsonify, send_from_directory, abort
import assemblyai as aai
from moviepy.editor import VideoFileClip
import whisper
import os

app = Flask(__name__)
output_folder = os.path.abspath("output")

@app.route('/', methods=['GET'])
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    type = request.args.get('transcriber', 'whisper').lower()

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Delete all files in the output directory
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    file_path = os.path.join(output_folder, file.filename)
    file.save(file_path)

    if file.filename.lower().endswith('.wav'):
        audio_path = file_path
    else:
        video = VideoFileClip(file_path)
        audio_path = file_path.rsplit('.', 1)[0] + '.wav'
        video.audio.write_audiofile(audio_path)

    # transcribe
    transcript_filename = file.filename.rsplit('.', 1)[0] + '_transcript.txt'
    transcript_path = os.path.join(output_folder, transcript_filename)
    if type == 'whisper':
        model = whisper.load_model("medium")
        result = model.transcribe(audio_path)
        with open(transcript_path, 'w') as f:
            f.write(result["text"])
    
    elif type == 'assembly':
        from keys import AAI_API_KEY
        aai.settings.api_key = AAI_API_KEY
        config = aai.TranscriptionConfig(speaker_labels=True)
        transcriber = aai.Transcriber()
        result = transcriber.transcribe(
            audio_path,
            config=config
        )

        with open(transcript_path, 'w') as f:
            for utterance in result.utterances:
                f.write(f"{utterance.speaker.upper()}: {utterance.text}\n")

    transcript_url = request.host_url + 'output/' + transcript_filename
    return jsonify({'message': 'File uploaded and processed successfully', 'transcript_url': transcript_url}), 200

@app.route('/output/<filename>')
def download_file(filename):
    file_path = os.path.join(output_folder, filename)
    if not os.path.exists(file_path):
        abort(404)  
    return send_from_directory(output_folder, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
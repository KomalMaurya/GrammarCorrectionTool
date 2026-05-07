from flask import Flask, render_template, request
from language_tool_python import LanguageTool
import os

# Initialize Flask app
app = Flask(__name__)

# Use LanguageTool public API
tool = LanguageTool(
    'en-GB',
    remote_server='https://api.languagetool.org'
)

# Home Route
@app.route('/')
def index():
    return render_template(
        'index.html',
        corrected_text='',
        original_text=''
    )

# Spell Check Route
@app.route('/spell', methods=['POST'])
def spell_check():
    try:
        # Get text from form
        text = request.form.get('text', '')

        # Correct grammar and spelling
        corrected_text = tool.correct(text)

        return render_template(
            'index.html',
            corrected_text=corrected_text,
            original_text=text
        )

    except Exception as e:
        return render_template(
            'index.html',
            corrected_text=f"Error: {str(e)}",
            original_text=''
        )

# Run Flask App
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )
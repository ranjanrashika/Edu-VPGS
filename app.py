from flask import Flask, render_template, request
import pandas as pd
from  model import get_video_recommendations

app = Flask(__name__)

dataset = pd.read_csv('C:\\Users\\Rashika Ranjan\\OneDrive\\Desktop\\DL-PROJECT\\videos.csv')
@app.route('/')
def home():
    """Render the homepage with a form."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """Handle recommendations based on syllabus input."""

    syllabus = request.form['syllabus'].split('\n')
    recommendations = get_video_recommendations(syllabus, dataset)

    return render_template('index.html', recommmendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
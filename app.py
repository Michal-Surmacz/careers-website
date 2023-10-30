from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': 50000
  },
  {
  'id': 2,
  'title': 'Java Developer',
  'location': 'Los Angeles',
  'salary': 55000
  },
  {
  'id': 3,
  'title': 'Web Developer',
  'location': 'Chicago',
  'salary': 48000
  },
  {
  'id': 4,
  'title': 'Software Engineer',
  'location': 'San Francisco',
  'salary': 60000
  },
  {
  'id': 5,
  'title': 'Front-End Developer',
  'location': 'Boston',
  'salary': 52000
  },
  {
  'id': 6,
  'title': 'Data Analyst',
  'location': 'Seattle',
  'salary': 51000
  }
]

@app.route("/")
def hello():
    return render_template('home.html', 
                           jobs=JOBS,
                          company_name='TechFusion')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

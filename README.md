<h1>🎵 Mood-Based Music Recommendation System</h1>

<h2>🩵 Project Overview</h2>
<p>The <strong>Mood-Based Music Recommendation System</strong> recommends songs based on the user’s mood.  
It takes input as a user-selected mood or a facial expression image, processes it through a machine learning model, and returns a personalized playlist or song suggestions.  
Recommended songs are played directly in <strong>Spotify</strong> using the Spotify Web API.</p>

<blockquote>
 <em>Example:</em><br>
If the user is feeling <strong>happy</strong>, the system may recommend upbeat songs and automatically play them on Spotify.
</blockquote>

<h2> Key Features</h2>
<ul>
  <li>* Detects user mood from facial expression images or manual selection</li>
  <li>* Uses ML/Deep Learning for mood classification</li>
  <li>* Provides personalized music recommendations</li>
  <li>* Plays recommended songs directly in <strong>Spotify</strong> via Spotify Web API</li>
  <li>* Backend implemented with FastAPI</li>
  <li>* Simple and user-friendly frontend with HTML</li>
  <li>* Easily extendable for new moods or music datasets</li>
</ul>

<h2> System Workflow</h2>
<ol>
  <li>User provides input:
    <ul>
      <li>Upload a facial expression image (<code>preprocess_image.py</code>)</li>
      <li>Or manually select mood from the frontend</li>
    </ul>
  </li>
  <li>Backend processes the input:
    <ul>
      <li>Preprocessing using <code>preprocess_image.py</code></li>
      <li>Mood prediction using trained model (<code>train_model.py</code>)</li>
      <li>Music recommendation using <code>music_recommender.py</code></li>
      <li>Play songs directly in <strong>Spotify</strong> using Spotify API</li>
    </ul>
  </li>
  <li>Response sent to frontend:
    <ul>
      <li>Recommended songs displayed in <code>index.html</code></li>
    </ul>
  </li>
</ol>

<h2> Technologies Used</h2>
<table>
<tr><th>Category</th><th>Tools / Libraries</th></tr>
<tr><td>Programming Language</td><td>Python 3.10</td></tr>
<tr><td>Backend Framework</td><td>FastAPI</td></tr>
<tr><td>Frontend</td><td>HTML, CSS</td></tr>
<tr><td>Deep Learning / ML</td><td>TensorFlow, Keras, scikit-learn</td></tr>
<tr><td>Image Processing</td><td>OpenCV, PIL</td></tr>
<tr><td>Data Handling</td><td>NumPy, Pandas</td></tr>
<tr><td>Spotify Integration</td><td>Spotipy / Spotify Web API</td></tr>
<tr><td>Utilities</td><td>utils.py for helper functions</td></tr>
<tr><td>IDE</td><td>VS Code</td></tr>
</table>

<h2> Project Folder Structure</h2>
<pre>
MoodMusicSystem/
│
├── backend/
│   └── app/
│       ├── main.py               # FastAPI main server
│       ├── models.py             # Data models / schemas
│       ├── music_recommender.py  # Logic to recommend songs
│       ├── preprocess_image.py   # Image preprocessing
│       ├── train_model.py        # Train mood classification model
│       └── utils.py              # Helper functions
├── frontend/
│   └── index.html                # Frontend interface
├── dataset/                       # Mood-labeled music / images
├── requirements.txt               # Dependencies list
└── README.md                      # Project documentation
</pre>

<h2> Installation & Setup (Windows)</h2>

<h3>1. Clone the Project</h3>
<pre><code>git clone https://github.com/yourusername/mood-music-recommender.git
cd mood-music-recommender
</code></pre>

<h3>2. Open Command Prompt or PowerShell</h3>
<p>Press <strong>Windows + R</strong>, type <code>cmd</code>, and press Enter.  
Navigate to the project folder:</p>
<pre><code>cd C:\Users\<YourUserName>\Desktop\MoodMusicSystem
</code></pre>

<h3>3. Create a Virtual Environment</h3>
<pre><code>python -m venv venv
</code></pre>

<h3>4. Activate the Virtual Environment</h3>
<pre><code>venv\Scripts\activate
</code></pre>
<p>After activation, you should see:</p>
<pre><code>(venv) C:\Users\YourName\Desktop\MoodMusicSystem&gt;
</code></pre>

<h3>5. Install Required Libraries</h3>
<p>If <code>requirements.txt</code> exists:</p>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>If not, install manually:</p>
<pre><code>pip install fastapi uvicorn tensorflow opencv-python numpy pandas spotipy
</code></pre>

<h3>6. Spotify API Setup</h3>
<p>To play songs in Spotify, you need a <a href="https://developer.spotify.com/dashboard/">Spotify Developer Account</a> and a Client ID & Client Secret.  
Store them in a <code>.env</code> file in the backend folder:</p>
<pre><code>SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
</code></pre>
<p>The backend uses these credentials to authenticate and play songs via the Spotify Web API.</p>

---

<h2> How to Run the Project</h2>

<h3> Step 1 — Start Backend Server</h3>
<pre><code>cd backend
uvicorn app.main:app --reload
</code></pre>
<p>This starts the FastAPI backend at <code>http://127.0.0.1:8000</code>.</p>

<h3> Step 2 — Open Frontend</h3>
<p>Open <code>frontend/index.html</code> in your web browser. The frontend communicates with the backend API to:</p>
<ul>
  <li>Send user mood selection or uploaded image</li>
  <li>Receive recommended music</li>
  <li>Play songs directly in <strong>Spotify</strong></li>
  <li>Display songs on the page</li>
</ul>

---

<h2> Example Output</h2>
<p><strong>Input:</strong> Upload an image of your face or select "Happy" mood from dropdown.</p>

<p><strong>Output:</strong></p>
<ul>
  <li>Detected mood: <strong>Happy</strong></li>
  <li>Recommended songs:</li>
  <ul>
    <li>"Happy" by Pharrell Williams — <em>played in Spotify</em></li>
    <li>"Can't Stop the Feeling!" by Justin Timberlake — <em>played in Spotify</em></li>
    <li>"Good Feeling" by Flo Rida — <em>played in Spotify</em></li>
  </ul>
</ul>

---

<h2> Future Improvements</h2>
<ul>
  <li>Train on larger, diverse datasets for more accurate mood detection</li>
  <li>Add support for additional moods (relaxed, angry, energetic)</li>
  <li>Integrate Spotify / YouTube APIs for live music recommendations</li>
  <li>Mobile-friendly frontend using React Native or Flutter</li>
</ul>

---

<h2> Author</h2>
<p><strong>Sasika Sewmini</strong><br>
University of Moratuwa — 3rd Year Undergraduate<br>
<a href="https://www.linkedin.com/in/sasika-sewmini-dp-829535351">LinkedIn Profile</a><br>
Email: <a href="mailto:dpsasikapeiris@gmail.com">dpsasikapeiris@gmail.com</a></p>

<p>⭐ If you like this project, give it a star on GitHub!</p>

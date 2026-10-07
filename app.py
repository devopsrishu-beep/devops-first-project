from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Banaras Diaries - Varanasi Blog</title>
        <style>
            body { font-family: Arial; margin:0; background:#fff8f0; }
            .header { background:white; padding:20px; text-align:center; box-shadow:0 2px 10px #ddd; }
            .header h1 { color:#ff6a00; margin:0; }
            .hero { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1561361058-c24cecae35ca'); background-size:cover; color:white; padding:80px 20px; text-align:center; }
            .hero h2 { font-size:40px; }
            .cards { display:flex; justify-content:center; gap:20px; padding:30px; flex-wrap:wrap; }
            .card { background:white; width:300px; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px #ccc; }
            .card img { width:100%; height:180px; object-fit:cover; }
            .card div { padding:15px; }
            .card h3 { margin:0; color:#333; }
        </style>
    </head>
    <body>
        <div class='header'><h1>Banaras Diaries</h1><p>Varanasi Blog - Temples, Ghats, Food & Culture</p></div>
        <div class='hero'><h2>Banaras - Dil Se</h2><p>Exploring the spiritual heart of Kashi</p></div>
        <div class='cards'>
            <div class='card'><img src='https://images.unsplash.com/photo-1561361058-c24cecae35ca'><div><h3>Top 10 Ghats in Varanasi</h3><p>Dashashwamedh to Assi Ghat ki kahani.</p></div></div>
            <div class='card'><img src='https://images.unsplash.com/photo-1504674900247-0877df9cc836'><div><h3>Famous Food of Banaras</h3><p>Chaat, Kachori, Malaiyo aur Lassi.</p></div></div>
            <div class='card'><img src='https://images.unsplash.com/photo-1555099962-4199c345e5dd'><div><h3>My DevOps Journey</h3><p>Kaise maine ye website banayi.</p></div></div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Rishu - Banaras Explorer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial; margin:0; padding:0; background:#FFF8E7; }
        .header { background:#FF6B00; color:white; padding:25px; text-align:center; }
        .about { background:white; margin:20px; padding:20px; border-radius:15px; box-shadow: 0 2px 10px #ccc; }
        .container { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; padding:20px; }
        .card { background:white; width:300px; border-radius:15px; overflow:hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
        .card img { width:100%; height:200px; object-fit:cover; }
        .card h3 { padding:10px 15px 0 15px; }
        .card p { padding:0 15px 15px 15px; color:#555; }
        .video-box { text-align:center; background:white; margin:20px; padding:20px; border-radius:15px; }
        .footer { background:#333; color:white; text-align:center; padding:15px; margin-top:20px; }
    </style>
</head>
<body>

<div class="header">
    <h1>🙏 Har Har Mahadev - Welcome to My Banaras Journey 🙏</h1>
    <p>DevOps | Docker | Cloud Learning Project</p>
</div>

<!-- MERE BARE ME - About Rishu -->
<div class="about">
    <h2>👋 About Me - Rishu</h2>
    <p><b>Namaste! Main Rishu, Varanasi (Kashi) se.</b></p>
    <p>Ek Banarasi ladka jo DevOps aur Cloud seekh raha hai. Is website ko maine Docker me banaya hai aur apne laptop se live kiya hai <b>devopsrishu.duckdns.org</b> pe.</p>
    <p>Mera sapna hai ek bada Cloud Engineer banna. Din me code, sham ko Assi Ghat pe chai! ☕</p>
    <p><b>Skills:</b> Docker, Git, Linux, Python Flask, AWS Learning</p>
    <p><i>"Banaras hai to sab kuch hai!"</i></p>
</div>

<!-- Photos Section - Sab Photos -->
<div class="container">

    <div class="card">
        <img src="/static/rishuassi.jpg">
        <h3>Subah-e-Banaras - Assi Ghat</h3>
        <p>Subah 5 baje Ganga kinare yoga, chai aur shanti. Meri favourite jagah.</p>
    </div>

    <div class="card">
        <img src="/static/rishuaarti.jpg">
        <h3>Ganga Aarti - Dashashwamedh Ghat</h3>
        <p>Shaam ko 7 baje hazaro diye jalte hai. Aisa nazara kahi nahi milega.</p>
    </div>

    <div class="card">
        <img src="/static/rishufood.jpg">
        <h3>Banarasi Zaika</h3>
        <p>Kachori-Sabzi, Malaiyo, Banarasi Paan aur Kulhad Lassi - Jaan hai Banaras ki!</p>
    </div>

    <div class="card">
        <img src="https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=500">
        <h3>Taj Mahal - Agra</h3>
        <p>Mohabbat ki nishani, ek baar to sabko dekhna chahiye. India ki shaan!</p>
    </div>

</div>

<!-- Video Section -->
<div class="video-box">
    <h2>📹 Banaras Darshan - Live Ganga Aarti Video</h2>
    <p>Video pe click karke dekho Kashi ki aarti</p>
    <iframe width="90%" height="400" 
        src="https://www.youtube.com/embed/K4C0J5ZIr3U"
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
        style="border-radius:15px; max-width:700px;">
    </iframe>
    <br><br>
    <h3>2nd Video - Drone View of Varanasi Ghats</h3>
    <iframe width="90%" height="400" 
        src="https://www.youtube.com/embed/QzVzh0lB1bM"
        frameborder="0" allowfullscreen
        style="border-radius:15px; max-width:700px;">
    </iframe>
</div>

<div class="footer">
    <p>Made with ❤️ by Rishu | Varanasi | devopsrishu.duckdns.org | 2026</p>
</div>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
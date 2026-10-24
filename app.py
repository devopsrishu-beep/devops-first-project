from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Banaras Diaries | DevOps Project</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;scroll-behavior:smooth}
.navbar{position:fixed;top:0;width:100%;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:15px 40px;background:rgba(0,0,0,0.6);backdrop-filter:blur(10px);color:white}
.navbar b{font-size:20px;letter-spacing:2px}
.navbar a{color:white;text-decoration:none;margin-left:20px;font-size:14px}
.hero{height:100vh;width:100%;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.hero img.bg{position:absolute;width:100%;height:100%;object-fit:cover;animation:zoom 20s infinite alternate}
@keyframes zoom{0%{transform:scale(1)}100%{transform:scale(1.1)}}
.overlay{position:absolute;width:100%;height:100%;background:linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7))}
.hero-content{position:relative;z-index:2;text-align:center;color:white;padding:20px}
.hero-content h1{font-size:75px;font-weight:900;line-height:0.9;text-shadow:0 5px 25px black}
.hero-content h1 span{color:#ffb700}
.hero-content p{letter-spacing:8px;margin-top:15px;font-size:16px}
.glass{margin-top:25px;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);backdrop-filter:blur(12px);padding:12px 25px;border-radius:30px;display:inline-block}
.btn{display:inline-block;margin-top:30px;background:#ffb700;color:black;padding:14px 35px;border-radius:30px;text-decoration:none;font-weight:700;transition:0.3s}
.btn:hover{background:white;transform:translateY(-3px)}
.section{padding:80px 30px;max-width:1100px;margin:auto;text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:25px;margin-top:40px}
.card{background:white;border-radius:18px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.1);transition:0.3s;text-align:left}
.card:hover{transform:translateY(-10px)}
.card img{width:100%;height:200px;object-fit:cover}
.card-body{padding:20px}
.tech{background:#0f0f0f;color:white;padding:70px 30px;text-align:center}
.tech-box{display:flex;justify-content:center;gap:15px;flex-wrap:wrap;margin-top:30px}
.tech-item{background:#1f1f1f;border:1px solid #333;padding:12px 22px;border-radius:30px;font-size:14px}
.video-sec{background:#fff8e1}
.video-wrap{max-width:850px;margin:30px auto;background:black;border-radius:20px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,0.2)}
video{width:100%;display:block}
@media(max-width:600px){.hero-content h1{font-size:45px}.navbar{padding:12px 15px}}
</style>
</head>
<body>

<div class="navbar">
<b>BANARAS</b>
<div><a href="#explore">GHATS</a><a href="#video">VIDEO</a><a href="#tech">DEVOPS</a></div>
</div>

<div class="hero">
<img class="bg" src="https://images.unsplash.com/photo-1561361058-c24cecae35ca?q=80&w=2000" alt="banaras">
<div class="overlay"></div>
<div class="hero-content">
<h1>BANARAS<br><span>DIARIES</span></h1>
<p>THE SOUL OF KASHI</p>
<div class="glass">LIVE - HTTPS SECURED - DOCKERIZED</div><br>
<a class="btn" href="#explore">EXPLORE KASHI</a>
</div>
</div>

<div class="section" id="explore">
<h2 style="font-size:36px;">Subah-e-Banaras</h2>
<p style="color:gray;margin-top:10px;">80 Ghats, 1 Soul. Har ghat ek kahani kehta hai.</p>
<div class="grid">
<div class="card"><img src="https://images.unsplash.com/photo-1581793745862-98f9d76a96f2"><div class="card-body"><h3>Assi Ghat</h3><p style="font-size:13px;color:gray;margin-top:8px;">Morning chai, boat ride aur sukoon. Yaha din ki shuruat hoti hai.</p></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1524492412937-b28074a5d7da"><div class="card-body"><h3>Ganga Aarti</h3><p style="font-size:13px;color:gray;margin-top:8px;">Dashashwamedh Ghat ki sham. Diye, mantra aur lakhon dil.</p></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1561361058-0c6ea48a20cc"><div class="card-body"><h3>Banarasi Food</h3><p style="font-size:13px;color:gray;margin-top:8px;">Malaiyo, Kachori, Lassi. Taste jo zindagi bhar yaad rahe.</p></div></div>
</div>
</div>

<div class="section video-sec" id="video">
<h2 style="font-size:36px;">My Kashi Journey - Video</h2>
<p style="color:gray;">Apna video /static folder me daalo</p>
<div class="video-wrap">
<video controls poster="https://images.unsplash.com/photo-1561361058-c24cecae35ca">
<source src="/static/banaras-video.mp4" type="video/mp4">
</video>
</div>
<p style="font-size:12px;color:gray;margin-top:10px;">Tip: banaras-video.mp4 ko static folder me rakhna hai</p>
</div>

<div class="tech" id="tech">
<h2 style="font-size:34px;">Built With Modern DevOps</h2>
<p style="color:#aaa;margin-top:10px;">Ye sirf blog nahi, pura DevOps project hai</p>
<div class="tech-box">
<div class="tech-item">Python Flask</div><div class="tech-item">Docker</div><div class="tech-item">Nginx Reverse Proxy</div><div class="tech-item">Lets Encrypt SSL</div><div class="tech-item">AWS EC2</div><div class="tech-item">DuckDNS</div>
</div>
<br><br>
<a href="https://devopsrishu.duckdns.org" style="color:#ffb700;text-decoration:none;">https://devopsrishu.duckdns.org - LIVE</a>
</div>

<footer style="background:black;color:#777;padding:25px;text-align:center;font-size:13px;">
Designed & Deployed from Varanasi | Har Har Mahadev | 2026
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
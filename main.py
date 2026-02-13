import http.server
import socketserver
import os

PORT = 8000

# HTML Pages
pages = {
    "index.html": """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>محمد الشرقاوي السلامي - فنان تشكيلي</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<nav>
<ul>
<li><a href="index.html">الرئيسية</a></li>
<li><a href="about.html">حول الفنان</a></li>
<li><a href="gallery.html">معرض الأعمال</a></li>
<li><a href="contact.html">تواصل معنا</a></li>
</ul>
</nav>
</header>

<section class="hero">
<h1>محمد الشرقاوي السلامي</h1>
<p>فنان تشكيلي</p>
<p>يستكشف الجمال في لوحاته ويعبّر عن مواضيع قريبة من قلبه</p>
</section>

<footer>
<p>&copy; 2026 محمد الشرقاوي السلامي</p>
</footer>
</body>
</html>
""",
    "about.html": """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>حول الفنان - محمد الشرقاوي السلامي</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<nav>
<ul>
<li><a href="index.html">الرئيسية</a></li>
<li><a href="about.html">حول الفنان</a></li>
<li><a href="gallery.html">معرض الأعمال</a></li>
<li><a href="contact.html">تواصل معنا</a></li>
</ul>
</nav>
</header>

<section class="biography">
<h2>حول محمد الشرقاوي السلامي</h2>
<p>محمد الشرقاوي السلامي هو فنان تشكيلي يحب أن يعبر في لوحاته عن مواضيع قريبة من قلبه، خاصة مواضيع أمه وعائلته. فنان متمكن ومتمرس في هوايته، وأعماله تمنح العين جمالاً وهدوءاً من خلال تفاصيلها الدقيقة وألوانها الهادئة.</p>
<p>كل لوحة تحمل إحساسه الخاص وتبرز طريقته الفريدة في التعبير الفني، مزيج بين التقليدي والعصري بطريقة تجعل كل عمل فني ممتع للعين وذو قيمة فنية عالية.</p>

<div class="gallery">
<img src="images/artwork1.jpg.jpg" alt="Artwork 1">
<img src="images/artwork5.webp" alt="Artwork 5">
<img src="images/artwork6.webp" alt="Artwork 6">
</div>
</section>

<footer>
<p>&copy; 2026 محمد الشرقاوي السلامي</p>
</footer>
</body>
</html>
""",
    "gallery.html": """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>معرض الأعمال - محمد الشرقاوي السلامي</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<nav>
<ul>
<li><a href="index.html">الرئيسية</a></li>
<li><a href="about.html">حول الفنان</a></li>
<li><a href="gallery.html">معرض الأعمال</a></li>
<li><a href="contact.html">تواصل معنا</a></li>
</ul>
</nav>
</header>

<section class="gallery">
<h2>معرض الأعمال</h2>
<div class="grid">
<img src="images/artwork1.jpg.jpg" alt="Artwork 1">
<img src="images/artwork2.jpg.jpg" alt="Artwork 2">
<img src="images/artwork3.jpg.webp" alt="Artwork 3">
<img src="images/artwork4.webp" alt="Artwork 4">
<img src="images/artwork5.webp" alt="Artwork 5">
<img src="images/artwork6.webp" alt="Artwork 6">
</div>
</section>

<footer>
<p>&copy; 2026 محمد الشرقاوي السلامي</p>
</footer>
</body>
</html>
""",
    "contact.html": """
<!DOCTYPE html>
<html lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>تواصل معنا - محمد الشرقاوي السلامي</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<nav>
<ul>
<li><a href="index.html">الرئيسية</a></li>
<li><a href="about.html">حول الفنان</a></li>
<li><a href="gallery.html">معرض الأعمال</a></li>
<li><a href="contact.html">تواصل معنا</a></li>
</ul>
</nav>
</header>

<section class="contact">
<h2>تواصل معنا</h2>
<form>
<input type="text" placeholder="الاسم" required>
<input type="email" placeholder="البريد الإلكتروني" required>
<textarea placeholder="الرسالة" required></textarea>
<button type="submit">إرسال</button>
</form>
</section>

<footer>
<p>&copy; 2026 محمد الشرقاوي السلامي</p>
</footer>
</body>
</html>
"""
}

# CSS
style_css = """
* { margin:0; padding:0; box-sizing:border-box; font-family:'Cairo', sans-serif; }
body { background:#f5f5f5; color:#111; line-height:1.6; scroll-behavior:smooth; }
header { background:#111; padding:1rem 2rem; position:sticky; top:0; z-index:100; box-shadow:0 2px 5px rgba(0,0,0,0.2);}
nav ul { display:flex; justify-content:center; list-style:none; gap:2rem;}
nav a { text-decoration:none; color:#f5f5f5; font-weight:600; transition:0.3s;}
nav a:hover { color:#888; transform:scale(1.1);}
.hero { background:#222; color:#f5f5f5; text-align:center; padding:6rem 2rem;}
.hero h1 { font-size:3rem; margin-bottom:1rem;}
.hero p { font-size:1.2rem; max-width:600px; margin:0 auto;}
section { max-width:1000px; margin:3rem auto; padding:2rem; background:#fff; border-radius:15px; box-shadow:0 8px 20px rgba(0,0,0,0.05); transition:0.3s;}
section:hover { transform:translateY(-5px); box-shadow:0 12px 25px rgba(0,0,0,0.1);}
h2 { color:#111; margin-bottom:1rem; text-align:center;}
.gallery { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1.5rem;}
.gallery img { width:100%; border-radius:10px; transition:0.3s;}
.gallery img:hover { transform:scale(1.05); box-shadow:0 8px 20px rgba(0,0,0,0.2);}
form { display:flex; flex-direction:column; gap:1rem;}
input,textarea { padding:0.8rem; border-radius:10px; border:1px solid #ccc; font-size:1rem; width:100%;}
button { padding:0.8rem; border-radius:10px; border:none; background:#111; color:#f5f5f5; font-weight:bold; cursor:pointer; transition:0.3s;}
button:hover { background:#444; transform:scale(1.05);}
footer { text-align:center; padding:2rem; background:#111; color:#f5f5f5; margin-top:3rem;}
@media(max-width:768px){ nav ul { flex-direction:column; gap:1rem;} .hero h1 { font-size:2rem;}}
"""

# إنشاء الملفات
for filename, content in pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

# تشغيل السيرفر
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()

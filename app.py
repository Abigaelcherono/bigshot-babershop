from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>BigShot Barbershop</title>
    <style>
        body {margin:0;font-family:Arial;background:black;color:white;}
        header {background:#000;padding:20px;text-align:center;border-bottom:2px solid gold;}
        nav a {color:gold;margin:15px;text-decoration:none;font-weight:bold;}
        section {padding:40px;text-align:center;}
        h2 {color:gold;}
        form {max-width:400px;margin:auto;}
        input, textarea, button {
            width:100%;padding:10px;margin:8px 0;border:none;border-radius:5px;
        }
        button {background:gold;color:black;font-weight:bold;cursor:pointer;}
        img {width:250px;border-radius:10px;margin:10px;}
        footer {text-align:center;padding:20px;border-top:1px solid gold;}
    </style>
</head>
<body>

<header>
    <h1>BigShot Barbershop</h1>
    <p>Moi Avenue Street, Nakuru</p>
    <nav>
        <a href="#services">Services</a>
        <a href="#booking">Book</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section>
    <h2>Welcome to BigShot</h2>
    <p>Premium grooming for modern gentlemen.</p>
    <img src="https://images.unsplash.com/photo-1621605815971-fbc98d665033">
    <img src="https://images.unsplash.com/photo-1599351431202-1e0f0137899a">
</section>

<section id="services">
    <h2>Our Services</h2>
    <p>Haircut • Beard Trim • Shaving • Hair Styling • Kids Cuts</p>
</section>

<section id="booking">
    <h2>Book Appointment</h2>
    <form method="POST" action="/book">
        <input name="name" placeholder="Your Name" required>
        <input name="date" type="date" required>
        <input name="time" type="time" required>
        <button type="submit">Book Now</button>
    </form>
</section>

<section id="contact">
    <h2>Contact Us</h2>
    <form method="POST" action="/contact">
        <input name="name" placeholder="Your Name" required>
        <textarea name="message" placeholder="Message"></textarea>
        <button type="submit">Send</button>
    </form>
</section>

<footer>
    <p>© BigShot Barbershop - Nakuru Moi Avenue</p>
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    print(f"Booking: {name} {date} {time}")
    return redirect(url_for('home'))

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    message = request.form['message']
    print(f"Message from {name}: {message}")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
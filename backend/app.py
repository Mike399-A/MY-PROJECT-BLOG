from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
import markdown

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev')

# Flask-Mail configuration (to be filled in requirements.txt and .env)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    # List markdown files in blog_posts
    posts = []
    for filename in os.listdir('blog_posts'):
        if filename.endswith('.md'):
            with open(os.path.join('blog_posts', filename), 'r') as f:
                content = f.read()
                html = markdown.markdown(content)
                posts.append({'title': filename[:-3].replace('_', ' ').title(), 'content': html})
    return render_template('blog.html', posts=posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        try:
            msg = Message(f'Contact Form: {name}', recipients=[app.config['MAIL_USERNAME']])
            msg.body = f'From: {name} <{email}>\n\n{message}'
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash('Failed to send message. Please try again later.', 'danger')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 
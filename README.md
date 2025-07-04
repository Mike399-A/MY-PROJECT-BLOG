# Personal Portfolio + Blog with Contact Form

## Overview
This project is a modern, professional web application that serves as both a personal portfolio and a blog. It is designed to showcase your software development skills, highlight your projects, share your thoughts via blog posts, and allow visitors to contact you directly through a functional contact form. The project uses a full-stack approach, combining a Python Flask backend with a responsive HTML, Tailwind CSS, and JavaScript frontend.

---

## Key Features

1. **Landing Page**
   - A visually appealing, mobile-responsive homepage.
   - Introduces you (the developer) and provides navigation to other sections.
   - Includes a call-to-action button to view your work.

2. **Portfolio Section**
   - Displays your projects in a clean, grid-based layout.
   - Each project card includes an image, title, description, and a link (e.g., to GitHub or a live demo).
   - Easily customizable to add or remove projects.

3. **Blog Section**
   - Dynamically lists blog posts written in Markdown format.
   - Each post is rendered as HTML for beautiful formatting, styled with Tailwind and a custom `.prose` class.
   - Allows you to easily add new posts by simply creating new Markdown files in the `blog_posts` directory.

4. **Contact Form**
   - A user-friendly form where visitors can enter their name, email, and message.
   - On submission, the form sends an actual email to your specified address using Flask-Mail.
   - Displays success or error messages to the user.

5. **Dark/Light Mode Toggle**
   - Users can switch between dark and light themes.
   - The preference is saved in the browser’s localStorage for a consistent experience.
   - Fully integrated with Tailwind's dark mode classes.

6. **Modern UI/UX**
   - Uses Tailwind CSS for layout, spacing, and design.
   - Subtle animations and transitions for a polished, professional feel.
   - Fully responsive: looks great on desktops, tablets, and phones.

---

## Technical Stack

- **Frontend:**  
  - HTML5, Tailwind CSS (via CDN), custom CSS for Markdown prose, Vanilla JavaScript (for interactivity and theme toggle)
- **Backend:**  
  - Python (Flask web framework)
  - Flask-Mail for sending emails
  - Markdown library for rendering blog posts
- **Templating:**  
  - Jinja2 (Flask's default templating engine)
- **Content:**  
  - Blog posts are written in Markdown files for easy editing and formatting.

---

## Project Structure

```
backend/
  app.py                # Main Flask application
  requirements.txt      # Python dependencies
  templates/            # Jinja2 HTML templates
    layout.html         # Base template with Tailwind and navigation
    index.html          # Home page
    portfolio.html      # Portfolio/projects
    blog.html           # Blog listing
    contact.html        # Contact form
  static/               # Static assets (JS, custom CSS, images)
    css/custom.css      # Custom styles for Markdown prose
    js/theme.js         # Dark/light mode toggle
    img/                # Project images
  blog_posts/           # Markdown files for blog posts
    hello_world.md
README.md               # Project documentation and setup instructions
```

---

## How It Works

- **Homepage** (`/`): Shows your intro and navigation.
- **Portfolio** (`/portfolio`): Lists your projects.
- **Blog** (`/blog`): Reads all Markdown files in `blog_posts/`, converts them to HTML, and displays them with modern styling.
- **Contact** (`/contact`): Handles GET (show form) and POST (send email) requests. Uses Flask-Mail to send emails to your configured address.
- **Theming:** JavaScript toggles a CSS class for dark/light mode and saves the preference, working with Tailwind's dark mode.

---

## Setup & Customization

- **Configuration:**  
  - Set your email and secret key in environment variables (or `.env` file):
    - `MAIL_USERNAME` (your email )
    - `MAIL_PASSWORD` (your email password or app password)
    - `MAIL_DEFAULT_SENDER` (your email )
    - `SECRET_KEY` (any random string)
  - Install dependencies with `pip install -r requirements.txt`.
  - Run the app with `python app.py`.

- **Frontend Customization:**  
  - Edit `layout.html` for navigation, branding, and global layout.
  - Add or update your projects in `portfolio.html`.
  - Add blog posts as Markdown files in `blog_posts/`.
  - Update your name and intro in `index.html`.
  - Add or tweak custom styles in `static/css/custom.css` (for Markdown, etc.).
  - Project images go in `static/img/`.

---

## Who Is This For?

- Developers who want a professional online presence.
- Anyone looking to showcase their work, share knowledge, and be easily contactable.
- Those who want a project that demonstrates full-stack skills (frontend, backend, email integration, Markdown processing, responsive design).

---

**In summary:**  
This project is a complete, production-quality personal website that demonstrates your abilities in HTML, Tailwind CSS, JavaScript, and Python. It's easy to maintain, extend, and customize, and it provides a great foundation for your online portfolio and blog.

const toggle = document.getElementById('theme-toggle');
const body = document.body;

function setTheme(dark) {
    if (dark) {
        body.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        toggle.textContent = '☀️';
    } else {
        body.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        toggle.textContent = '🌙';
    }
}

toggle.addEventListener('click', () => {
    setTheme(!body.classList.contains('dark'));
});

// On load
const saved = localStorage.getItem('theme');
if (saved === 'dark') setTheme(true);
else setTheme(false); 
// const PROPERTIES_FILE;
const burgerBtn = document.getElementById('burgerBtn');
const mobileMenu = document.getElementById('mobileMenu');
const version = document.getElementById('version')

fetch('/api/properties/version').then(response => response.json()).then(currentVersion => version.textContent = currentVersion);

burgerBtn.addEventListener('click', () => {
    burgerBtn.classList.toggle('active');
    mobileMenu.classList.toggle('active');
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.mobile-nav')) {
    burgerBtn.classList.remove('active');
    mobileMenu.classList.remove('active');
    }
});

document.querySelectorAll('.mobile-menu-item, .nav-btn').forEach(item => {
    item.addEventListener('click', (e) => {
    const text = e.currentTarget.textContent || e.currentTarget.title;
    console.log(`Clicked: ${text}`);

    });
});
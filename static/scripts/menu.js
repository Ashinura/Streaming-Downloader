const burgerBtn = document.getElementById("burgerBtn");
const mobileMenu = document.getElementById("mobileMenu");
const version = document.getElementById("version");

fetch("/api/properties/version")
	.then((response) => response.json())
	.then((currentVersion) => (version.textContent = currentVersion));

burgerBtn.addEventListener("click", () => {
	burgerBtn.classList.toggle("active");
	mobileMenu.classList.toggle("active");
});

document.addEventListener("click", (e) => {
	if (!e.target.closest(".mobile-nav")) {
		burgerBtn.classList.remove("active");
		mobileMenu.classList.remove("active");
	}
});

document.querySelectorAll(".mobile-menu-item, .nav-btn").forEach((item) => {
	item.addEventListener("click", (e) => {
		const text = e.currentTarget.textContent || e.currentTarget.title;
		console.log(`Clicked: ${text}`);
	});
});

function startUpdate(newVersion) {
    if (!confirm(`Installer la version ${newVersion} et redémarrer l'application ?`)) return;

    const icon = document.querySelector(".icon-update");
    if (icon) icon.style.animation = "spin 1s linear infinite";

    fetch("/api/update-project", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    })
    .then(async (response) => {
        if (!response.ok) {
            const data = await response.json().catch(() => ({}));
            alert("Erreur : " + (data.message || "Échec de la mise à jour"));
            if (icon) icon.style.animation = "";
            return;
        }
        alert("Mise à jour lancée. L'application va redémarrer dans quelques secondes.");
        setTimeout(waitForServer, 5000);
    })
    .catch((err) => {
        console.log("Le serveur redémarre...");
        setTimeout(waitForServer, 5000);
    });
}

function waitForServer() {
    fetch("http://127.0.0.1:5000/")
        .then(() => window.location.reload())
        .catch(() => setTimeout(waitForServer, 2000));
}
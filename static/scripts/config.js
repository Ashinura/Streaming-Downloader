window.addEventListener("DOMContentLoaded", async () => {
	// Éléments du DOM
	const language = document.getElementById("language");
	const autoupdateChkbx = document.getElementById("autoupdate-chkbx");
	const autoupdateInfo = document.getElementById("autoupdate-info");
	const flaskInfo = document.getElementById("flask-info");
	const flaskLvl = document.getElementById("flask-access-type");
	const flaskPort = document.getElementById("flask-port");
	const flaskDebugChkbx = document.getElementById("debug-chkbx");
	const resetBtn = document.getElementById("reset-btn");

	let config = {};

	try {
		const response = await fetch("/api/config");
		config = await response.json();
	} catch (err) {
		console.error("Erreur de chargement de la config :", err);
		return;
	}

	// Gère l'apparence et l'état du bouton Autoupdate selon le mode Debug
	function updateAutoupdateState() {
		if (flaskDebugChkbx.checked) {
			autoupdateChkbx.disabled = true;
			autoupdateChkbx.parentElement.style.opacity = "0.5";
			autoupdateChkbx.parentElement.style.cursor = "not-allowed";
		} else {
			autoupdateChkbx.disabled = false;
			autoupdateChkbx.parentElement.style.opacity = "1";
			autoupdateChkbx.parentElement.style.cursor = "pointer";
		}
	}

	async function loadConfig() {
		language.value = config.user.language === "fr" ? "french" : "english";

		autoupdateChkbx.checked = !!config.user.autoupdate;

		flaskLvl.value = config.flask.ip === "127.0.0.1" ? "local" : "network";

		flaskPort.value = config.flask.port;
		flaskDebugChkbx.checked = !!config.flask.debug;

		const paths = ["default", "video", "music", "social"];
		paths.forEach((p) => {
			const el = document.getElementById(`path-${p}`);
			if (el) el.value = config.path[p];
		});

		updateAutoupdateState();
	}

	async function toggleConfig(path, newValue) {
		const [section, key] = path.split(".");
		const payload = { [section]: { [key]: newValue } };

		try {
			const response = await fetch("/api/config", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(payload),
			});

			if (response.ok) {
				console.log(`MAJ réussie : ${path} = ${newValue}`);
				if (path === "user.language") location.reload();
			} else {
				const errorData = await response.json();
				alert("Erreur : " + errorData.message);
			}
		} catch (err) {
			console.error("Erreur réseau :", err);
		}
	}

	language.addEventListener("change", (e) => {
		toggleConfig(
			"user.language",
			e.target.value === "french" ? "fr" : "en",
		);
	});

	autoupdateChkbx.addEventListener("change", () => {
		toggleConfig("user.autoupdate", autoupdateChkbx.checked);
	});

	flaskDebugChkbx.addEventListener("change", () => {
		updateAutoupdateState();
		toggleConfig("flask.debug", flaskDebugChkbx.checked);
	});

	flaskLvl.addEventListener("change", (e) => {
		toggleConfig(
			"flask.ip",
			e.target.value === "local" ? "127.0.0.1" : "0.0.0.0",
		);
	});

	flaskPort.addEventListener("blur", () => {
		const port = parseInt(flaskPort.value);
		if (!isNaN(port) && port >= 1 && port <= 65535) {
			toggleConfig("flask.port", port);
		} else {
			alert("Le port est invalide (doit être entre 1 et 65535)");
			flaskPort.value = config.flask.port;
		}
	});

	if (autoupdateInfo) {
		autoupdateInfo.addEventListener("click", () => {
			alert(
				"Mise à jour automatique :\n\n" +
					"Cette option permet de vérifier et d'installer les nouvelles versions au démarrage.\n\n" +
					"Note : Cette fonctionnalité est désactivée lorsque le mode 'debug' est actif pour éviter tout conflit pendant le développement.",
			);
		});
	}

	
	if (flaskInfo) {
		flaskInfo.addEventListener("click", () => {
			alert(
				"Le Serveur Flask :\n\n" +
					"Permet un rendu graphique sous forme de page web et de communiquer avec l'application Python de base.\n\n" +
					"• Accès Local : L'application n'est accessible que sur cet ordinateur.\n" +
					"• Accès Réseau : Permet d'utiliser l'interface depuis un autre appareil connecté au même Wi-Fi.",
			);
		});
	}


	resetBtn.addEventListener("click", async () => {
		if (!confirm("Voulez-vous vraiment réinitialiser la configuration ?"))
			return;

		try {
			const responseDefault = await fetch("/api/config/default");
			const defaultConf = await responseDefault.json();

			await fetch("/api/config", {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(defaultConf),
			});

			location.reload();
		} catch (err) {
			console.error("Erreur lors du reset :", err);
		}
	});

	loadConfig();
})
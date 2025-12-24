window.addEventListener("DOMContentLoaded", async () => {

    const language = document.getElementById('language')
    const autoupdateChkbx = document.getElementById('autoupdate-chkbx')
    const flaskLvl = document.getElementById('flask-access-type')
    const flaskPort = document.getElementById('flask-port')
    const flaskDebugChkbx = document.getElementById('debug-chkbx')

    const resetBtn = document.getElementById('reset-btn')

    // Récupérer la config depuis le serveur
    let config = {}
    try {
        const response = await fetch("/api/config")
        config = await response.json()
    } catch (err) {
        console.error("Erreur de chargement de la config :", err)
        return
    }

    // Remplir les champs avec la config
    async function loadConfig() {

        // Langue
        switch (config.user.language) {
            case ("fr"):
                language.value = "french"
                break
            case ("en"):
                language.value = "english"
                break
            default: language.value = "english"
        }

        autoupdateChkbx.checked = !!config.user.autoupdate

        // Flask Level Access (IP)
        switch (config.flask.ip) {
            case ("127.0.0.1"):
                flaskLvl.value = "local"
                break
            case ("0.0.0.0"):
                flaskLvl.value = "network"
                break
            default: console.log('A faire')
        }

        flaskPort.value = config.flask.port
        flaskDebugChkbx.checked = !!config.flask.debug

        document.getElementById('path-default').value = config.path.default;
        document.getElementById('path-video').value = config.path.video;
        document.getElementById('path-music').value = config.path.music;
        document.getElementById('path-social').value = config.path.social;
    }

    async function toggleConfig(path, newValue) {

        // Shallow Copy
        const updatedConfig = { ...config };

        const pathParts = path.split('.');
        let current = updatedConfig;
        for (let i = 0; i < pathParts.length - 1; i++) {
            current = current[pathParts[i]];
        }
        current[pathParts[pathParts.length - 1]] = newValue;

        try {
            await fetch('/api/config', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedConfig)
            });
            config = updatedConfig;
        } catch (err) {
            console.error("Erreur lors de l'envoi de la config :", err);
        }
    }


    language.addEventListener("change", (event) => {
        toggleConfig("user.language", event.target.value === "french" ? "fr" : "en")
    });

    autoupdateChkbx.addEventListener('change', () => {
        toggleConfig("user.autoupdate", autoupdateChkbx.checked)
    })

    flaskLvl.addEventListener("change", (event) => {
        toggleConfig("flask.ip", event.target.value === "local" ? "127.0.0.1" : "0.0.0.0")
    })

    flaskPort.addEventListener("blur", () => {
        const port = parseInt(flaskPort.value);
        if (!isNaN(port) && port >= 1 && port <= 65535) {
            toggleConfig("flask.port", port);
        } else {
            console.warn("Invalid");
            alert("Le port est invalide ou n'est pas entre 1 et 65535");
        }
    });

    flaskDebugChkbx.addEventListener('change', () => {
        toggleConfig("flask.debug", flaskDebugChkbx.checked)
    })

    loadConfig()


    // Action
    async function resetConfig() {
        const defaultConf = {
            "user": {
                "autoupdate": true,
                "language": "fr"
            },
            "flask": {
                "debug": false,
                "ip": "0.0.0.0",
                "port": 5000
            },
            "path": {
                "default": "./downloads",
                "music": "./downloads",
                "social": "./downloads",
                "video": "./downloads"
            }
        }

        try {
            await fetch('/api/config', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(defaultConf)
            });
            config = defaultConf;
        } catch (err) {
            console.error("Erreur lors de l'envoi de la config :", err);
        }
    }

    resetBtn.addEventListener('click', () => {
        resetConfig().then(() => loadConfig())
    })
})
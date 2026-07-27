async function loadSystem(){

    const data = await apiGet("/api/dashboard");

    document.getElementById("device").textContent =
        data.system.device;

    document.getElementById("hardware").textContent =
        data.system.hardware;

    document.getElementById("version").textContent =
        data.system.version;

    document.getElementById("mode").textContent =
        data.system.mode;

}


document.addEventListener(
"DOMContentLoaded",
loadSystem
);

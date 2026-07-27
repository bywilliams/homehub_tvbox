// Carregamento de informações do sistema
async function loadDashboard() {

    try {

        const data =
        	await apiGet(
        		"/api/dashboard"	
        	);


        console.log(data);



        // Sistema

        document.getElementById("device").textContent =
            data.system.device;


        document.getElementById("hardware").textContent =
            data.system.hardware;


        document.getElementById("version").textContent =
            data.system.version;


        document.getElementById("mode").textContent =
            data.system.mode;



        // Serviços

        document.getElementById("mqtt").innerHTML =
            createStatusBadge(
                data.services.mqtt.status
            );
        
        document.getElementById("storage").innerHTML =
            createStatusBadge(
                data.services.storage.status
            );
        
        document.getElementById("files").innerHTML =
            createStatusBadge(
                data.services.files.status
            );
        
        document.getElementById("doctor").innerHTML =
            createStatusBadge(
                data.services.doctor.status
            );



        // Storage

        document.getElementById("storage_type").textContent =
            data.services.storage.type;


        document.getElementById("storage_capacity").textContent =
            data.services.storage.capacity;


        document.getElementById("storage_path").textContent =
            data.services.storage.path;


    }


    catch(error){

        console.error(
            "Erro carregando HomeHub:",
            error
        );

    }

}



document.addEventListener(
    "DOMContentLoaded",
    async () => {

        await loadDashboard();

        await loadFiles();

        updateLastRefresh();

        startAutoRefresh();

    }
);

function startAutoRefresh() {

    setInterval(async () => {

        await loadDashboard();

        await loadFiles();

         updateLastRefresh();

    }, 10000);

}

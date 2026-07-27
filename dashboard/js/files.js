// Carregamento de arquivos do SD Card 
async function loadFiles() {

    try {

        const data = 
        	await apiGet(
        		"/api/files/list"	
        	);

        const list =
            document.getElementById("file_list");

        list.innerHTML = "";

        if (data.count === 0) {

            list.innerHTML =
                "<li class='list-group-item'>Nenhum arquivo.</li>";

            return;
        }

        data.files.forEach(file => {

             list.appendChild(
        		createElement(
            		createFileCard(file)
        		)
    		);

        });

    }

    catch(error){

        console.error(error);

    }

}



// Upload de arquivo
// Upload de arquivo
async function uploadFile() {

    const input =
        document.getElementById("file_upload");

    if (input.files.length === 0) {

        showAlert(
            "Selecione um arquivo.",
            "warning"
        );

        return;

    }

    const formData =
        new FormData();

    formData.append(
        "file",
        input.files[0]
    );

    try {

        const result =
            await apiPost(
                "/api/files/upload",
                formData
            );

        if (result.status === "ONLINE") {

            input.value = "";

            showAlert(
                "Upload realizado com sucesso.",
                "success"
            );

            await loadFiles();

        }

        else {

            showAlert(
                result.message,
                "danger"
            );

        }

    }

    catch(error){

        console.error(error);

        showAlert(
            "Erro no upload.",
            "danger"
        );

    }

}

document
    .getElementById(
        "upload_button"
    )
    .addEventListener(
        "click",
        uploadFile
    );



// Deletar arquivo
async function deleteFile(filename) {

    if (!confirm("Deseja excluir este arquivo?")) {
        return;
    }

    try {

        const result = 
        	await apiDelete(
        		`/api/files/${filename}`	
        	);

        if (result.status === "DELETED") {

        	showAlert(
        	    "Arquivo removido com sucesso.",
        	    "success"
        	);

            await loadFiles();

        } else {

            alert(result.message);

        }

    } catch (error) {

        console.error(error);

        showAlert(
            "Erro ao remover arquivo.",
            "danger"
        );

    }

}

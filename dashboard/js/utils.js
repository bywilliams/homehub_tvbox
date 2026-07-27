// Formatação de tamanho do arquivo
function formatFileSize(bytes) {

    if (bytes < 1024) {
        return bytes + " bytes";
    }

    if (bytes < 1024 * 1024) {
        return (bytes / 1024).toFixed(1) + " KB";
    }

    if (bytes < 1024 * 1024 * 1024) {
        return (bytes / 1024 / 1024).toFixed(1) + " MB";
    }

    return (bytes / 1024 / 1024 / 1024).toFixed(1) + " GB";
}

// Formatação da data BR
function formatDate(dateString) {

    return new Date(dateString)
        .toLocaleString("pt-BR");
}


// Refresh da tela
function updateLastRefresh() {

    document.getElementById(
        "last_update"
    ).textContent =
        new Date().toLocaleTimeString();

}

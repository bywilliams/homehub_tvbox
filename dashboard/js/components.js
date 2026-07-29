/// Badge de Status
function createStatusBadge(status) {

    const colors = {
        ONLINE: "success",
        OFFLINE: "danger",
        NOT_MOUNTED: "warning",
        ERROR: "danger",
        UNKNOWN: "secondary"
    };

    const color = colors[status] || "secondary";

    return `
        <span class="badge bg-${color}">
            ${status}
        </span>
    `;
}


// Criar cards
function createFileCard(file) {

	const downloadPath = file.path
	    .split("/")
	    .map(encodeURIComponent)
	    .join("/");

    return `
        <div class="card mb-2 shadow-sm">

            <div class="card-body d-flex justify-content-between align-items-center">

                <div>

                    <h6 class="mb-1">
                        📄 ${file.name}
                    </h6>

                    <small class="text-muted">
                        ${formatFileSize(file.size)}
                    </small>

                    <br>

                    <small class="text-muted">
                        ${formatDate(file.modified)}
                    </small>

                </div>

                <div class="d-flex gap-2">

                    <a
                        href="${API_BASE}/api/files/download/${downloadPath}"
                        class="btn btn-primary btn-sm"
                    >
                        ⬇
                    </a>

                    <button
                        class="btn btn-danger btn-sm"
                        onclick="deleteFile('${encodeURIComponent(file.path)}')"
                    >
                        🗑
                    </button>

                </div>

            </div>

        </div>
    `;
}


// converte HTML em elemento DOM
function createElement(html) {

    const div = document.createElement("div");

    div.innerHTML = html.trim();

    return div.firstElementChild;

}



// Mostra alertas personalizados
function showAlert(message, type = "success") {

    const alerts = document.getElementById("alerts");

    const alert = document.createElement("div");

    alert.className =
        `alert alert-${type} alert-dismissible fade show`;

    alert.innerHTML = `
        ${message}

        <button
            type="button"
            class="btn-close"
            data-bs-dismiss="alert">
        </button>
    `;

    alerts.appendChild(alert);

    setTimeout(() => {

        alert.remove();

    }, 4000);

}

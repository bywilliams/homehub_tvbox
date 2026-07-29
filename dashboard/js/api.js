const API_BASE = `http://${window.location.hostname}:8000`;

async function apiGet(url) {

    const response = await fetch(
		API_BASE + url
    );

    return await response.json();

}


async function apiPost(url, body) {

    const response = await fetch(
    	API_BASE + url,
        {
            method: "POST",
            body: body
        }
    );

    return await response.json();

}


async function apiDelete(url) {

    const response = await fetch(
        API_BASE + url,
        {
            method: "DELETE"
        }
    );

    return await response.json();

}

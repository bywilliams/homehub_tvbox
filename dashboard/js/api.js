async function apiGet(url) {

    const response = await fetch(url);

    return await response.json();

}


async function apiPost(url, body) {

    const response = await fetch(
        url,
        {
            method: "POST",
            body: body
        }
    );

    return await response.json();

}


async function apiDelete(url) {

    const response = await fetch(
        url,
        {
            method: "DELETE"
        }
    );

    return await response.json();

}

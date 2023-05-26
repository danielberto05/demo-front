function createClient(url, client_name, client_email=null) {
    client_response = fetch(`${url}/api/v1/clients`, {
        method: "POST",
        body: JSON.stringify({
            name: client_name,
            email: client_email,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });

    clearFields();
}

function clearCFields() {
    document.getElementById('client_name').value = "";
    document.getElementById('client_email').value = "";
    document.getElementById('product_name').value = "";
    document.getElementById('product_name').value = "";
}

function createProduct(url, product_name, product_price) {
    client_response = fetch(`${url}/api/v1/products`, {
        method: "POST",
        body: JSON.stringify({
            name: product_name,
            price: parseFloat(product_price),
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
}

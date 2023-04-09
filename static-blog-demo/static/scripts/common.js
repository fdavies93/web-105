function fetch_json(url, data, method) {
    var data_obj = {
        headers: {
            'Content-Type': 'application/json',
        }
    }
    if (method == "POST") {
        data_obj.method = "POST"
        data_obj.body = JSON.stringify(data)
    }
    return fetch(url, data_obj)
}
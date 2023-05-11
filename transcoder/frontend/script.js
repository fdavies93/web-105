let uploadBox, uploadForm, uploadText;

const setUploadText = function (value, classes) {
    uploadText.innerText = value
    uploadText.className = ""
    for (cls of classes) {
        uploadText.classList.add(cls)
    }
}

const onSubmit = (ev) => {
    ev.preventDefault()
    // send upload to API
    let data = new FormData()
    data.append("file", uploadBox.files[0])
    fetch("http://localhost:5000", {method: "POST", body: data})
    .then( (res) => {
        setUploadText("Upload successful!", ["success"])
    })
    .catch( (err) => {
        setUploadText("Upload failed. :(", ["failure"])
    })
}

window.onload = function () {
    uploadBox = document.getElementById("upload-box")
    uploadForm = document.getElementById("upload-form")
    uploadText = document.getElementById("upload-text")
    uploadForm.addEventListener("submit", onSubmit)
}
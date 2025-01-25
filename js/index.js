const form = document.getElementById("fileUploadForm");
const file = document.getElementById("fileUpload");

form.addEventListener("submit", e => {
    e.preventDefault();
    const formData = new FormData();

    if (file.files.length === 0) {
        alert("loser");
    }

    console.log(file.files);
    formData.append("file", file.files[0]);

    //Add the name to the site.
    const fileNames = document.getElementById("fileNames");
    fileNames.innerHTML = `${file.files[0].name}`;
});


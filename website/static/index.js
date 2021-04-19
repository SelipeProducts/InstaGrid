function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}


document.getElementById("create_blog").onclick = function () {
        location.href = "/create";
        alert();
};


function create_blog() {
  location.href = "create";
  alert();
}
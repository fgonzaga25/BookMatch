function input() {
    var nomeLivro = (document.querySelector(".bookInput").value).trim().replace(" ", "_");
    //console.log(nomeLivro)
    //window.location.replace("http://127.0.0.1:5000/recommend/" + nomeLivro);
    window.location.href = "http://127.0.0.1:5000/recommend/" + nomeLivro
}

function handleKeyPress(event) {
  if (event.keyCode === 13) {
    input()
  }
}
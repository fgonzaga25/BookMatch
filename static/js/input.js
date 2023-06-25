function input() {
    var nomeLivro = (document.querySelector(".bookInput").value).trim().replace(" ", "_");
    //console.log(nomeLivro)
    //window.location.replace(window.location.href + "/" + nomeLivro);
    window.location.href = "http://127.0.0.1:5000/recommend/" + nomeLivro
}

document.querySelector(".bookInput").addEventListener("keyup", (event) => {
  if (event.key === "Enter") {
    input()
  }
});
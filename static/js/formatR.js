/*
* Formatação dos Livros Recomendados
*/

function formatR(book) {
    return `
    <div class="books">
    <img src="${book[3]}" alt="book-logo" class="booksImg">
        <div id="infoDiv">
            <p>Tittle: ${book[0]}</p>
            <p>Date:${book[2]}</p>
            <p>Author: ${book[1]}</p>
        </div>
    </div>
    `
}
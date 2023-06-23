/*
* Formatação dos Livros da Página Inicial
*/

function format(book) {
    return `
    <div class="books">
    <img src="${book['Image-URL-L']}" alt="book1-logo" class="booksImg">
        <div id="infoDiv">
            <p>Tittle: ${book['Book-Title']}</p>
            <p>Date:${book['Year-Of-Publication']}</p>
            <p>Author: ${book['Book-Author']}</p>
            <p>Num Views: ${book['Num_views']}</p>
            <p>Num Rating: ${book['Num_ratings']}</p>
            <p>Average rating: ${book['Avg_ratings']}</p>
        </div>
    </div>
    `
}
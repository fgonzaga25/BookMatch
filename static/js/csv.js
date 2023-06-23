/* 
* Leitura dos arquivos em csv
*/

function getPath(i) {
    switch (i) {
        case 1:
            return 'static/csv/mais_avaliados.csv'
        case 2:
            return 'static/csv/menos_avaliados.csv'
        case 3:
            return 'static/csv/mais_visualizados.csv'
        case 4:
            return 'static/csv/menos_visualizados.csv'
        case 5:
            return 'static/csv/melhores_medias.csv'
        case 6:
            return 'static/csv/piores_medias.csv'    

        default:
            break;
    }
}

function parseCSV() {
    let i = parseInt(document.getElementById('filter').value)
    let path = getPath(i)
    document.querySelector('.containerBooks').innerHTML = ""
    Papa.parse(path, {
            header: true,
            delimiter: ',',
            download: true,
            step: function (row) {
                if (row.data['Avg_ratings'] != undefined){
                    document.querySelector('.containerBooks').innerHTML += format(row.data)
                }
            }
        }
    )
}

parseCSV(5)
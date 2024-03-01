$(document).ready(function() {
    $("#list-datatable").DataTable({
        responsive: true,
        autowidth: false,
        "language": {
            url : spanishData
        },
        "order": [[ 0, "desc" ]] // Ordena por la primera columna (ID) de mayor a menor
    });
});

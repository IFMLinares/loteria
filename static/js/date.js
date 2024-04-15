var FechaHora = (function() {
    // Variables privadas
    var date = new Date();
    date.setDate(date.getDate() - 1);
    var day = date.getDate();
    var month = date.getMonth() + 1;
    var year = date.getFullYear();

    day = (day < 10) ? '0' + day : day;
    month = (month < 10) ? '0' + month : month;

    var yesterday = day + '/' + month + '/' + year;

    // Métodos privados
    function actualizarFechaHora() {
        let ahora = new Date();

        // Formatea la fecha como DD/MM/YY
        let fecha = ahora.toLocaleDateString('es-VE', { day: '2-digit', month: '2-digit', year: 'numeric' });

        // Formatea la hora como HH:MM:SS
        let hora = ahora.toLocaleTimeString('es-VE', { hour: '2-digit', minute: '2-digit', second: '2-digit' });

        // Actualiza los elementos HTML
        $('h1[fecha]').text('RESULTADO DE LOS ANIMALITOS ' + fecha);
        $('h1[hora]').text(hora);
    }

    // Métodos públicos
    return {
        iniciar: function() {
            $('.yesterday').text('RESULTADO DE LOS ANIMALITOS ' + yesterday);
            setInterval(actualizarFechaHora, 1000);
        }
    };
})();

// Uso del objeto
FechaHora.iniciar();

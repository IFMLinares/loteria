var ReloadManager = (function() {
    // Método privado
    function reloadPage() {
        $.ajax({
            type: "POST",
            url: window.location.href,  // Asegúrate de que esta URL apunta a tu vista IndexView
            data: {
                'reload': 'reload'
            },
            success: function(data) {
                console.log("Solicitud POST enviada correctamente");
            }
        });
    }

    // Métodos públicos
    return {
        iniciar: function() {
            $('#reload-button').click(reloadPage);
        },
    };
})();

// Uso del objeto
ReloadManager.iniciar();

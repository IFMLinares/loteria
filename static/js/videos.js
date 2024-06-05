var VideoManager = (function() {
    // Método privado
    function onVideoEnd() {
        console.log('Video ended');
        $('#carouselExampleFade').carousel('next');
    }

    function onSlide(event) {
        var activeSlide = $(event.relatedTarget);
        var videoElement = activeSlide.find('video'); // Encuentra el elemento de video dentro del slide activo

        if (videoElement.length > 0) {
            videoElement[0].currentTime = 0; // Reinicia el video
            videoElement[0].play(); // Reproduce el video
        }
    }

    // Métodos públicos
    return {
        iniciar: function() {
            // Asegúrate de que el selector aquí coincida con el contenedor de tus videos
            
    $('#video_promo_1')[0].play()
            $('.carousel-item video').on('ended', onVideoEnd); // Selecciona todos los videos dentro de los items del carrusel
            $('#carouselExampleFade').on('slid.bs.carousel', onSlide);
        }
    };
})();

// Uso del objeto
$(document).ready(function() {
    VideoManager.iniciar();
});

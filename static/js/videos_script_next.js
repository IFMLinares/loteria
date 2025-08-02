var VideoManager = (function() {
    // Método privado
    function onVideoEnd() {
        console.log('Video ended');
        $('#carouselExampleFade').carousel('next');
    }

    function onSlide(event) {
        var activeSlide = $(event.relatedTarget);
        var ids = ['video_1', 'video_2', 'video_3', 'video_4', 'video_5'];
        if (ids.includes(activeSlide.attr('id'))) {
            var videoElement = null;
            switch(activeSlide.attr('id')) {
                case 'video_1':
                    videoElement = $('#video_promo_1');
                    break;
                case 'video_2':
                    videoElement = $('#video_promo_2');
                    break;
                case 'video_3':
                    videoElement = $('#video_promo_3');
                    break;
                case 'video_4':
                    videoElement = $('#video_promo_4');
                    break;
                case 'video_5':
                    videoElement = $('#video_promo_5');
                    break;
            }
            if (videoElement && videoElement.length > 0) {
                videoElement[0].currentTime = 0; // Reinicia el video
                videoElement[0].play(); // Reproduce el video
            }
        }
    }

    // Métodos públicos
    return {
        iniciar: function() {
            $('#video_promo').on('ended', onVideoEnd); // Cambia '#video_1 video' por '#video_promo'
            $('#carouselExampleFade').on('slid.bs.carousel', onSlide);
        }
    };
})();

// Uso del objeto
VideoManager.iniciar();

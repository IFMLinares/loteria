var WebSocketManager = (function() {
    // Variables privadas
    let horarios = {
        'TripleCaliente': ['1:00 PM', '4:30 PM', '7:10 PM'],
        'TripleCaracas': ['1:00 PM', '4:30 PM', '7:00 PM'],
        'TripleZulia': ['12:45 PM', '4:45 PM', '7:05 PM'],
        'TripleZamorano': ['12:00 PM', '4:00 PM', '7:00 PM'],
        'TripleChance': ['1:00 PM', '4:30 PM', '7:00 PM'],
        'TripleTachira': ['1:15 PM', '4:45 PM', '7:20 PM'],
        // 'TrioActivo': ['1:00 PM', '4:30 PM', '7:10 PM'],
        // 'Ricachona': ['1:00 PM', '4:30 PM', '7:10 PM'],
        // Añade aquí los horarios para los otros modelos
    };

    let webSocket;
    let url = `ws://${window.location.host}/ws/socket-server/`;

    // Métodos privados
    function connect() {
        webSocket = new WebSocket(url);

        webSocket.onopen = function(e) {
            // console.log('Conexión WebSocket abierta');
        };

        webSocket.onclose = function(e) {
            // console.log('Conexión WebSocket cerrada. Reconectando...');
            setTimeout(connect, 1000);
        };

        webSocket.onerror = function(err) {
            // console.error('WebSocket Error:', err);
        };

        webSocket.onmessage = function(e) {
            let data = JSON.parse(e.data);
            console.log(data)
            if (data === 'reload') {
                location.reload();
            }else{
            let tablaId = data.modelo;
            let modelos = ['TripleCaliente', 'TripleCaracas', 'TripleZulia', 'TripleZamorano', 'TripleChance', 'TripleTachira', 'TrioActivo', 'Ricachona','FruitaGana'];
            if (modelos.includes(tablaId)) {
                if (tablaId === 'TrioActivo' || tablaId === 'Ricachona') {
                    let tablas = document.querySelectorAll(`.${tablaId}`);
                    for (let tabla of tablas) {
                        let hora = tabla.querySelector('thead tr th').textContent;
                        if (hora === data.hour_sort) {
                            let fila = tabla.querySelector('tbody tr');
                            fila.children[0].textContent = data.a;
                            break;
                        }
                    }
                }else {
                    let indice = horarios[tablaId].indexOf(data.hour_sort) + 1;
                    let tabla = document.querySelector(`.${tablaId}-${indice}`);
                    let filaVieja = tabla.querySelector('tbody tr');
                    filaVieja.remove();
                    let nuevaFila = tabla.querySelector('tbody').insertRow(-1);
    
                    if(tablaId === 'TripleZamorano'){
                        nuevaFila.insertCell(0).textContent = data.a;
                        nuevaFila.insertCell(1).textContent = data.c;
                            let celdaZod = nuevaFila.insertCell(2);
                        celdaZod.textContent = data.zod;
                        celdaZod.style.color = 'red';
                    }else{
                        nuevaFila.insertCell(0).textContent = data.a;
                        nuevaFila.insertCell(1).textContent = data.b;
                        nuevaFila.insertCell(2).textContent = data.c;
                        let celdaZod = nuevaFila.insertCell(3);
                        celdaZod.textContent = data.zod;
                        celdaZod.style.color = 'red';
                    }
                }
            } else {
                let filas = document.querySelectorAll(`#${tablaId} tbody tr`);
                for (let i = 0; i < filas.length; i++) {
                    let fila = filas[i];
                    let hora = fila.children[0].textContent;
    
                    if (hora === data.hour_sort) {
                        fila.children[1].textContent = data.animalito;
                        fila.children[2].textContent = data.animalito_name;
                        let imagen = fila.children[3].children[0];
                        imagen.src = data.image_path;
                        imagen.alt = data.animalito_name;
                        imagen.style.opacity = '1';
                        break;
                    }
                }
            }
            }
    };
    }

    // Métodos públicos
    return {
        iniciar: function() {
            connect();
        }
    };
})();

// Uso del objeto
WebSocketManager.iniciar();

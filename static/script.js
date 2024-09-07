"use strict";

document.addEventListener("DOMContentLoaded", function () {
    // Obtener referencias a los elementos del DOM
    const toggleButton = getElementByIdSafe("toggle-button");
    const Form1 = document.querySelector("#SEARCH_1");
    const Form2 = document.querySelector("#SEARCH_2");

    // Verifica que los elementos existan
    if (toggleButton && Form1 && Form2) {
        // Asignar el evento para alternar los formularios
        toggleButton.addEventListener("click", function () {
            formula(toggleButton, Form1, Form2);
        });
    }

    // Asignar el evento para buscar por ciudad
    const BSeach1 = getElementByIdSafe('BSeach1');
    if (BSeach1) {
        BSeach1.addEventListener('click', function (event) {
            document.querySelector("#card_clima").style.display = "none";
            event.preventDefault();
            borra_list()
            buscarPorCiudad();
        });
    }

    // Asignar el evento para buscar por código IATA
    const BSeach2 = getElementByIdSafe('BSeach2');
    if (BSeach2) {
        BSeach2.addEventListener('click', function (event) {
            event.preventDefault();
            borra_list()
            buscarPorIATA();
        });
    }
});

// Función para obtener elementos de manera segura y verificar si existen
function getElementByIdSafe(id) {
    const element = document.getElementById(id);
    if (!element) {
        console.error(`Elemento con ID ${id} no encontrado`);
    }
    return element;
}

// Función para alternar entre formularios de búsqueda por ciudad o IATA
function formula(toggleButton, Form1, Form2) {
    borrarTexto(); // Asume que tienes una función borrarTexto() definida en otro lugar
    const isForm2Visible = Form2.style.display === "flex"; // Determinar si Form2 es visible

    Form1.style.display = isForm2Visible ? "flex" : "none";
    Form2.style.display = isForm2Visible ? "none" : "flex";
    // Usa innerHTML para agregar texto y HTML juntos
    toggleButton.innerHTML = isForm2Visible
        ? 'Buscar por ciudad <span class="material-symbols-outlined">change_circle</span>'
        : 'Buscar por IATA <span class="material-symbols-outlined">change_circle</span>';
}

// Función para manejar las búsquedas genéricas
function manejarBusqueda(url, procesarRespuesta) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // O .text() si esperas texto
        })
        .then(data => {
            console.log(data)
            if (data) {
                expoErro(data, procesarRespuesta);
            } else {
                console.log(`Hubo un error al procesar la respuesta:  ${data}`);
            }
        })
        .catch(error => console.error('Error:', error));
}

// Función específica para buscar por ciudad
function buscarPorCiudad() {
    let ciudadOrigen = document.getElementById('ciudad-input').value;
    let ciudadDestino = document.getElementById('airline-input').value;
    const url = `/search?ciudad=${encodeURIComponent(ciudadOrigen)}&destino=${encodeURIComponent(ciudadDestino)}`;

    // Usamos la función manejarBusqueda y pasamos expoDatos como callback
    manejarBusqueda(url, data => expoDatos(data));
}

// Función específica para buscar por código IATA
function buscarPorIATA() {
    let codigoVuelo = document.getElementById('iata-input').value;
    const url = `/search?iata=${encodeURIComponent(codigoVuelo)}`;

    // Usamos la función manejarBusqueda y procesamos la respuesta directamente en la consola
    manejarBusqueda(url, data => expoElem(data[0]));
}

// Función para borrar el texto de los formularios (asegúrate de definirla)
function borrarTexto() {
    document.getElementById('ciudad-input').value = '';
    document.getElementById('airline-input').value = '';
    document.getElementById('iata-input').value = '';
}

/*document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-button");
    const Form1 = document.querySelector("#SEARCH_1");
    const Form2 = document.querySelector("#SEARCH_2");
    const boton = document.querySelector("#BSeach");
    const erro = document.querySelector(".error");

    // Verifica si los elementos existen
    if (toggleButton && Form2.length && Form1.length) {
        toggleButton.addEventListener("click", function () {
            borrarTexto();
            if (Form2.style.display === "none" || !Form2.style.display) {
                // Mostrar el div "iata_search" y ocultar los "ciudad_search"
                Form2.style.display = "flex";
                Form1.style.display = "none";
                toggleButton.textContent = "Buscar por IATA";
            } else {
                // Mostrar los divs "ciudad_search" y ocultar el "iata_search"
                Form2.style.display = "none";
                Form1.style.display = "flex";
                toggleButton.textContent = "Buscar por ciudad";
            }
        });
    }

    document.getElementById('BSeach1').addEventListener('click', function(event) {
    event.preventDefault();

    let ciudadOrigen = document.getElementById('ciudad-input').value;
    let ciudadDestino = document.getElementById('airline-input').value;

    fetch(`/search?ciudad=${encodeURIComponent(ciudadOrigen)}&destino=${encodeURIComponent(ciudadDestino)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Asegúrate de que el servidor devuelve JSON
        })
        .then(data => {
            if (!data) {
                console.log("Hubo un error");
            } else {
                expoDatos(data); // Supone que data es un objeto JSON
            }
        }).catch(error => console.error('Error:', error));
    });

    document.getElementById('BSeach2').addEventListener('click', function(event) {
        event.preventDefault(); // Evita el envío tradicional del formulario

        let codigoVuelo = document.getElementById('iata-input').value;

        fetch(`/search?iata=${encodeURIComponent(codigoVuelo)}`)
            .then(response => response.text())
            .then(data => {
                expoElem(data) // Aquí puedes actualizar el DOM con la respuesta
            }).catch(error => console.error('Error:', error));

        // Si deseas enviar el formulario al servidor, puedes hacerlo con fetch o similar
        this.click(); // Opcionalmente puedes enviar el formulario después de la lógica
    });
});*/

// Expone los datos del JSON en la página web
// Expone los datos del JSON en la página web
function expoDatos(datos) {
    const ticket = document.getElementById('ticket');
    const lista = document.getElementById("listaVuelo");
    const boton = document.querySelector("#BSeach");

    if (!lista) {
        console.error('Elemento con ID "listaVuelo" no encontrado');
        return;
    }

    datos.forEach(vuelo => {
        const li = document.createElement('li');

        li.dataset.id = vuelo.iata;

        // Clona el formato del ticket
        const tClone = ticket.cloneNode(true);
        tClone.classList.add('vuelo_ticket');
        tClone.querySelector('.lineaDevuelo').textContent = vuelo.aereolinea;
        tClone.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
        tClone.querySelector('.iata_vuelos').textContent = vuelo.iata;
        tClone.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

        // Agregar la etiqueta clonada al li
        li.appendChild(tClone);

        // Almacena los detalles del vuelo clonados
        const clim = asigna(vuelo)
        clim.style.display = "none";
        clim.classList.add("detalles");
        li.appendChild(clim);
        lista.appendChild(li);

        // Añadir el evento de clic para desplegar/ocultar detalles
        tClone.addEventListener('click', function () {
            const esActivo = li.classList.contains('detalles');

            // Cerramos cualquier otra sección abierta
            document.querySelectorAll('#listaVuelo li.active').forEach(item => {
                item.classList.remove('active');
                item.querySelector('.detalles').style.display = 'none';
            });

            // Desplegar detalles si no estaba activo, si estaba activo lo oculta
            if (!esActivo) {
                li.classList.add('active');
                li.querySelector('.detalles').style.display = 'flex';
            }
        });
    });
}


// Asigna valores del JSON a las etiquetas que se muestran en el frontend
function asigna(vuelo) {
    const clima = document.querySelector('#informacion');

    if (clima) {
        // Clonamos el div de clima y asignamos los valores del JSON
        const cClone = clima.cloneNode(true);
        cClone.classList.add("climas");
        cClone.querySelector('#infoAero_01').textContent = vuelo.origen;
        cClone.querySelector('#info_ciudad01').textContent = `Ciudad ${vuelo.ciudadOr}`;
        cClone.querySelector('#infoHora01').textContent = `Hora: ${vuelo["hora realOr"]}`;
        cClone.querySelector('#infociudad_01').textContent = vuelo.ciudadOr;
        cClone.querySelector('#infofecha01').textContent = `${vuelo["hora realOr"]} CST • ${vuelo["fecha abreviadaOr"]}`;
        cClone.querySelector('#infClima_01').textContent = vuelo.clima_origen.Clima;
        cClone.querySelector('#infoTemp_01').textContent = vuelo.clima_origen.Temperatura;
        cClone.querySelector('#range01').textContent = `${vuelo.clima_origen['Temperatura minima']}° - ${vuelo.clima_origen["Temperatura maxima"]}°`;
        cClone.querySelector('#principal01').textContent = `Condición principal: ${vuelo.clima_origen["Descripcion"]}.`;
        cClone.querySelector('#CNubosa01').textContent = `Cobertura nubosa: ${vuelo.clima_origen.Nubosidad}%`;
        cClone.querySelector('#Humedad01').textContent = `Humedad: ${vuelo.clima_origen.Humedad}%`;
        cClone.querySelector('#Termica01').textContent = `Sensación térmica: ${vuelo.clima_origen.Termica}°`;
        cClone.querySelector('#velocidad01').textContent = `Velocidad del viento: ${vuelo.clima_origen["Velocidad del viento"]} m/s.`;
        cClone.querySelector('#direccion01').textContent = `Dirección del viento: ${vuelo.clima_origen["Direccion del viento"]}°`;
        cClone.querySelector('#atmosfera01').textContent = `Presión atmosférica: ${vuelo.clima_origen["Presion atmosferica"]} hPa`;
        icono(cClone, "#oIcono", vuelo.clima_origen.icono)

        cClone.querySelector('#infoAero_02').textContent = vuelo.destino;
        cClone.querySelector('#info_ciudad02').textContent = `Ciudad ${vuelo.ciudadDes}`;
        cClone.querySelector('#infoHora02').textContent = `Hora: ${vuelo["hora realDes"]}`;
        cClone.querySelector('#infociudad_02').textContent = vuelo.ciudadDes;
        cClone.querySelector('#infofecha02').textContent = `${vuelo["hora realDes"]} CST • ${vuelo["fecha abreviadaDes"]}`;
        cClone.querySelector('#infClima_02').textContent = vuelo.clima_destino.Clima;
        cClone.querySelector('#infoTemp_02').textContent = vuelo.clima_destino.Temperatura;
        cClone.querySelector('#range02').textContent = `${vuelo.clima_destino['Temperatura minima']}° - ${vuelo.clima_destino["Temperatura maxima"]}°`;
        cClone.querySelector('#principal02').textContent = `Condición principal: ${vuelo.clima_destino["Descripcion"]}.`;
        cClone.querySelector('#CNubosa02').textContent = `Cobertura nubosa: ${vuelo.clima_destino.Nubosidad}%`;
        cClone.querySelector('#Humedad02').textContent = `Humedad: ${vuelo.clima_destino.Humedad}%`;
        cClone.querySelector('#Termica02').textContent = `Sensación térmica: ${vuelo.clima_destino.Termica}°`;
        cClone.querySelector('#velocidad02').textContent = `Velocidad del viento: ${vuelo.clima_destino["Velocidad del viento"]} m/s.`;
        cClone.querySelector('#direccion02').textContent = `Dirección del viento: ${vuelo.clima_destino["Direccion del viento"]}°`;
        cClone.querySelector('#atmosfera02').textContent = `Presión atmosférica: ${vuelo.clima_destino["Presion atmosferica"]} hPa`;
        icono(cClone, "#dIcono", vuelo.clima_destino.icono)

        return cClone;
    }
    return document.createElement('div'); // Retorna un elemento vacío si 'informacion' no existe
}

function borra_list() {
    const lista = document.getElementById('listaVuelo');
    lista.innerHTML = '';
}

function expoElem(vuelo) {
    const copia = asigna(vuelo);
    const clima = document.querySelector('#informacion');
    const ticket = document.getElementById('ticket');
    const info = document.getElementById('card_clima');

    if (!clima || !ticket || !info) {
        console.error("Uno de los elementos no existe en el DOM");
        return;
    }

    ticket.querySelector('.lineaDevuelo').textContent = vuelo.aereolinea;
    ticket.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
    ticket.querySelector('.iata_vuelos').textContent = vuelo.iata;
    ticket.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

    clima.replaceWith(copia);

    ticket.classList.remove('vuelo_ticket');
    ticket.classList.add('copia');
    info.style.display = "block";
}

/**
 * Asigna el ícono de clima respectivo.
 * @param {HTMLElement} clima - Elemento HTML que contiene la información del clima.
 * @param {string} selector - Selector del ícono en HTML.
 * @param {string} idIcono - ID del ícono del JSON.
 */
function icono(clima, selector, idIcono) {
    // Selecciona el elemento del ícono usando el selector proporcionado
    const iconoElement = clima.querySelector(selector);

    // Mapa de iconos con sus clases correspondientes
    const iconos = {
        "01d": "wi-day-sunny",
        "01n": "wi-night-clear",
        "02d": "wi-day-cloudy",
        "02n": "wi-night-alt-cloudy",
        "03d": "wi-cloud",
        "03n": "wi-cloud",
        "04d": "wi-cloudy",
        "04n": "wi-cloudy",
        "09d": "wi-showers",
        "09n": "wi-night-alt-showers",
        "10d": "wi-day-rain",
        "10n": "wi-night-alt-rain",
        "11d": "wi-day-thunderstorm",
        "11n": "wi-night-alt-thunderstorm",
        "13d": "wi-day-snow",
        "13n": "wi-night-alt-snow",
        "50d": "wi-day-fog",
        "50n": "wi-night-fog"
    };

    // Obtiene la clase correspondiente para el ícono
    const clase = iconos[idIcono] || "noIcono";

    // Si el elemento del ícono existe, actualiza su clase
    if (iconoElement) {
        iconoElement.classList.add(clase);
        iconoElement.classList.add(dia_o_noche(idIcono));
    }
}

/**
 * Elige el estilo de ícono dependiendo si es de día o noche.
 * @param {string} idIcono - ID del ícono.
 * @returns {string} Clase del estilo de CSS para el ícono.
 */
function dia_o_noche(idIcono) {
    // Verifica si el cuarto carácter del ID es 'd' o 'n'
    if (idIcono[2] === 'd') {
        return "IconoStyleDay";
    } else if (idIcono[2] === 'n') {
        return "IconoStyleNight";
    } else {
        return "None";
    }
}

/**
 * Busca los codigos de errores de tipo error de entrada erronea
 * @param data codigo de datos
 * @returns {boolean} error encontrado
 */
function buscaError01(data) {
    const Errores = ["500", "101", "103", "104", "105", "106", "107", "109"];
    // Verifica si el primer elemento de 'data' está en la lista de 'Errores'
    return Errores.includes(data[0]);
}

/**
 * Busca los codigos de errores de tipo error de codigo
 * @param data codigo de datos
 * @returns {boolean} error encontrado
 */
function buscaError02(data) {
    const Errores = ["108", "102", "200", "201", "202", "203", "204", "300", "301", "302"];
    // Verifica si el primer elemento de 'data' está en la lista de 'Errores'
    return Errores.includes(data[0]);
}

function expoErro(data, procesarRespuesta) {
    // Selecciona los elementos de error de una sola vez
    const errorElement = document.querySelector('.error');
    const apiErrorElement = document.querySelector('.apierror');

    // Oculta los mensajes de error inicialmente
    errorElement.style.display = 'none';
    apiErrorElement.style.display = 'none';

    // Verifica si hay errores en los datos
    if (data.length === 0 || buscaError01(data)) {
        errorElement.style.display = 'block'; // Muestra el error general
    } else if (buscaError02(data)) {
        apiErrorElement.style.display = 'block'; // Muestra el error específico de la API
    } else {
        procesarRespuesta(data); // Procesa la respuesta si no hay errores
    }
}

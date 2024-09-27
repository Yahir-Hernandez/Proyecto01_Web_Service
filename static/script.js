"use strict";

<<<<<<< HEAD
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
=======
/**
 * Se ejecuta cuando el DOM ha sido completamente cargado.
 *
 * @event DOMContentLoaded
 */
document.addEventListener("DOMContentLoaded", function () {
    const BotonC = getElementByIdSafe("toggle-button");
    const Form1 = document.querySelector("#SEARCH_1");
    const Form2 = document.querySelector("#SEARCH_2");

    cambioBusqueda(BotonC, Form1, Form2);
    consultaPorCiudad();
    consultaPorIata();
});

/**
 *  Maneja la interaccion de el boton de cambio de busqueda
 */
function cambioBusqueda(BotonC, Form1, Form2) {
    if (BotonC && Form1 && Form2) {
        BotonC.addEventListener("click", function () {
            document.querySelector('.search-container').classList.remove('active');
            document.querySelector('.container-suggestions').style.border = 'none';
            formula(BotonC, Form1, Form2);
        });
    }
}

/**
 *  Maneja la interaccion de el boton de busqueda por ciudades
 */
function consultaPorCiudad() {
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
    const BSeach1 = getElementByIdSafe('BSeach1');
    if (BSeach1) {
        BSeach1.addEventListener('click', function (event) {
            document.querySelector("#card_clima").style.display = "none";
<<<<<<< HEAD
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
=======
            document.querySelector('.search-container').classList.remove('active');
            document.querySelector('.container-suggestions').style.border = 'none';
            event.preventDefault();
            quitaClima();
            noSpam(BSeach1);
            borra_list()
            buscarPorCiudad();
            borrarTexto()
        });
    }
}

/**
 *  Maneja la interaccion de el boton de busqueda por Iata de vuelo
 */
function consultaPorIata() {
     const BSeach2 = getElementByIdSafe('BSeach2');
    if (BSeach2) {
        BSeach2.addEventListener('click', function (event) {
            document.querySelector('.search-container').classList.remove('active');
            document.querySelector('.container-suggestions').style.border = 'none';
            document.querySelector('.carga').style.display = 'flex';
            event.preventDefault();
            quitaClima();
            noSpam(BSeach2);
            borra_list();
            buscarPorIATA();
            borrarTexto();
        });
    }
}

/**
 * Devuelve el elemento consultado por Id
 * @param {string} id del elemento HTML
 * @returns {HTMLElement} elemento encontrado
 */
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
function getElementByIdSafe(id) {
    const element = document.getElementById(id);
    if (!element) {
        console.error(`Elemento con ID ${id} no encontrado`);
    }
    return element;
}

<<<<<<< HEAD
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
=======
/**
 * Maneja la interaccion de el boton de cambio de busqueda
 * @param {HTMLElement} toggleButton boton de cambio de tipo de busqueda
 * @param {HTMLElement} Form1 campo de busqueda por ciudades
 * @param {HTMLElement} Form2 campo de busqueda por iata de vuelo
 */
function formula(toggleButton, Form1, Form2) {
    borrarTexto();
    const isForm2Visible = Form2.style.display === "flex";

    Form1.style.display = isForm2Visible ? "flex" : "none";
    Form2.style.display = isForm2Visible ? "none" : "flex";
    quitaClima();
    // Usa innerHTML para agregar texto y HTML juntos
    toggleButton.innerHTML = isForm2Visible
        ? 'Cambiar busqueda <span class="material-symbols-outlined">change_circle</span>'
        : 'Cambiar busqueda <span class="material-symbols-outlined">change_circle</span>';
}

/**
 * Maneja la busqueda de vuelos
 * @param {string} url enviada por el servidor
 * @param {function} procesarRespuesta funcion para procesar los datos
 */
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
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

<<<<<<< HEAD
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
=======
/**
 * Metodo para la busqueda por ciudades indicadas
 */
function buscarPorCiudad() {
    let ciudad = document.getElementById('ciudad-input').value;
    const url = `/search?ciudad=${encodeURIComponent(ciudad)}`;
    manejarBusqueda(url, data => expoclima(data[0]));
}

/**
 * Metodo para la busqueda por codigo iata del vuelo indicado
 */
function buscarPorIATA() {
    let codigoVuelo = document.getElementById('iata-input').value;
    const url = `/search?iata=${encodeURIComponent(codigoVuelo)}&iata=${encodeURIComponent(codigoVuelo)}`;
    manejarBusqueda(url, data => expoElem(data[0]));
}

/**
 * Borra el texto en la campos de busqueda.
 */
function borrarTexto() {
    document.getElementById('ciudad-input').value = '';
    document.getElementById('iata-input').value = '';
}

/**
 * Elimina de la vista informacion del clima de busquedas
 * anteriores para mostrar nueva informacion de clima
 */
function quitaClima() {
    const ticket = document.querySelector('.content_vuelo');
    const clima = document.querySelector('#climaCiudad-Iata');
    if (ticket || (ticket.style.display === "flex")) {ticket.style.display = 'none';}
    if (clima || (clima.style.display === "flex")) {clima.style.display = 'none';}
}

/**
 * Espone el clima que el usuario especifico
 * @param {object} data informacion del clima especificado
 */
function expoclima(data) {
    let clima = document.querySelector('.clima_unico');
    let carga = document.querySelector('.carga'); // Asegúrate de seleccionar el elemento correctamente

    if (clima && carga) {
        asignaClima(clima, data);

        setTimeout(() => {
            clima.style.display = 'flex';
            console.log('Ocultando carga...');
            carga.style.display = 'none'; // Asegúrate de que esta línea esté funcionando
        }, 10000);
    } else {
        console.error('El elemento .clima_unico o .carga no existe en el DOM');
    }
}

/**
 *  Asigna los valores del onjeto clima a las etiquetas correspondientes
 *  en el front
 * @param {HTMLElement} clima etiqueta HTMl clima
 * @param {object} data informacion del clima especificado
 */
function asignaClima(clima,data) {
    clima.querySelector(`#ciudad`).textContent = data.Ciudad;
    clima.querySelector(`#horaFecha`).textContent = `${data.Hora_actual} CST • ${data['Fecha simplificada']}`;
    clima.querySelector(`.estado`).textContent = data.Clima;
    clima.querySelector(`.temp-actual`).textContent = `${data.Temperatura}°`;
    clima.querySelector(`.temp-range`).textContent = `${data['Temperatura minima']}° - ${data["Temperatura maxima"]}°`;
    clima.querySelector(`#principal`).textContent = data["Descripcion"];
    clima.querySelector(`#CNubosa`).textContent = `${data.Nubosidad}%`;
    clima.querySelector(`#Humedad`).textContent = `${data.Humedad}%`;
    clima.querySelector(`#Termica`).textContent = `${data.Termica}°`;
    clima.querySelector(`#velocidad`).textContent = `${data["Velocidad del viento"]} m/s.`;
    clima.querySelector(`#direccion`).textContent = `${data["Direccion del viento"]}°`;
    clima.querySelector(`#atmosfera`).textContent = `${data["Presion atmosferica"]} hPa`;
    icono(clima, `#oIcono`, data.icono);
}

/**
 *  Agrega vuelos a la lista definida en index.html
 * @param {object} datos datos de vuelos especificados
 */
function expoDatos(datos) {
    const ticket = document.getElementById('ticket');
    const lista = document.getElementById("listaVuelo");
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8

    if (!lista) {
        console.error('Elemento con ID "listaVuelo" no encontrado');
        return;
    }

    datos.forEach(vuelo => {
        const li = document.createElement('li');
<<<<<<< HEAD

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
=======
        li.classList.add('content_vuelo')
        li.dataset.id = vuelo.iata;

        const tClone = ticket.cloneNode(true);
        tClone.classList.add('vuelo_ticket');
        ingresaInfo(tClone, vuelo);

        li.appendChild(tClone);

        const clim = asigna(vuelo);
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
        clim.style.display = "none";
        clim.classList.add("detalles");
        li.appendChild(clim);
        lista.appendChild(li);

<<<<<<< HEAD
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

=======
        tClone.addEventListener('click', () => desplega(li));
    });
}

/**
 *  Metodo interactivo, despliega y repliega la informacion del clima de origen y destino
 * @param {HTMLElement} li elemento lista de HTML
 */
function desplega(li) {
    const esActivo = li.classList.contains('active');

    document.querySelectorAll('#listaVuelo li.active').forEach(item => {
        item.classList.remove('active');
        item.querySelector('.detalles').style.display = 'none';
    });

    if (!esActivo) {
        li.classList.add('active');
        li.querySelector('.detalles').style.display = 'flex';
    }
}

/**
 * Asigna toda la informacion de vuelo a un elemento de HTML
 * @param {object} vuelo informacion general de vuelo
 * @returns {HTMLElement} etiqueta de vuelo clonada con la informacion
 */
function asigna(vuelo) {
    const clima = document.querySelector('#informacion');

    if (!clima) {
        return document.createElement('div');
    }

    const cClone = clima.cloneNode(true);
    cClone.classList.add("climas");

    asignaInformacion(cClone, vuelo.clima_origen, '01',vuelo);
    asignaInformacion(cClone, vuelo.clima_destino, '02',vuelo);

    return cClone;
}

/**
 * Asigna la informacion general del vuelo a la etiqueta de clone
 * @param {HTMLElement} clone etiqueta clonada de la informacion de vuelo
 * @param {object} climaInfo informacion del vuelo
 * @param {string} prefix prefijo de clima de origen o destino
 * @param {object} vuelo informacion general del vuelo
 */
function asignaInformacion(clone, climaInfo, prefix, vuelo) {
    clone.querySelector(`#infoAero_${prefix}`).textContent = climaInfo === vuelo.clima_origen ? vuelo.origen : vuelo.destino;
    clone.querySelector(`#info_ciudad${prefix}`).textContent = `Ciudad: ${climaInfo === vuelo.clima_origen ? vuelo.ciudadOr :  vuelo.ciudadDes}`;
    clone.querySelector(`#infoHora${prefix}`).textContent = `Hora: ${vuelo["hora real" + (climaInfo === vuelo.clima_origen ? "Or" : "Des")]}`;
    clone.querySelector(`#infociudad_${prefix}`).textContent = climaInfo === vuelo.clima_origen ? vuelo.ciudadOr :  vuelo.ciudadDes;
    clone.querySelector(`#infofecha${prefix}`).textContent = `${vuelo["hora real" + (climaInfo === vuelo.clima_origen ? "Or" : "Des")]} CST • ${vuelo["fecha abreviada" + (climaInfo === vuelo.clima_origen ? "Or" : "Des")]}`;

    asignaClimaClone(clone, climaInfo, prefix);
}

/**
 * Asigna elementos de climaInfo a clone
 * @param {HTMLElement} clone etiqueta de vuelo clonada
 * @param {object} climaInfo objeto de vuelo
 * @param {string} prefix prefijo de clima de origen o destino
 */
function asignaClimaClone(clone, climaInfo, prefix) {
    clone.querySelector(`#infClima_${prefix}`).textContent = climaInfo.Clima;
    clone.querySelector(`#infoTemp_${prefix}`).textContent = `${climaInfo.Temperatura}°`;
    clone.querySelector(`#range${prefix}`).textContent = `${climaInfo['Temperatura minima']}° - ${climaInfo["Temperatura maxima"]}°`;
    clone.querySelector(`#principal${prefix}`).textContent = climaInfo["Descripcion"];
    clone.querySelector(`#CNubosa${prefix}`).textContent = `${climaInfo.Nubosidad}%`;
    clone.querySelector(`#Humedad${prefix}`).textContent = `${climaInfo.Humedad}%`;
    clone.querySelector(`#Termica${prefix}`).textContent = `${climaInfo.Termica}°`;
    clone.querySelector(`#velocidad${prefix}`).textContent = `${climaInfo["Velocidad del viento"]} m/s.`;
    clone.querySelector(`#direccion${prefix}`).textContent = `${climaInfo["Direccion del viento"]}°`;
    clone.querySelector(`#atmosfera${prefix}`).textContent = `${climaInfo["Presion atmosferica"]} hPa`;
    icono(clone, `#${prefix === '01' ? 'o' : 'd'}Icono`, climaInfo.icono);
}

/**
 * Borra la lista de vuelo en la pagina Web
 */
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
function borra_list() {
    const lista = document.getElementById('listaVuelo');
    lista.innerHTML = '';
}

<<<<<<< HEAD
=======
/**
 * Expone un vuelo en la pagina Web
 * @param {object} vuelo informacion del vuelo
 */
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
function expoElem(vuelo) {
    const copia = asigna(vuelo);
    const clima = document.querySelector('#informacion');
    const ticket = document.getElementById('ticket');
    const info = document.getElementById('card_clima');
<<<<<<< HEAD
=======
    const carga = document.querySelector('.carga');
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8

    if (!clima || !ticket || !info) {
        console.error("Uno de los elementos no existe en el DOM");
        return;
    }

<<<<<<< HEAD
    ticket.querySelector('.lineaDevuelo').textContent = vuelo.aereolinea;
    ticket.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
    ticket.querySelector('.iata_vuelos').textContent = vuelo.iata;
    ticket.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

=======
    ingresaInfo(ticket, vuelo);
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
    clima.replaceWith(copia);

    ticket.classList.remove('vuelo_ticket');
    ticket.classList.add('copia');
<<<<<<< HEAD
    info.style.display = "block";
=======
    carga.style.display = 'none';
    info.style.display = "block";

}

/**
 * Asigna informacion general del vuelo
 * @param {HTMLElement} ticket etiqueta de informacion general del vuelo
 * @param {object} vuelo informacion del vuelo
 */
function ingresaInfo(ticket, vuelo) {
    ticket.querySelector('.lineaDevuelo').textContent = vuelo.aereolinea;
    ticket.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
    ticket.querySelector('.iata_vuelos').textContent = vuelo.iata;
    ticket.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
}

/**
 * Asigna el ícono de clima respectivo.
 * @param {HTMLElement} clima - Elemento HTML que contiene la información del clima.
 * @param {string} selector - Selector del ícono en HTML.
 * @param {string} idIcono - ID del ícono del JSON.
 */
function icono(clima, selector, idIcono) {
<<<<<<< HEAD
    // Selecciona el elemento del ícono usando el selector proporcionado
    const iconoElement = clima.querySelector(selector);

    // Mapa de iconos con sus clases correspondientes
=======
    const iconoElement = clima.querySelector(selector);

>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
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

<<<<<<< HEAD
    // Obtiene la clase correspondiente para el ícono
    const clase = iconos[idIcono] || "noIcono";

    // Si el elemento del ícono existe, actualiza su clase
=======
    const clase = iconos[idIcono] || "noIcono";

>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
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
<<<<<<< HEAD
 * @param data codigo de datos
=======
 * @param {array} data codigo de datos
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
 * @returns {boolean} error encontrado
 */
function buscaError01(data) {
    const Errores = ["500", "101", "103", "104", "105", "106", "107", "109"];
    // Verifica si el primer elemento de 'data' está en la lista de 'Errores'
    return Errores.includes(data[0]);
}

/**
 * Busca los codigos de errores de tipo error de codigo
<<<<<<< HEAD
 * @param data codigo de datos
=======
 * @param {array} data codigo de error
>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8
 * @returns {boolean} error encontrado
 */
function buscaError02(data) {
    const Errores = ["108", "102", "200", "201", "202", "203", "204", "300", "301", "302"];
<<<<<<< HEAD
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
=======
    return Errores.includes(data[0]);
}

/**
 * Expone errores en la pagina
 * @param  {string} data codigo de error
 * @param  {function} procesarRespuesta Realiza la accion de respuesta al error
 */
function expoErro(data, procesarRespuesta) {
    const errorElement = document.querySelector('.error');
    const apiErrorElement = document.querySelector('.apierror');
    const carga = document.querySelector('.carga');
    const boton1 = document.querySelector('#BSeach1');
    const boton2 = document.querySelector('#BSeach2');

    errorElement.style.display = 'none';
    apiErrorElement.style.display = 'none';

    if (data.length === 0 || buscaError01(data)) {
        carga.style.display = 'none';
        errorElement.style.display = 'block';
        setTimeout(() => {
            boton1.style.backgroundColor = '#1EA7FF';
            boton2.style.backgroundColor = '#1EA7FF';
            boton1.disabled = false;
            boton2.disabled = false;
        }, 3000);
    } else if (buscaError02(data)) {
        apiErrorElement.style.display = 'block';
        carga.style.display = 'none';
        setTimeout(() => {
            boton1.style.backgroundColor = '#1EA7FF';
            boton2.style.backgroundColor = '#1EA7FF';
            boton1.disabled = false;
            boton2.disabled = false;
        }, 3000);

    } else {
        procesarRespuesta(data);
    }
}

/**
 * Evita el spam en lo botones de busqueda.
 * @param {HTMLElement} boton que sera desactivado por un momento
 */
function noSpam(boton) {

    // Deshabilitar el botón inmediatamente
    boton.disabled = true;
    boton.style.backgroundColor = "#1E1F25";

    // Lógica o acción que se debe ejecutar
    console.log('Enviando datos...');

    // Rehabilitar el botón después de 5 segundos
    setTimeout(() => {
        boton.style.backgroundColor = '#1EA7FF';
        boton.disabled = false;
        console.log('Botón habilitado de nuevo');
    }, 10000); // 5000 ms = 5 segundos
}

>>>>>>> 11749fc26b5cc0fddd7565ed6f5331abbe572dc8

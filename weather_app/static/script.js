"use strict";

import {manejarBusqueda, asignaClima} from "./metodos.js";

/**
 * Se ejecuta cuando el DOM ha sido completamente cargado.
 *
 * @event DOMContentLoaded
 */
document.addEventListener("DOMContentLoaded", function () {
    const BotonC = getElementByIdSafe("toggle-button");
    const Form1 = document.querySelector("#SEARCH_1");
    const Form2 = document.querySelector("#SEARCH_2");
    const botonB1 = document.querySelector("#BSeach1");
    const botonB2 = document.querySelector("#BSeach2");

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
    const BSeach1 = getElementByIdSafe('BSeach1');
    if (BSeach1) {
        BSeach1.addEventListener('click', function (event) {
            document.querySelector("#card_clima").style.display = "none";
            document.querySelector('.search-container').classList.remove('active');
            document.querySelector('.container-suggestions').style.border = 'none';
            document.querySelector('.carga').style.display = 'flex';
            event.preventDefault();
            quitaClima();
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
function getElementByIdSafe(id) {
    const element = document.getElementById(id);
    if (!element) {
        console.error(`Elemento con ID ${id} no encontrado`);
    }
    return element;
}

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
    
    toggleButton.innerHTML = isForm2Visible
        ? 'Buscar por ticket <span class="material-symbols-outlined">change_circle</span>'
        : 'Buscar por ciudad/Iata <span class="material-symbols-outlined">change_circle</span>';
}

/**
 * Metodo para la busqueda por ciudades indicadas
 */
function buscarPorCiudad() {
    let ciudad = document.getElementById('ciudad-input').value;
    const url = `/search?ciudad=${encodeURIComponent(ciudad)}`;
    manejarBusqueda(url, data => expoclima(data), datosNulos);
}

/**
 * Metodo para la busqueda por codigo iata del vuelo indicado
 */
function buscarPorIATA() {
    let codigoVuelo = document.getElementById('iata-input').value;
    const url = `/search?iata=${encodeURIComponent(codigoVuelo)}`;
    manejarBusqueda(url, data => expoElem(data[0]), datosNulos);
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
    let clima = document.querySelector('#climaCiudad-Iata');
    let carga = document.querySelector('.carga'); 

    if (clima && carga) {
        asignaClima(clima, data[0]);
        carga.style.display = 'none';
        clima.style.display = 'flex';
    } else {
        console.error('El elemento .clima_unico o .carga no existe en el DOM');
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
 * Expone un vuelo en la pagina Web
 * @param {object} vuelo informacion del vuelo
 */
function expoElem(vuelo) {
    const copia = asigna(vuelo);
    const clima = document.querySelector('#informacion');
    const ticket = document.getElementById('ticket');
    const info = document.getElementById('card_clima');
    const carga = document.querySelector('.carga');

    if (!clima || !ticket || !info) {
        console.error("Uno de los elementos no existe en el DOM");
        return;
    }

    ingresaInfo(ticket, vuelo);
    clima.replaceWith(copia);

    ticket.classList.remove('vuelo_ticket');
    ticket.classList.add('copia');
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
}

/**
 * Asigna el ícono de clima respectivo.
 * @param {HTMLElement} clima - Elemento HTML que contiene la información del clima.
 * @param {string} selector - Selector del ícono en HTML.
 * @param {string} idIcono - ID del ícono del JSON.
 */
function icono(clima, selector, idIcono) {
    const iconoElement = clima.querySelector(selector);

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

    const clase = iconos[idIcono] || "noIcono";

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

    if (idIcono[2] === 'd') {
        return "IconoStyleDay";
    } else if (idIcono[2] === 'n') {
        return "IconoStyleNight";
    } else {
        return "None";
    }
}

/**
 * Muestra error de datos nulos
 */
function datosNulos() {
    const error = document.querySelector('.apierror').style.display = 'block';
    setTimeout(() => {
        error.style.display = 'none';
    }, 10000)
}



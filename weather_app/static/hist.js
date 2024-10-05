"use strict";
import {asignaClima, icono, manejarBusqueda} from "./metodos.js";

/**
 * Se ejecuta cuando el DOM ha sido completamente cargado.
 *
 * @event DOMContentLoaded
 */
document.addEventListener("DOMContentLoaded", () => {
    const boton1 = document.querySelector('#boton1');
    const boton2 = document.querySelector('#boton2');
    consulta('/historial/iatas', expoClimas , boton1, boton2);
    consulta('/historial/tickets', expoDatos , boton2, boton1);
});

/**
 * Metodo que maneja el boton de consulta del tipo de historial
 * @param {String} url de respuesta a la peticion de datos
 * @param {function} manejaRespuesta metodo que manejaran lo datos recibidos
 * @param {HTMLElement} boton1 de accion de consulta del historial
 * @param {HTMLElement} boton2 de accion de consulta del historial
 */
function consulta(url, manejaRespuesta, boton1, boton2) {
    if (boton1) {
        boton1.addEventListener('click', function (event) {
            event.preventDefault();
            desBoton(boton1, boton2);
            clearList()
            manejarBusqueda(url, manejaRespuesta, sinHistorial);
        });
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
 * Asigna los valores del objeto clima a las etiquetas correspondientes en el front-end.
 * @param {HTMLElement} clima Elemento HTML que contiene las etiquetas del clima.
 * @param {object} data Información del clima proporcionada.
 */
export function asignaClim(clima, data) {
    clima.querySelector(`#ciudad`).textContent = data.Ciudad ? data.Ciudad : 'None';
    clima.querySelector(`#horaFecha`).textContent = `${data['Hora simplificada']} CST • ${data['Fecha simplificada'] || 'No disponible'}`;
    clima.querySelector(`.estado`).textContent = data.Clima;
    clima.querySelector(`.temp-actual`).textContent = `${data.Temperatura}°`;
    clima.querySelector(`.temp-range`).textContent = `${data['Temperatura minima']}° - ${data['Temperatura maxima']}°`;
    clima.querySelector(`#principal`).textContent = data.Descripcion;
    clima.querySelector(`#CNubosa`).textContent = `${data.Nubosidad}%`;
    clima.querySelector(`#Humedad`).textContent = `${data.Humedad}%`;
    clima.querySelector(`#Termica`).textContent = `${data.Termica}°`;
    clima.querySelector(`#velocidad`).textContent = `${data['Velocidad del viento']} m/s`;
    clima.querySelector(`#direccion`).textContent = `${data['Direccion del viento']}°`;
    clima.querySelector(`#atmosfera`).textContent = `${data['Presion atmosferica']} hPa`;
    icono(clima, `#oIcono`, data.icono);
}

/**
 *  Agrega vuelos a la lista definida en index.html
 * @param {object} datos datos de vuelos especificados
 */
function expoDatos(datos) {
    const ticket = document.querySelector('#ticket');
    const lista = document.querySelector('.listaClimas');

    if (!lista) {
        console.error('Elemento con clase "listaClimas" no encontrado');
        return;
    }

    datos.forEach(vuelo => {
        const li = document.createElement('li');
        li.classList.add('content_vuelo');
        li.dataset.id = vuelo.iata;

        const tClone = ticket.cloneNode(true);
        tClone.classList.add('vuelo_ticket');
        ingresaInfo(tClone, vuelo);

        li.appendChild(tClone);

        const clim = asigna(vuelo);
        clim.style.display = "none"; 
        clim.classList.add("detalles");
        li.appendChild(clim);
        lista.appendChild(li);

        tClone.addEventListener('click', () => desplega(li));
    });
}

/**
 *  Metodo interactivo, despliega y repliega la informacion del clima de origen y destino
 * @param {HTMLElement} li elemento lista de HTML
 */
function desplega(li) {
    const esActivo = li.classList.contains('active');

    document.querySelectorAll('.listaClimas li.active').forEach(item => {
        item.classList.remove('active');
        item.querySelector('.detalles').style.display = 'none';
    });

    if (!esActivo) {
        li.classList.add('active');
        li.querySelector('.detalles').style.display = 'flex';
    }
}

/**
 * Desactiva el boton presionado
 * @param {HTMLElement} boton1 boton a desactivar
 * @param {HTMLElement} boton2 boton a activar
 */
function desBoton(boton1, boton2) {
    boton1.disabled = true;
    boton1.style.backgroundColor =  '#131517';
    boton2.disabled = false;
    boton2.style.backgroundColor = '#1EA7FF';
}

/**
 * Limpia la lista de climas consultados,
 * para que no se repitan.
 */
function clearList() {
    const lista = document.querySelector('.listaClimas');
    lista.innerHTML = '';
}

/**
 * Expone los datos del historial por ciudad-iata
 * @param {object} datos datos del historial
 */
function expoClimas(datos){
    const clima = document.querySelector('#climaCiudad-Iata');
    const lista = document.querySelector('.listaClimas');

    if (!lista) {
        console.error('Elemento con clase "listaClimas" no encontrado');
        return;
    }

    datos.forEach(vuelo => {
        const li = document.createElement('li');
        const tClone = clima.cloneNode(true);
        li.dataset.id = vuelo.id;
        tClone.classList.remove('unica');
        li.classList.add('histClima');
        tClone.style.display = 'flex';
        asignaClim(tClone, vuelo);
        li.appendChild(tClone);
        lista.appendChild(li);
    })
}

/**
 *  Muestra anuncia si no hay historial disponible
 */
function sinHistorial() {
    const lista = document.querySelector('.listaClimas');
    const historial = document.querySelector('.sinHistorial').cloneNode(true);
    const li = document.createElement('li');
    li.classList.add('histClima');
    li.appendChild(historial);
    historial.style.display = 'block';
    lista.appendChild(li);
}







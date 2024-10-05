/**
 * Busca los codigos de errores de tipo error de entrada erronea
 * @param {array} data codigo de datos
 * @returns {boolean} error encontrado
 */
export function buscaError01(data) {
    const Errores = ["500", "101", "103", "104", "105", "106", "107", "109"];
    
    return Errores.includes(data[0]);
}

/**
 * Busca los codigos de errores de tipo error de codigo
 * @param {array} data codigo de error
 * @returns {boolean} error encontrado
 */
export function buscaError02(data) {
    const Errores = ["108", "102", "200", "201", "202", "203", "204", "300", "301", "302"];
    return Errores.includes(data[0]);
}

/**
 * Asigna el ícono de clima respectivo.
 * @param {HTMLElement} clima - Elemento HTML que contiene la información del clima.
 * @param {string} selector - Selector del ícono en HTML.
 * @param {string} idIcono - ID del ícono del JSON.
 */
export function icono(clima, selector, idIcono) {
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
export function dia_o_noche(idIcono) {

    if (idIcono[2] === 'd') {
        return "IconoStyleDay";
    } else if (idIcono[2] === 'n') {
        return "IconoStyleNight";
    } else {
        return "None";
    }
}

/**
 * Maneja la busqueda de vuelos
 * @param {string} url enviada por el servidor
 * @param {function} procesarRespuesta funcion para procesar los datos
 * @param {function} nullError metodo cuando los datos son nulos
 */
export function manejarBusqueda(url, procesarRespuesta, nullError) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); 
        })
        .then(data => {
            if (data) {
                expoErro(data, procesarRespuesta, nullError);
            } else {
                nullError();
            }
        })
        .catch(error => console.error('Error:', error));
}

/**
 * Expone errores en la pagina
 * @param  {string} data codigo de error
 * @param  {function} procesarRespuesta Realiza la accion de respuesta al error
 * @param {function} nullError Muestra error de datos nulo
 */
function expoErro(data, procesarRespuesta, nullError) {
    const errorElement = document.querySelector('.error');
    const apiErrorElement = document.querySelector('.apierror');
    const carga = document.querySelector('.carga');
    const boton1 = document.querySelector('#BSeach1');
    const boton2 = document.querySelector('#BSeach2');

    errorElement.style.display = 'none';
    apiErrorElement.style.display = 'none';

    if (data.length === 0 ) {
        noSpam(boton1, 3000);
        nullError();
    } else if (buscaError01(data)) {
        noSpam(boton1, 3000);
        muestraError1(errorElement, carga, boton1, boton2);
    } else if (buscaError02(data)) {
        noSpam(boton1, 3000);
        muestraError2(apiErrorElement, carga, boton1, boton2);
    } else {
        noSpam(boton1, 7000);
        procesarRespuesta(data);
    }
}

/**
 * Muestra errores generados cuando el usuario ingresa datos erroneos
 * @param {HTMLElement} errorElement etiqueta que muestra el error de respuesta
 * @param {HTMLElement} carga etiqueta que muestra la carga de datos
 * @param {HTMLElement} boton1 que se evitara ser spameado
 * @param {HTMLElement} boton2 que se evitara ser spameado
 */
function muestraError1(errorElement, carga, boton1, boton2){
    carga.style.display = 'none';
    errorElement.style.display = 'block';
    setTimeout(() => {
        boton1.style.backgroundColor = '#1EA7FF';
        boton2.style.backgroundColor = '#1EA7FF';
        boton1.disabled = false;
        boton2.disabled = false;
        }, 3000);
}

/**
 * Muestra errores de api
 * @param {HTMLElement} apiErrorElement etiqueta que muestra el error de api
 * @param {HTMLElement} carga etiqueta que muestra la carga de datos
 * @param {HTMLElement} boton1 que se evitara ser spameado
 * @param {HTMLElement} boton2 que se evitara ser spameado
 */
function muestraError2(apiErrorElement, carga, boton1, boton2) {
    apiErrorElement.style.display = 'block';
    carga.style.display = 'none';
    setTimeout(() => {
        boton1.style.backgroundColor = '#1EA7FF';
        boton2.style.backgroundColor = '#1EA7FF';
        boton1.disabled = false;
        boton2.disabled = false;
        }, 3000);
}

/**
 * Asigna los valores del objeto clima a las etiquetas correspondientes en el front-end.
 * @param {HTMLElement} clima Elemento HTML que contiene las etiquetas del clima.
 * @param {object} data Información del clima proporcionada.
 */
export function asignaClima(clima, data) {
    clima.querySelector(`#ciudad`).textContent = data.Ciudad ? data.Ciudad : 'None';
    clima.querySelector(`#horaFecha`).textContent = `${formFecha()} CST • ${data['Fecha simplificada'] || 'No disponible'}`;
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
 *  Crea la fecha actual en formato requerdio
 * @returns {string} fecha actual en formato "hora:minuto"
 */
function formFecha() {
    const fechaActual = new Date();
    const horas = fechaActual.getHours().toString().padStart(2, '0'); 
    const minutos = fechaActual.getMinutes().toString().padStart(2, '0');
    return `${horas}:${minutos}`;
}

/**
 * Evita el spam en lo botones de busqueda.
 * @param {HTMLElement} boton que sera desactivado por un momento
 * @param {int} tiempo tiempo del boton desactivado
 */
function noSpam(boton,tiempo) {

    if (boton) {
        
        boton.disabled = true;
        boton.style.backgroundColor = "#1E1F25";


        setTimeout(() => {
            boton.style.backgroundColor = '#1EA7FF';
            boton.disabled = false;
        }, tiempo); 
    }
}


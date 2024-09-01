"use strict";

document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-button");
    const ciudadSearchDivs = document.querySelectorAll(".ciudad_search");
    const iataSearchDiv = document.querySelector(".iata_search");
    const boton = document.querySelector("#BSeach");
    const erro = document.querySelector(".error");

    // Verifica si los elementos existen
    if (toggleButton && ciudadSearchDivs.length && iataSearchDiv) {
        toggleButton.addEventListener("click", function () {
            borrarTexto();
            if (iataSearchDiv.style.display === "none" || !iataSearchDiv.style.display) {
                // Mostrar el div "iata_search" y ocultar los "ciudad_search"
                iataSearchDiv.style.display = "block";
                ciudadSearchDivs.forEach(div => div.style.display = "none");
                toggleButton.textContent = "Buscar por IATA";
            } else {
                // Mostrar los divs "ciudad_search" y ocultar el "iata_search"
                iataSearchDiv.style.display = "none";
                ciudadSearchDivs.forEach(div => div.style.display = "block");
                toggleButton.textContent = "Buscar por ciudad";
            }
        });
    }

    // Verifica si el botón existe antes de agregar el evento
    if (boton) {
        boton.addEventListener("click", function() {
            fetch("http://127.0.0.1:5501/plantilla.json") // Ruta al archivo JSON local
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json(); // Parsear JSON y retornar la promesa
                })
                .then(data => {
                    boton.textContent = "Datos cargados"; // Actualiza el texto para indicar que los datos han sido cargados
                    expoDatos(data); // Pasar datos a expoDatos después de que se resuelve la promesa
                })
                .catch(error => {
                    boton.textContent = "Error"; // Actualiza el texto para indicar que ocurrió un error
                    console.error('There has been a problem with your fetch operation:', error);

                    // Verifica si el elemento de error está disponible antes de manipularlo
                    if (erro) {
                        erro.style.display = "block";
                    }
                });
        });
    }
});

// Función para borrar los textos de los inputs
function borrarTexto() {
    const inputs = document.querySelectorAll("input[type='text']");
    inputs.forEach(input => input.value = '');
}

// Expone los datos del JSON en la página web
// Expone los datos del JSON en la página web
function expoDatos(datos) {
    console.log("Datos recibidos:", datos); 
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
        tClone.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
        tClone.querySelector('.iata_vuelos').textContent = vuelo.iata;
        tClone.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

        // Agregar la etiqueta clonada al li
        li.appendChild(tClone);

        // Almacena los detalles del vuelo clonados
        const clim = asigna(vuelo)
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
    console.log("Elemento clima:", clima); // Añadido para depuración

    if (clima) {
        // Clonamos el div de clima y asignamos los valores del JSON
        const cClone = clima.cloneNode(true);
        cClone.classList.add("climas");
        cClone.querySelector('#infoAero_01').textContent = vuelo.origen;
        cClone.querySelector('#info_ciudad01').textContent = `Ciudad ${vuelo.ciudadOr}`;
        cClone.querySelector('#infoHora01').textContent = `Hora: ${vuelo.hrorigen}`;
        cClone.querySelector('#infociudad_01').textContent = vuelo.ciudadOr;
        cClone.querySelector('#infofecha01').textContent = `${vuelo.hrorigen} CST • ${vuelo.fOrigen}`;
        cClone.querySelector('#infClima_01').textContent = vuelo.clima_origen.Clima;
        cClone.querySelector('#infoTemp_01').textContent = vuelo.clima_origen.Temperatura;
        cClone.querySelector('#range01').textContent = `${vuelo.clima_origen.TemperaturaMinima}° - ${vuelo.clima_origen.TemperaturaMaxima}°`;
        cClone.querySelector('#principal01').textContent = `Condición principal: ${vuelo.clima_origen["Descripcion del clima"]}.`;
        cClone.querySelector('#CNubosa01').textContent = `Cobertura nubosa: ${vuelo.clima_origen.Nubosidad}%`;
        cClone.querySelector('#Humedad01').textContent = `Humedad: ${vuelo.clima_origen.Humedad}%`;
        cClone.querySelector('#Termica01').textContent = `Sensación térmica: ${vuelo.clima_origen.Termica01}°`;
        cClone.querySelector('#velocidad01').textContent = `Velocidad del viento: ${vuelo.clima_origen["Velocidad del viento"]} m/s.`;
        cClone.querySelector('#direccion01').textContent = `Dirección del viento: ${vuelo.clima_origen["Direccion del viento"]}`;
        cClone.querySelector('#rafaga01').textContent = `Ráfagas de viento: ${vuelo.clima_origen["Rafagas de viento"]} m/s.`;

        cClone.querySelector('#infoAero_02').textContent = vuelo.destino;
        cClone.querySelector('#info_ciudad02').textContent = `Ciudad ${vuelo.ciudadDes}`;
        cClone.querySelector('#infoHora02').textContent = `Hora: ${vuelo.hrdestino}`;
        cClone.querySelector('#infociudad_02').textContent = vuelo.ciudadDes;
        cClone.querySelector('#infofecha02').textContent = `${vuelo.hrdestino} CST • ${vuelo.fDestino}`;
        cClone.querySelector('#infClima_02').textContent = vuelo.clima_destino.Clima;
        cClone.querySelector('#infoTemp_02').textContent = vuelo.clima_destino.Temperatura;
        cClone.querySelector('#range02').textContent = `${vuelo.clima_destino.TemperaturaMinima}° - ${vuelo.clima_destino.TemperaturaMaxima}°`;
        cClone.querySelector('#principal02').textContent = `Condición principal: ${vuelo.clima_destino["Descripcion del clima"]}.`;
        cClone.querySelector('#CNubosa02').textContent = `Cobertura nubosa: ${vuelo.clima_destino.Nubosidad}%`;
        cClone.querySelector('#Humedad02').textContent = `Humedad: ${vuelo.clima_destino.Humedad}%`;
        cClone.querySelector('#Termica02').textContent = `Sensación térmica: ${vuelo.clima_destino.Termica01}°`;
        cClone.querySelector('#velocidad02').textContent = `Velocidad del viento: ${vuelo.clima_destino["Velocidad del viento"]} m/s.`;
        cClone.querySelector('#direccion02').textContent = `Dirección del viento: ${vuelo.clima_destino["Direccion del viento"]}`;
        cClone.querySelector('#rafaga02').textContent = `Ráfagas de viento: ${vuelo.clima_destino["Rafagas de viento"]} m/s.`;

        cClone.style.display = "none";
        cClone.classList.add("detalles");
        return cClone;
    }
    return document.createElement('div'); // Retorna un elemento vacío si 'informacion' no existe
}


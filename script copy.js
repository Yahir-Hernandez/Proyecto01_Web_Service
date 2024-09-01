
"use strict";

//Evento para cambiar el tipo de busqueda que se desea hacer
document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-button");
    const ciudadSearchDivs = document.querySelectorAll(".ciudad_search");
    const iataSearchDiv = document.querySelector(".iata_search");

    toggleButton.addEventListener("click", function() {
        borrarTexto();
        if (iataSearchDiv.style.display === "none") {
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
});

//Funcion para borrar los testos de los inputs
function borrarTexto() {
    const inputs = document.querySelectorAll("input[type='text']");
    inputs.forEach(input => input.value = '');
}

//Funcion para cargar los datos de un json 
function cargaJson() {
    fetch('vuelo_MTX_MEX.json') // Ruta al archivo JSON local
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Parsear JSON y retornar la promesa
    })
    .then(data => {
        expoDatos(data); // Pasar datos a expoDatos después de que se resuelve la promesa
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

//Expone los datos del json en la pagina web
function expoDatos(datos) {
    const ticket = document.getElementById('ticket');

    const lista = document.querySelector('.listaVuelo');

    datos.forEach( vuelo => {
        const li = document.createElement('li');
        li.classList.add('.content_vuelo');

        //Clona el formato del ticket 
        const tClone = ticket.cloneNode(true);
        tClone.classList.add('.vuelo_card');
        tClone.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
        tClone.querySelector('.iata_vuelos').textContent = vuelo.iata;
        tClone.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

        //Agregar la etiqueta clonada al li
        li.appendChild(tClone);
        li.dataset.id = vuelo.iata; // Almacena el ID del objeto

        li.appendChild(asigna(vuelo));
        lista.append(li);

        // Añadir el evento de clic para desplegar/ocultar detalles
        li.addEventListener('click', function() {
            const esActivo = li.classList.contains('active');
            
            // Cerramos cualquier otra sección abierta
            document.querySelectorAll('#listaObjetos li').forEach(item => {
                item.classList.remove('active');
            });

            // Desplegar detalles si no estaba activo, si estaba activo lo oculta
            if (!esActivo) {
                li.classList.add('active');
            }
        });
    });
}

//Asigna valores del json a las etiquetas que muestran en front
function asigna(vuelo) {
    const clima = document.getElementById('informacion');

    // Creamos un div para los detalles, inicialmente oculto
    const cClone = clima.cloneNode(true);
    cClone.classList.add("climas");
    cClone.getElementById('infoAero_01').textContent = vuelo.origen;
    cClone.getElementById('info_ciudad01').textContent = `Ciudad ${vuelo.ciudadOr}`;
    cClone.getElementById('infoHora01').textContent = `Hora: ${vuelo.hrorigen}`;
    cClone.getElementById('infociudad_01').textContent = vuelo.ciudadOr;
    cClone.getElementById('infofecha01').textContent = `${vuelo.hrorigen} CST • ${vuelo.fOrigen}`;
    cClone.getElementById('infClima_01').textContent = vuelo.clima_origen.Clima;
    cClone.getElementById('infoTemp_01').textContent = vuelo.clima_origen.Temperatura;
    cClone.getElementById('range01').textContent = `${vuelo.clima_origen.TemperaturaMinima}° - ${vuelo.clima_origen.TemperaturaMaxima}°`;
    cClone.getElementById('principal01').textContent = `Condición principal: ${vuelo.clima_origen["Descripción del clima"]}.`;
    cClone.getElementById('CNubosa01').textContent = `Cobertura nubosa: ${vuelo.clima_origen.Nubosidad}%`;
    cClone.getElementById('Humedad01').textContent = `Humedad: ${vuelo.clima_origen.Humedad}%`;
    cClone.getElementById('Termica01').textContent = `Sensación térmica: ${vuelo.clima_origen.Termica01}°`;
    cClone.getElementById('velocidad01').textContent = `Velocidad del viento: ${vuelo.clima_origen["Velocidad del viento"]} m/s.`;
    cClone.getElementById('direccion01').textContent = `Dirección del viento: ${vuelo.clima_origen["Dirección del viento"]}`;
    cClone.getElementById('rafaga01').textContent = `Ráfagas de viento: ${vuelo.clima_origen["Rafagas de viento"]} m/s.`;

    cClone.getElementById('infoAero_02').textContent = vuelo.destino;
    cClone.getElementById('info_ciudad02').textContent = `Ciudad ${vuelo.ciudadDes}`;
    cClone.getElementById('infoHora02').textContent = `Hora: ${vuelo.hrdestino}`;
    cClone.getElementById('infociudad_02').textContent = vuelo.ciudadDes;
    cClone.getElementById('infofecha02').textContent = `${vuelo.hrdestino} CST • ${vuelo.fDestino}`;
    cClone.getElementById('infClima_02').textContent = vuelo.clima_destino.Clima;
    cClone.getElementById('infoTemp_02').textContent = vuelo.clima_destino.Temperatura;
    cClone.getElementById('range02').textContent = `${vuelo.clima_destino.TemperaturaMinima}° - ${vuelo.clima_destino.TemperaturaMaxima}°`;
    cClone.getElementById('principal02').textContent = `Condición principal: ${vuelo.clima_destino["Descripción del clima"]}.`;
    cClone.getElementById('CNubosa02').textContent = `Cobertura nubosa: ${vuelo.clima_destino.Nubosidad}%`;
    cClone.getElementById('Humedad02').textContent = `Humedad: ${vuelo.clima_destino.Humedad}%`;
    cClone.getElementById('Termica02').textContent = `Sensación térmica: ${vuelo.clima_destino.Termica01}°`;
    cClone.getElementById('velocidad02').textContent = `Velocidad del viento: ${vuelo.clima_destino["Velocidad del viento"]} m/s.`;
    cClone.getElementById('direccion02').textContent = `Dirección del viento: ${vuelo.clima_destino["Dirección del viento"]}`;
    cClone.getElementById('rafaga02').textContent = `Ráfagas de viento: ${vuelo.clima_destino["Rafagas de viento"]} m/s.`;

    // Retorna el elemento clonado con la información asignada
    return cClone;
}

//



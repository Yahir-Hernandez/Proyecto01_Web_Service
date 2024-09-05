"use strict";

document.addEventListener("DOMContentLoaded", function () {
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

    /*/ Verifica si el botón existe antes de agregar el evento
    if (boton) {
        boton.addEventListener("click", function() {
            borra_list();
            fetch('http://127.0.0.1:5000/templates/plantilla.json') // Ruta al archivo JSON local
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json(); // Parsear JSON y retornar la promesa
                })
                .then(data => {
                    consulta(data);
                })
                .catch(error => {
                    boton.textContent = "Error"; // Actualiza el texto para indicar que ocurrió un error

                    // Verifica si el elemento de error está disponible antes de manipularlo
                    if (erro) {
                        erro.style.display = "block";
                    }
                });
            borrarTexto();
        });
    }*/

    /*document.getElementById('BSeach').addEventListener('click', function(event) {
        event.preventDefault();

        let ciudad = document.getElementById('ciudad-input').value;
        let destino = document.getElementById('airline-input').value;

        fetch(`/search?ciudad=${encodeURIComponent(ciudad)}&destino=${encodeURIComponent(destino)}`)
            .then(response => response.text())
            .then(data => {
                console.log(data); // Aquí puedes actualizar el DOM con la respuesta
            })
            .catch(error => console.error('Error:', error));
    });*/

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
        })
        .catch(error => console.error('Error:', error));
    });

    document.getElementById('BSeach2').addEventListener('click', function(event) {
        event.preventDefault(); // Evita el envío tradicional del formulario

        let codigoVuelo = document.getElementById('iata-input').value;

        fetch(`/search?iata=${encodeURIComponent(codigoVuelo)}`)
            .then(response => response.text())
            .then(data => {
                console.log(data); // Aquí puedes actualizar el DOM con la respuesta
            })
            .catch(error => console.error('Error:', error));

        // Si deseas enviar el formulario al servidor, puedes hacerlo con fetch o similar
        this.click(); // Opcionalmente puedes enviar el formulario después de la lógica
    });
});

// Función para borrar los textos de los inputs
function borrarTexto() {
    const inputs = document.querySelectorAll("input[type='text']");
    inputs.forEach(input => input.value = '');
}

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
        cClone.querySelector('#direccion01').textContent = `Dirección del viento: ${vuelo.clima_origen["Direccion del viento"]}°`;
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
        cClone.querySelector('#direccion02').textContent = `Dirección del viento: ${vuelo.clima_destino["Direccion del viento"]}°`;
        cClone.querySelector('#rafaga02').textContent = `Ráfagas de viento: ${vuelo.clima_destino["Rafagas de viento"]} m/s.`;

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
    
    ticket.querySelector('.ciudadOr').textContent = vuelo.ciudadOr;
    ticket.querySelector('.iata_vuelos').textContent = vuelo.iata;
    ticket.querySelector('.ciudadDes').textContent = vuelo.ciudadDes;

    clima.replaceWith(copia);

    ticket.classList.remove('vuelo_ticket');
    ticket.classList.add('copia');
    info.style.display = "block";
}

function consulta(data) {

    if (data.length > 1) {
        expoDatos(data);
    } else {
        expoElem(data);
    }
}

//Funcion temporal de prueba
function direc() {
    const input = prompt("Por favor, ingresa el número:");

    if (input != 1) {
        return "http://127.0.0.1:5501/plantilla.json";
    } 

    return "http://127.0.0.1:5501/solo.json";
}

/**
 * Array de sugerencias de ciudades y códigos IATA.
 * @type {string[]}
 */
let suggestions = [
    "TLC", "Toluca", "MTY", "Monterrey", "MEX", "Ciudad de México", "TAM", "Tampico",
    "GDL", "Guadalajara", "CJS", "Ciudad Juárez", "CUN", "Cancún", "TIJ", "Tijuana",
    "HMO", "Hermosillo", "CME", "Ciudad del Carmen", "MID", "Mérida", "CTM", "Chetumal",
    "VER", "Veracruz", "OAX", "Oaxaca", "HUX", "Huatulco", "PVR", "Puerto Vallarta",
    "PXM", "Puerto Escondido", "ACA", "Acapulco", "ZIH", "Ixtapa-Zihuatanejo",
    "AGU", "Aguascalientes", "VSA", "Villahermosa", "CZM", "Cozumel", "CUU", "Chihuahua",
    "TRC", "Torreón", "QRO", "Querétaro", "BJX", "Guanajuato", "PBC", "Puebla",
    "SLP", "San Luis Potosí", "ZCL", "Zacatecas", "LIM", "Lima", "HAV", "La Habana",
    "BOG", "Bogotá", "MIA", "Miami", "LAX", "Los Ángeles", "JFK", "Nueva York",
    "MZT", "Mazatlán", "GUA", "Ciudad de Guatemala", "BZE", "Belice", "DFW", "Dallas/Fort Worth",
    "ORD", "Chicago", "PHX", "Phoenix", "PHL", "Filadelfia", "CLT", "Charlotte",
    "YYZ", "Toronto", "IAH", "Houston", "YVR", "Vancouver", "CDG", "París",
    "AMS", "Ámsterdam", "ATL", "Atlanta", "CEN", "Ciudad Obregón", "MAD", "Madrid",
    "SCL", "Santiago de Chile", "AUS", "Austin", "EZE", "Buenos Aires", "BOS", "Boston",
    "CPE", "Campeche", "CUL", "Culiacán", "DEN", "Denver", "DTW", "Detroit", "DXB", "Dubái",
    "DGO", "Durango", "IST", "Estambul", "FRA", "Frankfurt", "LAP", "La Paz", "LAS", "Las Vegas",
    "BJX", "León/Bajío", "LMM", "Los Mochis", "MGA", "Managua", "ZLO", "Manzanillo",
    "MAM", "Matamoros", "MDE", "Medellín", "MXL", "Mexicali", "MTT", "Minatitlán",
    "MSP", "Minneapolis", "YUL", "Montreal", "EWR", "Newark", "NLD", "Nuevo Laredo",
    "OAK", "Oakland", "MCO", "Orlando", "PTY", "Panamá", "RDU", "Raleigh",
    "REX", "Reynosa", "FCO", "Roma", "SAT", "San Antonio", "SFO", "San Francisco",
    "SAL", "San Salvador", "SLC", "Salt Lake City", "SJO", "San José", "GRU", "São Paulo",
    "SEA", "Seattle", "ICN", "Seúl", "SZX", "Shenzhen", "SJD", "San José del Cabo",
    "SDQ", "Santo Domingo", "TPA", "Tampa", "TAP", "Tapachula", "TPQ", "Tepic",
    "NRT", "Tokio", "TGZ", "Tuxtla Gutiérrez", "DCA", "Washington D.C."
];

/**
 * Selecciona el contenedor de búsqueda y el input de búsqueda.
 * @type {HTMLElement}
 */
const searchContainer = document.querySelector('.search-container');

/**
 * Selecciona el input de búsqueda.
 * @type {HTMLInputElement}
 */
const inputSearch = searchContainer.querySelector('input');

/**
 * Selecciona el contenedor de sugerencias.
 * @type {HTMLElement}
 */
const boxSuggestions = document.querySelector('.container-suggestions');

/**
 * Evento 'keyup' que maneja la lógica de filtrado y sugerencias para el input de búsqueda.
 * @param {Event} e - El evento de teclado.
 */
inputSearch.onkeyup = e => {
    let userData = e.target.value; // Obtiene el valor ingresado por el usuario
    let emptyArray = [];

    if (userData) {
        // Filtra las sugerencias que comienzan con el valor ingresado por el usuario.
        emptyArray = suggestions.filter(data => {
            return data
                .toLocaleLowerCase()
                .startsWith(userData.toLocaleLowerCase());
        });

        // Aplica estilo a las sugerencias.
        styleSuggestions(emptyArray);

        // Convierte las sugerencias filtradas en elementos <li>.
        emptyArray = emptyArray.map(data => {
            boxSuggestions.style.border = '2px solid #1DA7FF'; // Aplica un borde cuando hay sugerencias.
            return `<li>${data}</li>`;
        });

        // Añade la clase 'active' al contenedor de búsqueda.
        searchContainer.classList.add('active');
        // Muestra las sugerencias en el contenedor.
        showSuggestions(emptyArray);

        // Añade un evento 'onclick' a cada elemento <li>.
        let allList = boxSuggestions.querySelectorAll('li');
        allList.forEach(li => {
            li.setAttribute('onclick', 'select(this)');
        });
    } else {
        boxSuggestions.style.border = 'none'; // Elimina el borde cuando no hay sugerencias.
        searchContainer.classList.remove('active'); // Remueve la clase 'active' si no hay datos.
    }
};

/**
 * Función para seleccionar una sugerencia.
 * @param {HTMLElement} element - El elemento <li> seleccionado.
 */
function select(element) {
    let selectUserData = element.textContent; // Obtiene el texto de la sugerencia seleccionada.
    inputSearch.value = selectUserData; // Asigna el valor seleccionado al input de búsqueda.
    searchContainer.classList.remove('active'); // Remueve la clase 'active' al seleccionar una sugerencia.
    boxSuggestions.style.border = 'none'; // Elimina el borde del contenedor de sugerencias.
}

/**
 * Muestra las sugerencias en el contenedor de sugerencias.
 * @param {string[]} list - La lista de sugerencias a mostrar.
 */
const showSuggestions = list => {
    let listData;

    if (!list.length) {
        let userValue = inputSearch.value;
        listData = `<li>${userValue}</li>`; // Si no hay sugerencias, muestra el valor del input.
    } else {
        listData = list.join(' '); // Junta las sugerencias en una sola cadena.
        boxSuggestions.style.border = '2px solid #1DA7FF'; // Aplica un borde cuando hay sugerencias.
    }
    boxSuggestions.innerHTML = listData; // Asigna las sugerencias al contenedor de sugerencias.
};

/**
 * Aplica estilos al contenedor de sugerencias en función de si hay sugerencias o no.
 * @param {string[]} emptyArray - La lista filtrada de sugerencias.
 */
function styleSuggestions(emptyArray) {
    if (emptyArray.length === 0) {
        boxSuggestions.style.border = '2px solid #1DA7FF'; // Aplica un borde si no hay sugerencias.
    } else {
        boxSuggestions.style.border = 'none'; // Elimina el borde si hay sugerencias.
    }
}
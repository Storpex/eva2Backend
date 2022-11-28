// ========================== DARK-MODE ========================== //

/**
 * Esta funcion lo que hace es que al apretar el boton (en este caso seria un anchor, pero lo estamos usando de boton) con la id 'switch-mode',
 * al hacerle click se ejecutara una funcion, que donde en la etiqueta de body, se le agregara una clase llamada 'dark-mode'.
 * En donde en el archivo style.css, tiene por defecto unos paramentos, donde al tener una clase llamada 'dark-mode', se colocara el modo oscuro.
 * Esto modificara el estilo visual y se le cambiara el fondo a uno mas oscuro y las letras a blanco para hacer el contraste y puedan leerse.
 */
const BODY_OSCURO = document.getElementById('switch-mode');
BODY_OSCURO.onclick = function(){
    document.body.classList.toggle('dark-mode');
};

// ========================== AUMENTAR FONT-SIZE ========================== //

/**
 * Esta funcion lo que hace es que al apretar el boton (en este caso seria un anchor, pero lo estamos usando de boton) con la id 'font-plus',
 * al hacerle click se ejecutara una funcion, que donde en la etiqueta de body, se le agregara una clase llamada 'add-font'.
 * En donde en el archivo style.css, tiene por defecto unos paramentos, donde al tener una clase llamada 'add-font', aumentara el fontsize unos pixeles.
 * Esto modificara el estilo visual y se agrandara las letras.
 */
const PLUSFONT = document.getElementById('font-plus');
PLUSFONT.onclick = function(){
    document.body.classList.toggle('add-font');
};
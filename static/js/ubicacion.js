
function comenzar(){
    let miBoton = document.getElementById("dame_ubicacion");

    miBoton.addEventListener("click", obtener, false);
}

function obtener(){

    let parametros = {enableHighAccuracy: true, timeout:10000, maximumAge: 60000};
    navigator.geolocation.getCurrentPosition(mostrar_posicion, gestion_errores, parametros);
}

function mostrar_posicion(posicion){

    let ubicacion = document.getElementById("ubicacion");
    
    //let miUbicacion = "";

    // miUbicacion += "Latitud: " + posicion.coords.latitude + "<br>";
    // miUbicacion += "Longitud: " + posicion.coords.longitude + "<br>";
    // miUbicacion += "Exactitud: " + posicion.coords.accuracy + "<br>";

    let miMapa = "https://www.openstreetmap.org/export/embed.html?bbox=" + posicion.coords.longitude + "%2C" + posicion.coords.latitude + "%2C" + posicion.coords.longitude + "%2C" + posicion.coords.latitude + "&amp;layer=mapnik&amp;marker=" + posicion.coords.latitude + "%2C" + posicion.coords.longitude ;
    let miMapa2 = "https://www.openstreetmap.org/?mlat=" + posicion.coords.latitude + "&amp;mlon=" + posicion.coords.longitude + "#map=14/" + posicion.coords.latitude + "/" + posicion.coords.longitude;
    
    ubicacion.innerHTML = "<iframe width='100%' height='380' frameborder='0' scrolling='no' marginheight='0' marginwidth='0'  src='" +miMapa +"' style ='border: 1px solid black' ></iframe><br/><small><a href='" +miMapa2 + "'>Ver mapa más grande</a></small>" ;

}

function gestion_errores(error){
    alert("Ha ocurrido un error, " + error.code + " "+ error.message);
    if(error.code == 1){
        alert("Debes permitir el uso de la geolocalizacion en tu navegador")
    }else if(error.code == 2){
        alert("Ubicacion no disponible, intente más tarde")
    }else if(error.code == 3){
        alert("El tiempo para detectar la ubicacion ha sido excedido")
    }else{
        alert("Ni idea de que ha pasado aqui")
    }
}

window.addEventListener("load", comenzar, false);
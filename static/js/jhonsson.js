/**
 * Created with PyCharm.
 * User: Jhonsson
 * Date: 12/10/14
 * Time: 12:05 AM
 * To change this template use File | Settings | File Templates.
 */


function newUrl(url) {
    window.location.assign(url);
}

function envioRecepcionAjax(url, params)
{
    ajaxPost(url, params, function(content){
        //onSuccess
        castear(content);
    });
}

function hora()
{
    var  dia = new Date();
    var  hora = dia.getHours();
    var  minutos = dia.getMinutes();
    var  segundos = dia.getSeconds();

    var meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
    var diasSemana = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"];

    if ((hora >= 0)&&(hora <= 9)){
        hora="0"+hora;
    }

    if ((minutos >= 0)&&(minutos <= 9)){
        minutos="0"+minutos;
    }

    if ((segundos >= 0)&&(segundos <= 9)){
        segundos="0"+segundos;
    }

    document.getElementById("hora").
        innerHTML =  " "  + hora + ":" + minutos + ":" + segundos;
    document.getElementById("fecha").
        innerHTML =  " "  + diasSemana[dia.getDay()] + ", " + dia.getDate() + ". " + meses[dia.getMonth()]+" "+dia.getFullYear();

    window.setTimeout("hora()",1000);
}
document.getElementById('nav').style.opacity = '0';
document.getElementById('menu').addEventListener('click', e=> {
    if (document.getElementById('nav').style.opacity == "0") {
        document.getElementById('nav').style.opacity = "1";
        document.getElementById('nav').style.marginTop = "10px";
    }
    else {
        document.getElementById('nav').style.opacity = '0';
        document.getElementById('nav').style.marginTop = "-400px";
    }
})

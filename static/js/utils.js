// Helper function
function sendHttpRequest(ipAdress) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", ipAdress, false);
    try {
        xhttp.send();
    } catch (error) {
        console.log(error)
        return false;
    }
    return xhttp;
}
const ipAdress = "http://10.10.0.87:5000/"

if (checkCameraConnection()) {
    setInterval(fetchPhoto, 200)
}

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


function checkCameraConnection() {
    var xhttp = sendHttpRequest(ipAdress)
    if (xhttp.status === 200) {
        return true;
    } else {
        return false;
    }
}

// Live feed
function fetchPhoto(){
    var ip = ipAdress.concat("take_photo")
    var xhttp = sendHttpRequest(ip)

    var json_response = JSON.parse(xhttp.responseText);
    photo = json_response.image_org_b64;

    document.getElementById('image').src = photo;
}

// Take photo predict button
function takePhotoPredict() {
    var ip = ipAdress.concat("take_photo_and_predict")
    var xhttp = sendHttpRequest(ip)

    var json_response = JSON.parse(xhttp.responseText);
    photo = json_response.image_pred_b64;
    score = json_response.score;
    thresh = json_response.thresh;

    document.getElementById('canvas').src = photo;
    document.getElementById('score').src = score;
    document.getElementById('thresh').src = thresh;
}

// Save photo predict button
function saveImage() {
    var ip = ipAdress.concat("save_photo")
    var xhttp = sendHttpRequest(ip)

    // Display response alert
    if (xhttp.status === 200) {
        var alert = document.getElementById("saved_image_success_alert");
        // Add filename to alert
        var txt = document.getElementById("saved_image_success_alert_text");
        txt.textContent = xhttp.responseText;
        
        alert.style.display = "block";
        setTimeout(function() {
            alert.style.display = "none";
        }, 2500);
        
    } else {
        var alert = document.getElementById("saved_image_failed");

        alert.style.display = "block";
        setTimeout(function() {
            alert.style.display = "none";
        }, 2500);
    }
}



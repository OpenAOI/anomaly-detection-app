
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

// Live feed
function updateCrop(){
    var input_field_x1 = document.getElementById("input_x1");
    var input_field_x2 = document.getElementById("input_x2");
    var input_field_y1 = document.getElementById("input_y1");
    var input_field_y2 = document.getElementById("input_y2");

    x1 = input_field_x1.value;
    x2 = input_field_x2.value;
    y1 = input_field_y1.value;
    y2 = input_field_y2.value;

    var adress = "update_crop" + "?x_1=" + x1 + "&x_2=" + x2 + "&y_1=" + y1 + "&y_2=" + y2;
    var ip = ipAdress.concat(adress);
    var xhttp = sendHttpRequest(ip);

    //var json_response = JSON.parse(xhttp.responseText);
    if (xhttp.status === 200) {
        window.location.href = '/edit/take_photo';
        return true;
    }
}




/*
// Predict image button
function takePhotoPredict() {
    var ip = ipAdress.concat("take_photo_and_predict")
    var xhttp = sendHttpRequest(ip)

    var json_response = JSON.parse(xhttp.responseText);
    photo = json_response.image_pred_b64;
    score = json_response.score;
    thresh = json_response.thresh;

    document.getElementById('canvas').src = photo;
    document.getElementById('score-data').innerHTML = score;
    document.getElementById('thresh-data').innerHTML = thresh;
}

// Save photo to train
function savePhoto() {
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
        
    } 
    
    else {
        var alert = document.getElementById("saved_image_failed");

        alert.style.display = "block";
        setTimeout(function() {
            alert.style.display = "none";
        }, 2500);
    }
    
}

function updateCrop(){
    var input_field_x1 = document.getElementById("input_x1");
    var input_field_x2 = document.getElementById("input_x2");
    var input_field_y1 = document.getElementById("input_y1");
    var input_field_y2 = document.getElementById("input_y2");

    x1 = input_field_x1.value;
    x2 = input_field_x2.value;
    y1 = input_field_y1.value;
    y2 = input_field_y2.value;

    var adress = "update_crop" + "?x_1=" + x1 + "&x_2=" + x2 + "&y_1=" + y1 + "&y_2=" + y2;
    var ip = ipAdress.concat(adress);
    var xhttp = sendHttpRequest(ip);

    //var json_response = JSON.parse(xhttp.responseText);
    if (xhttp.status === 200) {
        window.location.href = '/edit/take_photo';
        return true;
    }
}
*/
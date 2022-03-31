$(document).ready(function(){
    // Load images to gallery grid
    //loadImageGallery();
    
    // Show modal when click
    $("#img1").click(function(){
        $("#imgModal").attr("src", $(this).attr('src'));
        $("#modal").css("display", "block");
    });
    // Hide modal when click on image
    $("#modal").click(function(){
        $("#modal").css("display", "none");
    });
    // Hide modal on X button
    $$(".close:eq(0)").click(function(){
        $("#modal").css("display", "none");
    });
});

function loadImageGallery() {
    var ip = ipAdress.concat("get_all_project_images");
    var xhttp = sendHttpRequest(ip);

    var json_response = JSON.parse(xhttp.responseText);
    var images = json_response.images;

    // List projects in html
    for (var i = 0; i < images.length; i++) {
        document.getElementById("imgGallery").innerHTML += 
        '<div class="thumbnail" style="width: 150px;">' +
        '<div class="item">' +
        '<img src="' + images[i].image_b64 + '" alt="' + images[i].name + '" id="myImg">' +
        '<div class="caption">' +
        '<span class="right">Delete</span><span class="left">View</span>​' +
        '<p style="text-align:left;"><a href="#" onclick="displayImage()">View</a></p>' +
        '</div>' +
        '</div>' +
        '</div>';
    }
}


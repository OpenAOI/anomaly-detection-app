// Crop info to be sent to server
var x1;
var x2;
var y1;
var y2;

var minCroppedWidth = 150;

window.onload = function () {
    'use strict';
    
    // Sliders + input fields
    var slider_h = document.getElementById("slider_h");
    var slider_v = document.getElementById("slider_v");
    var slider_size = document.getElementById("slider_size");
    var input_field_v = document.getElementById("input_v");
    var input_field_h = document.getElementById("input_h");
    var input_field_size = document.getElementById("input_size");
    // Image to crop
    const imageCrop = document.getElementById('image-crop');
    const imagePreview = document.getElementById('preview-crop');

    var Cropper = window.Cropper;

    var options = {
    autoCrop: false,
    viewMode: 1, // zoom as free
    guides: false,  // hide guid lines
    dragMode: 'none',  // dragging mode of cropper
    movable: false,  // enable image move
    cropBoxMovable: true,  // crop box move disable
    cropBoxResizable: false,  // crop box resize disable
    zoomOnWheel: false,  // scroll zoom
    aspectRatio: 1,
    preview: imagePreview,
    ready: function (e) {
        console.log(e.type);
        this.cropper.crop();

        // Update global crop data
        var data = cropper.getData();
        x1 = data["x"];
        x2 = data["x"] + data["width"];
        y1 = data["y"];
        y2 = data["y"] + data["height"];
    },
    cropstart: function (e) {
        console.log(e.type, e.detail.action);
    },
    cropmove: function (e) {
        console.log(e.type, e.detail.action);
    },
    cropend: function (e) {
        console.log(e.type, e.detail.action);
    },
    crop: function (e) {
        console.log(e.type);
        var data = e.detail;

        if (data.width < minCroppedWidth) {
          cropper.setData({"width": minCroppedWidth});
        }

        // Update sliders + input fields
        input_field_h.value = Math.round(data.x);
        input_field_v.value = Math.round(data.y);
        input_field_size.value = Math.round(data.width);

        slider_h.value = Math.round(data.x);
        slider_v.value = Math.round(data.y);
        slider_size.value = Math.round(data.width);

        // Update global crop data
        x1 = data["x"];
        x2 = data["x"] + data["width"];
        y1 = data["y"];
        y2 = data["y"] + data["height"];
    },
    zoom: function (e) {
        console.log(e.type, e.detail.ratio);
    }
    };

    const cropper = new Cropper(imageCrop, options);


    // Create link between sliders and input fields
    // Horizontal
    slider_h.oninput = function() {
      input_field_h.value = this.value;
      cropper.setData({"x": parseInt(this.value)});
      console.log(cropper.getData());
    },
      input_field_h.oninput = function() {
      slider_h.value = this.value;
      cropper.setData({"x": parseInt(this.value)});
    }

    // Vertical
    slider_v.oninput = function() {
      input_field_v.value = this.value;
      cropper.setData({"y": parseInt(this.value)});
    },
    input_field_v.oninput = function() {
      slider_v.value = this.value;
      cropper.setData({"y": parseInt(this.value)});
    }

    // Size
    slider_size.oninput = function() {
      input_field_size.value = this.value;
      cropper.setData({"width": parseInt(this.value), "height": parseInt(this.value)});
      
    },
    input_field_size.oninput = function() {
        slider_size.value = this.value;
        cropper.setData({"width": parseInt(this.value), "height": parseInt(this.value)});
    }
  
};

function updateCrop(){
  var adress = "update_crop" + "?x_1=" + parseInt(x1) + "&x_2=" + parseInt(x2) + "&y_1=" + parseInt(y1) + "&y_2=" + parseInt(y2);
  var adress2 = window.location.search.replace("?", "&");
  var ip = ipAdress.concat(adress + adress2);
  var xhttp = sendHttpRequest(ip);

  if (xhttp.status === 200) {
      window.location.href = '/edit/take_photo' + window.location.search;
  }
}

$("#save-crop-btn").click(function(){
  updateCrop();
})

window.onload = function () {
    'use strict';
  
    var Cropper = window.Cropper;

    // Sliders + input fields
    var slider_x1 = document.getElementById("slider_x1");
    var slider_x2 = document.getElementById("slider_x2");
    var slider_y1 = document.getElementById("slider_y1");
    var slider_y2 = document.getElementById("slider_y2");
    var input_field_x1 = document.getElementById("input_x1");
    var input_field_x2 = document.getElementById("input_x2");
    var input_field_y1 = document.getElementById("input_y1");
    var input_field_y2 = document.getElementById("input_y2");

    const imageCrop = document.getElementById('image-crop');

    var options = {
    autoCrop: false,
    viewMode: 1,                // zoom as free
    guides: false,              // hide guid lines
    dragMode: 'move',           // dragging mode of cropper
    movable: false,              // enable image move
    cropBoxMovable: true,      // crop box move disable
    cropBoxResizable: true,    // crop box resize disable
    zoomOnWheel: false,
    ready: function (e) {
        console.log(e.type);
        this.cropper.crop();
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

        // Update sliders + input fields
        input_field_x1.value = Math.round(data.x);
        input_field_x2.value = Math.round(data.x + data.width);
        input_field_y1.value = Math.round(data.y);
        input_field_y2.value = Math.round(data.y + data.height);

        slider_x1.value = Math.round(data.x);
        slider_x2.value = Math.round(data.x + data.width);
        slider_y1.value = Math.round(data.y);
        slider_y2.value = Math.round(data.y + data.height);
    },
    zoom: function (e) {
        console.log(e.type, e.detail.ratio);
    }
    };
    const cropper = new Cropper(imageCrop, options);

    // Create link between sliders and input fields

    // Slider x1
    slider_x1.oninput = function() {
    input_field_x1.value = this.value;

    },
    input_field_x1.oninput = function() {
    slider_x1.value = this.value;
    },

    // Slider x2
    slider_x2.oninput = function() {
    input_field_x2.value = this.value;
    },
    input_field_x2.oninput = function() {
    slider_x2.value = this.value;
    },

    // Slider y1
    slider_y1.oninput = function() {
    input_field_y1.value = this.value;
    },
    input_field_y1.oninput = function() {
    slider_y1.value = this.value;
    },

    // Slider y2
    slider_y2.oninput = function() {
    input_field_y2.value = this.value;
    },
    input_field_y2.oninput = function() {
    slider_y2.value = this.value;
    }

};

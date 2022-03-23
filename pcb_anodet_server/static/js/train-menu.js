window.addEventListener('load', function () {
    moveEditMenu();
})

function moveEditMenu() {
    path = window.location.pathname;

    var cropCameraText = document.querySelector("#camera-crop-text");
    var takePhotoText = document.querySelector("#take-photo-text");
    var viewImagesText = document.querySelector("#view-images-text");
    var trainProjectText = document.querySelector("#train-project-text");


    if (path.startsWith("/edit/crop_camera")) {
        console.log(1)
        cropCameraText.style.fontSize = "14px";
        cropCameraText.style.fontWeight = "bold";
        cropCameraText.style.opacity = 1;
    }

    if (path.startsWith("/edit/take_photo")) {
        console.log(1)
        takePhotoText.style.fontSize = "14px";
        takePhotoText.style.fontWeight = "bold";
        takePhotoText.style.opacity = 1;
    }

    if (path.startsWith("/edit/view_images")) {
        console.log(1)
        viewImagesText.style.fontSize = "14px";
        viewImagesText.style.fontWeight = "bold";
        viewImagesText.style.opacity = 1;
    }

    if (path.startsWith("/edit/train_project")) {
        console.log(1)
        trainProjectText.style.fontSize = "14px";
        trainProjectText.style.fontWeight = "bold";
        trainProjectText.style.opacity = 1;
    }
}
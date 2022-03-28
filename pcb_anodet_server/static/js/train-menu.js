window.addEventListener('load', function () {
    moveEditMenu();
})

function moveEditMenu() {
    path = window.location.pathname;

    var cropCameraText = document.querySelector("#camera-crop-text");
    var takePhotoText = document.querySelector("#take-photo-text");
    var viewImagesText = document.querySelector("#view-images-text");
    var trainProjectText = document.querySelector("#train-project-text");

    if (path.startsWith("/edit/crop_camera")) 
    {
        cropCameraText.style.fontSize = "14px";
        cropCameraText.style.fontWeight = "bold";
        cropCameraText.style.opacity = 1;
    } 
    else if (path.startsWith("/edit/take_photo")) 
    {
        takePhotoText.style.fontSize = "14px";
        takePhotoText.style.fontWeight = "bold";
        takePhotoText.style.opacity = 1;
    } 
    else if (path.startsWith("/edit/view_images")) 
    {
        viewImagesText.style.fontSize = "14px";
        viewImagesText.style.fontWeight = "bold";
        viewImagesText.style.opacity = 1;
    } 
    else if (path.startsWith("/edit/train_project")) 
    {
        trainProjectText.style.fontSize = "14px";
        trainProjectText.style.fontWeight = "bold";
        trainProjectText.style.opacity = 1;
    }
}
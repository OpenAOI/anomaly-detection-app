window.addEventListener('load', function () {
    moveEditMenu();
})

function moveEditMenu() {
    path = window.location.pathname;

    var cropCameraText = document.querySelector("#camera-crop-text");
    var takePhotoText = document.querySelector("#take-photo-text");
    var viewImagesText = document.querySelector("#view-images-text");
    var trainProjectText = document.querySelector("#train-project-text");

    var lineFat = document.querySelector(".line-fat");
    var lineThin = document.querySelector(".line-thin");

    if (path.startsWith("/edit/crop_camera")) 
    {
        cropCameraText.style.fontSize = "14px";
        cropCameraText.style.fontWeight = "bold";
        cropCameraText.style.opacity = 1;

        lineFat.style.width = "12.5%";

        lineThin.style.marginLeft = "12.5%";
        lineThin.style.width = "87.5%";
    } 
    else if (path.startsWith("/edit/take_photo")) 
    {
        takePhotoText.style.fontSize = "14px";
        takePhotoText.style.fontWeight = "bold";
        takePhotoText.style.opacity = 1;

        lineFat.style.width = "37.5%";

        lineThin.style.marginLeft = "37.5%";
        lineThin.style.width = "62.5%";
    } 
    else if (path.startsWith("/edit/view_images")) 
    {
        viewImagesText.style.fontSize = "14px";
        viewImagesText.style.fontWeight = "bold";
        viewImagesText.style.opacity = 1;

        lineFat.style.width = "62.5%";

        lineThin.style.marginLeft = "62.5%";
        lineThin.style.width = "37.5%";
    } 
    else if (path.startsWith("/edit/train_project")) 
    {
        trainProjectText.style.fontSize = "14px";
        trainProjectText.style.fontWeight = "bold";
        trainProjectText.style.opacity = 1;

        lineFat.style.width = "87.5%";

        lineThin.style.marginLeft = "87.5%";
        lineThin.style.width = "12.5%";
    }
}
function listProjects() {
    var ip = ipAdress.concat("get_projects")
    var xhttp = sendHttpRequest(ip)

    var json_response = JSON.parse(xhttp.responseText);
    var projects = json_response.projects;

    // List projects in html
    for (var i = 0; i < projects.length; i++) {
        document.getElementById("project-list").innerHTML += '<li class="list-group-item"><a href="/predict">' + projects[i].name + '</a><br></li>';
    }
}

function createProject(){
    var projectName = document.getElementById("project-name");
    projectName = projectName.value;

    var adress = "init_project" + "?new_project_name=" + projectName;
    var ip = ipAdress.concat(adress);
    var xhttp = sendHttpRequest(ip);

    window.location.href = '/edit/crop_camera';
      
}

from os import path

server_path = path.dirname(__file__)
project_path = server_path + "/projects/"
ip_address = "http://10.10.0.87:5000/"  # Enter your local IP-Address
device_type = "cpu"  # If cuda is enabled you can change "cpu" to "cuda"
camera_source = 0  # Camera source is an int if usb camera. Can be changed to rtsp or ip camera and passed in as a string

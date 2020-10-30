function getNotifications() {
    var access_token = getCookie("access");
    if (!access_token) {
        return false;
    }

    let socket = io("https://iss.ishraak.com?token=" + access_token, {autoConnect: false});

    socket.on('connect', () => {
        socket.on('disconnect', () => {
            console.log('Disconnected');
        });
        console.log('Connected');
    });

    socket.on('receive', (data) => {
        if (typeof(data) == 'string'){
            data = JSON.parse(data)
        }

        if (data.type == "status") {
            if (data.text == "valid") {
                console.log("authenticated");
            } else {
                console.log("invalid credential");
                socket.disconnect();
            }
        } else if (data.type == "notification") {
            var notification = JSON.parse(data.text);
            toastr.info(notification.message);
        } else if (data.type == "message") {
            var message = JSON.parse(data.text);
            toastr.info("New message received");
        }

    });

    socket.connect();
}

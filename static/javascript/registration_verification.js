function checkUsername() {
    let uPattern = /^[a-zA-Z0-9_@.+--]{4,30}$/;
    let userName = $("#id_username").val();
    if (uPattern.test(userName)){
        $("#userInfo").text("Available Username")
        $("#userInfo").css("color","black")
    }else {
        $("#userInfo").text("Unavailable Username")
        $("#userInfo").css("color","red")
    }
}

function test(){
    alert("test");
}
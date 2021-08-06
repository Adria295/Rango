var flag = true;

function checkUsername() {
    let uPattern = /^[a-zA-Z0-9_@.+--]{4,30}$/;
    let userName = $("#id_username").val();
    if (uPattern.test(userName)){
        $("#userInfo").text("Available Username")
        $("#userInfo").css("color","black")
    }else {
        $("#userInfo").text("Unavailable Username")
        $("#userInfo").css("color","red")
        flag = false;
    }
}

function checkEmail() {
    let email = $("#id_email").val();
    let reg = new RegExp("^[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+([.][a-zA-Z0-9-_]+)+$");
    if(reg.test(email)) {
        $("#userEmail").text("")
        $("#userEmail").css("color","black")
    } else {
        $("#userEmail").text("The email address you entered is wrong, please check!")
        $("#userEmail").css("color","red")
        flag = false;
    }
}

function checkPsw() {
    let password = $("#id_password1").val();

    if(password.length >= 6) {
        $("#userPsw1").text("")
        $("#userPsw1").css("color","black")
    } else {
        $("#userPsw1").text("The password must be at least 6 characters long")
        $("#userPsw1").css("color","red")
        flag = false;
    }
}

function checkRepsw() {
    let password = $("#id_password2").val();

    if(password.length >= 6) {
        $("#userPsw2").text("")
        $("#userPsw2").css("color","black")
    } else {
        $("#userPsw2").text("The password must be at least 6 characters long")
        $("#userPsw2").css("color","red")
        // If the password length verification fails, the subsequent logic does not need to be executed again
        flag = false;
        return;
    }
    // Compare the password
    let psw = $("#id_password1").val();
    if(psw == password) {
        $("#userPsw2").text("")
        $("#userPsw2").css("color","black")
    } else {
        $("#userPsw2").text("The two passwords are inconsistent, please check!")
        $("#userPsw2").css("color","red")
        flag = false;
    }
}

function checkForm(){
    flag = true;
    checkUsername();
    checkEmail();
    checkPsw();
    checkPsw();

    return flag;
}


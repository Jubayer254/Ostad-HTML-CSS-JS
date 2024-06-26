const switchButton = document.getElementById("theme");
switchButton.addEventListener("click", function(){
    var rootStyle = document.querySelector(":root");
    var rootVal = getComputedStyle(rootStyle);
    const isWhite = rootVal.getPropertyValue("--theme-bg");
    if (isWhite === '#E8E8E8') {
        rootStyle.style.setProperty("--theme-bg", "#212121");
        rootStyle.style.setProperty("--font-col", "#FFF");
        rootStyle.style.setProperty("--btn-col2", "#212121");
        rootStyle.style.setProperty("--btn-col", "#000");
    }
    else{
        rootStyle.style.setProperty("--theme-bg", "#E8E8E8");
        rootStyle.style.setProperty("--font-col", "#000");
        rootStyle.style.setProperty("--btn-col2", "#c5c5c5");
        rootStyle.style.setProperty("--btn-col", "#fff");
    }

})

function moveFocus(event) {
    const currentInput = event.target;
    const nextInput = currentInput.nextElementSibling;
    const prevInput = currentInput.previousElementSibling;
    
    // Check if there's a next input and the current input has a value
    if (event.key !== 'Backspace' && nextInput && currentInput.value !== "") {
        nextInput.focus();
    } else if (event.key === 'Backspace' && prevInput) {
        prevInput.focus();
    }
}

const btn2 = document.getElementById("btn");
btn2.addEventListener("click", function(){
    var in1 = document.getElementById("in1").value;
    var in2 = document.getElementById("in2").value;
    var in3 = document.getElementById("in3").value;
    var in4 = document.getElementById("in4").value;
    otp = in1+in2+in3+in4;
    
    if(otp.length !=4){
        Swal.fire({
            icon: "warning",
            title: "Oops...",
            text: "Please enter the 4 digit OTP",
        });
        return;
    }
    
    if(otp == 1234){
        Swal.fire({
            icon: "success",
            title: "Welcome",
            text: "Succesfully Logged in",
        });
        return;
    }
    else{
        Swal.fire({
            icon: "error",
            title: "Wrong OTP",
            text: "Logged in failed",
        });
    }
    
    
})
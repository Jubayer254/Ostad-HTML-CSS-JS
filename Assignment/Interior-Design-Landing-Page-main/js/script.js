// DARK MODE

const switchButton = document.getElementById("theme");
switchButton.addEventListener("click", function(){
    var rootStyle = document.querySelector(":root");
    var rootVal = getComputedStyle(rootStyle);
    const isWhite = rootVal.getPropertyValue("--theme-font-color");
    if (isWhite === '#FFFFFF') {
        rootStyle.style.setProperty("--theme-font-color", "#11061C");
        rootStyle.style.setProperty("--theme-bg", "#8C94F2");
        rootStyle.style.setProperty("--color-black", "#eddefc");
        rootStyle.style.setProperty("--theme-font-color-secondary", "#0a0212");
        rootStyle.style.setProperty("--theme-bg-light", "#99a0ec");
        rootStyle.style.setProperty("--theme-footer-color", "#0a0212");
        rootStyle.style.setProperty("--color-alert", "#212121");
    }
    else{
        rootStyle.style.setProperty("--theme-font-color", "#FFFFFF");
        rootStyle.style.setProperty("--theme-bg", "#FE6347");
        rootStyle.style.setProperty("--color-black", "#000000");
        rootStyle.style.setProperty("--theme-font-color-secondary", "#e8e5e5");
        rootStyle.style.setProperty("--theme-bg-light", "#ff846e");
        rootStyle.style.setProperty("--theme-footer-color", "#F1F1F1");
        rootStyle.style.setProperty("--color-alert", "#FFFFFF");
    }

})

// PRICING BASIC

document.getElementById("minus-basic-price").addEventListener("click", function(){
    let value = parseFloat(document.getElementById("basic-price").textContent);
    let room = parseInt(document.getElementById("room-basic").textContent);
    if(value > 199 && room > 1){
        value = value - 199;
        document.getElementById("basic-price").textContent = value;
        room = room - 1
        document.getElementById("room-basic").textContent = room;
    }
    else{
        return;
    }
});


document.getElementById("plus-basic-price").addEventListener("click", function(){
    let value = parseFloat(document.getElementById("basic-price").textContent);
    let room = parseInt(document.getElementById("room-basic").textContent);
    value = value + 199;
    document.getElementById("basic-price").textContent = value;
    room = room + 1
    document.getElementById("room-basic").textContent = room;
});

// PRICING PRO

document.getElementById("minus-pro-price").addEventListener("click", function(){
    let value = parseFloat(document.getElementById("pro-price").textContent);
    let room = parseInt(document.getElementById("room-pro").textContent);
    if(value > 249 && room > 1){
        value = value - 249;
        document.getElementById("pro-price").textContent = value;
        room = room - 1
        document.getElementById("room-pro").textContent = room;
    }
    else{
        return;
    }
});

document.getElementById("plus-pro-price").addEventListener("click", function(){
    let value = parseFloat(document.getElementById("pro-price").textContent);
    let room = parseInt(document.getElementById("room-pro").textContent);
    value = value + 249;
    document.getElementById("pro-price").textContent = value;
    room = room + 1
    document.getElementById("room-pro").textContent = room;
});

// SIGNUP BASIC
const basicSignUpButton = document.getElementById("sign-up-basic");
basicSignUpButton.addEventListener("click", function(){
    let room = parseInt(document.getElementById("room-basic").textContent);
    document.querySelector('#check-out-basic').innerHTML = `<div class="project-body-packages-info-body">` +
                                                                `<p class="checkout-text">Thank you for choosing ${room} room</p>` +
                                                            `</div>`;

})

// SIGNUP PRO
const proSignUpButton = document.getElementById("sign-up-pro");
proSignUpButton.addEventListener("click", function(){
    let room = parseInt(document.getElementById("room-pro").textContent);
    document.querySelector('#check-out-pro').innerHTML = `<div class="project-body-packages-info-body">` +
                                                            `<p class="checkout-text">Thank you for choosing ${room} room</p>` +
                                                        `</div>`;

})

// EMAIL VALIDATION
function isValidEmail(email) {
    // Simple email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// CONTACT
const contact_btn_id = document.getElementById("contact-btn-id");
contact_btn_id.addEventListener("click", function(event){
    event.preventDefault();

    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var msg = document.getElementById("msg").value;

    if(!name || !email || !msg){
        Swal.fire({
            icon: "warning",
            title: "Oops...",
            text: "Please input the required fields!",
            customClass: {
                confirmButton: 'warning-button' // Apply the custom class to the button
            }
          });
    }
    else if (!isValidEmail(email)) {
        Swal.fire({
          icon: "warning",
          title: "Invalid Email",
          text: "Please enter a valid email address!",
          customClass: {
            confirmButton: 'warning-button' // Apply the custom class to the button
          }
        });
    }
    else{
        Swal.fire({
            icon: "success",
            title: "Thank You",
            text: "Your feedback has been successfully submitted!",
            customClass: {
                confirmButton: 'success-button' // Apply the custom class to the button
            }
          });
    }
})
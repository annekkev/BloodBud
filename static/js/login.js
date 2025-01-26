const loginBtn = document.getElementById("loginBtn");
const loginForm = document.getElementById("loginForm");

loginBtn.addEventListener("submit", e => {
    e.preventDefault();

    const logins = ["jason123", "amandaB", "ali3434"];

    //CHECK PASSWORD CORRECT
    let validPassword = true;

    if (validPassword) {
        window.open("http://127.0.0.1:5000/menu/");
    } else {
        alert("Please enter your password again.");
    }
    
});
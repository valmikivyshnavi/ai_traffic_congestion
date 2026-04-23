document.addEventListener("DOMContentLoaded", function () {

  const container = document.getElementById("container");
  const loginForm = document.getElementById("loginForm");
  const registerForm = document.getElementById("registerForm");

  // 🔄 TOGGLE SLIDE
  window.toggle = function () {
    container.classList.toggle("active");
  };

  // 🔐 LOGIN → DASHBOARD
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    window.location.href = "/dashboard";
  });

  // 📝 REGISTER → DASHBOARD
  registerForm.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Registered successfully!");
    window.location.href = "/dashboard";
  });

});
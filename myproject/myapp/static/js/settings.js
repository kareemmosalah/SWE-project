document.addEventListener("DOMContentLoaded", () => {
    const newPassword = document.getElementById("new-password");
    const confirmPassword = document.getElementById("confirm-password");
    const passwordHint = document.getElementById("password-match");
    const updatePasswordButton = document.getElementById("update-password-btn");

    // Password validation: check if passwords match
    const validatePasswords = () => {
        const newPasswordValue = newPassword.value;
        const confirmPasswordValue = confirmPassword.value;

        if (newPasswordValue && confirmPasswordValue) {
            if (newPasswordValue === confirmPasswordValue) {
                passwordHint.textContent = "Passwords match!";
                passwordHint.style.color = "green";
                passwordHint.classList.add("active");
                updatePasswordButton.disabled = false;
            } else {
                passwordHint.textContent = "Passwords do not match!";
                passwordHint.style.color = "red";
                passwordHint.classList.add("active");
                updatePasswordButton.disabled = true;
            }
        } else {
            passwordHint.textContent = "";
            passwordHint.classList.remove("active");
            updatePasswordButton.disabled = true;
        }
    };

    newPassword.addEventListener("input", validatePasswords);
    confirmPassword.addEventListener("input", validatePasswords);
});

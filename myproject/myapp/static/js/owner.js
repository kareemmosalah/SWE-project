document.addEventListener("DOMContentLoaded", () => {
    const courtNameInput = document.getElementById("courtName");
    const locationInput = document.getElementById("location");
    const priceInput = document.getElementById("price");
    const cityInput = document.getElementById("city");
    const addCourtButton = document.getElementById("add-court-btn");
    const form = document.getElementById("add-court-form");

    // Function to validate all inputs
    const validateInputs = () => {
        const isCourtNameValid = courtNameInput.value.trim() !== "";
        const isLocationValid = locationInput.value.trim() !== "";
        const isPriceValid = priceInput.value > 0;
        const isCityValid = cityInput.value.trim() !== "";

        if (isCourtNameValid && isLocationValid && isPriceValid && isCityValid) {
            addCourtButton.disabled = false;
        } else {
            addCourtButton.disabled = true;
        }
    };

    // Add event listeners to inputs for real-time validation
    [courtNameInput, locationInput, priceInput, cityInput].forEach(input => {
        input.addEventListener("input", validateInputs);
    });

    // Add a listener to prevent form submission if inputs are invalid
    form.addEventListener("submit", (event) => {
        validateInputs(); // Double-check validation before submitting
        if (addCourtButton.disabled) {
            event.preventDefault();
            alert("Please fill out all fields correctly before submitting!");
        }
    });

    // Real-time styling for invalid inputs
    [courtNameInput, locationInput, priceInput, cityInput].forEach(input => {
        input.addEventListener("input", () => {
            if (input.value.trim() === "" || (input === priceInput && input.value <= 0)) {
                input.style.borderColor = "red";
            } else {
                input.style.borderColor = "#007bff";
            }
        });
    });
});

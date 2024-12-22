document.addEventListener("DOMContentLoaded", () => {
    const profileImage = document.querySelector(".profile-picture img");
    const profileContainer = document.querySelector(".profile-container");

    // Add hover effect to profile container
    profileContainer.addEventListener("mouseover", () => {
        profileContainer.style.boxShadow = "0 8px 20px rgba(0, 0, 0, 0.2)";
    });

    profileContainer.addEventListener("mouseout", () => {
        profileContainer.style.boxShadow = "0 5px 15px rgba(0, 0, 0, 0.1)";
    });

    // Click to enlarge profile picture
    profileImage.addEventListener("click", () => {
        profileImage.style.transform = "scale(1.2)";
        setTimeout(() => {
            profileImage.style.transform = "scale(1)";
        }, 500);
    });
});

const navLinkElements = document.querySelectorAll(".nav-link");
navLinkElements.forEach((navLinkElement) => {
  navLinkElement.addEventListener("click", () => {
    document.querySelector(".active").classList.remove("active");
    navLinkElement.classList.add("active");
  });
});

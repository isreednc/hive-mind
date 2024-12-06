// Func that creates the cards in container

function createCard(imageSrc, labelText) {

    const container = document.querySelector(".container");
    const card = document.createElement("div");

    card.classList.add("Project");

    const img = document.createElement("img");
    img.src = imageSrc; 
    img.alt = labelText; 
    card.appendChild(img);

     
    const label = document.createElement("p");
    label.textContent = labelText;  
    card.appendChild(label);
    
    if (container) {
        container.appendChild(card);
    } else {
        console.error("no container");
    }
}

// For redirecting to the group page when clicking a proj
document.addEventListener("DOMContentLoaded", () => {

    const projectElements = document.querySelectorAll(".Project");

    projectElements.forEach((project) => {
        project.addEventListener("click", () => {
            // your redirect code to the project taskboard
        });
    });
});


// Creating a new project
const newProjBtn = document.querySelector(".new-project");
newProjBtn.addEventListener("click", () =>{
    //whatever django you need
    console.log("hi");
    // syntax for creating card on the page
    createCard("https://i.ibb.co/D7ykSY6/HiveMind.png", "Project Dodo");
});



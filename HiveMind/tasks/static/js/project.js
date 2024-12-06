// Func that creates the cards in container
const modal = document.getElementById("projectModal");
const closeModalButton = document.getElementById("closeModalButton");
const openModalButton = document.getElementsByClassName("new-project");

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
    modal.style.display = 'block';
    console.log("hi");

    const projectForm = document.getElementById('projectForm');
    projectForm.onsubmit = function(event) {
        event.preventDefault(); // Prevent the form from submitting
        const projectName = document.getElementById('projectName').value;           // represents the group name in django
        const projectDescription = document.getElementById('projectDescription').value;
        console.log('New Project Created: ', projectName, projectDescription);
        modal.style.display = "none"; // Close modal after form submission
    }

    // syntax for creating card on the page
    createCard("https://i.ibb.co/D7ykSY6/HiveMind.png", projectName);
});

openModalButton.onclick = function() {
    modal.style.display = "block";
}

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}


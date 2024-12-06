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
        // const csrfToken = getCSRFToken();  // Get CSRF token

        const data = {
            name: projectName
        }

        fetch("/create-group/", {
        method: "POST",
        headers: {
            "X-Requested-With": "XMLHttpRequest",  // Indicate this is an AJAX request
            "Content-Type": "application/json",    // We're sending JSON data
            // "X-CSRFToken": csrfToken              // Include CSRF token for security
        },
        body: JSON.stringify(data)  // Send data as JSON
        })
        .then(response => response.json())  // Parse JSON response
        .then(data => {
            location.reload();
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("responseMessage").innerHTML = "<p style='color: red;'>Error while creating the group.</p>";
        });


        console.log('New Project Was Not Created: ', projectName);
        modal.style.display = "none"; // Close modal after form submission
            
        // syntax for creating card on the page
        // createCard("https://i.ibb.co/D7ykSY6/HiveMind.png", projectName);
    }

});

openModalButton.onclick = function() {
    modal.style.display = "block";
}

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

function getCSRFToken() {
    let csrfToken = null;
        const cookies = document.cookie.split(';');
        cookies.forEach(cookie => {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                csrfToken = value;
            }
        });
        return csrfToken;
}


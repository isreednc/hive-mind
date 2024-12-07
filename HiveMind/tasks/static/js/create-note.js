
const card = document.getElementById("create-card");
const group = card.getAttribute('data-group-name');
const newNoteButton = document.querySelector(".new-note");
let isCreatingNote = false;

console.log(group);

if (!card.classList.contains('hidden')) {
    card.classList.add("hidden");
}

newNoteButton.addEventListener('click', CreateNote);

function CreateNote(event) {
    if (isCreatingNote) return;

    card.classList.remove('hidden');
    isCreatingNote = true;
    card.style.zIndex = 2;

    const submitBtn = document.getElementById("new-note-submit-btn");
    const textarea = card.querySelector('textarea');

    const cancelCardBtn = document.getElementById("cancel-card");
    cancelCardBtn.addEventListener('click', () => {
        card.classList.add('hidden');
        isCreatingNote = false;
    })

    textarea.focus();

    submitBtn.addEventListener('click', () => {
        console.log("click");
        // Show confirmation window
        const isConfirmed = confirm("Are you sure you want to submit this note?");
        if (isConfirmed) {
            // Get note data
            const noteContent = textarea.value;

            // Validate the input
            if (!noteContent.trim()) {
                alert("Note cannot be empty!");
                return;
            }

            // Send data to the backend
            sendDataToBackend(noteContent, group);

            // Reset and hide the note card
            card.classList.add('hidden');
            textarea.value = "";
            isCreatingNote = false;
        }
    });

}

function sendDataToBackend(noteContent, group_name) {
    fetch(`/submit-note/${group_name}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({ note: noteContent }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to submit note.");
            }
            return response.json();
        })
        .then(data => {
            console.log("Note submitted successfully:", data);
            location.reload();
        })
        .catch(error => {
            console.error("Error submitting note:", error);
            alert("There was an error submitting your note. Please try again.");
        });
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
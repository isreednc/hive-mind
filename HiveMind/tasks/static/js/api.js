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

function logNewPos(cardObj) {
    const noteId = cardObj.id;
    const top = cardObj.style.top;
    const left = cardObj.style.left;

    const data = {
        noteId: noteId,
        top: top,
        left: left
    }

    fetch('/update-note-position/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()  // Send CSRF token for security
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Position updated successfully');
                } else {
                    console.error('Error updating position');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
}

export { logNewPos };
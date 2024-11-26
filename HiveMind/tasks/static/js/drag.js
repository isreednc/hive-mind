
const headers = document.querySelectorAll('.card .card-header');

console.log(headers);

const navbarHeight = 0;


headers.forEach((header) => {
    header.addEventListener('mousedown', onMouseDown);
});

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

    console.log(noteId);
    console.log(top);
    console.log(left);

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
                console.log(data);
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

function onMouseDown(event) {
    console.log("mmousedown")
    const header = event.target;
    const card = header.parentElement;

    const startX = event.clientX;
    const startY = event.clientY;
    const rect = card.getBoundingClientRect();
    const offsetX = startX - rect.left;
    const offsetY = startY - rect.top;

    function onMouseMove(event) {
        const newLeft = Math.max(event.clientX - offsetX, 0);
        const newTop = Math.max(event.clientY - offsetY, navbarHeight);

        const contentWrapper = document.querySelector('.content-wrapper');
        const contentRect = contentWrapper.getBoundingClientRect();
        const rightBound = Math.min(newLeft, contentRect.width - card.offsetWidth);
        const bottomBound = Math.min(newTop, contentRect.height - card.offsetHeight);

        card.style.left = `${rightBound}px`;
        card.style.top = `${bottomBound}px`;

    }

    function onMouseUp() {
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);

        logNewPos(card);
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
}

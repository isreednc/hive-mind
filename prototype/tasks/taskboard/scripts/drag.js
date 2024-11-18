const headers = document.querySelectorAll('.card .card-header');

const navbarHeight = 0;

headers.forEach((header) => {
    header.addEventListener('mousedown', onMouseDown);
});

function onMouseDown(event) {
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
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
}

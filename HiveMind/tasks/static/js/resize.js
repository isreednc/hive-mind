document.querySelectorAll('.resize-handler').forEach((handler) => {
    handler.addEventListener('mousedown', onResizeMouseDown);
});
 
const defaultCardHeader = document.querySelector('.card-header');
const defaultCardContent = document.querySelector('.card-body');

function onResizeMouseDown(event) {
    const handler = event.target;
    const card = handler.closest('.card');
    const cardHeader = card.querySelector('.card-header');
    const cardContent = card.querySelector('.card-body');
    const cardFooter = card.querySelector('.card-footer');

    const minWidth = Math.max(defaultCardHeader.offsetWidth, defaultCardContent.offsetWidth);
    const minHeight = Math.max(defaultCardHeader.offsetHeight + defaultCardContent.offsetHeight, defaultCardHeader.offsetHeight);

    const startWidth = card.offsetWidth;
    const startHeight = card.offsetHeight;
    const startX = event.clientX;
    const startY = event.clientY;

    function onMouseMove(event) {
        let newWidth = startWidth + (event.clientX - startX);
        let newHeight = startHeight + (event.clientY - startY);

        newWidth = Math.max(newWidth, minWidth);
        newHeight = Math.max(newHeight, minHeight);

        card.style.width = `${newWidth}px`;
        card.style.height = `${newHeight}px`;
    }

    function onMouseUp() {
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
}
  
  
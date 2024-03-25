<script>
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('#imageContainer .checkbox');
    checkboxes.forEach(function(checkbox) {
        const x = checkbox.dataset.x;
        const y = checkbox.dataset.y;
        checkbox.style.position = 'absolute';
        checkbox.style.left = x;
        checkbox.style.top = y;
    });
}); // Remove this line
}); // Add this line
</script>

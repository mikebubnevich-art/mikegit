
document.getElementById('myButton').addEventListener('click', function() {
    alert('НЕВЕРОЯТНО');
});


const photoButton = document.getElementById('photoButton');
const photoContainer = document.getElementById('photoContainer');
const myPhoto = document.getElementById('myPhoto');


const photoPath = 'фото.jpg';

photoButton.addEventListener('click', function() {
    myPhoto.src = photoPath;
    photoContainer.style.display = 'block';
    photoButton.textContent = 'Невероятно! ✓';
    photoButton.disabled = true;
});

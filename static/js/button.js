const myBtn = document.getElementById('myBtn')

myBtn.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
})
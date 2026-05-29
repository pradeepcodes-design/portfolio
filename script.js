document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const targetId = link.getAttribute('href').slice(1);
        document.querySelectorAll('.section').forEach(s => s.classList.add('hidden'));
        document.getElementById(targetId).classList.remove('hidden');
    });
});

const words = ["Backend Developer", "Frontend Developer", "Web Developer"];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typedSpan = document.querySelector(".typed-text");

function typeEffect(){
    const current = words[wordIndex];
    if(isDeleting){
        typedSpan.textContent = current.substring(0, charIndex--);
    }else{
        typedSpan.textContent = current.substring(0, charIndex++);
    }

    let delay = isDeleting ? 50 : 100;

    if(!isDeleting && charIndex === current.length + 1){
        delay = 2000;
        isDeleting = true;
    }

    if(isDeleting && charIndex === 0){
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
        delay = 500;
    }

    setTimeout(typeEffect, delay);
}

typeEffect();

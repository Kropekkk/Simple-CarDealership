const carLogo = document.querySelector('#mainPage');

const GoBack = () => {
    document.documentElement.scrollTop=0;
}

carLogo.addEventListener('click', GoBack)
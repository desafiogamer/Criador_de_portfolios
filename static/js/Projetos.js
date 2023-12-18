const navbar = document.querySelector('.navbar');
const menuIcon = document.getElementById('btn-menu');

menuIcon.addEventListener('click', function () {
    navbar.classList.toggle('active')
    menuIcon.classList.toggle('ativar')
})

const Confirmar = document.querySelector('.card-copiado')

const input = document.querySelector('#Link')

function abrirModal1() {
    Confirmar.classList.add('active')
    navigator.clipboard.writeText(input.value).then(() => {
        setTimeout(function () {
            Confirmar.classList.remove('active')
        }, 2000);
    })

}


const input2 = document.querySelector('#Link2')

function abrirModal2() {
    Confirmar.classList.add('active')
    navigator.clipboard.writeText(input2.value).then(() => {
        setTimeout(function () {
            Confirmar.classList.remove('active')
        }, 2000);
    })

}

const input3 = document.querySelector('#Link3')

function abrirModal3() {
    Confirmar.classList.add('active')
    navigator.clipboard.writeText(input3.value).then(() => {
        setTimeout(function () {
            Confirmar.classList.remove('active')
        }, 2000);
    })

}
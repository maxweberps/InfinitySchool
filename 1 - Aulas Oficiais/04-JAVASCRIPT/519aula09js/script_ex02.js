const energia = document.querySelector("#energia")
const brincar = document.querySelector("#brincar")
const pular = document.querySelector("#pular")
const comer = document.querySelector("#comer")
const dormir = document.querySelector("#dormir")


brincar.addEventListener("click",() => energia.textContent = Number(energia.textContent) - 10)
pular.addEventListener("click",() => energia.textContent = Number(energia.textContent) - 5)
comer.addEventListener("click",() => energia.textContent = Number(energia.textContent) + 5)
dormir.addEventListener("click",() => energia.textContent = Number(energia.textContent) + 10)
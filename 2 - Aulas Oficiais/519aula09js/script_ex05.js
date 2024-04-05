const vermelho = document.querySelector("#vermelho")
const amarelo = document.querySelector("#amarelo")
const verde = document.querySelector("#verde")
const resposta = document.querySelector("#resposta")


vermelho.addEventListener("click", ()=>{
    resposta.className = ""
    resposta.classList.add("pare")
    resposta.textContent = "Pare!!!!!!!!!"
})

amarelo.addEventListener("click", ()=>{
    resposta.className = ""
    resposta.classList.add("atencao")
    resposta.textContent = "Atenção!!!!!!!!!"
})

verde.addEventListener("click", ()=>{
    resposta.className = ""
    resposta.classList.add("prossiga")
    resposta.textContent = "Prossiga!!!!!!!!!"
})
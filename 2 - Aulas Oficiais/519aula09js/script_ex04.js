const idade = document.querySelector("#idade")
const formulario = document.querySelector("#formulario")
const resposta = document.querySelector("#resposta")

function checarIdade(event){
    event.preventDefault()
    if(+idade.value >= 18){
        resposta.textContent = "Pode ser preso"
        resposta.classList.remove("verde")
        resposta.classList.add("vermelho")
    }else{
        resposta.textContent = "Vai pra febem"
        resposta.classList.remove("vermelho")
        resposta.classList.add("verde")
    }
}

formulario.addEventListener("submit", checarIdade)
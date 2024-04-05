const atividade = document.querySelector("#atividade")
const formulario = document.querySelector("#formulario")
const lista = document.querySelector("#lista")


function cadastrarAtividade(event){
    event.preventDefault()
    const novo_elemento = document.createElement("li")
    novo_elemento.textContent = atividade.value
    lista.appendChild(novo_elemento)
    atividade.value = ""
    atividade.focus()
}

formulario.addEventListener("submit", cadastrarAtividade)
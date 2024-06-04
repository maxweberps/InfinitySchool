const atividade = document.querySelector("#atividade")
const formulario = document.querySelector("#formulario")
const lista = document.querySelector("#lista")


function cadastrarAtividade(event){
    event.preventDefault()
    const novo_elemento = document.createElement("li")

    const caixinha = document.createElement("input")
    caixinha.type = "checkbox"

    caixinha.addEventListener("click", (event)=>{
        if(event.target.checked){
            texto.classList.add("marcado")
        }else{
            texto.classList.remove("marcado")
        }
    })


    const texto = document.createElement("span")
    texto.textContent = atividade.value

    const botao_excluir = document.createElement("button")
    botao_excluir.textContent = "Excluir"

    botao_excluir.addEventListener("click", ()=>{
        lista.removeChild(novo_elemento)
    })


    novo_elemento.appendChild(caixinha)
    novo_elemento.appendChild(texto)
    novo_elemento.appendChild(botao_excluir)


    lista.appendChild(novo_elemento)
    atividade.value = ""
    atividade.focus()
}

formulario.addEventListener("submit", cadastrarAtividade)
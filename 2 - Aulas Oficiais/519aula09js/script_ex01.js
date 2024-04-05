const email = document.querySelector("#email")
const senha = document.querySelector("#senha")
const formulario = document.querySelector("#formulario")

const email_correto = "joao@email.com"
const senha_correta = "123456"

function enviarDados(event){
    event.preventDefault()
    if(email.value === email_correto && senha.value === senha_correta){
        alert("Login efetuado com sucesso")
    }else{
        alert("Email ou senha estão incorretos")
    }
}

formulario.addEventListener("submit", enviarDados )
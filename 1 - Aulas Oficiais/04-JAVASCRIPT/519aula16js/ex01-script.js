const formulario = document.querySelector("#formulario")
const cep = document.querySelector("#cep")
const resposta = document.querySelector("#resposta")

async function buscarCep(e){
    e.preventDefault()
    try{
        const resposta_api = await fetch(`https://viacep.com.br/ws/${cep.value}/json/`)
        const dados = await resposta_api.json()
        console.log(dados);
        if(dados.erro){
            resposta.innerHTML = "CEP Inválido"
        }else{
            resposta.innerHTML = `
                <p>Endereço: ${dados.logradouro}</p>
                <p>Complemento: ${dados.complemento}</p>
                <p>Bairro: ${dados.bairro}</p>
                <p>Cidade: ${dados.localidade}</p>
                <p>Estado: ${dados.uf}</p>
            `
            cep.value = ""
            cep.focus()
        }
    }catch(erro_do_catch){
        alert("Digite exatamente 8 digitos")
    }
}


formulario.addEventListener("submit", buscarCep)
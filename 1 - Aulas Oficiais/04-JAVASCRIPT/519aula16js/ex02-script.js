const personagens = document.querySelector("#personagens")

async function buscarPersonagens(){
    const resposta = await fetch("https://rickandmortyapi.com/api/character")
    const dados = await resposta.json()
    const lista_de_personagens_da_api = dados.results

    lista_de_personagens_da_api.forEach((personagem_da_vez)=>{
        const novo_card = document.createElement("div")

        const nova_imagem = document.createElement("img")
        nova_imagem.src = personagem_da_vez.image

        const novo_nome = document.createElement("h2")
        novo_nome.textContent = `Nome: ${personagem_da_vez.name}`

        const novo_especie = document.createElement("p")
        novo_especie.textContent = `Espécie: ${personagem_da_vez.species}`

        const novo_status = document.createElement("p")
        novo_status.textContent = `Status: ${personagem_da_vez.status}`

        const novo_localizacao = document.createElement("p")
        novo_localizacao.textContent = `Localização: ${personagem_da_vez.location.name}`
        
        novo_card.append(nova_imagem, novo_nome, novo_especie, novo_status, novo_localizacao)

        personagens.append(novo_card)
    })
}

buscarPersonagens()
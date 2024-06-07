const filmes_populares = document.querySelector("#filmes_populares")

async function buscarFilmesPopulares(){
    try{
        const resposta = await fetch("https://api.themoviedb.org/3/movie/popular?api_key=77c4e2b070a2e1396500d0b42ebf7cec&language=pt-BR")
        const dados = await resposta.json()
        dados.results.forEach((filme_da_vez)=>{
            const novo_card = document.createElement("div")

            const novo_titulo = document.createElement("h3")
            novo_titulo.textContent = filme_da_vez.title

            const nova_capa = document.createElement("img")
            nova_capa.src = `https://image.tmdb.org/t/p/w500${filme_da_vez.poster_path}` 

            novo_card.append(novo_titulo, nova_capa)

            filmes_populares.append(novo_card)

        })

    }catch(error){
        console.log("Algum problema na requisição da API")
    }
}

buscarFilmesPopulares()
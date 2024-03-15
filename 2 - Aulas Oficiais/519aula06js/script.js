let nome = prompt("Digite seu nome completo: ")
console.log(nome.trim().toLowerCase())

const vogais = 'aeiouáâàãéêíóôõú'
const consoantes = 'bcdfghjklmnpqrstvxywz'

let cont_vogal = 0
let cont_consoante = 0
let cont_palavras = 1

for (letra of nome.trim().toLowerCase()) {
    if (vogais.includes(letra)) {
        cont_vogal++
    } else if (consoantes.includes(letra)) {
        cont_consoante++
    } else {
        cont_palavras++
    }
}

console.log(`Seu nome possui ${cont_palavras} palavras, ${cont_vogal} vogais e ${cont_consoante} consoantes.`)
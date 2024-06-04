const notas = [5,8,9,4,6,7]

let soma = 0

notas.forEach((n) => {
    soma += n
})

let media = soma/notas.length
alert(`Média: ${media}`)
/* Atividade 01: Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
let nomes = []

console.log('Digite 5 nomes de pessoas')
for (let i = 0;i < 5; i++){
    nome = prompt(`Nome ${i+1}: `)
    nomes.push(nome)
}
console.log(nomes)*/

/* Atividade 02: Faça um programa que leia 20 números inteiros e armazene-os em
um vetor. Armazene os números pares no vetor 'PAR' e os números ímpares no vetor
'ímpar'. Imprima os três vetores.

let vetor = []
let vetor_par = []
let vetor_impar = []*/

/* Atividade 03

let respostas = []
let resposta = ''

// Pergunta 01
while (true){
resposta = prompt('01. Telefonou para a vítima? "Sim" "Não"')
if (resposta == 'Sim' || resposta == 'Não'){
    respostas.push(resposta)
    break
}
else
    alert('Resposta inválida')
}

respostas.push(prompt('02 - Esteve no local do crime? "Sim" "Não"'))
respostas.push(prompt('03 - Mora perto da vítima? "Sim" "Não"'))
respostas.push(prompt('04 - Devia para a vítima? "Sim" "Não"'))
respostas.push(prompt('05 - Já trabalhou com a vítima? "Sim" "Não"'))

let cont_sim = 0
for (resposta of respostas) {
    if (resposta == 'Sim')
        cont_sim += 1

}

if (cont_sim == 5)
    console.log('Assasino')
else if ((cont_sim == 3) || (cont_sim == 4))
    console.log('Cúmplice')
else if (cont_sim == 2)
    console.log('Suspeita')
else
    console.log('Inocente')*/
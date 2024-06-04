/* Atividade 01:
Escreva um programa que imprima no console os números de 0 a 10.
for (let i=0;i<=10;i++){
    console.log(i)
}*/

/* Atividade 02:
Escreva um programa que solicite um número inteiro e imprima a
tabuada desse número de 1 a 10. 
let num = Number(prompt("Digite um número: "))
for (i = 1; i <= 10; i++) {
    console.log(`${num} x ${i} = ${num * i}`)
}*/


/* Atividade 03:
Escreva um programa que solicite um número inteiro positivo e
faça uma contagem regressiva a partir desse número até 0.
num = Number(prompt('Digite um número: '))
for (let i = num; i >= 0; i--) {
    console.log(i)
}*/


/* Atividade 04:
Escreva um programa que solicite um número e verifique se ele é
um número primo.

num = Number(prompt('Digite um número: '))
contador = 0
for (let i = 1; i <= num; i++) {
    if (num % i == 0) {
        contador++
        console.log(`${num} é divisível por ${i}`)
    } else {
        console.log(`${num} NÃO é divisível por ${i}`)
    }
}

if (contador == 2) {
    console.log(`O número ${num} é primo`)
} else {
    console.log(`O número ${num} NÃO é primo`)
}*/

/* Atividade 06:
Escreva um programa que irá solicitar ao usuário uma palavra e que
imprimirá no console a palavra sem vogais.
let palavra = prompt('Digite uma palavra: ')
nova_palavra = ''
console.log(`Palavra digitada: ${palavra}`)
for (letra of palavra) {
    if (!'aeiouAEIOU'.includes(letra)) {
        nova_palavra += letra
    }
}
console.log(`Palavra digitada sem as vogais: ${nova_palavra}`)*/

/* Atividade 07:
Escreva uma programa que irá receber um texto e mostrará no
console se esse texto é um palíndromo ou não. (palíndromos são
palavras que são lidas da mesma forma de trás pra frente) Ex:
arara
let palavra = prompt('Digite uma palavra: ')
palavra = palavra.toLowerCase()

nova_palavra = ''
cont = palavra.length - 1
for(i = cont; i >= 0; i--){
    nova_palavra += palavra[i]
}

console.log(`Palavra digitada: ${palavra}`)
console.log(`Palavra invertida: ${nova_palavra}`)

if (palavra == nova_palavra){
    console.log('É palíndromo')
} else {
    console.log('Não é palindromo')
}*/

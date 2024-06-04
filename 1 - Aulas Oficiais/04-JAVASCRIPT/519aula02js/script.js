/* Atividade 01: Peça ao usuário para inserir um número e escrever um programa que determine se o número é positivo e par 

let numero = Number(prompt("Insira um número: "))
if (numero > 0 && numero % 2 == 0) {
  console.log("O número é positivo e par")
} else {
  console.log("O número não é positivo ou não é par")
} */

/* Atividade 02: Crie um programa que solicite ao usuário seu peso (em kg) e altura (em metros) e calcule o IMC (Índice de Mass). Em seguida, informe a classificação do IMC: abaixo do peso, peso normal, sobrepeso, obesidade grau 1, obesidade grau 2. 

let peso = Number(prompt("Insira seu peso: "))
let altura = Number(prompt("Insira sua altura: "))
let imc = peso / (altura * altura)
if (imc < 18.5)
  console.log('Abaixo do peso')
else if (imc >= 18.5 && imc <= 24.9)
  console.log('Peso normal')
else if (imc >= 25 && imc <= 29.9)
  console.log('Sobrepeso')
else if (imc >= 30 && imc <= 34.9)
  console.log('Obesidade grau 1')
else if (imc >= 35 && imc <= 39.9)
  console.log('Obesidade grau 2')
else {
  console.log('Fora do intervalo.')
}*/
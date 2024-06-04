/*Atividade 01: Crie um programa que solicita ao usuário um número e, em seguida,
conta regressivamente até zero, imprimindo cada número no console.
O programa deve terminar quando atingir zero.
let numero = Number(prompt("Insira um número: "))
while (numero > 0){
  console.log(numero)
  numero--
}
console.log(`Fim do programa. Número = ${numero}`)*/

/*Atividade 02: Desenvolva um programa que solicita ao usuário que insira suas
notas de uma série de disciplinas. O programa deve calcular e
imprimir a média das notas, o usuário pode continuar adicionando
notas até decidir parar.

contador = 0
soma_nota = 0
let nota = 0

console.log("Digite suas notas. \nPara encerrar digite '-1'.")

while(true){
  
  nota = Number(prompt(`Nota ${contador+1}:`))
  if (nota == -1){
    break
  } else {
  soma_nota = soma_nota + nota
  contador++
  }
  
}

media = soma_nota/contador
console.log(`Sua média é: ${media}`)*/
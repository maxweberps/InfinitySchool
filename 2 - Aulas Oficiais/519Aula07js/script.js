// TAREFA 1
/*function saudar(nome,horario){
    if(horario >= 5 && horario <= 12){
        return `Bom dia ${nome}`
    } else if (horario > 12 && horario <= 18){
        return `Boa tarde ${nome}`
    } else{
        return `Boa noite ${nome}`
    }
}

let nome = prompt('Seu nome: ')
let horario = Number(prompt('Horário: '))

alert(saudar(nome,horario))*/

// TAREFA 2
/*let vogais = 'aeiou'

function contar_vogais(palavra){
    cont_vogal = 0
    for (letra of palavra.toLowerCase()){
        if (vogais.includes(letra)){
            cont_vogal ++
        }
    }
    return cont_vogal
}

palavra = prompt('Digite uma palavra: ')
alert(`A palavra ${palavra} possui ${contar_vogais(palavra)} vogais`)*/

// DESAFIO
const maiuscula = 'ABCDEFGHIJLKMNOPQRSTUVWXZ'
const minuscula = 'abcdefghijklmnopqrstuvwxz'
const numero = '0123456789'
const especial = '@&*#/{}][$'

function verificar_senha(senha){
    let cont_req = 0
    //requisito 1: ter 8  ou mais caracteres
    if (senha.length >= 8){
        cont_req++
    }

    //requisito 2: 1 MAIUSCULA
    for(char of senha){
        if (maiuscula.includes(char)){
            cont_req++
            break
        }
    }

    //requisito 3: 1 minuscula
    for (char of senha){
        if (minuscula.includes(char)){
            cont_req++
            break
        }
    }

    //requisito 4: 1 número
    for (char of senha){
        if (numero.includes(char)){
            cont_req++
            break
        }
    }

    //requisito 5: 1 char especial
    for (char of senha){
        if (especial.includes(char)){
            cont_req++
            break
        }
    }

    console.log(`Quantidade de requisito atendidos: ${cont_req}`)

    if ( cont_req >= 1 && cont_req <= 2){
        return 'fraca'
    } else if (cont_req >= 3 && cont_req <= 4){
        return 'média'
    } else if (cont_req >= 5){
        return 'forte'
    } else{
        return 'não atende nenhum requisito!'
    }
}
    

senha = prompt('Digite sua senha: ')
alert(`Sua senha é ${verificar_senha(senha)}`)

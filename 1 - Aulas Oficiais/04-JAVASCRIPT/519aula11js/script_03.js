const nomes = ['Mouse','Teclado','Monitor','Gabinete','CD']
const lista = nomes.filter((nome) => {
    return nome.length >= 5
})

console.log(lista)
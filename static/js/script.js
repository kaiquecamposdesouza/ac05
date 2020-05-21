const raiz = document.getElementById('lista');

fetch('/login') // GET por default
.then(res => {return res.json();})
.then(data => {
    data.login.forEach(element => {
        // criamos a linha da tabela
        var linha = document.createElement('tr');
        raiz.appendChild(linha);

        // criamos as colunas
        var nome = document.createElement('td');
        nome.textContent = element.nome;
        linha.appendChild(nome);

        var sobrenome = document.createElement('td');
        sobrenome.textContent = element.sobrenome ;
        linha.appendChild(sobrenome);

        var email = document.createElement('td');
        semail.textContent = element.email ;
        linha.appendChild(email);

        var assunto = document.createElement('td');
        assunto.textContent = element.assunto ;
        linha.appendChild(assubto);

        var mensagem = document.createElement('td');
        assunto.textContent = element.mensagem ;
        linha.appendChild(mensagem);
        
    });
})
.catch( err => {
    console.log('Ocorreu um problema.');
})
.finally(() =>{
    console.log('Linha que sempre aparece no final');
})
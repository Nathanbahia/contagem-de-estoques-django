let contagem = document.querySelector('#contagem');

let body = document.querySelector('body');
let codigo = $('#busca_codigo');
let btn = $('#btn-busca');		
let p1 = document.querySelector('#td_codigo');
let p2 = document.querySelector('#td_produto');
let p3 = document.querySelector('#td_secao');
let p4 = document.querySelector('#td_quantidade');

let msgBox = $('.alert');

$(btn).on('click', function () {

    $(msgBox).hide(200);
    $(contagem).focus();

    p1.innerHTML = '';
    p2.innerHTML = '';
    p3.innerHTML = '';
    p4.innerHTML = '';
    let cod = $(codigo).val();			
    for (let i = 0; i < dados.length; i++) {
        if (cod === dados[i]['Cod']) {					
            p1.innerHTML = dados[i]['Cod'];
            p2.innerHTML = dados[i]['Produto'];
            p3.innerHTML = dados[i]['Secao'];
            p4.innerHTML = dados[i]['Quantidade'];
            return;
        } 				  		    
    }
    alert('Produto não localizado!');
})

let btn_form = $('#btn-adiciona');
let form = $('#formulario');

$(form).on('submit', function (e) {
    try {
        let cod_ = document.querySelector('#codigo');
        let nome_ = document.querySelector('#nome');
        let secao_ = document.querySelector('#secao');
        let qtde_ = document.querySelector('#qtde');

            cod_.value = p1.innerHTML;
            nome_.value = p2.innerHTML;
            secao_.value = p3.innerHTML;
            qtde_.value = p4.innerHTML;

        if (cod_.value != '' && nome_.value != '' && secao_.value != '' && qtde_.value != '') {
            form.submit();
            } else {
            e.preventDefault();
            alert('Dados inconsistentes...');
            }
    }

    catch (e) {
        console.log('Dados inconsistentes...');
    }

});
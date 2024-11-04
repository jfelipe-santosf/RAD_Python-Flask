document.getElementById('search_id').addEventListener('submit', function(event){
    event.preventDefault();
    var identifier = document.getElementById('identifier').value;

    var datas = {
        id: identifier
    };
    console.log(datas)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/searchid',{
        method:'GET',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
});

document.getElementById('listbydate').addEventListener('submit', function(event){
    event.preventDefault();
    var date1 = document.getElementById('date_min').value;
    var date2 = document.getElementById('date_max').value;

    var datas = {
        date_min: date1,
        date_max: date2
    };
    console.log(datas)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/listbydate',{
        method:'GET',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
});

document.getElementById('form_create').addEventListener('submit', function(event){
    event.preventDefault();
    var name = document.getElementById('name').value;
    var data_lancamento = document.getElementById('release_date').value;
    var destino = document.getElementById('destination').value;
    var estado_missao = document.getElementById('mission_state').value;
    var tripulacao = document.getElementById('crew').value;
    var carga_util = document.getElementById('payload').value;
    var duracao = document.getElementById('mission_duration').value;
    var custo = document.getElementById('mission_cost').value;
    var descricao = document.getElementById('description').value;

    var datas = {
        name: name,
        release_date: data_lancamento,
        destination: destino,
        mission_state: estado_missao,
        crew: tripulacao,
        payload: carga_util,
        mission_duration: duracao,
        mission_cost: custo,
        description: descricao
    };
    console.log(datas)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/create',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
});

document.getElementById('form_update').addEventListener('submit', function(event){
    event.preventDefault();
    var identifier = document.getElementById('identifier').value;
    var name = document.getElementById('name').value;
    var data_lancamento = document.getElementById('release_date').value;
    var destino = document.getElementById('destination').value;
    var estado_missao = document.getElementById('mission_state').value;
    var tripulacao = document.getElementById('crew').value;
    var carga_util = document.getElementById('payload').value;
    var duracao = document.getElementById('mission_duration').value;
    var custo = document.getElementById('mission_cost').value;
    var descricao = document.getElementById('description').value;

    var datas = {
        id: identifier,
        name: name,
        release_date: data_lancamento,
        destination: destino,
        mission_state: estado_missao,
        crew: tripulacao,
        payload: carga_util,
        mission_duration: duracao,
        mission_cost: custo,
        description: descricao
    };
    console.log(datas)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/update',{
        method:'PUT',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
});

document.getElementById('delete').addEventListener('submit', function(event){
    event.preventDefault();
    var deleteid = document.getElementById('delete').value;

    var datas = {
        id: deleteid
    };
    console.log(datas)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:5000/delete',{
        method:'DELETE',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datas)
    })
    // tratamento da resposta da requisição
    .then(response => response.text())
    .catch(error =>{
        //exibir mensagem de erro
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
});
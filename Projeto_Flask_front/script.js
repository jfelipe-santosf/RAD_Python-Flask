document.addEventListener("DOMContentLoaded", function() {
    listatabela(); // Chama a função para carregar a lista automaticamente
});

function listatabela(){
    let tbody = document.getElementById('tbody');
    tbody.innerHTML = ""; // Limpa o tbody antes de adicionar as novas linhas

    fetch('http://127.0.0.1:5000/list')
        .then(response => response.json())
        .then(list_all => {
            list_all.forEach(mission => {
                let tr = tbody.insertRow();

                let td_id = tr.insertCell();
                let td_name = tr.insertCell();
                let td_releaseDate = tr.insertCell();
                let td_destination = tr.insertCell();
                let td_missionState = tr.insertCell();

                td_id.innerText = mission.id;
                td_name.innerText = mission.name;
                td_releaseDate.innerText = mission.release_date;
                td_destination.innerText = mission.destination;
                td_missionState.innerText = mission.mission_state;
            });
        })
        .catch(error => {
            console.error("Erro ao carregar a lista:", error);
            alert("Erro ao carregar a lista de missões.");
        });
}

function Searchbyid(event) {
    event.preventDefault();
    var identifier = document.getElementById('identifier').value;

    fetch(`http://127.0.0.1:5000/searchid?id=${identifier}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => {
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
}

function Listbydate(event) {
    event.preventDefault();
    var date1 = document.getElementById('date_min').value;
    var date2 = document.getElementById('date_max').value;

    fetch(`http://127.0.0.1:5000/listbydate?date_min=${date1}&date_max=${date2}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => {
        alert('Erro ao processar a requisição.');
        console.log('Erro', error);
    });
}

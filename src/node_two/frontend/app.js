document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('name-form');
    const personNameInput = document.getElementById('person_name');
    const sharedPersonName = document.getElementById('shared-person-name');
    const account_nume = document.getElementById('account_number')

    let socket;

    try {
        socket = new WebSocket('ws://localhost:8070/');

        socket.onopen = (event) => {
            console.log('WebSocket connected---:', event);
        };
        console.log('122222222222222222222222')
        form.addEventListener('submit', async function (e) {
            e.preventDefault();
             console.log("_+==========================")
            const personName = personNameInput.value;
            const accountNumber = account_nume.value;
            console.log(account_nume , "_-----------------")
            socket.send(JSON.stringify({ person_name: personName, account_number : accountNumber }));
        });

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            // console.log("++++++++++++++++++++++++++++++")
            if (data.person_names) {
                console.log(data.person_names, "*******************")
                console.log(data.account_number, "*******************")
                sharedPersonName.textContent = data.person_names.join(', ');
            
                let tableHTML = createTable(data.person_names, data.account_number.reverse());

                // Inject the table into an element with the id 'table-container'
                document.getElementById('table-container').innerHTML = tableHTML;
            }
        };
    } catch (error) {
        console.error('Error creating WebSocket:', error);
    }
});


function createTable(personNames, accountNumbers) {
    let table = '<table><tr><th>person_name</th><th>account_number</th></tr>';
    for (let i = 0; i < personNames.length; i++) {
        table += '<tr><td>' + personNames[i] + '</td><td>' + accountNumbers[i] + '</td></tr>';
    }
    table += '</table>';
    return table;
}

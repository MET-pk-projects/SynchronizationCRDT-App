document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('name-form');
    const personNameInput = document.getElementById('person_name');
    const sharedPersonName = document.getElementById('shared-person-name');
    const accountNumberInput = document.getElementById('account_number');

    let socket;

    try {
        socket = new WebSocket('ws://localhost:8070/');

        socket.onopen = (event) => {
            console.log('WebSocket connected:', event);
        };

        form.addEventListener('submit', async function (e) {
            e.preventDefault();
            const personName = personNameInput.value;
            const accountNumber = accountNumberInput.value;
            socket.send(JSON.stringify({ person_name: personName, account_number: accountNumber }));
        });

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.person_names) {
                sharedPersonName.textContent = data.person_names.join(', ');
                let tableHTML = createTable(data.person_names, data.account_number.reverse());
                document.getElementById('table-container').innerHTML = tableHTML;
            }
        };
    } catch (error) {
        console.error('Error creating WebSocket:', error);
    }
});

function createTable(personNames, accountNumbers) {
    let table = '<div class="data-table"><table><tr><th>person_name</th><th>account_number</th></tr>';
    for (let i = 0; i < personNames.length; i++) {
        table += '<tr><td>' + personNames[i] + '</td><td>' + accountNumbers[i] + '</td></tr>';
    }
    table += '</table></div>';
    return table;
}

document.addEventListener('DOMContentLoaded', function(event) {
    
    var filePath
    let title = document.querySelector("title")
    console.log(window.location.href)
    if(window.location.href == "http://127.0.0.1:5000/temprature")    
    {
        filePath = '/static/predicted/T.csv'; 
        title.innerHTML = "Temprature CSV Data"
    }else if(window.location.href == "http://127.0.0.1:5000/absolute_humidity")
        {
            filePath = '/static/predicted/AH.csv'; 
            title.innerHTML = "Absoulute Humidity CSV Data"
            
        }
        else if(window.location.href == "http://127.0.0.1:5000/relative_humidity"){
            filePath = '/static/predicted/RH.csv'; 
            title.innerHTML = "Relative Humidity CSV Data"
    }
    else{
        window.location.href = "/"
    }
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(text => {
            const data = parseCSV(text);
            generateTable(data);
        })
        .catch(error => console.error('Error fetching CSV file:', error));
});

function parseCSV(text) {
    const lines = text.split('\n');
    return lines.map(line => line.split(','));
}

function generateTable(data) {
    const tableHead = document.querySelector('#csvTable thead');
    const tableBody = document.querySelector('#csvTable tbody');

    tableHead.innerHTML = '';
    tableBody.innerHTML = '';

    if (data.length > 0) {
        const headers = data[0];
        const headerRow = document.createElement('tr');
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        tableHead.appendChild(headerRow);

        for (let i = 1; i < data.length; i++) {
            const row = data[i];
            const tableRow = document.createElement('tr');
            row.forEach(cell => {
                const td = document.createElement('td');
                td.textContent = cell;
                tableRow.appendChild(td);
            });
            tableBody.appendChild(tableRow);
        }
    }
}
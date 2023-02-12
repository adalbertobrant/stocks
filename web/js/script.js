function start(){
  var lines = document.querySelector('#json_data'); 
  
  lines.innerHTML = "";
  //fetch data from local directory
  fetch("./json/stocks_json_12-02-2023.json")
  .then((res) => res.json())
  .then((data) => {
    //create td rows here    
    for (let i = 0; i < data.length; i++){
      const key = Object.keys(data[i]).toString();
      const value = data[i][key].toString();
      console.log(key, value);

      var tr = document.createElement('tr');
      var tdLinesStock = document.createElement('td');
      tdLinesStock.classList.add('lines');
      tdLinesStock.textContent = key;
      
      var tdLinesPrice = document.createElement('td');
      tdLinesPrice.classList.add('lines');
      tdLinesPrice.textContent = "R$ "+parseFloat(value).toFixed(2);

      tr.appendChild(tdLinesStock);
      tr.appendChild(tdLinesPrice);
      lines.appendChild(tr);
      
    }

    makeTable(data);
    
  });
  


}
start();

let makeTable = (data) => {
    // Create the table element
    let table = document.createElement("table");

    // Create table header row
    let headerRow = document.createElement("tr");
    let stockNameHeader = document.createElement("th");
    let stockPriceHeader = document.createElement("th");
    stockNameHeader.innerHTML = "Stock Name";
    stockPriceHeader.innerHTML = "Price";
    headerRow.appendChild(stockNameHeader);
    headerRow.appendChild(stockPriceHeader);
    table.appe
    

    // Process each stock data
    for(let i = 0; i < data.length; i++) {
        // Create table data row
        let row = document.createElement("tr");
        let stockNameColumn = document.createElement("td");
        let stockPriceColumn = document.createElement("td");
        const key = Object.keys(data[i]).toString();
        const value = data[i][key].toString();
        stockNameColumn.innerHTML = key;
        stockPriceColumn.innerHTML = value;
        row.appendChild(stockNameColumn);
        row.appendChild(stockPriceColumn);
        table.appendChild(row);
    }

    // Return the table element
    return table;
};





  
  


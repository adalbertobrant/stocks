function start() {
  alert("ATENÇÃO: As informações apresentadas neste site não devem ser consideradas como aconselhamento, recomendação, oferta ou solicitação para comprar ou vender ações, títulos, valores mobiliários ou qualquer outro instrumento financeiro. É importante destacar que investimentos envolvem riscos e é responsabilidade do investidor avaliar cuidadosamente suas opções antes de tomar qualquer decisão de investimento. Os dados fornecidas neste site são apenas para fins informativos, educacionais e não garantem a precisão ou integridade dos dados apresentados.")
  // fetch data from local directory
  fetch("./json/stocks_tomorrow.json")
    .then((res) => res.json())
    .then((data) => {
      const container = document.getElementById("container");

      data.forEach((item) => {
        const box = document.createElement("div");
        box.classList.add("box");

        const title = document.createElement("h2");
        title.textContent = item.title;

        const logo = document.createElement("img");
        logo.src = item.logo_link;
        logo.alt = item.title + " logo";

        const price = document.createElement("h2");
        price.textContent = "Closing Price: R$ " + Number(item.price).toFixed(2);

        const link = document.createElement("a");
        link.href = item.link;
        link.textContent = "Learn more";

        box.appendChild(title);
        box.appendChild(logo);
        box.appendChild(price);
        box.appendChild(link);

        container.appendChild(box);
      });
    });
}

start();

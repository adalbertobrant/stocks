function start() {
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

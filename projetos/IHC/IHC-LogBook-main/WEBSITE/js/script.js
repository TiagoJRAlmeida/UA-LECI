(function ($) {
  "use strict";

  // Preloader Initialization
  var initPreloader = function () {
    $(document).ready(function ($) {
      var Body = $("body");
      Body.addClass("preloader-site");
    });
    $(window).load(function () {
      $(".preloader-wrapper").fadeOut();
      $("body").removeClass("preloader-site");
    });
  };

  // Chocolat Lightbox Initialization
  var initChocolat = function () {
    Chocolat(document.querySelectorAll(".image-link"), {
      imageSize: "contain",
      loop: true,
    });
  };

  // Swiper Initialization
  var initSwiper = function () {
    new Swiper(".main-swiper", {
      speed: 500,
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

    new Swiper(".category-carousel", {
      slidesPerView: 6,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".category-carousel-next",
        prevEl: ".category-carousel-prev",
      },
      breakpoints: {
        0: { slidesPerView: 2 },
        768: { slidesPerView: 3 },
        991: { slidesPerView: 4 },
        1500: { slidesPerView: 6 },
      },
    });

    new Swiper(".products-carousel", {
      slidesPerView: 5,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".products-carousel-next",
        prevEl: ".products-carousel-prev",
      },
      breakpoints: {
        0: { slidesPerView: 1 },
        768: { slidesPerView: 3 },
        991: { slidesPerView: 4 },
        1500: { slidesPerView: 6 },
      },
    });
  };

  // Quantity Button Logic with Event Delegation
  var initProductQty = function () {
    // Attach event listener to the document or a parent container
    document.addEventListener("click", function (e) {
      // Handle the plus button
      if (e.target.closest(".quantity-right-plus")) {
        e.preventDefault();
        const productQty = e.target.closest(".product-qty");
        const input = productQty.querySelector(".input-number");
        let quantity = parseInt(input.value, 10);
        if (!isNaN(quantity)) {
          input.value = quantity + 1;
        }
      }

      // Handle the minus button
      if (e.target.closest(".quantity-left-minus")) {
        e.preventDefault();
        const productQty = e.target.closest(".product-qty");
        const input = productQty.querySelector(".input-number");
        let quantity = parseInt(input.value, 10);
        if (!isNaN(quantity) && quantity > 1) {
          input.value = quantity - 1;
        }
      }
    });
  };

  // Postal Code Location Display
  var initPostalCodeDisplay = function () {
    // Find the postal code input field
    const postalCodeInput = document.querySelector('input[placeholder="Código Postal"]');
    
    if (!postalCodeInput) {
      console.warn('Postal code input not found');
      return;
    }

    // Create location display element
    const locationDisplay = document.createElement('span');
    locationDisplay.className = 'postal-location-display ms-2 me-3 text-muted';
    locationDisplay.style.fontSize = '0.875rem';
    locationDisplay.style.display = 'none';
    
    // Insert the location display after the postal code input
    postalCodeInput.parentNode.insertBefore(locationDisplay, postalCodeInput.nextSibling);

    // Postal code to location mapping
    const postalCodeMap = {
      '3810-516': 'Aveiro'
      // Add more postal codes and locations as needed
      // '1000-001': 'Lisboa',
      // '4000-001': 'Porto'
    };

    // Function to update location display
    function updateLocationDisplay(value) {
      const cleanedValue = value.trim();
    
      // ✅ Save to localStorage so produto.html can access it
      localStorage.setItem('codigo_postal', cleanedValue);
    
      if (postalCodeMap[cleanedValue]) {
        locationDisplay.textContent = postalCodeMap[cleanedValue];
        locationDisplay.style.display = 'inline';
      } else {
        locationDisplay.style.display = 'none';
      }
    }
    

    // Add event listeners
    postalCodeInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault(); // Prevent form submission if inside a form
        updateLocationDisplay(e.target.value);
      }
    });

    postalCodeInput.addEventListener('blur', function(e) {
      updateLocationDisplay(e.target.value);
    });

    // Check initial value if any (only if user presses Enter or loses focus)
    // Removed automatic checking of initial value
  };

  // Fetch and Render Featured Products
  var renderFeaturedProducts = function () {
    const container = document.getElementById("featured-container");

    fetch("data/produtos.json")
      .then((res) => res.json())
      .then((produtos) => {
        const destaques = produtos.filter((p) => p.destaque);

        container.innerHTML = destaques
          .map((p) => `
          <div class="product-item swiper-slide">
            <a href="produto.html?id=${p.id}" class="btn-wishlist">
              <svg width="24" height="24"><use xlink:href="#heart"></use></svg>
            </a>
            <figure>
              <a href="produto.html?id=${p.id}" title="${p.nome}">
                <img src="${p.imagem}" class="tab-image" alt="${p.nome}">
              </a>
            </figure>
            <h3>${p.nome}</h3>
            <span class="qty">1 Unidade</span>
            <span class="rating">
              <svg width="24" height="24" class="text-primary"><use xlink:href="#star-solid"></use></svg> 4.5
            </span>
            <span class="price">€ ${parseFloat(p.preco).toFixed(2)}</span>
            <div class="d-flex align-items-center justify-content-between">
              <div class="input-group product-qty">
                <span class="input-group-btn">
                  <button type="button" class="quantity-left-minus btn btn-danger btn-number" data-type="minus">
                    <svg width="16" height="16"><use xlink:href="#minus"></use></svg>
                  </button>
                </span>
                <input type="text" name="quantity" class="form-control input-number" value="1">
                <span class="input-group-btn">
                  <button type="button" class="quantity-right-plus btn btn-success btn-number" data-type="plus">
                    <svg width="16" height="16"><use xlink:href="#plus"></use></svg>
                  </button>
                </span>
              </div>
            
              <a href="#comparador-panel" class="nav-link" onclick="adicionarAoComparador(${JSON.stringify(p).replace(/"/g, "&quot;")})">
                Comparar<iconify-icon icon="uil:shopping-cart"></iconify-icon>
              </a>
            </div>
          </div>
        `
          )
          .join("");

        // Reinitialize Swiper for Featured Products
        new Swiper(".products-carousel", {
          slidesPerView: 1,
          spaceBetween: 20,
          navigation: {
            nextEl: ".products-carousel-next",
            prevEl: ".products-carousel-prev",
          },
          breakpoints: {
            576: { slidesPerView: 2 },
            768: { slidesPerView: 3 },
            992: { slidesPerView: 4 },
            1200: { slidesPerView: 5 },
          },
        });
      })
      .catch((err) => {
        console.error("Erro ao carregar produtos de destaque:", err);
        container.innerHTML =
          '<p class="text-muted">Não foi possível carregar os produtos de destaque.</p>';
      });
  };

  // Document Ready
  $(document).ready(function () {
    initPreloader();
    initSwiper();
    initProductQty();
    initChocolat();
    renderFeaturedProducts();
    initPostalCodeDisplay(); // Added postal code functionality
  });
})(jQuery);

let comparador = [];

function adicionarAoComparador(produto) {
  const existe = comparador.find(p => p.loja === produto.loja && p.nome === produto.nome);

  if (existe) {
    mostrarToast("Este produto já está no comparador.");
    return;
  }

  comparador.push(produto);
  atualizarComparador();
  mostrarToast("Produto adicionado ao comparador.");
}

// Make the function globally accessible
window.adicionarAoComparador = adicionarAoComparador;

// Extrai número do preço para comparações
function parsePreco(precoStr) {
  return parseFloat(precoStr.replace('€','').replace(',', '.'));
}

// Remove um item do comparador e atualiza a vista
function removerDoComparador(i) {
  comparador.splice(i, 1);
  atualizarComparador();
}

function atualizarComparador() {
  const container = document.getElementById("comparador-panel-body");
  container.innerHTML = "";

  if (comparador.length === 0) {
    container.innerHTML = "<p>Nenhum produto no comparador.</p>";
    return;
  }

  // Se só há 1, mostra card com botão "Remover"
  if (comparador.length === 1) {
    abrirComparador();
    const p = comparador[0];
    container.innerHTML = `
      <div class="card mb-3">
        <div class="row g-0">
          <div class="col-4 text-center">
            <img src="${p.imagem}" class="img-fluid rounded-start" alt="${p.nome}">
          </div>
          <div class="col-8">
            <div class="card-body">
              <h5 class="card-title">${p.nome}</h5>
              <p class="card-text"><strong>${p.preco}</strong> – ${p.loja}</p>
              ${p.promocao ? `<span class="badge bg-success">${p.promocao}</span><br>` : ""}
              <button class="btn btn-sm btn-outline-danger mt-2" onclick="removerDoComparador(0)">
                Remover
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
    return;
  }

  // ≥2 itens: tabela comparativa
  const atributos = [
    { label: "Nome", key: "nome" },
    { label: "Preço", key: "preco" },
    { label: "Loja", key: "loja" },
    { label: "Promoção", key: "promocao" }
  ];

  // Destacar preço mais barato
  const precos = comparador.map(p => parsePreco(p.preco));
  const minPreco = Math.min(...precos);

  let html = `
    <table class="table table-bordered text-center">
      <thead class="table-light">
        <tr>
          <th>Atributo</th>
          ${comparador.map((p, i) => `
            <th>
              ${p.nome}
              <button class="btn-close btn-close-red" aria-label="Remover" onclick="removerDoComparador(${i})"></button>
            </th>
          `).join("")}
        </tr>
      </thead>
      <tbody>
  `;

  atributos.forEach(attr => {
    html += `<tr>
      <th scope="row">${attr.label}</th>`;
    comparador.forEach(p => {
      let valor = p[attr.key] || "—";
      let classe = "";
      if (attr.key === "preco" && parsePreco(p.preco) === minPreco) {
        classe = "table-success";
      }
      html += `<td class="${classe}">${valor}</td>`;
    });
    html += `</tr>`;
  });

  html += `</tbody></table>`;
  container.innerHTML = html;
}

function abrirComparador() {
  document.getElementById("comparador-panel").classList.add("aberto");
}

function fecharComparador() {
  document.getElementById("comparador-panel").classList.remove("aberto");
}

function mostrarToast(mensagem) {
  const toast = document.getElementById("toast");
  toast.textContent = mensagem;
  toast.classList.add("show");

  setTimeout(() => {
    toast.classList.remove("show");
  }, 2500);
}
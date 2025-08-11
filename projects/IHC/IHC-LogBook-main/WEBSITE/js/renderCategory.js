// js/renderCategory.js

document.addEventListener('DOMContentLoaded', () => {
  console.log('🚀 renderCategory.js carregado');

  // 1) Captura a categoria da URL
  const params      = new URLSearchParams(window.location.search);
  const categoria   = params.get('nome');
  console.log('🍂 categoria lida do URL:', categoria);
  const titleEl     = document.getElementById('category-title');
  const nameEl      = document.getElementById('category-name');
  const filtersRoot = document.getElementById('filters-container');
  const container   = document.getElementById('category-container');
  const sortSelect  = document.getElementById('sort-select');

  if (!categoria) {
    container.innerHTML = '<div class="col-12"><p class="text-center text-danger">Categoria não informada.</p></div>';
    return;
  }
  titleEl.textContent = categoria;
  nameEl .textContent = categoria;

  // 2) Configurações de filtros por categoria
  const defaultFilters = [
    { type: 'search', id: 'filter-search',    placeholder: 'Pesquisar produtos...' },
    { type: 'number', id: 'filter-min-price', label: 'Preço Mínimo',   placeholder: '0' },
    { type: 'number', id: 'filter-max-price', label: 'Preço Máximo',   placeholder: '100' }
  ];

  const filterConfigs = {
    'Frutas & Legumes': [
      { type: 'search', id: 'filter-search',    placeholder: 'Pesquisar frutas...' },
      { type: 'number', id: 'filter-min-price', label: 'Preço Mínimo',   placeholder: '0' },
      { type: 'number', id: 'filter-max-price', label: 'Preço Máximo',   placeholder: '100' },
      { type: 'select', id: 'filter-season',    label: 'Sazonalidade',   options: ['Todas','Verão','Outono','Inverno','Primavera'] },
      { type: 'select', id: 'filter-discount',  label: 'Desconto',       options: ['Sim','Não'] },
      { type: 'select', id: 'filter-bio',       label: 'Bio',            options: ['Sim','Não'] }
    ],
    'Padaria': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] }
    ],
    'Higiene & Beleza': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: ['Cabelo','Corpo','Rosto','Maquilhagem','Higiene Oral','Higiene Íntima','Preservativos e Estimuladores','Lentes e Cuidados de Saúde','Papel Higiénico']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
    ],
    'Bebidas': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: ['Sumos e Refrigerantes','Água','Bebidas Energéticas e Isotónicas','Cervejas e Sidras','Vinhos','Bebidas Espirituosas','Champanhe e Espumante']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-sugar',       label: 'Produto Sem Açúcar', options:  ['Sim','Não'] },
    ],
    'Charcutaria': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: ['Novilho, Vitela e Vitelão','Frango e Peru','Porco','Pato e Coelho','Cabrito e Borrego']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] }
    ],
    'Bio & Saudável': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: ['Nutrição Desportiva','Vegetariano e Vegan','Biológicos','Sem Glúten','Sem Lactose']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-sugar',       label: 'Produto Sem Açúcar', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-lactose',     label: 'Produto Sem Lactose', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegan',       label: 'Produto Vegan', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegetariano', label: 'Produto Vegetariano', options:  ['Sim','Não'] }
    ],
    'Congelados': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: [ 'Frutas e Legumes','Batata Frita e Puré','Nuggets e Crocantes','Douradinhos e Filetes','Hambúrgueres e Almôndegas','Peixe, Marisco e Carne','Pizzas','Refeições Prontas','Salgados, Folhados e Pastelaria','Vegetariano e Vegan','Sobremesas']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-sugar',       label: 'Produto Sem Açúcar', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-lactose',     label: 'Produto Sem Lactose', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegan',       label: 'Produto Vegan', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegetariano', label: 'Produto Vegetariano', options:  ['Sim','Não'] }
    ],
    'Laticínios & Ovos': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar laticínios...' },
      { type: 'select',   id: 'filter-type',  label: 'Tipo', options: [ 'Leite','Iogurtes','Ovos','Manteigas e Cremes para Barrar','Natas e Bechamel','Bebidas Vegetais','Sobremesas','Queijos']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-fat',         label: '% Gordura',    options: ['Todas','0%','1.5%','3.2%','Integral'] },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-sugar',       label: 'Produto Sem Açúcar', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-lactose',     label: 'Produto Sem Lactose', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegan',       label: 'Produto Vegan', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegetariano', label: 'Produto Vegetariano', options:  ['Sim','Não'] }
    ],
    'Animais': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',        label: 'Tipo', options: [ ]}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      {
      type:    'select',
      id:      'filter-type',
      label:   'Tipo',
      options: [
        'Cão',
        'Gato',
        'Outros Animais',
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-porte',
      label:   'Porte',
      options: [
        'Porte Pequeno',
        'Porte Médio',
        'Porte Grande'
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-idade',
      label:   'Idade Recomendada',
      options: [
        'Júnior',
        'Adulto',
        'Sénior'
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-ingrediente',
      label:   'Ingrediente Principal',
      options: [
        'Aves',
        'Peixe',
        'Vaca',
        'Cereais',
        'Borrego',
        'Outros'
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-necessidades',
      label:   'Necessidades Específicas',
      options: [
        'Pele e Pelo',
        'Controlo de Peso',
        'Trato Renal e Urinário',
        'Esterilizado',
        'Higiene Oral',
        'Natural'
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-nutricao',
      label:   'Nutrição',
      options: [
        'Light',
        'Sem Cereais'
      ]
    },
    {
      type:    'checkbox-inline',
      id:      'filter-quantidade',
      label:   'Quantidade',
      options: [
        'até 100 gr',
        '100 gr – 300 g',
        '300 g – 1 kg',
        '1 – 2 kg',
        '2 – 4 kg',
        '4 – 10 kg',
        '+10 kg',
        'Packs'
      ]
      }
    ],
    'Limpeza': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',  label: 'Tipo', options: [ 'Roupa','Cozinha','Casa de Banho','Limpeza Geral','Papel Higiénico','Guardanapos e Rolos','Velas e Ambientadores','Sacos e Baldes do Lixo','Mopas, Esfregonas e Vassouras','Panos, Esfregonas e Luvas','Inseticidas e Desumidificadores','Limpeza Auto e Motos']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
    ],
    'Casa, Bricolage & Jardim': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',  label: 'Tipo', options: ['Jardim e Praia',
      'Mobiliário e Colchões',
      'Têxtil Lar',
      'Decoração e Banho',
      'Cozinha',
      'Mesa',
      'Eletrodomésticos',
      'Lavandaria e Organização',
      'Festa',
      'Pilhas e Lâmpadas',
      'Bricolage']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
    ],
    'Mercearia': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar ' },
      { type: 'select',   id: 'filter-type',  label: 'Tipo', options: [ 'Café, Chá e Bebidas Solúveis',
        'Cereais e Barras',
        'Bolachas, Biscoitos e Tostas',
        'Chocolate, Gomas e Rebuçados',
        'Arroz, Massa e Farinha',
        'Azeite, Óleo e Vinagre',
        'Conservas',
        'Molhos, Temperos e Sal',
        'Snacks e Batatas Fritas',
        'Compotas, Cremes e Mel',
        'Açúcar e Sobremesas',
        'Alimentação Infantil']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
      { type: 'select',   id: 'filter-bio',         label: 'Produto Biológico', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-gluten',      label: 'Produto Sem Glúten', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-sugar',       label: 'Produto Sem Açúcar', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-lactose',     label: 'Produto Sem Lactose', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegan',       label: 'Produto Vegan', options:  ['Sim','Não'] },
      { type: 'select',   id: 'filter-vegetariano', label: 'Produto Vegetariano', options:  ['Sim','Não'] }
    ],
    'Bebé': [
      { type: 'search',   id: 'filter-search',      placeholder: 'Pesquisar' },
      { type: 'select',   id: 'filter-type',  label: 'Tipo', options: ['Fraldas e Toalhitas',
        'Banho e Higiene',
        'Alimentação e Acessórios',
        'Leites em Pó e Bebidas Lácteas',
        'Cadeiras Auto',
        'Passeio e Viagem',
        'Quarto',
        'Brinquedos e Livraria',
        'Amamentação',
        'Higiene Íntima']}, 
      { type: 'number',   id: 'filter-min-price',   label: 'Preço Mínimo', placeholder: '0' },
      { type: 'number',   id: 'filter-max-price',   label: 'Preço Máximo', placeholder: '100' },
      { type: 'select',   id: 'filter-discount',    label: 'Desconto', options: ['Sim','Não'] },
    ]
  };
  const configs = filterConfigs[categoria] || defaultFilters;

  // 3) Cria controles de filtro
  function createFilterControls() {
    filtersRoot.innerHTML = '';
    configs.forEach(f => {
      let wrapper = document.createElement('div');
      wrapper.className = 'filter-card mb-3';

      // header com toggle
      const header = document.createElement('div');
      header.className = 'filter-card__header';
      header.innerHTML = `<h3>${f.label || f.placeholder}</h3><button class="toggle-btn" aria-label="Expandir/colapsar"></button>`;
      wrapper.append(header);

      // corpo
      const body = document.createElement('div');
      body.className = 'filter-card__body';
      let el;
      switch(f.type) {
        case 'search':
          el = document.createElement('input');
          el.type = 'search'; el.id = f.id; el.placeholder = f.placeholder;
          el.className = 'filter-input form-control';
          break;
        case 'number':
          el = document.createElement('input');
          el.type = 'number'; el.id = f.id; el.placeholder = f.placeholder;
          el.className = 'filter-input form-control';
          break;
        case 'select':
          el = document.createElement('select');
          el.id = f.id; el.className = 'form-select';
          f.options.forEach(opt => {
            const o = document.createElement('option');
            o.value = opt === 'Todas' ? '' : opt;
            o.textContent = opt;
            el.appendChild(o);
          });
          break;
        case 'checkbox-inline':
          el = document.createElement('div');
          el.className = 'd-flex flex-wrap gap-2';
          f.options.forEach(opt => {
            const chkWrapper = document.createElement('div');
            chkWrapper.className = 'form-check form-check-inline';
            const input = document.createElement('input');
            input.type = 'checkbox'; input.name = f.id; input.value = opt;
            input.id = `${f.id}_${opt.replace(/\W/g,'')}`;
            input.className = 'form-check-input';
            const label = document.createElement('label');
            label.htmlFor = input.id; label.className = 'form-check-label';
            label.textContent = opt;
            chkWrapper.append(input, label);
            el.appendChild(chkWrapper);
          });
          break;
      }
      if (el) body.appendChild(el);
      wrapper.appendChild(body);
      filtersRoot.appendChild(wrapper);

      // adiciona evento de toggle
      header.addEventListener('click', () => wrapper.classList.toggle('collapsed'));
    });
  }

  // 4) Renderiza lista de produtos
  function renderList(list) {
    if (!list.length) {
      container.innerHTML = '<div class="col-12"><p class="text-center text-muted">Nenhum produto encontrado.</p></div>';
      return;
    }
    container.innerHTML = list.map(p => `
      <div class="col-md-4">
        <div class="product-item">
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
      </div>
    `).join('');
  }

  // 5) Aplica filtros e ordenação
  function applyFilters() {
    console.log('Aplicando filtros...');
    let filtered = allProducts.slice();
    
    // Apply filters
    configs.forEach(f => {
        if (['search', 'number', 'select'].includes(f.type)) {
            const el = document.getElementById(f.id);
            if (!el) return;
            
            const val = el.value.trim();
            if (!val) return;  // Ignora filtros vazios

            if (f.type === 'search') {
                const valLower = val.toLowerCase();
                filtered = filtered.filter(p => 
                    p.nome.toLowerCase().includes(valLower) || 
                    (p.descricao && p.descricao.toLowerCase().includes(valLower))
                );
            } 
            else if (f.type === 'number') {
                const num = parseFloat(val.replace(',', '.'));
                if (!isNaN(num)) {
                    filtered = filtered.filter(p => {
                        const price = parseFloat(String(p.preco).replace(',', '.'));
                        return f.id.includes('min') ? price >= num : price <= num;
                    });
                }
            } 
            else if (f.type === 'select') {
                const field = f.id.replace('filter-', '');
                // Só filtra se o campo existir no produto
                if (filtered.some(p => field in p)) {
                    filtered = filtered.filter(p => 
                        p[field] && String(p[field]).toLowerCase() === val.toLowerCase()
                    );
                }
            }
        }
    });

    // Apply sorting
    const order = sortSelect.value;
    if (filtered.length > 0) {
        if (order === 'price-asc') {
            filtered.sort((a, b) => parseFloat(a.preco.replace(',', '.')) - parseFloat(b.preco.replace(',', '.')));
        } 
        else if (order === 'price-desc') {
            filtered.sort((a, b) => parseFloat(b.preco.replace(',', '.')) - parseFloat(a.preco.replace(',', '.')));
        }
    }

    renderList(filtered);
  }

  // 6) Inicialização: carregar filtros e dados
  let allProducts = [];
  createFilterControls();
  sortSelect.addEventListener('change', applyFilters);

  configs.forEach(f => {
    if (f.type === 'checkbox-inline') {
      document.querySelectorAll(`input[name="${f.id}"]`).forEach(chk => chk.addEventListener('change', applyFilters));
    } else {
      const el = document.getElementById(f.id);
      if (el) el.addEventListener('input', applyFilters);
    }
  });

  fetch('data/produtos.json')
  .then(res => res.json())
  .then(all => {
    console.log('🔍 Lista completa de produtos:');
    console.table(all, ['id','nome','categoria','subcategoria']);
    
    allProducts = all.filter(p => p.categoria === categoria);
    console.log('✅ produtos após filtro:', allProducts);
    renderList(allProducts);
  })
  .catch(console.error);


});

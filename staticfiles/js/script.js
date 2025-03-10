document.addEventListener('DOMContentLoaded', () => {
    // Parallax Effect
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        document.querySelector('.mid-layer').style.transform = 
            `translateY(${scrolled * 0.5}px) translateZ(1px) scale(0.99)`;
    });

    

    // Dynamic Category Generation
    const categories = [
        {icon: 'fa-tractor', title: 'Maquinário', items: ['Tratores', 'Colheitadeiras', 'Plantadeiras']},
        {icon: 'fa-seedling', title: 'Sementes', items: ['Grãos', 'Hortaliças', 'Forrageiras']},
        {icon: 'fa-flask', title: 'Fertilizantes', items: ['Orgânicos', 'Minerais', 'Líquidos']},
        {icon: 'fa-tint', title: 'Irrigação', items: ['Gotejamento', 'Aspersores', 'Bombas']},
        {icon: 'fa-shield-alt', title: 'Proteção', items: ['EPIs', 'Pulverizadores', 'Sinalização']},
        {icon: 'fa-leaf', title: 'Orgânicos', items: ['Adubos', 'Defensivos', 'Sementes']},
        {icon: 'fa-microscope', title: 'Laboratório', items: ['Análise de Solo', 'Sementes', 'Tecidos']},
        {icon: 'fa-solar-panel', title: 'Energia', items: ['Solar', 'Eólica', 'Biomassa']},
        {icon: 'fa-robot', title: 'Automação', items: ['Drones', 'Sensores', 'Controladores']},
        {icon: 'fa-truck', title: 'Logística', items: ['Transporte', 'Armazenagem', 'Embalagens']}
    ];

    const grid = document.querySelector('.grid-container');
    categories.forEach(cat => {
        const card = document.createElement('div');
        card.className = 'category-card';
        card.innerHTML = `
            <div class="card-inner">
                <div class="card-front">
                    <i class="fas ${cat.icon}"></i>
                    <h3>${cat.title}</h3>
                </div>
                <div class="card-back">
                    <ul>${cat.items.map(item => `<li>${item}</li>`).join('')}</ul>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
});

// Hero animation
const floatingIcon = document.querySelector('.floating-icon');
function animateFloating() {
    floatingIcon.animate([
        { transform: 'translateY(0)' },
        { transform: 'translateY(-50px)' },
        { transform: 'translateY(0)' }
    ], {
        duration: 3000,
        iterations: Infinity
    });
}
// animateFloating();
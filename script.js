document.addEventListener('DOMContentLoaded', () => {
    // Pestañas y Secciones
    const jobsTab = document.getElementById('jobs-tab');
    const analysisTab = document.getElementById('analysis-tab');
    const aboutTab = document.getElementById('about-tab');
    const jobsSection = document.getElementById('jobs-section');
    const analysisSection = document.getElementById('analysis-section');
    const aboutSection = document.getElementById('about-section');
    const jobsContainer = document.getElementById('jobs-container');

    // Contenedores de Análisis
    const locationAnalysis = document.getElementById('analysis-location');
    const salaryAnalysis = document.getElementById('analysis-salary');
    const companyAnalysis = document.getElementById('analysis-company');
    const roleAnalysis = document.getElementById('analysis-role');
    const recencyAnalysis = document.getElementById('analysis-recency');

    // Función para cambiar de pestaña
    function showSection(sectionToShow, activeTab) {
        [jobsSection, analysisSection, aboutSection].forEach(section => section.classList.add('hidden'));
        [jobsTab, analysisTab, aboutTab].forEach(tab => tab.classList.remove('active'));

        sectionToShow.classList.remove('hidden');
        activeTab.classList.add('active');
    }

    jobsTab.addEventListener('click', () => showSection(jobsSection, jobsTab));
    analysisTab.addEventListener('click', () => showSection(analysisSection, analysisTab));
    aboutTab.addEventListener('click', () => showSection(aboutSection, aboutTab));

    // Cargar y procesar datos
    fetch('computrabajo_jobs.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al cargar el archivo JSON: ${response.statusText}`);
            }
            return response.json();
        })
        .then(jobs => {
            displayJobs(jobs);
            performAnalysis(jobs);
        })
        .catch(error => {
            console.error('Error al procesar el archivo JSON:', error);
            jobsContainer.innerHTML = '<p>Ocurrió un error al cargar las ofertas. Intenta de nuevo.</p>';
        });

    // Función para mostrar los trabajos
    function displayJobs(jobs) {
        if (!jobs || jobs.length === 0) {
            jobsContainer.innerHTML = '<p>No se encontraron ofertas de trabajo.</p>';
            return;
        }

        jobs.forEach(job => {
            const jobCard = document.createElement('div');
            jobCard.classList.add('job-card');
            jobCard.innerHTML = `
                <h3>${job.title}</h3>
                <p><strong>Empresa:</strong> ${job.empresa || 'No especificada'}</p>
                <p><strong>Ubicación:</strong> ${job.location}</p>
                <p><strong>Salario:</strong> ${job.salario || 'No especificado'}</p>
                <p><strong>Publicado:</strong> ${job.date}</p>
                <a href="${job.link}" target="_blank">Ver oferta</a>
            `;
            jobsContainer.appendChild(jobCard);
        });
    }

    // Función para realizar y mostrar los análisis
    function performAnalysis(jobs) {
        if (!jobs || jobs.length === 0) {
            analysisSection.innerHTML = '<p>No hay datos suficientes para realizar un análisis.</p>';
            return;
        }

        // 1. Análisis de Ubicación
        const locations = jobs.map(job => job.location.split(',')[0].trim());
        const locationCounts = countOccurrences(locations);
        renderList(locationAnalysis, locationCounts);

        // 2. Análisis Salarial
        const salaries = jobs.map(job => job.salario).filter(s => s && s.includes('$'));
        if (salaries.length > 0) {
            const numericSalaries = salaries.map(s => parseFloat(s.replace(/[^\d.-]/g, '')));
            const avgSalary = numericSalaries.reduce((a, b) => a + b, 0) / numericSalaries.length;
            const minSalary = Math.min(...numericSalaries);
            const maxSalary = Math.max(...numericSalaries);
            salaryAnalysis.innerHTML = `<p>De las ${salaries.length} ofertas que especifican un salario:</p>
                                        <ul>
                                            <li>Salario Promedio: <strong>$${avgSalary.toFixed(2)}</strong></li>
                                            <li>Salario Mínimo: <strong>$${minSalary.toFixed(2)}</strong></li>
                                            <li>Salario Máximo: <strong>$${maxSalary.toFixed(2)}</strong></li>
                                        </ul>`;
        } else {
            salaryAnalysis.innerHTML = '<p>No hay suficientes datos de salarios para un análisis significativo.</p>';
        }

        // 3. Análisis de Empresas
        const companies = jobs.map(job => job.empresa).filter(c => c && c !== 'Empresa no especificada');
        const companyCounts = countOccurrences(companies);
        renderList(companyAnalysis, companyCounts, ' contrataciones');

        // 4. Análisis de Roles
        const roles = jobs.map(job => job.title.toLowerCase());
        const roleCounts = countOccurrences(roles);
        renderList(roleAnalysis, roleCounts, ' menciones');

        // 5. Análisis de Recencia
        const recency = jobs.map(job => job.date.trim());
        const recencyCounts = countOccurrences(recency);
        renderList(recencyAnalysis, recencyCounts, ' ofertas');
    }

    // --- Funciones de Utilidad para Análisis ---

    function countOccurrences(arr) {
        return arr.reduce((acc, curr) => {
            acc[curr] = (acc[curr] || 0) + 1;
            return acc;
        }, {});
    }

    function renderList(container, counts, suffix = '') {
        const sortedCounts = Object.entries(counts).sort(([,a],[,b]) => b - a);
        
        if (sortedCounts.length === 0) {
            container.innerHTML = '<p>No hay datos para mostrar.</p>';
            return;
        }
        
        const ul = document.createElement('ul');
        sortedCounts.forEach(([item, count]) => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${item}:</strong> ${count}${suffix}`;
            ul.appendChild(li);
        });
        container.innerHTML = '';
        container.appendChild(ul);
    }
});

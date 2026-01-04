document.addEventListener('DOMContentLoaded', () => {
    const jobsTab = document.getElementById('jobs-tab');
    const aboutTab = document.getElementById('about-tab');
    const jobsSection = document.getElementById('jobs-section');
    const aboutSection = document.getElementById('about-section');
    const jobsContainer = document.getElementById('jobs-container');

    // Función para cambiar de pestaña
    function showSection(sectionToShow, activeTab) {
        [jobsSection, aboutSection].forEach(section => section.classList.add('hidden'));
        [jobsTab, aboutTab].forEach(tab => tab.classList.remove('active'));

        sectionToShow.classList.remove('hidden');
        activeTab.classList.add('active');
    }

    jobsTab.addEventListener('click', () => showSection(jobsSection, jobsTab));
    aboutTab.addEventListener('click', () => showSection(aboutSection, aboutTab));

    // Cargar y mostrar los trabajos desde el JSON
    fetch('computrabajo_jobs.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al cargar el archivo JSON: ${response.statusText}`);
            }
            return response.json();
        })
        .then(jobs => {
            if (jobs.length === 0) {
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
                    <p><strong>Salario:</strong> ${job.salario}</p>
                     <p><strong>Jornada:</strong> ${job.jornada}</p>
                    <p><strong>Publicado:</strong> ${job.date}</p>
                    <a href="${job.link}" target="_blank">Ver oferta</a>
                `;

                jobsContainer.appendChild(jobCard);
            });
        })
        .catch(error => {
            console.error('Error al procesar el archivo JSON:', error);
            jobsContainer.innerHTML = '<p>Ocurrió un error al cargar las ofertas de trabajo. Por favor, intenta de nuevo más tarde.</p>';
        });
});

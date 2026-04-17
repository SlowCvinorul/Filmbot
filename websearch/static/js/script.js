
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('form');
    const resultsSection = document.querySelector('.results-count');
    
    if (searchForm && resultsSection) {
        searchForm.addEventListener('submit', function() {
            setTimeout(() => {
                resultsSection.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 100);
        });
    }
});
// Script principal
/**
 * JC2B Countdown - Gestion complète du compte à rebours (13/11/2025)
 * Auto-initialisation au chargement du DOM.
 */

// Configuration
const CONFIG = {
    eventDate: new Date('November 13, 2025 09:00:00').getTime(),
    elementIds: {
        days: 'days',
        hours: 'hours',
        mins: 'mins',
        secs: 'secs'
    },
    debug: true // Affiche des logs dans la console si true
};

// État de l'application
const state = {
    countdownInterval: null,
    elements: {}
};

/**
 * Récupère les éléments du DOM et les stocke dans `state.elements`.
 * @throws {Error} Si un élément est manquant.
 */
function getDomElements() {
    const elements = {};
    for (const [key, id] of Object.entries(CONFIG.elementIds)) {
        const element = document.getElementById(id);
        if (!element) {
            throw new Error(`Élément non trouvé : ${id}`);
        }
        elements[key] = element;
    }
    return elements;
}

/**
 * Met à jour l'affichage du compte à rebours.
 * @param {number} days - Jours restants.
 * @param {number} hours - Heures restantes.
 * @param {number} mins - Minutes restantes.
 * @param {number} secs - Secondes restantes.
 */
function updateDisplay(days, hours, mins, secs) {
    state.elements.days.textContent = days.toString().padStart(2, '0');
    state.elements.hours.textContent = hours.toString().padStart(2, '0');
    state.elements.mins.textContent = mins.toString().padStart(2, '0');
    state.elements.secs.textContent = secs.toString().padStart(2, '0');
}

/**
 * Calcule le temps restant et met à jour l'affichage.
 */
function updateCountdown() {
    const now = new Date().getTime();
    const distance = CONFIG.eventDate - now;

    if (distance <= 0) {
        updateDisplay(0, 0, 0, 0);
        clearInterval(state.countdownInterval);
        if (CONFIG.debug) console.log("Événement JC2B commencé !");
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const secs = Math.floor((distance % (1000 * 60)) / 1000);

    updateDisplay(days, hours, mins, secs);
}

/**
 * Initialise le compte à rebours.
 */
function init() {
    try {
        state.elements = getDomElements();
        updateCountdown(); // Mise à jour immédiate
        state.countdownInterval = setInterval(updateCountdown, 1000);
        if (CONFIG.debug) console.log("Compte à rebours JC2B initialisé (événement le 13/11/2025).");
    } catch (error) {
        console.error("Erreur lors de l'initialisation du compte à rebours :", error);
    }
}

// Auto-exécution quand le DOM est chargé
document.addEventListener('DOMContentLoaded', init);

console.log("Site JC2B chargé !");


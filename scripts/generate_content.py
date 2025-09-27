import os
from datetime import datetime

# ======================
# 1. FONCTIONS DE GÉNÉRATION DES SECTIONS
# ======================

def generate_language_switch(current_lang="en"):
    """Bouton de changement de langue pour la navbar"""
    if current_lang == "fr":
        return '<a href="index.html" class="btn-lang" title="Switch to English">🇬🇧 English</a>'
    else:
        return '<a href="index_fr.html" class="btn-lang" title="Passer en français">🇫🇷 Français</a>'

def generate_header(lang="en"):
    return """
    <header class="site-header">
        <!-- Bannière EN DEHORS du conteneur -->
        <div class="header-banner">
            <img src="/assets/images/jc2b_logo2.png" alt="JC2B 2025 - Junior Conference of Computational Biology">
        </div>
        <!-- Le reste du header (navbar, etc.) reste dans le conteneur -->
        <div class="container">
            <!-- Autres éléments du header si besoin -->
        </div>
    </header>
    """

def generate_burger_menu():
    return """
    <button class="burger-menu" id="burger-menu" aria-label="Open menu">
        <span></span>
    </button>
    """

def generate_mobile_nav(lang="en"):
    lang_switch = generate_language_switch(lang)
    if lang == "en":
        return f"""
        <nav class="mobile-nav" id="mobile-nav">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#practical-info">Practical information</a></li>
                <li><a href="#program">Program</a></li>
                <li><a href="#call-for-contributions">Call for Contributions</a></li>
                <li><a href="#registration">Registration</a></li>
                <li><a href="#organization">Organization</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="lang-switch">{lang_switch}</div>
        </nav>
        """
    else:
        return f"""
        <nav class="mobile-nav" id="mobile-nav">
            <ul>
                <li><a href="#home">Accueil</a></li>
                <li><a href="#practical-info">Informations pratiques</a></li>
                <li><a href="#program">Programme</a></li>
                <li><a href="#call-for-contributions">Appel à contributions</a></li>
                <li><a href="#registration">Inscriptions</a></li>
                <li><a href="#organization">Organisation</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="lang-switch">{lang_switch}</div>
        </nav>
        """

def generate_navbar(lang="en"):
    lang_switch = generate_language_switch(lang)
    return f"""
    <div class="burger-nav-wrapper">
        {generate_burger_menu()}
        {generate_mobile_nav(lang)}
        <nav class="navbar">
            <div class="container navbar-flex">
                <ul>
                    {"".join([
                        '<li><a href="#home">Home</a></li>',
                        '<li><a href="#program">Program</a></li>',
                        '<li><a href="#registration">Registration</a></li>',
                        '<li><a href="#call-for-contributions">Call for Contributions</a></li>',
                        '<li><a href="#practical-info">Practical information</a></li>',
                        '<li><a href="#organization">Organization</a></li>',
                        '<li><a href="#contact">Contact</a></li>',
                    ]) if lang == "en" else "".join([
                        '<li><a href="#home">Accueil</a></li>',
                        '<li><a href="#program">Programme</a></li>',
                        '<li><a href="#registration">Inscriptions</a></li>',
                        '<li><a href="#call-for-contributions">Appel à contributions</a></li>',
                        '<li><a href="#practical-info">Informations pratiques</a></li>',
                        '<li><a href="#organization">Organisation</a></li>',
                        '<li><a href="#contact">Contact</a></li>',
                    ])}
                </ul>
                <div class="lang-switch">{lang_switch}</div>
            </div>
        </nav>
    </div>
    """

def generate_home_section(lang="fr"):
    if lang == "en":
        return """
        <section id="home" class="home">
            <div class="container">
                <h2>Home</h2>
                <div class="home-content">
                    <p style="margin-bottom: 20px;">
                        The <strong>Junior Conference of Computational Biology (JC2B 2025)</strong> is an event
                        organized by students of the <strong>AMI2B Master's program in Orsay</strong>, with support from
                        <strong>Université Paris-Saclay</strong> and <strong>I2BC</strong>.
                    </p>
                    <p style="margin-bottom: 20px;">
                        This conference aims to bring together <strong>Master's students, PhD students,
                        postdocs, and researchers</strong> around recent advances in bioinformatics.
                        It provides a platform to:
                    </p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>Present <strong>young scientists' work</strong>;</li>
                        <li>Strengthen <strong>links between programs</strong> (BIBS, AMI2B Orsay/Évry);</li>
                        <li>Foster <strong>intergenerational exchanges</strong>;</li>
                        <li>Create <strong>networking opportunities</strong> for academic and industrial careers.</li>
                    </ul>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="home" class="home">
            <div class="container">
                <h2>Accueil</h2>
                <div class="home-content">
                    <p style="margin-bottom: 20px;">
                        La <strong>Junior Conference of Computational Biology (JC2B 2025)</strong> est un événement
                        organisé par les étudiants du <strong>Master AMI2B d'Orsay</strong>, avec le soutien de
                        l'<strong>Université Paris-Saclay</strong> et de l'<strong>I2BC</strong>.
                    </p>
                    <p style="margin-bottom: 20px;">
                        Cette conférence a pour vocation de rassembler <strong>étudiants en master, doctorants,
                        post-doctorants et chercheurs</strong> autour des avancées récentes en bioinformatique.
                        Elle offre une plateforme pour :
                    </p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>Présenter les <strong>travaux de jeunes scientifiques</strong> ;</li>
                        <li>Renforcer les <strong>liens entre les formations</strong> (BIBS, AMI2B Orsay/Évry) ;</li>
                        <li>Favoriser les <strong>échanges intergénérationnels</strong> ;</li>
                        <li>Créer des <strong>opportunités de réseau</strong> pour les carrières académiques et industrielles.</li>
                    </ul>
                </div>
            </div>
        </section>
        """

def generate_program_section(lang="fr"):
    program_unavailable = f"""
    <div class="program-unavailable">
        <div class="program-unavailable-header">
            <i class="fas fa-info-circle"></i>
            <h3>{"Programme en cours de finalisation" if lang == "fr" else "Program Under Finalization"}</h3>
        </div>
        <p class="program-unavailable-message">
            {"Le programme est susceptible d'être modifié. Revenez régulièrement pour les mises à jour."
            if lang == "fr" else "The program is subject to change. Check back regularly for updates."}
        </p>
    </div>
    """
     
    if lang == "en":
        return f"""
        <section id="program" class="program">
            <div class="container">
                <h2>Programme</h2>
                {program_unavailable}
                <div>
                    <div class="program-session">
                        <p>
                        This edition will feature two keynote speakers, experts in AI and predictive models in bioinformatics, 
                        who will shed light on this central theme through their innovative research and applications.
                        </p>

                        <!-- NOUVEAU : Section pour les images des keynote speakers -->
                    <div class="keynote-speakers">
                        <div class="speaker">
                            <div class="speaker-image">
                                <img src="/assets/images/speakers/laurent_jacob.png" alt="Laurent Jacob">
                            </div>
                            <p class="speaker-name"><strong>Laurent Jacob</strong></p>
                            <p class="speaker-affiliation">CNRS/Sorbonne Université</p>
                        </div>
                        <div class="speaker">
                            <div class="speaker-image">
                                <img src="/assets/images/speakers/magali_richard.png" alt="Magali Richard">
                            </div>
                            <p class="speaker-name"><strong>Magali Richard</strong></p>
                            <p class="speaker-affiliation">CNRS/Université Grenoble Alpes</p>
                        </div>
                    </div>

                        <h3 style="margin-bottom: 20px;">Morning Session: AI Applications in Structure and Evolution</h3>
                        <ul class="program-timeline">
                            <ul class="program-session">
                                <li><strong>9:00</strong>: Opening note by <em>Anne Lopes</em> et <em>Daniel Gautheret</em></li>
                                <li><strong>9:15</strong>: Keynote speaker: <em>Laurent Jacob</em>, Laboratoire de Biologie Computationnelle et Quantitative, CNRS/Sorbonne Université</li>
                                <li><strong>10:00</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>10:30</strong>: Coffee break</li>
                            <ul class="program-session">
                                <li><strong>11:00</strong>: Selected speaker</li>
                                <li><strong>11:30</strong>: Selected speaker</li>
                                <li><strong>12:00</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>12:30</strong>: Buffet</li>
                        </ul>
                    </div>
                    <div>
                        <ul class="program-timeline">
                            <ul class="program-special">
                                <li><strong>13h30</strong> : INTERNSHIP FAIR</li>
                            </ul>
                        </ul>
                    </div>
                    <div class="program-session">
                        <h3 style="margin-bottom: 20px;">Afternoon Session: Predictive Modelling in Genomics and Health</h3>
                        <ul class="program-timeline">
                            <ul class="program-session">
                                <li><strong>14:00</strong>: Keynote speaker: <em>Magali Richard</em>, CNRS/Université Grenoble Alpes</li>
                                <li><strong>14:45</strong>: Selected speaker</li>
                                <li><strong>15:15</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>15:45</strong>: Pause café</li>
                            <ul class="program-session">
                                <li><strong>16:15</strong>: Selected speaker</li>
                                <li><strong>16:45</strong>: Selected speaker</li>
                                <li><strong>17:15</strong>: Closing note</li>
                            </ul>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        """

    else:
        return f"""
        <section id="program" class="program">
            <div class="container">
                <h2>Programme</h2>
                {program_unavailable}
                <div>
                    <div class="program-session">
                        <p>
                        Cette édition 2025 mettra à l’honneur deux keynote speakers, experts en IA et modèles prédictifs en bioinformatique, 
                        qui viendront éclairer ce thème central à travers leurs recherches et applications innovantes.
                        </p>

                        <!-- NOUVEAU : Section pour les images des keynote speakers -->
                    <div class="keynote-speakers">
                        <div class="speaker">
                            <div class="speaker-image">
                                <img src="/assets/images/speakers/laurent_jacob.png" alt="Laurent Jacob">
                            </div>
                            <p class="speaker-name"><strong>Laurent Jacob</strong></p>
                            <p class="speaker-affiliation">CNRS/Sorbonne Université</p>
                        </div>
                        <div class="speaker">
                            <div class="speaker-image">
                                <img src="/assets/images/speakers/magali_richard.png" alt="Magali Richard">
                            </div>
                            <p class="speaker-name"><strong>Magali Richard</strong></p>
                            <p class="speaker-affiliation">CNRS/Université Grenoble Alpes</p>
                        </div>
                    </div>

                        <h3 style="margin-bottom: 20px;">Session Matin : Applications de l'IA en Structure et Évolution</h3>
                        <ul class="program-timeline">
                            <ul class="program-session">
                                <li><strong>9:00</strong>: Mot d'ouverture par <em>Anne Lopes</em> et <em>Daniel Gautheret</em></li>
                                <li><strong>9:15</strong>: Conférencier invité : <em>Laurent Jacob</em>, Laboratoire de Biologie Computationnelle et Quantitative, CNRS/Sorbonne Université</li>
                                <li><strong>10:00</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>10:30</strong>: Pause café</li>
                            <ul class="program-session">
                                <li><strong>11:00</strong>: Selected speaker</li>
                                <li><strong>11:30</strong>: Selected speaker</li>
                                <li><strong>12:00</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>12:30</strong>: Buffet</li>
                        </ul>
                    </div>
                    <div>
                        <ul class="program-timeline">
                            <ul class="program-special">
                                <li><strong>13h30</strong> : FOIRE AUX STAGES</li>
                            </ul>
                        </ul>
                    </div>
                    <div class="program-session">
                        <h3 style="margin-bottom: 20px;">Session Après-midi : Modélisation Prédictive en Génomique et Santé</h3>
                        <ul class="program-timeline">
                            <ul class="program-session">
                                <li><strong>14:00</strong>: Conférencier invité : <em>Magali Richard</em>, CNRS/Université Grenoble Alpes</li>
                                <li><strong>14:45</strong>: Selected speaker</li>
                                <li><strong>15:15</strong>: Selected speaker</li>
                            </ul>
                            <li class="program-break"><strong>15:45</strong>: Pause café</li>
                            <ul class="program-session">
                                <li><strong>16:15</strong>: Selected speaker</li>
                                <li><strong>16:45</strong>: Selected speaker</li>
                                <li><strong>17:15</strong>: Mot de clôture</li>
                            </ul>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        """

def generate_call_for_contributions(lang="fr"):
    if lang == "en":
        return """
        <section id="call-for-contributions" class="call-for-contributions">
            <div class="container">
                <h2>Call for Contributions</h2>
                <p>
                    JC2B 2025 invites students, PhD candidates, and young researchers to submit their work
                    in English as:
                </p>
                <div class="contribution-types">
                    <div class="contribution-type">
                        <h3><i class="fas fa-microphone"></i> Oral Presentations</h3>
                        <p>Duration: <strong>20 minutes</strong> (including questions).</p>
                    </div>
                </div>
                <div class="submission-details">
                    <h3>Submission Guidelines</h3>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>Language: <strong>English</strong>;</li>
                        <li>Abstract: <strong>300 words max</strong> (text or PDF);</li>
                        <li>No formal review process (acceptance subject to relevance);</li>
                        <li>At least one author must be present at the event.</li>
                    </ul>
                    <div class="important-dates">
                        <h3>Important Dates</h3>
                        <table>
                            <tr><td><strong>Submission opens</strong></td><td>September 25, 2025</td></tr>
                            <tr><td><strong>Submission deadline</strong></td><td>October 25, 2025</td></tr>
                            <tr><td><strong>Notification to authors</strong></td><td>October 25, 2025</td></tr>
                        </table>
                    </div>
                    <div class="submission-link">
                        <a href="#registration" class="btn" rel="noopener noreferrer">
                            <i class="fas fa-paper-plane"></i> Submit a contribution
                        </a>
                        <p class="note">
                            <i class="fas fa-info-circle"></i> Projects are submitted via the event registration form.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="call-for-contributions" class="call-for-contributions">
            <div class="container">
                <h2>Appel à contributions</h2>
                <p>
                    La JC2B 2025 invite les étudiants, doctorants et jeunes chercheurs à soumettre leurs travaux
                    en anglais sous forme de :
                </p>
                <div class="contribution-types">
                    <div class="contribution-type">
                        <h3><i class="fas fa-microphone"></i> Présentations orales</h3>
                        <p>Durée : <strong>20 minutes</strong> (incluant les questions).</p>
                    </div>
                </div>
                <div class="submission-details">
                    <h3>Consignes de soumission</h3>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>Langue : <strong>anglais</strong> ;</li>
                        <li>Résumé : <strong>300 mots maximum</strong> ;</li>
                        <li>Pas de processus d'évaluation formelle (acceptation sous réserve de pertinence) ;</li>
                        <li>Un auteur par contribution devra être présent lors de l'événement.</li>
                    </ul>
                    <div class="important-dates">
                        <h3>Dates importantes</h3>
                        <table>
                            <tr><td><strong>Ouverture des soumissions</strong></td><td>25 septembre 2025</td></tr>
                            <tr><td><strong>Date limite de soumission</strong></td><td>20 octobre 2025</td></tr>
                            <tr><td><strong>Notification aux auteurs</strong></td><td>21 octobre 2025</td></tr>
                        </table>
                    </div>
                    <div class="submission-link">
                        <a href="#registration" class="btn" rel="noopener noreferrer">
                            <i class="fas fa-paper-plane"></i> Soumettre une contribution
                        </a>
                        <p class="note">
                            <i class="fas fa-info-circle"></i> Les projets sont soumis via le formulaire d’inscription à l’événement.
                        </p>
                    </div>
                </div>
            </div>
        </section>
        """

def generate_registration_section(lang="fr"):
    if lang == "en":
        return """
        <section id="registration" class="registration">
            <div class="container">
                <h2>Registration</h2>
                <p class="note">
                    <i class="fas fa-exclamation-circle"></i> Registration will close once the 120 available spots are filled.
                </p>
                <div class="registration-info">
                    <p>
                        Participation in JC2B 2025 is <strong>free</strong> for all and includes:
                    </p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>Access to all sessions;</li>
                        <li>Lunch (buffet);</li>
                        <li>Coffee breaks;</li>
                        <li>Goodies (while stocks last).</li>
                    </ul>
                    <div class="important-dates">
                        <h3>Important Dates</h3>
                        <table>
                            <tr><td><strong>Registration opens</strong></td><td>September 25, 2025</td></tr>
                            <tr><td><strong>Registration closes</strong></td><td>October 20, 2025</td></tr>
                        </table>
                    </div>
                    <div class="registration-link">
                        <a href="https://framaforms.org/inscription-jc2b-jc2b-registration-1758198276" class="btn" target="_blank" rel="noopener noreferrer">
                            <i class="fas fa-user-plus"></i> Register for JC2B 2025
                        </a>
                        <p class="note">
                            <i class="fas fa-info-circle"></i>
                            Registration is via a Framaforme form.
                        </p>
                    </div>
                    <div class="registration-faq">
                        <h3>Frequently Asked Questions</h3>
                        <div class="faq-item">
                            <h4><i class="fas fa-question-circle"></i> Is registration mandatory?</h4>
                            <p>Yes, for logistical reasons (meals, badges, spaces).</p>
                        </div>
                        <div class="faq-item">
                            <h4><i class="fas fa-question-circle"></i> Can I cancel my registration?</h4>
                            <p>
                                Yes, until November 10, 2025 by contacting
                                <a href="mailto:jc2b.paris.saclay@gmail.com">the organizers.</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="registration" class="registration">
            <div class="container">
                <h2>Inscriptions</h2>
                <p class="note">
                    <i class="fas fa-exclamation-circle"></i>
                    Les inscriptions seront closes dès que les 120 places disponibles seront attribuées.
                </p>
                <div class="registration-info">
                    <p>
                        La participation à la JC2B 2025 est <strong>gratuite</strong> pour tous et inclut :
                    </p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>L'accès à toutes les sessions ;</li>
                        <li>Le repas du midi (buffet) ;</li>
                        <li>Les pauses café ;</li>
                        <li>Des goodies (dans la limite des stocks).</li>
                    </ul>
                    <div class="important-dates">
                        <h3>Dates importantes</h3>
                        <table>
                            <tr><td><strong>Ouverture des inscriptions</strong></td><td>25 septembre 2025</td></tr>
                            <tr><td><strong>Clôture des inscriptions</strong></td><td>20 octobre 2025</td></tr>
                        </table>
                    </div>
                    <div class="registration-link">
                        <a href="https://framaforms.org/inscription-jc2b-jc2b-registration-1758198276" class="btn" target="_blank" rel="noopener noreferrer">
                            <i class="fas fa-user-plus"></i> S'inscrire à la JC2B 2025
                        </a>
                        <p class="note">
                            <i class="fas fa-info-circle"></i>
                            Les inscriptions se font via un formulaire Framaforme.
                        </p>
                    </div>
                    <div class="registration-faq">
                        <h3>Questions fréquentes</h3>
                        <div class="faq-item">
                            <h4><i class="fas fa-question-circle"></i> L'inscription est-elle obligatoire ?</h4>
                            <p>Oui, pour des raisons logistiques (repas, badges, espaces).</p>
                        </div>
                        <div class="faq-item">
                            <h4><i class="fas fa-question-circle"></i> Puis-je annuler mon inscription ?</h4>
                            <p>
                                Oui, jusqu'au 10 novembre 2025 en contactant
                                <a href="mailto:jc2b.paris.saclay@gmail.com">les organisateurs.</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    
def generate_practical_info_section(lang="fr"):
    if lang == "en":
        return """
        <section id="practical-info" class="practical-info">
            <div class="container">
                <h2>Practical information</h2>
                <div class="practical-info-content">
                    <p><strong>Venue and accessibility</strong><br>
                    JC2B 2025 will take place on November 13, 2025 at I2BC, located in Gif-sur-Yvette, southwest of Paris.</p>
                    <p>
                    <strong>Conference venue address:</strong><br>
                    I2BC - Building 21 | 1 Avenue de la Terrasse, 91190 Gif-su-Yvette
                    </p>
                    <h3>Access map</h3>
                    <div class="map-container">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1440.0811122042815!2d2.130794386265531!3d48.7037236553588!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e67f7f484e8983%3A0xa3df8cb85292dc02!2sCNRS%20Ile-de-France%20-%20Gif-sur-Yvette!5e0!3m2!1sfr!2sfr!4v1758890775085!5m2!1sfr!2sfr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                    <p><strong>To get to the venue:</strong></p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>
                            <strong>By public transport</strong> (see the Ile-de-France Mobilités website):<br>
                            By RER: take the RER B to the ‘Gif-sur-Yvette’ stop (I2BC is a 15-minute walk from there).<br>
                            By bus: take the 4610 or 4611 lines to the 'Fond Fanet' stop (I2BC is a 5-minute walk from there).
                        </li>
                        <li>
                            <strong>By car:</strong> Permission to drive on site will be distributed by email.
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="practical-info" class="practical-info">
            <div class="container">
                <h2>Informations pratiques</h2>
                <div class="practical-info-content">
                    <p><strong>Site et accessibilité</strong><br>
                    JC2B 2025 aura lieu le 13 novembre 2025 à l'I2BC, situé à Gif-sur-Yvette au Sud-Ouest de Paris.</p>
                    <p>
                    <strong>Adresse du site de la conférence :</strong><br>
                    I2BC - Bâtiment 21 | 1 Avenue de la Terrasse, 91190 Gif-su-Yvette
                    </p>
                    <h3>Plan d'accès</h3>
                    <div class="map-container">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1440.0811122042815!2d2.130794386265531!3d48.7037236553588!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e67f7f484e8983%3A0xa3df8cb85292dc02!2sCNRS%20Ile-de-France%20-%20Gif-sur-Yvette!5e0!3m2!1sfr!2sfr!4v1758890775085!5m2!1sfr!2sfr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                    <p><strong>Pour accéder au site :</strong></p>
                    <ul style="list-style-type: disc; padding-left: 40px;">
                        <li>
                            <strong>En transport en commun</strong> (voir le site Ile-de-France Connect):<br>
                            En RER : prendre le RER B jusqu'à l'arrêt 'Gif-sur-Yvette'<br>
                            En bus : prendre les lignes 4610 et 4611 jusqu'à l'arrêt 'Fond Fanet'
                        </li>
                        <li>
                            <strong>En voiture :</strong> L'autorisation de circulation sur le site sera distribuée par mail.
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        """

def generate_organization_section(lang="fr"):
    if lang == "en":
        return """
        <section id="organization" class="organization">
            <div class="container">
                <h2>Organizing Committee</h2>
                <p>
                    JC2B 2025 is organized by <strong>all students of the AMI2B Master's program in Orsay</strong>,
                    under the supervision of two faculty coordinators, with support from Université Paris-Saclay and I2BC.
                </p>
                <div class="committee-members">
                    <h3>Members</h3>
                    <p><strong>Students of the AMI2B Master's (Orsay)</strong>: Full list available on request.</p>
                    <p><strong>Faculty coordinators</strong>: Anne Lopes et Daniel Gautheret</p>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="organization" class="organization">
            <div class="container">
                <h2>Comité d'organisation</h2>
                <p>
                    La JC2B 2025 est organisée par <strong>l'ensemble des étudiants du Master AMI2B d'Orsay</strong>,
                    sous la supervision de deux enseignant·es responsables, avec le soutien de l'Université Paris-Saclay et de l'I2BC.
                </p>
                <div class="committee-members">
                    <h3>Membres</h3>
                    <p><strong>Étudiants du Master AMI2B (Orsay)</strong> : Liste complète disponible sur demande.</p>
                    <p><strong>Enseignants responsables</strong> : Anne Lopes et Daniel Gautheret</p>
                </div>
            </div>
        </section>
        """

def generate_contact_section(lang="fr"):
    if lang == "en":
        return """
        <section id="contact" class="contact">
            <div class="container">
                <h2>Contact</h2>
                <div class="contact-info">
                    <p>For any questions, contact us:</p>
                    <div class="contact-email">
                        <i class="fas fa-envelope"></i>
                        <p>Email: <a href="mailto:jc2b.paris.saclay@gmail.com">jc2b.paris.saclay@gmail.com</a></p>
                    </div>
                    <div class="social-media">
                        <h3>Social Media</h3>
                        <p>Our accounts will be available soon!</p>
                        <div class="social-icons">
                            <div class="social-icon placeholder">
                                <i class="fab fa-mastodon"></i> <span>@JC2B</span>
                            </div>
                            <div class="social-icon placeholder">
                                <i class="fab fa-linkedin"></i> <span>JC2B</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """
    else:
        return """
        <section id="contact" class="contact">
            <div class="container">
                <h2>Contact</h2>
                <div class="contact-info">
                    <p>Pour toute question, contactez-nous :</p>
                    <div class="contact-email">
                        <i class="fas fa-envelope"></i>
                        <p>Email : <a href="mailto:jc2b.paris.saclay@gmail.com">jc2b.paris.saclay@gmail.com</a></p>
                    </div>
                    <div class="social-media">
                        <h3>Réseaux sociaux</h3>
                        <p>Nos comptes seront bientôt disponibles !</p>
                        <div class="social-icons">
                            <div class="social-icon placeholder">
                                <i class="fab fa-mastodon"></i> <span>@JC2B</span>
                            </div>
                            <div class="social-icon placeholder">
                                <i class="fab fa-linkedin"></i> <span>JC2B</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """

def generate_footer(lang="fr"):
    current_year = datetime.now().year
    if lang == "en":
        return f"""
        <footer class="site-footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>JC2B {current_year}</h3>
                        <p>
                            November 13, 2025<br>
                            I2BC - Building 21<br>
                            1 Avenue de la Terrasse, 91190 Gif-sur-Yvette
                        </p>
                    </div>
                    <div class="footer-section">
                        <h3>Useful Links</h3>
                        <ul>
                            <li><a href="#home">Home</a></li>
                            <li><a href="#program">Program</a></li>
                            <li><a href="#registration">Registration</a></li>
                            <li><a href="#call-for-contributions">Call for Contributions</a></li>
                            <li><a href="#practical-info">Practical information</a></li>
                            <li><a href="#organization">Organization</a></li>
                            <li><a href="#contact">Contact</a></li>
                        </ul>
                    </div>
                    <div class="footer-section">
                        <h3>Partners</h3>
                        <div class="footer-partner-logos">
                            <img src="/assets/images/partners/paris_saclay_logo.png" alt="Paris-Saclay" class="logo-blanc">
                            <img src="/assets/images/partners/i2bc_logo.png" alt="I2BC">
                            <img src="/assets/images/partners/rebrand_asso_ami2b_logo2.png" alt="Master AMI2B">
                        </div>
                    </div>
                </div>
                <div class="footer-legal">
                    <p>
                        &copy; {current_year} JC2B - All rights reserved.
                        Site developed by students of the AMI2B Master's program.
                    </p>
                    <ul class="footer-links">
                        <li><a href="/legal-notice">Legal Notice</a></li>
                        <li><a href="/privacy-policy">Privacy Policy</a></li>
                    </ul>
                </div>
            </div>
        </footer>
        """
    else:
        return f"""
        <footer class="site-footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h3>JC2B {current_year}</h3>
                        <p>
                            13 novembre 2025<br>
                            I2BC - Bâtiment 21<br>
                            1 Avenue de la Terrasse, 91190 Gif-sur-Yvette
                        </p>
                    </div>
                    <div class="footer-section">
                        <h3>Liens utiles</h3>
                        <ul>
                            <li><a href="#home">Accueil</a></li>
                            <li><a href="#program">Programme</a></li>
                            <li><a href="#registration">Inscriptions</a></li>
                            <li><a href="#call-for-contributions">Appel à contributions</a></li>
                            <li><a href="#practical-info">Informations pratiques</a></li>
                            <li><a href="#organization">Organisation</a></li>
                            <li><a href="#contact">Contact</a></li>
                        </ul>
                    </div>
                    <div class="footer-section">
                        <h3>Partenaires</h3>
                        <div class="footer-partner-logos">
                            <img src="/assets/images/partners/paris_saclay_logo.png" alt="Paris-Saclay" class="logo-blanc">
                            <img src="/assets/images/partners/i2bc_logo.png" alt="I2BC">
                            <img src="/assets/images/partners/rebrand_asso_ami2b_logo2.png" alt="Master AMI2B">
                        </div>
                    </div>
                </div>
                <div class="footer-legal">
                    <p>
                        &copy; {current_year} JC2B - Tous droits réservés.
                        Site développé par les étudiants du Master AMI2B.
                    </p>
                    <ul class="footer-links">
                        <li><a href="/pages/mentions-legales.html">Mentions légales</a></li>
                        <li><a href="/pages/politique-confidentialite.html">Politique de confidentialité</a></li>
                    </ul>
                </div>
            </div>
        </footer>
        """

def generate_scrollspy_script():
    return """
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const sections = document.querySelectorAll("main section[id]");
        const navLinks = document.querySelectorAll(".navbar a[href^='#']");
        function onScroll() {
            let scrollPos = window.scrollY || window.pageYOffset;
            let offset = 120; // Décalage pour la navbar
            let currentId = "";
            sections.forEach(section => {
                if (section.offsetTop - offset <= scrollPos) {
                    currentId = section.id;
                }
            });
            navLinks.forEach(link => {
                link.classList.remove("nav-link-active");
                if (currentId && link.getAttribute("href") === "#" + currentId) {
                    link.classList.add("nav-link-active");
                }
            });
        }
        window.addEventListener("scroll", onScroll, {passive:true});
        onScroll();
    });
    </script>
    """

def generate_scroll_to_top_button():
    return """
    <button id="scroll-to-top" aria-label="Scroll to top" title="Remonter en haut">
        <i class="fas fa-arrow-up"></i>
    </button>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const btn = document.getElementById("scroll-to-top");
        window.addEventListener("scroll", function() {
            if (window.scrollY > 200) {
                btn.classList.add("visible");
            } else {
                btn.classList.remove("visible");
            }
        }, {passive:true});
        btn.addEventListener("click", function() {
            window.scrollTo({top: 0, behavior: "smooth"});
        });
    });
    </script>
    """

def generate_burger_script():
    return """
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const burger = document.getElementById("burger-menu");
        const mobileNav = document.getElementById("mobile-nav");
        const navLinks = mobileNav.querySelectorAll("a[href^='#']");
        function closeMenu() {
            burger.classList.remove("open");
            mobileNav.classList.remove("open");
            document.body.style.overflow = "";
        }
        burger.addEventListener("click", function() {
            burger.classList.toggle("open");
            mobileNav.classList.toggle("open");
            if (mobileNav.classList.contains("open")) {
                document.body.style.overflow = "hidden";
            } else {
                document.body.style.overflow = "";
            }
        });
        navLinks.forEach(link => {
            link.addEventListener("click", closeMenu);
        });
        // Ferme le menu si on clique en dehors
        mobileNav.addEventListener("click", function(e) {
            if (e.target === mobileNav) closeMenu();
        });
    });
    </script>
    """

# ======================
# 2. GÉNÉRATION DE LA PAGE D'ACCUEIL
# ======================

def generate_homepage(lang="en"):
    """Génère la page d'accueil complète pour la langue donnée"""
    output_path = "../pages/index.html" if lang == "en" else "../pages/index_fr.html"
    os.makedirs("../pages", exist_ok=True)

    header = generate_header(lang)
    navbar = generate_navbar(lang)
    home = generate_home_section(lang)
    program = generate_program_section(lang)
    call_for_contributions = generate_call_for_contributions(lang)
    registration = generate_registration_section(lang)
    practical_info = generate_practical_info_section(lang)
    organization = generate_organization_section(lang)
    contact = generate_contact_section(lang)
    footer = generate_footer(lang)

    content = f"""
    {header}
    {navbar}
    <main>
        {home}
        {program}
        {registration}
        {call_for_contributions}
        {practical_info}
        {organization}
        {contact}
    </main>
    {footer}
    {generate_scroll_to_top_button()}
    {generate_scrollspy_script()}
    {generate_burger_script()}
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="{lang}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Junior Conference of Computational Biology - Conference for young researchers in bioinformatics">
            <title>JC2B 2025 - Junior Conference of Computational Biology</title>
            <link rel="stylesheet" href="/assets/css/main.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <link rel="icon" href="/assets/images/favicon.ico" type="image/x-icon">
        </head>
        <body>
        {content}
        </body>
        </html>
        """)

    print(f"✅ Page d'accueil générée avec succès : {output_path}")

# ======================
# 3. POINT D'ENTRÉE
# ======================

if __name__ == "__main__":
    generate_homepage("en")
    generate_homepage("fr")

# Site Web JC2B
## Description
Ce projet est le site officiel de la **Junior Conference of Computational Biology (JC2B)**, un événement organisé par et pour les étudiants, doctorants et chercheurs en bioinformatique. Le site propose des informations sur la conférence (programme, intervenants, partenaires), des pages légales, et une section dédiée aux mentions légales.

## Structure du projet
```
jc2b-website
├── assets
│   ├── css
│   │   └── main.css          # Styles CSS principaux
│   ├── images
│   │   ├── partners          # Logos des partenaires
│   │   └── speakers          # Photos des intervenants
│   └── js
│       └── main.js           # Scripts pour le site (si applicable)
├── pages
│   ├── index.html            # Page d'accueil (version anglaise)
│   ├── index_fr.html         # Page d'accueil (version française)
│   ├── legal-notice.html     # Mentions légales
│   ├── mentions-legales.html # Mentions légales (version française)
│   ├── politique-confidentialite.html # Politique de confidentialité
│   └── privacy-policy.html   # Privacy Policy (version anglaise)
├── scripts
│   └── generate_content.py  # Script Python pour générer du contenu dynamique
└── README.md                 # Documentation du projet
```

## Installation
1. Clonez le dépôt ou téléchargez les fichiers du projet.
2. Ouvrez le fichier `index_fr.html` (pour le français) ou `index.html` (pour l'anglais) dans un navigateur web.

## Utilisation
- Naviguez entre les sections via les liens intégrés (programme, intervenants, etc.).
- Consultez les pages légales via les liens en pied de page.

## Contribuer
Les contributions sont les bienvenues ! Pour proposer des modifications :
1. Fork le dépôt.
2. Créez une branche dédiée (`git checkout -b feature/nom-prenom-ma-nouvelle-fonctionnalité`).
3. Soumettez une Pull Request.

---
### 🔧 Branches en cours de développement

| Branche                                  | Description                                                                 | Statut          | Comment contribuer ?                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------|
| `feature/ange-louis-countdown-conference` | Ajoute un **compte à rebours dynamique** pour la JC2B (13/11/2025) sur la page d’accueil. | **En revue**    | Testez la branche et donnez votre avis sur l’ergonomie/le design |

#### **Comment tester cette feature ?**
1. Basculez sur la branche :
   ```bash
   git checkout feature/ajout-countdown-ange-louis


## License
Ce projet est sous licence MIT.

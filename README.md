# Site Web JC2B
![Bannière JC2B](assets/images/jc2b_banniere.png)
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
│   ├── legal-notice.html     # Mentions légales
│   ├── mentions-legales.html # Mentions légales (version française)
│   ├── politique-confidentialite.html # Politique de confidentialité
│   └── privacy-policy.html   # Privacy Policy (version anglaise)
├── scripts
│   └── generate_content.js  # Script js pour générer du contenu dynamique
├── index.html            # Page d'accueil (version anglaise)
├── index_fr.html         # Page d'accueil (version française)
└── README.md                 # Documentation du projet
```

## Installation
1. Clonez le dépôt ou téléchargez les fichiers du projet.
2. Ouvrez le fichier `index_fr.html` (pour le français) ou `index.html` (pour l'anglais) dans un navigateur web à l'aide de Live Share (extension VS Code).

## Utilisation
- Naviguez entre les sections via les liens intégrés (programme, intervenants, etc.).
- Consultez les pages légales via les liens en pied de page.

## Contribuer
Les contributions sont les bienvenues ! Pour proposer des modifications :
1. Fork le dépôt.
2. Créez une branche dédiée (`git checkout -b feature/nom-prenom-ma-nouvelle-fonctionnalité`).
3. Soumettez une Pull Request.

## License
Ce projet est sous licence MIT.

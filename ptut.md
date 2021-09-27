# Ptut interface neuronal

## Modalités de travail
* Rapport hebdomadaire par mail à <rbeaubois@u-bordeaux.fr> le "jour à définir"
* Réunion hebdomadaire le Mardi de 13h à 13h30
* Code, programmation et commits en anglais
* Gestion des sources avec Git
* Documentation du projet avec Sphinx (Markdown et/ou reStructured text)
* Support matériel : Raspberry Pi4
* Charge de travail : ~5h/semaine

## Récapitulatif du projet
Le but de projet est d'analyser des données en provenance d'un FPGA via SPI. Les données correspondent à l'activité de neurones artificiels calculée par le FPGA. L'activité du réseau de neurone est envoyer par SPI à interval de temps régulier.
La trame commence par un timestamp indiquant le numéro de l'échantillon (n) ou le temps actuel (n*dt).
La suite de la trame correspond à l'activité des électrodes par ordre croissant.
Les données devront être analysées selon les normes et standards en vigueur dans la littérature pour les activités de neurones.
Les résultats d'analyse ainsi que les données devront être enregistrables, exportable et affichable.
Le délai maximal de traitement est fixé à 5 secondes.

## Tâches à accomplir
* Analyse des données reçues
* Enregistrement et export des résultats d'analyse
* Affichage des résultats d'analyse
* Affichage de l'activité avec interface graphique
* Enregistrement et export de l'activité
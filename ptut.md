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
<p style=text-align:justify;>
Le but de projet est d'analyser des données envoyées en SPI par un FPGA. Les données correspondent à l'activité de neurones artificiels calculée par le FPGA. 
</p>

<p style=text-align:justify;>
L'activité du réseau de neurones est envoyée par SPI à interval de temps régulier (de 10kHz à 40kHz). La trame commence par un timestamp indiquant le numéro de l'échantillon (n) ou le temps écoulé (n*dt). La suite de la trame correspond à l'activité des électrodes par ordre croissant.
</p>

<p style=text-align:justify;>
Les données devront être analysées selon les normes et standards en vigueur dans la littérature pour les activités de neurones.
Les résultats d'analyse ainsi que les données devront être enregistrables, exportable et affichable.
Le délai maximal de traitement est fixé à 5 secondes.
</p>

## Tâches à accomplir
- [ ] Analyse des données reçues
- [ ] Enregistrement et export des résultats d'analyse
- [ ] Affichage des résultats d'analyse
- [ ] Affichage de l'activité avec interface graphique
- [ ] Enregistrement et export de l'activité
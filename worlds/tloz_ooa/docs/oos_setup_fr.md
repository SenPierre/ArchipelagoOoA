# Guide d'installation de The Legend of Zelda : Oracle of Seasons

## Logiciel requis

- [Oracle of Seasons .apworld](https://github.com/Dinopony/Archipelago/releases/latest)
- [Oracles Archipelago Patcher](https://github.com/Dinopony/oracles-archipelago-patcher/releases/latest)
- Bizhawk 2.9.1 (x64)](https://tasvideos.org/BizHawk/ReleaseHistory)
- Votre ROM Oracle of Seasons US obtenu légalement

## Instructions d'installation

1. Téléchargez le fichier **Oracle of Seasons .apworld** et placez-le dans le sous-répertoire "lib/worlds/" de votre répertoire d'installation d'Archipelago.
2. Générez en utilisant votre fichier de configuration .yaml (voir le modèle ci-dessous).
3. Lors de la génération, le serveur a généré pour vous un fichier .patcherdata qui pourra être transmis au logiciel **Oracles Archipelago Patcher**, téléchargez-le.
4. Téléchargez le logiciel **Oracles Archipelago Patcher** et décompressez-le dans son propre répertoire.
5. Placez votre **Rom de Oracles of Seasons US** dans ce dossier (le nom n'a pas d'importance tant qu'il a l'extension .gbc).
6. Récupérez votre propre fichier .patcherdata qui a été généré par Archipelago lors de la génération du fichier .patcherdata.
7. Faites un clic droit sur le fichier .patcherdata, sélectionnez "Open With..." et pointez sur **oracles-archipelago-patcher.exe** dans le même répertoire que celui où vous avez placé la ROM vanille.
8. Si tout s'est bien passé, la ROM patchée devrait apparaître à côté du fichier .patcherdata.
9. Ouvrez la ROM patchée dans Bizhawk
10. Dans Bizhawk, allez dans "Tools > Lua Console", puis "Script > Open Script" et choisissez le fichier "connector_bizhawk_generic.lua" dans le sous-dossier "data/lua/" de votre installation Archipelago. 
11. Lancez Bizhawk Generic Client, il devrait se connecter automatiquement à l'émulateur.
12. Connectez le client au serveur AP de votre choix, et vous pouvez commencer à jouer !

## Créer un fichier de configuration (.yaml)

Pour obtenir le fichier modèle:
1. Installer le fichier .apworld en suivant les instructions ci-dessus
2. Si le Launcher Archipelago était en cours de fonctionnement, fermez-le
3. Démarrez le Launcher Archipelago
4. Cliquez sur "Generate Template Settings"
5. Cela devrait ouvrir un explorateur de fichiers dans un dossier précis, prenez le fichier `The Legend of Zelda - Oracle of Seasons.yaml`

A partir de là, vous pouvez éditer ce fichier à votre convenance et le placer directement dans le répertoire "Players" de votre installation Archipelago.
Dès que vous avez un ou plusieurs fichiers dedans, vous pouvez lancer "ArchipelagoGenerate" et profiter de votre multiworld fraîchement créé ! 
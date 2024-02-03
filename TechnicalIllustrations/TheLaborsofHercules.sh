#!/bin/bash

echo "Starting the Twelve Labors of Hercules"

labors=("Nemean Lion" "Lernaean Hydra" "Ceryneian Hind" "Erymanthian Boar" "Augean stables" "Stymphalian Birds" "Cretan Bull" "Mares of Diomedes" "Belt of Hippolyta" "Cattle of Geryon" "Apples of the Hesperides" "Capture Cerberus")

for labor in "${labors[@]}"; do
  echo "Hercules completes the labor: $labor"
done

echo "Hercules has completed all twelve labors."

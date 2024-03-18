#!/bin/bash

source venv/bin/activate

# Запуск Geth с необходимыми параметрами в фоновом режиме
geth --datadir ./ --networkid 1547 --http --http.corsdomain "*" --allow-insecure-unlock --syncmode full
# Дайте Geth некоторое время для запуска
sleep 5

geth attach geth.ipc --exec "miner.setEtherbase('0xb10310fd55edd97b2ba832ce5c5b56b7197604bd'); miner.start()"

python app.py
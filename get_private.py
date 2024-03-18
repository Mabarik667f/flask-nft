from web3 import Web3
from eth_account import Account

# Подключение к локальному узлу Geth
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Укажите ваш порт, если он отличается

# Адрес вашей учетной записи Ethereum
address = '0xb10310fd55EDD97b2BA832cE5c5b56b7197604BD'

# Пароль вашей учетной записи
password = 'boba28++'

# Прочитайте содержимое файла keystore
with open('/home/mamba/tr1/keystore/UTC--2024-03-15T19-28-43.693446463Z--b10310fd55edd97b2ba832ce5c5b56b7197604bd', 'r') as file:
    encrypted_key = file.read()

# Создайте объект аккаунта, используя приватный ключ
account = Account.from_key(web3.eth.account.decrypt(encrypted_key, password))

print('Private Key:', account.address, account.key.hex())


from web3 import Web3
from contract_data import abi, bytecode
geth_provider = "HTTP://127.0.0.1:8545"
w3: Web3 = Web3(Web3.HTTPProvider(geth_provider))

# contract_address = "0x74F89dc155143636BAC851acf594940260b910d8"
w3.eth.default_account = w3.eth.accounts[0]
App = w3.eth.contract(bytecode=bytecode, abi=abi)
tx_hash = App.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract = w3.eth.contract(address=tx_receipt.contract_address, abi=abi)
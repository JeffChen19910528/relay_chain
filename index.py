from web3 import Web3
import json

class Password:
    def __init__(self):
        pass

    def getPassword(self):
        path = 'password.txt'
        file1 = open(path, 'r')
        pwd = file1.readlines()
        return pwd
   


# 建立一個 web3 實例，連接到以太坊節點
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # 使用你的以太坊節點的 URL

accounts = w3.eth.accounts
print('account balance: ' + str(w3.eth.get_balance(accounts[1])))

pw = Password()
pwd = pw.getPassword()

count = 0
for account in accounts:
    result = w3.geth.personal.unlock_account(str(account), pwd[count].strip())
    print(result)
    count += 1

# 合約地址和 ABI
path = 'truffleProject/contractAddr.txt'
f = open(path, 'r')
contract_address = f.read().strip()
abi = 'truffleProject/build/contracts/Test.json'
with open(abi) as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
# 載入合約 ABI
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def store_data(data):
    nonce = w3.eth.get_transaction_count(accounts[1])
    txn_dict = contract.functions.storeData(data).build_transaction({
        'chainId': 10,  # Replace with the chain ID where your contract is deployed
        'gas': 1000000,  # Adjust gas limit accordingly
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
    })

    pk_path = 'private_key.txt'
    f = open(pk_path, 'r')
    pk = f.read().strip()
    print(pk)
    signed_txn = w3.eth.account.sign_transaction(txn_dict, pk)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return receipt

data_to_store = 'Hello, World!'
receipt = store_data(data_to_store)
print("Transaction receipt:", receipt)
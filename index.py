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


# 設置一個錢包地址
tx_hash = contract.functions.setWalletAddress('alice', 'ethereum', '0x679569ebda8da95065445521dd0e7db0d7d79a17').transact({'from': w3.eth.accounts[0]})
set_success = w3.eth.wait_for_transaction_receipt(tx_hash)
print(set_success)

# 獲取錢包地址
wallet_address = contract.functions.getWalletAddress('alice', 'ethereum').call()
print("Wallet Address:", wallet_address)

# 記錄交易
tx_hash = contract.functions.recordTransaction('alice', 'ethereum', '0x1c5657211adede74223b02bb47d63ff5f29d4b3aeb3033f77326186e7bcec9b3').transact({'from': w3.eth.accounts[0]})
record_success = w3.eth.wait_for_transaction_receipt(tx_hash)
print(record_success)

# 獲取交易記錄
transactions = contract.functions.getTransactions('alice', 'ethereum').call()
print("Transactions:", transactions)

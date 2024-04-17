pragma solidity ^0.8.0;

contract Test {
    // 儲存用戶在不同鏈上的錢包地址
    mapping(string => string) private wallets;
    // 儲存用戶在不同鏈上的交易記錄，鍵是“username:chain”，值是交易的數據
    mapping(string => string[]) private transactions;

    // 事件
    event WalletUpdated(string indexed username, string chain, string walletAddress);
    event TransactionRecorded(string indexed username, string chain, string transactionData);

    // 設定錢包地址
    function setWalletAddress(string calldata username, string calldata chain, string calldata walletAddress) public returns (bool) {
        string memory key = string(abi.encodePacked(username, ":", chain));
        wallets[key] = walletAddress;
        emit WalletUpdated(username, chain, walletAddress);
        return true; 
    }

    // 獲取錢包地址
    function getWalletAddress(string calldata username, string calldata chain) public view returns (string memory) {
        string memory key = string(abi.encodePacked(username, ":", chain));
        return wallets[key];
    }

    // 記錄一個交易
    function recordTransaction(string calldata username, string calldata chain, string calldata transactionData) public returns (bool) {
        string memory key = string(abi.encodePacked(username, ":", chain));
        transactions[key].push(transactionData);
        emit TransactionRecorded(username, chain, transactionData);
        return true; 
    }

    // 獲取用戶在指定鏈上的所有交易記錄
    function getTransactions(string calldata username, string calldata chain) public view returns (string[] memory) {
        string memory key = string(abi.encodePacked(username, ":", chain));
        return transactions[key];
    }
}

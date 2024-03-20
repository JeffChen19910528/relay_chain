pragma solidity ^0.8.0;

contract Test {
    event DataStored(address sender, string data);

    // 將資料存儲在合約中
    function storeData(string memory _data) public {
        // 觸發資料儲存事件，傳遞發送者地址和資料
        emit DataStored(msg.sender, _data);
    }
}

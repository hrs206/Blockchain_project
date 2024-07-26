// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SuperCoin {
    uint256 internal issuedCoins = 2000;
    mapping(string => uint256) internal balances;

    constructor(){
        balances["three@gmail.com"] = issuedCoins;
    }

    struct Transaction {
        string sender;
        string receiver;
        uint256 amount;
        uint256 timestamp;
    }

    Transaction[] public transactions;

    event Transfer(string sender, string recipient, uint256 amount, uint256 t);

    function totalCoins() public view returns (uint256){
        return issuedCoins;
    }


    function addCoins(uint256 coins) public returns (bool){
        issuedCoins += coins;
        emit Transfer("None", "three@gmail.com", coins, block.timestamp);
        return true;
    }

    function getBalance(string memory email) public view returns (uint256){
        return balances[email];
    }

    function createAccount(string memory email) public returns (bool){
        balances[email] = 0;
        return true;
    }

    function transfer(string memory sender, string memory recipient, uint256 amount) public returns (bool){
        balances[recipient] += amount;
        balances[sender] -= amount;
        Transaction memory newTransaction = Transaction({
            sender: sender,
            receiver: recipient,
            amount: amount,
            timestamp: block.timestamp
        });
        transactions.push(newTransaction);
        emit Transfer(sender, recipient, amount, block.timestamp);
        return true;
    }

}
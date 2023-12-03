// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Lottery DApp
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script scripts/deploy_with_web3.ts
 */
contract Lottery {
    address payable[] public players;
    address public manager;

    constructor() {
        manager = payable(msg.sender);
    }

    receive() external payable {
        require(msg.value == 1 ether);
        players.push(payable(msg.sender));
    }

    function getBalance() public view returns (uint) {
        require(msg.sender == manager);
        return address(this).balance;
    }

    function random() internal view returns (uint) {
        return uint(keccak256(abi.encode(blockhash(block.number - 1), block.timestamp, players.length)));
    }

    function pickWinner() public {
        require(msg.sender == manager);
        require(players.length >= 3);

        uint r = random();
        address payable winner;
        uint index = r % players.length;

        winner = players[index];
        winner.transfer(getBalance());
        delete players;
    }
}


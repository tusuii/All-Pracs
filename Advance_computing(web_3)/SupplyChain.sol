// SPDX-License-Identifier: GPL-3
pragma solidity ^0.8.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */

contract SupplyChain {
    uint public productCount = 0;

    struct Product {
        uint id;
        string name;
        uint quantity;
        address owner;
        address payable[] history;
    }

    mapping(uint => Product) public products;

    event ProductCreated(uint id, string name, uint quantity, address owner);
    event ProductTransferred(uint id, address from, address to);

    function createProduct(string memory _name, uint _quantity) public {
        productCount++;
        address payable[] memory initialHistory;
        products[productCount] = Product(productCount, _name, _quantity, msg.sender, initialHistory);
        emit ProductCreated(productCount, _name, _quantity, msg.sender);
    }

    function transferProduct(uint _productId, address _newOwner) public {
        require(_productId > 0 && _productId <= productCount, "Invalid ID");
        Product storage product = products[_productId];
        require(msg.sender == product.owner, "Only the owner can transfer the product");

        product.owner = _newOwner;
        product.history.push(payable(_newOwner));

        emit ProductTransferred(_productId, msg.sender, _newOwner);
    }

    function getProductHistory(uint _productId) public view returns (address payable[] memory) {
        require(_productId > 0 && _productId <= productCount, "Invalid product ID");
        return products[_productId].history;
    }
}

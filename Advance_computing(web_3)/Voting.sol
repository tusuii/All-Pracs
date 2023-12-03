// SPDX-License-Identifier: MIT 

pragma solidity ^0.8.0; 
/** 

* @title Storage 

* @dev Store & retrieve value in a variable 

* @custom:dev-run-script scripts/deploy_with_ethers.ts

*/ 

contract Voting {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    mapping(uint => Candidate) public candidates;
    mapping(address => bool) public hasVoted;
    uint public candidatesCount;
    constructor() {
        addCandidate("Candidate 1");
        addCandidate("Candidate 2");
    }

    function addCandidate(string memory _name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    function vote(uint _candidateId) public {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        require(!hasVoted[msg.sender], "You have already voted");

        hasVoted[msg.sender] = true;

        candidates[_candidateId].voteCount++;

        emit Voted(_candidateId, candidates[_candidateId].name);
    }

    event Voted(uint indexed candidateId, string candidateName);
}

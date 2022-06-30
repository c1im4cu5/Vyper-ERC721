# ERC721 Full Guide to Contract Deployment, Batch Minting and Contract Interaction

This guide is mean for anyone interested in a complete deployment of ERC721. It will cover a range of topics from IPFS, web3, json, Python. We will not spend too much time on Vyper. We encourage you to compile the contract on a testnet (from Remix) to learn.

# Preparation
## TokenURI and JSON
NFT's (or ERC721 tokens) are stored as json files. Each NFT must possess it's own json file. Due to a need to protect the end user from a rug pull, we will store these files in the IPFS filesystem. An example file can be located under "tokenURI.json" from the site.

##IPFS
If you have not acquinted yourself ipfs, please take the time to do so. In a quick summation, ipfs (interplanetary file system) will give us a hash of the document/file/folder that is provided to the filesystem. If the item is altered, it receives a different hash.
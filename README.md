# ERC721 Full Guide to Contract Deployment, Batch Minting and Contract Interaction

This guide is meant for those interested in a complete deployment of ERC721. It will cover a range of topics from IPFS, web3, json, Python. We will not spend too much time on Vyper. We encourage you to compile the contract on a testnet (from Remix) to learn.

# Preparation
## TokenURI and JSON
NFT's (or ERC721 tokens) are stored as json files. Each NFT must possess it's own json file. Due to a need to protect the end user from a rug pull, we will store these files in the IPFS filesystem. An example file can be located under "token.json" from the repository. 

```python
{
  "name": "Theseus",
  "description": "King of Athens - Theseus",
  "image": "ipfs://<hash>/<name>.png",
  "attributes": [
                {"trait_type": "rank",
                  "value": 1}
                ]
}
```
When uploading these files to IPFS, you must upload them in a folder! Do not upload the individual files to IPFS. While this is certainly possible, we'll need to reference the individual "json" file as seen in the script above. Uploading an entire folder (even with one file) is required.

## IPFS
If you have not acquinted yourself with ipfs, please take the time to do so. In a quick summation, ipfs (interplanetary file system) will give us a hash of the document/file/folder that is provided to the filesystem. If the item is altered, it receives a different hash. For the purposes of this tutorial, you will find references to Pinata for file storage on ipfs. Preferred method would be to create a node with constant connection (perhaps via AWS or GCP).

Pinata will allow you to upload documents to the ipfs filesystem. Here is a link:
<a href="https://www.pinata.cloud/" target="_blank">Pinata</a>

Upon account generation, you will be able to upload the directory.

## Compiling
At the time of this writing, deploying a Vyper contract is problematic. Users should run the file labeled "server.py". While the python server is running, compile on Remix via localhost:8080/compile. After compiling, you can shut down the server.

## Deployment
You'll need to populate the name and token information. A base url can be applied (and will need to be applied to use the contract.py file). The base url should link to the folder that holds all of your json files. Example: ipfs://hash of folder/

Here is a Deployed Contract on AVAX:
0x9a011056BA0E39e312B00D84C057a8Ffd2BfE21d

Here is a link to the minted tokens:
<a href="https://nftrade.com/users/avalanche/0x7d8b6fb26c78ab7e46918c2707bf0016a53dcb26?search=&sort=listed_desc" target="_blank">nftrade.com</a>

Here is a link to a Flask API that queries IPFS and supports the mint:
<a href="https://parcae.io/nftSearch" target="_blank">Parcae.io</a>

## Contribing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to added/altered.

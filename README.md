# ERC721 Full Guide to Contract Deployment, Batch Minting and Contract Interaction

This guide is meant for those interested in a complete deployment of ERC721. It will cover a range of topics from IPFS, web3, json, Python. We will not spend too much time on Vyper. We encourage you to compile the contract on a testnet (from Remix) to learn.

# Preparation
## TokenURI and JSON
NFT's (or ERC721 tokens) are stored as json files. Each NFT must possess it's own json file. Due to a need to protect the end user from a rug pull, we will store these files in the IPFS filesystem. An example file can be located under "token.json" from the site. 

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
If you have not acquinted yourself ipfs, please take the time to do so. In a quick summation, ipfs (interplanetary file system) will give us a hash of the document/file/folder that is provided to the filesystem. If the item is altered, it receives a different hash.

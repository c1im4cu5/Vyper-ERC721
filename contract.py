from web3 import Web3
import web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv
import time

#Load .env
load_dotenv()

#Stored .env variables
PRIVATE_KEY = os.getenv('PK')
CONTRACT_ADDR = os.getenv("CONTRACT_ADDR")
BLANK_ADDRESS = os.getenv("BLANK_ADDRESS")

#Contract ABI for Connection
ABI = [{"name":"Transfer","inputs":[{"name":"sender","type":"address","indexed":True},{"name":"receiver","type":"address","indexed":True},{"name":"tokenId","type":"uint256","indexed":True}],"anonymous":False,"type":"event"},{"name":"Approval","inputs":[{"name":"owner","type":"address","indexed":True},{"name":"approved","type":"address","indexed":True},{"name":"tokenId","type":"uint256","indexed":True}],"anonymous":False,"type":"event"},{"name":"ApprovalForAll","inputs":[{"name":"owner","type":"address","indexed":True},{"name":"operator","type":"address","indexed":True},{"name":"approved","type":"bool","indexed":False}],"anonymous":False,"type":"event"},{"stateMutability":"nonpayable","type":"constructor","inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_baseURI","type":"string"},{"name":"_maxSupply","type":"uint256"},{"name":"_minter","type":"address"},{"name":"_beneficiary","type":"address"}],"outputs":[]},{"stateMutability":"view","type":"function","name":"supportsInterface","inputs":[{"name":"_interfaceID","type":"bytes32"}],"outputs":[{"name":"","type":"bool"}],"gas":4149},{"stateMutability":"payable","type":"fallback"},{"stateMutability":"view","type":"function","name":"balanceOf","inputs":[{"name":"_owner","type":"address"}],"outputs":[{"name":"","type":"uint256"}],"gas":3338},{"stateMutability":"view","type":"function","name":"ownerOf","inputs":[{"name":"_tokenId","type":"uint256"}],"outputs":[{"name":"","type":"address"}],"gas":2903},{"stateMutability":"view","type":"function","name":"getApproved","inputs":[{"name":"_tokenId","type":"uint256"}],"outputs":[{"name":"","type":"address"}],"gas":5130},{"stateMutability":"view","type":"function","name":"isApprovedForAll","inputs":[{"name":"_owner","type":"address"},{"name":"_operator","type":"address"}],"outputs":[{"name":"","type":"bool"}],"gas":3280},{"stateMutability":"view","type":"function","name":"name","inputs":[],"outputs":[{"name":"","type":"string"}],"gas":13133},{"stateMutability":"view","type":"function","name":"symbol","inputs":[],"outputs":[{"name":"","type":"string"}],"gas":10886},{"stateMutability":"view","type":"function","name":"tokenURI","inputs":[{"name":"_tokenId","type":"uint256"}],"outputs":[{"name":"","type":"string"}],"gas":26796},{"stateMutability":"view","type":"function","name":"totalSupply","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":5458},{"stateMutability":"view","type":"function","name":"tokenByIndex","inputs":[{"name":"_index","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":10198},{"stateMutability":"view","type":"function","name":"tokenOfOwnerByIndex","inputs":[{"name":"_owner","type":"address"},{"name":"_index","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":8463},{"stateMutability":"view","type":"function","name":"baseURI","inputs":[],"outputs":[{"name":"","type":"string"}],"gas":13313},{"stateMutability":"nonpayable","type":"function","name":"transferFrom","inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"}],"outputs":[],"gas":366890},{"stateMutability":"nonpayable","type":"function","name":"safeTransferFrom","inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"}],"outputs":[],"gas":384201},{"stateMutability":"nonpayable","type":"function","name":"safeTransferFrom","inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"},{"name":"_data","type":"bytes"}],"outputs":[],"gas":384201},{"stateMutability":"nonpayable","type":"function","name":"approve","inputs":[{"name":"_approved","type":"address"},{"name":"_tokenId","type":"uint256"}],"outputs":[],"gas":47041},{"stateMutability":"nonpayable","type":"function","name":"setApprovalForAll","inputs":[{"name":"_operator","type":"address"},{"name":"_approved","type":"bool"}],"outputs":[],"gas":39816},{"stateMutability":"payable","type":"function","name":"mint","inputs":[{"name":"_to","type":"address"},{"name":"_tokenURI","type":"string"}],"outputs":[{"name":"","type":"bool"}],"gas":394829},{"stateMutability":"nonpayable","type":"function","name":"withdraw","inputs":[],"outputs":[],"gas":39191},{"stateMutability":"nonpayable","type":"function","name":"burn","inputs":[{"name":"_tokenId","type":"uint256"}],"outputs":[],"gas":358348},{"stateMutability":"view","type":"function","name":"maxSupply","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3186}]

#Initialize Web3 object connected to Avalanceh Blockchain - Test
w3 = Web3(Web3.HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#Unlock print line below to check on connection status
#Returns Boolean value
#print(w3.isConnected())

#Retrieve address from private key
addr = w3.eth.account.privateKeyToAccount(PRIVATE_KEY).address

#Connect to contract
contract = w3.eth.contract(address=CONTRACT_ADDR, abi=ABI)

#Associate Chain ID (Already connected to Avalanche Testnet on Web3)
CHAIN_ID = 43113  # Avalanche Testnet


#Enter Gas Amount
GAS_AMOUNT = 8000000

#Function to auto generate minted tokens
def mint_tokens(wallet, n):

    #Initial Variable to monitor batch creation
    i=0
    n = n+1

    #While function to generate the tokens.
    #Note: A baseURL was assigned during deployment of contract. There is no need to assign a full url to the URI.
    while i !=  n:
        uri= str(i) + ".json"
        i += 1
        nonce = w3.eth.getTransactionCount(addr)
        transaction = contract.functions.mint(wallet, uri).buildTransaction({
            'chainId': CHAIN_ID,
            'gas': GAS_AMOUNT,
            'maxFeePerGas': w3.eth.gas_price + 1000,
            'maxPriorityFeePerGas': w3.eth.gas_price,
            'from': addr,
            'nonce': nonce
        })

        #print(transaction)
        signed_txn = w3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = w3.toHex(w3.keccak(signed_txn.rawTransaction))
        sent = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        #tx_hash = w3.toHex(w3.eth.send_raw_transaction(signed_txn.rawTransaction))

        print("Mint Complete")
        print(sent)
        print("/n")
        time.sleep(8)

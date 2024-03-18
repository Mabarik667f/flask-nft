from eth_utils import to_checksum_address
from services import *


class ContractMethods:

    def __init__(self, address):
        self.address = to_checksum_address(address)

    def get_token_balance(self):
        return contract.functions.getTokenBalance(self.address).call({'from': self.address})

    def get_nft_amount(self, nft_id):
        return contract.functions.getNFTAmount(self.address, nft_id).call({'from': self.address})

    def get_user_data(self):
        return Profile(contract.functions.users(self.address).call({'from': self.address}))

    def get_all_nft_on_sale(self):
        nft_items = []
        i = 0
        while True:
            try:
                lot = NFTForSale(contract.functions.allLots(i).call({'from': self.address}))
                nft_items.append(lot)
                i += 1
            except:
                return nft_items

    def get_all_auctions(self):
        auctions_items = []
        i = 0
        while True:
            try:
                id = contract.functions.allAcutions().call({'from': self.address})
                auction = self.get_auction_detail(id)
                if auction.status:
                    auctions_items.append(auction)
                i += 1
            except:
                return auctions_items

    def get_auction_detail(self, auction_id):
        return Auction(contract.functions.auctionData(auction_id).call({'from': self.address}))

    def get_all_nft_on_user(self, flag=False):
        nft_items = []
        i = 0
        while True:
            try:
                id = contract.functions.allNFT(i).call({'from': self.address})
                if self.get_nft_amount(id) != 0:
                    if flag:
                        nft_items.append((id, self.get_nft_detail(id)))
                    else:
                        nft_items.append(self.get_nft_detail(id))
                i += 1
            except:
                return nft_items

    def get_nft_detail(self, nft_id):
        return NFT(contract.functions.nftData(nft_id).call({'from': self.address}))

    def get_all_collection_on_user(self):
        i = 0
        collections_items = []
        while True:
            try:
                collection_id = contract.functions.collectionsOnUser(self.address, i).call({'from': self.address})
                collections_items.append(self.get_collection_detail(collection_id))
            except:
                return collections_items

    def get_all_collections(self):
        collections_items = list()
        collections_items.append((0, 'Нет'))
        i = 0
        while True:
            try:
                id = contract.functions.allCollections(i).call({'from': self.address})
                collections_items.append((id, self.get_collection_detail(id).name))
                i += 1
            except:
                return collections_items

    def get_collection_detail(self, collection_id):
        return Collection(contract.functions.collectionData(collection_id).call({'from': self.address}), collection_id)

    def get_nft_lot_data(self, lot_id):
        return NFTForSale(contract.functions.allLots[lot_id].call({'from': self.address}))

    def get_ntf_ids(self, collection_id):
        return contract.functions.getAllNFTOnCollection(collection_id).call({'from': self.address})

    def create_nft(self, data) -> None:
        contract.functions.createNFT(*data).transact({'from': self.address})

    def create_collection(self, data) -> None:
        contract.functions.createCollection(*data).transact({'from': self.address})

    def start_auction(self, data) -> None:
        contract.functions.startAuction(*data).transact({'from': self.address})

    def end_auction(self, auction_id) -> None:
        contract.functions.endAuction(auction_id).transact({'from': self.address})

    def bid_auction(self, auction_id, bid) -> None:
        contract.functions.bidAuction(auction_id, bid).transact({'from': self.address})

    def buy_nft(self, lot_id) -> None:
        contract.functions.buyNFT(lot_id).transact({'from': self.address})

    def sell_nft(self, data) -> None:
        contract.functions.sellNFT(*data).transact({'from': self.address})

    def gift(self, to, nft_id) -> None:
        contract.functions.gift(to, nft_id).transact({'from': self.address})

    def activate_referral_code(self, ref_code) -> None:
        contract.functions.activateReferralCode(ref_code).transact({'from': self.address})
from contract import contract
class NFT:

    def __init__(self, nft):
        self.name = nft[0]
        self.describe = nft[1]
        self.img = nft[2]
        self.price = nft[3]
        self.amount = nft[4]
        self.amount_to_buy = nft[5]
        self.create_date = nft[6]
        self.collection_id = nft[7]


class NFTForSale:

    def __init__(self, nft):
        self.owner = nft[0]
        self.nft_id = nft[1]
        self.price = nft[2]
        self.amount = nft[3]


class Collection:

    def __init__(self, collection, col_id):
        self.name = collection[0]
        self.describe = collection[1]
        self.col_id = col_id


class Auction:

    def __init__(self, auction):
        self.collection_id = auction[0]
        self.start_date = auction[1]
        self.end_date = auction[2]
        self.start_bid = auction[3]
        self.current_bid = auction[4]
        self.max_bid = auction[5]
        self.future_owner = auction[6]
        self.status = auction[7]


class AuctionBid:

    def __init__(self, bid):
        self.account = bid[0]
        self.bid = bid[1]


class Profile:

    def __init__(self, user):
        self.address = user[0]
        self.name = user[1]
        self.balance = user[2]
        self.ref_code = user[3]
        self.discount = user[4]
        self.is_activated_code = user[5]
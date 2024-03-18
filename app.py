import os.path

from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from flask.views import MethodView
from contract_functions import ContractMethods
from forms import *

app = Flask(__name__)
app.secret_key = "8c20116e385a277a9588b73d893c3965"


class MainView(MethodView):

    def get(self):
        return render_template('index.html')

    def post(self):
        return render_template('index.html')


class ProfileView(MethodView):

    def get(self):
        form = ActivateCode()
        address = session.get('address', None)
        user = ContractMethods(address).get_user_data()
        return render_template('profile.html', user=user, form=form)

    def post(self):
        address = session.get('address', None)
        form = ActivateCode(request.form)
        if form.validate():
            ContractMethods(address).activate_referral_code(form.data['ref_code'])
            return redirect('profile')
        user = ContractMethods(address).get_user_data()
        return render_template('profile.html', user=user, form=form)


class MarketView(MethodView):

    def get(self):
        address = session.get('address', None)
        nfts = ContractMethods(address).get_all_nft_on_sale()
        return render_template('market.html', nfts=nfts)


class NFTDetailView(MethodView):

    def get(self, nft_id):
        address = session.get('address', None)
        nft_on_sale = ContractMethods(address).get_nft_lot_data(nft_id)
        nft = ContractMethods(address).get_nft_detail(nft_on_sale.nft_id)
        return render_template('nft-detail.html', nft=nft, nft_on_sale=nft_on_sale)

    def post(self, nft_id):
        address = session.get('address', None)
        ContractMethods(address).buy_nft(nft_id)
        nft_on_sale = ContractMethods(address).get_nft_lot_data(nft_id)
        nft = ContractMethods(address).get_nft_detail(nft_on_sale.nft_id)
        return render_template('nft-detail.html', nft=nft, nft_on_sale=nft_on_sale)


class AuctionsView(MethodView):

    def get(self):
        address = session.get('address', None)
        auctions = ContractMethods(address).get_all_auctions()
        return render_template('auctions.html', auctions=auctions)


class AuctionDetailView(MethodView):

    def get(self, auction_id):
        address = session.get('address', None)
        form = Bid()
        auction = ContractMethods(address).get_auction_detail(auction_id)
        return render_template('auction-detail.html', auction=auction, form=form)

    def post(self, auction_id):
        address = session.get('address', None)
        form = Bid(request.form)
        if form.validate():
            ContractMethods(address).bid_auction(auction_id, form.data['bid'])
            return redirect('profile')
        auction = ContractMethods(address).get_auction_detail(auction_id)
        return render_template('auction-detail.html', auction=auction, form=form)


class CreateNFTView(MethodView):

    def get(self):
        address = session.get('address', None)
        choices = ContractMethods(address).get_all_collections()
        form = CreateNFT(collections=choices)
        return render_template('create-nft.html', form=form)

    def post(self):
        address = session.get('address', None)
        choices = ContractMethods(address).get_all_collections()
        form = CreateNFT(request.form, collections=choices)
        if form.validate():
            file = request.files['img']
            filename = file.filename
            file.save(os.path.join('static/images', filename))
            data = [form.data['name'],
                    form.data['describe'],
                    filename,
                    form.data['price'],
                    form.data['amount'],
                    int(form.data['collection_id'])]
            ContractMethods(address).create_nft(data)
            return redirect(url_for('profile'))
        return render_template('create-nft.html', form=form)


class CreateCollectionView(MethodView):
    def get(self):
        form = CreateNFTCollection()
        return render_template('create-collection.html', form=form)

    def post(self):
        address = session.get('address', None)
        form = CreateNFTCollection(request.form)
        if form.validate():
            data = [form.data['name'],
                    form.data['describe']]
            ContractMethods(address).create_collection(data)
            return redirect('profile')
        return render_template('create-collection.html', form=form)


class ShowMyCollectionsView(MethodView):
    def get(self):
        address = session.get('address', None)
        collections = ContractMethods(address).get_all_collection_on_user()
        return render_template('show-collections.html', collections=collections)


class CollectionDetailView(MethodView):
    def get(self, collection_id):
        address = session.get('address', None)
        collection = ContractMethods(address).get_collection_detail(collection_id)
        nft_ids = ContractMethods(address).get_ntf_ids(collection_id)
        return render_template('collection-detail.html', collection=collection, nft_ids=nft_ids)


class ShowMyNFTsView(MethodView):
    def get(self):
        address = session.get('address', None)
        nfts = ContractMethods(address).get_all_nft_on_user()
        return render_template('show-nft.html', nfts=nfts)


class MyNFTDetailView(MethodView):
    def get(self, nft_id):
        address = session.get('address', None)
        form = SellNFT()
        nft = ContractMethods(address).get_nft_detail(nft_id)
        return render_template('my-nft-detail.html', nft=nft, form=form)

    def post(self, nft_id):
        address = session.get('address', None)
        form = SellNFT(request.form)
        if form.validate():
            data = [nft_id,
                    form.data['price'],
                    form.data['amount']]
            ContractMethods(address).sell_nft(data)
            return redirect('profile')

        nft = ContractMethods(address).get_nft_detail(nft_id)
        return render_template('my-nft-detail.html', nft=nft, form=form)


class GiftView(MethodView):
    def get(self):
        address = session.get('address', None)
        nft_ids = ContractMethods(address).get_all_nft_on_user(flag=True)
        form = Gift(nft_ids=nft_ids)
        return render_template('gift.html', form=form)

    def post(self):
        address = session.get('address', None)
        nft_ids = ContractMethods(address).get_all_nft_on_user(flag=True)
        form = Gift(request.form, nft_ids=nft_ids)
        if form.validate():
            ContractMethods(address).gift(form.data['to'], form.data['nft_ids'])
            return redirect('profile')
        return render_template('gift.html', form=form)


class SetSessionView(MethodView):
    def post(self, address):
        session['address'] = address
        return jsonify({'message': 'Успешно'})


class GetSessionView(MethodView):
    def get(self):
        return jsonify(address=session.get('address', None))


app.add_url_rule('/', view_func=MainView.as_view("home"))
app.add_url_rule("/profile/", view_func=ProfileView.as_view("profile"))
app.add_url_rule("/gift/", view_func=GiftView.as_view("gift"))

app.add_url_rule("/auctions/", view_func=AuctionsView.as_view("auctions"))
app.add_url_rule("/market/", view_func=MarketView.as_view("market"))

app.add_url_rule("/nft-detail/<int:nft_id>/", view_func=NFTDetailView.as_view("nft-detail"))
app.add_url_rule("/action-detail/<int:auction_id>/", view_func=AuctionDetailView.as_view("auction-detail"))

app.add_url_rule("/create-nft/", view_func=CreateNFTView.as_view("create-nft"))
app.add_url_rule("/create-collection/", view_func=CreateCollectionView.as_view("create-collection"))

app.add_url_rule("/show-collections/", view_func=ShowMyCollectionsView.as_view("show-collections"))
app.add_url_rule("/show-nft/", view_func=ShowMyNFTsView.as_view("show-nft"))

app.add_url_rule("/collection-detail/<int:collection_id>/", view_func=CollectionDetailView.as_view("collection-detail"))
app.add_url_rule("/my-nft-detail/<int:nft_id>/", view_func=MyNFTDetailView.as_view("my-nft-detail"))

app.add_url_rule("/get-session/", view_func=GetSessionView.as_view('get-session'))
app.add_url_rule("/set-session/<string:address>/", view_func=SetSessionView.as_view('set-session'))

if __name__ == '__main__':
    app.run(debug=True)

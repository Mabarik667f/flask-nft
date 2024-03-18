from wtforms import Form
import wtforms
from wtforms.widgets import DateTimeInput


class CreateNFT(Form):
    name = wtforms.StringField(label='Название')
    describe = wtforms.StringField(label='Описание')
    img = wtforms.FileField(label='Изображение')
    price = wtforms.IntegerField(label='Цена')
    amount = wtforms.IntegerField(label='Количество')
    collection_id = wtforms.SelectField(label='Коллекция', choices=[])

    def __init__(self, *args, **kwargs):
        collections = kwargs.pop('collections', None)
        super(CreateNFT, self).__init__(*args, **kwargs)
        if collections:
            self.collection_id.choices = collections


class CreateNFTCollection(Form):
    name = wtforms.StringField(label='Название')
    describe = wtforms.StringField(label='Описание')


class SellNFT(Form):
    price = wtforms.IntegerField(label='Цена')
    amount = wtforms.IntegerField(label='Количество')


class Bid(Form):
    price = wtforms.IntegerField(label='Ваша Ставка')


class ActivateCode(Form):
    ref_code = wtforms.StringField(label='Код друга')


class StartAuction(Form):
    collection_id = wtforms.SelectField('Коллекция')
    start = wtforms.DateTimeField('Дата начала', widget=DateTimeInput())
    end = wtforms.DateTimeField('Дата окончания', widget=DateTimeInput())
    start_bid = wtforms.IntegerField('Начальная ставка')
    max_bid = wtforms.IntegerField('Максимальная ставка')

    def __init__(self, collections, *args, **kwargs):
        super(StartAuction, self).__init__(*args, **kwargs)
        self.collection_id.choices = collections


class Gift(Form):
    to = wtforms.StringField("Адрес получателя")
    nft_ids = wtforms.SelectField('NFT')

    def __init__(self, nft_ids, *args, **kwargs):
        super(Gift, self).__init__(*args, **kwargs)
        self.nft_ids.choices = nft_ids
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class ProductTypes(models.Model): # テーブル作成 商品のカテゴリー
    name = models.CharField(('カテゴリー'),max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) # 作成日
    updated_at = models.DateTimeField(auto_now=True) # 更新日
    
    class Meta:
        db_table = 'product_types' # テーブル名の定義
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'
        
    def __str__(self): # 管理画面に表示されるモデル内のデータ(レコード)を判別するために必要
        return self.name
    
class Traders(models.Model): # テーブル作成 業者
    name = models.CharField(('業者'),max_length=1000)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    created_at = models.DateTimeField(auto_now_add=True) # 作成日
    updated_at = models.DateTimeField(auto_now=True) # 更新日
    class Meta:
        db_table = 'traders'# テーブル名の定義
        verbose_name = '業者'
        verbose_name_plural = '業者'
        
    def __str__(self):
        return self.name # 管理画面に表示されるモデル内のデータ(レコード)を判別するために必要


class ProductPictures(models.Model): # 製品の写真
    name = models.CharField(('画像名'),max_length=1000)
    picture = models.FileField(('画像'),upload_to='product_pictures/')
    created_at = models.DateTimeField(auto_now_add=True) # 作成日
    updated_at = models.DateTimeField(auto_now=True) # 更新日

    class Meta:
        db_table = 'product_pictures' # テーブル名の定義
        verbose_name = '商品の画像'
        verbose_name_plural = '商品の画像'
    
    def __str__(self): 
        return self.name
        
    
class Products(models.Model): # 製品
    name = models.CharField('名前', max_length=1000)
    stock = models.IntegerField('在庫数') # 在庫数
    proper_stock= models.IntegerField('適正在庫数') # 最大在庫数
    created_at = models.DateTimeField(auto_now_add=True) # 作成日
    updated_at = models.DateTimeField(auto_now=True) # 更新日
    product_type = models.ForeignKey( # 外部キー　CASCADEの場合紐付け先が削除されたら強制的に削除される
        ProductTypes, on_delete=models.CASCADE,verbose_name = '収納場所'
    )
    trader = models.ForeignKey(
        Traders, on_delete=models.CASCADE,verbose_name = '業者'
    )
    product_picture = models.ForeignKey(
        ProductPictures, on_delete=models.CASCADE,verbose_name = '写真'
    )
    
    class Meta:
        db_table = 'products' # テーブル名の定義
        verbose_name = '商品'
        verbose_name_plural = '商品'
        
    def __str__(self): # 管理画面に表示されるモデル内のデータ(レコード)を判別するために必要
        return self.name
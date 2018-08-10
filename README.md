# Try_django
<p>models.py</p>
このアプリケーションのモデル
データを保存したり、データベースとやり取りする
<p>views.py</p>
URLにリクエストが来たときに対応する処理を記述する
いわゆるコントローラーにあたる
<p>tests.py</p>
テストを記述する
<p>apps.py</p>
アプリケーションの設定を行う
今回は使用しない
<p>admin.py</p>
Djanogの管理サイトにこのアプリケーションを登録するときに使う

<p>manage.py</p>
管理コマンド
開発サーバーを起動したり、データベースのマイグレーションなどを行う
microblogディレクトリ
<p>settings.py</p>
microblog（ウェブアプリケーション）の設定
<p>urls.py</p>
URLとビューを結びつけるためのファイル
<p>wsgi.py</p>
デプロイするときに使う

```bash
python manage.py createsuperuser
```

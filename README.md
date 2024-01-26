# ex001.city_names_csv

全国の郵便番号一覧を保持するオブジェクトを作成する速度を計測する。


## app_from_csv.py

素朴にCSVから読み込む。

平均：0.249sec

思ったより全然速い。。



## app_from_py.py

pythonファイルにリテラルとして書く。

## app_from_pickle.py

作成したCityクラスのリストをpickle形式で保存し、それを読み込む。

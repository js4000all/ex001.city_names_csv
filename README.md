# ex001.city_names_csv

全国の市区町村名一覧を保持するオブジェクトを作成する速度を計測する。


## app_from_csv.py

素朴にCSVから読み込む。

平均：0.039sec

思ったより全然速いので、別の題材を探す。。



## app_from_py.py

pythonファイルにリテラルとして書く。

## app_from_pickle.py

作成したCityクラスのリストをpickle形式で保存し、それを読み込む。


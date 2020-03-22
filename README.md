# steem-Delegate-api
# steem代理查询api

本api可以查询代理给谁，以及谁代理给你

steemdatabase.db为数据库文件，目前已同步到区块41857643

database.py为更新数据库的文件，读取block.txt为开始区块开始更新

python_api.py 为API文件

用法：
查询你代理给谁？
http://127.0.0.1:667/who?id=maiyude&hash=7DFC55Axxxxx

查询谁代理给你？
http://127.0.0.1:667/towho?id=maiyude&hash=7DFC55Axxxxx

id=需要查询的用户
hash=python_api内设定的hash值


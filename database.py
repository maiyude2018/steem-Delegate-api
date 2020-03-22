import sqlite3
from beem.block import Block
from beem.steem import Steem
import time
p=1
www=0




s = Steem("https://steemd.minnowsupportproject.org")
s = Steem("https://api.steemit.com")

#读取日志
con = sqlite3.connect('steemdatabase.db')
cur = con.cursor()
f2 = open('block.txt', 'r')
txt = f2.read()
number_block=int(txt)
print("start:",number_block)

while p==1:
    try:
        #while True:
        block = Block(number_block,steem_instance=s)
        a=block.json_transactions
        print("Block:",number_block)
        write=0

        for i in a:
            timess=i["expiration"]
            operations=i["operations"][0]
            types=operations["type"]
            if types == "delegate_vesting_shares_operation":
                write=1
                print("find:",operations)
                name = operations["value"]["delegator"]
                towho = operations["value"]["delegatee"]
                vesting_shares=operations["value"]["vesting_shares"]["amount"]
                vesting = float(vesting_shares)/1000000
                number=s.vests_to_sp(vesting)
                number=round(number,2)
                print(name,towho,number,vesting,timess)
                cur.execute('REPLACE INTO daili VALUES (?,?,?,?,?)', (name,towho,number,vesting,timess))
        if write ==1 :
            con.commit()
        number_block += 1
        www +=1
        # 写入日志
        if www >1000:
            with open('block.txt', "w") as f:
                f.write(str(number_block))
            www =0
    except Exception as e:
        con.commit()
        print(e)
        # 写入日志
        with open('block.txt', "w") as f:
            f.write(str(number_block))
        print("wait,15s")
        time.sleep(15)
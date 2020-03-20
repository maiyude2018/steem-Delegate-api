import sqlite3
from beem.block import Block
from beem.steem import Steem

con = sqlite3.connect('daili5.db')
cur = con.cursor()


s = Steem()

#读取日志
number_block=20000000
end_block=number_block+2500000-1

print("开始区块:",number_block)

while True:
    if number_block >= end_block:
        with open('block.txt', "w") as f:
            f.write(str(number_block))
        con.commit()
        break
    try:
        if number_block >=end_block:
            with open('block.txt', "w") as f:
                f.write(str(number_block))
            con.commit()
            break
        www=0
        #while True:
        block = Block(number_block)
        a=block.json_transactions
        print("区块:",number_block)
        write=0
        for i in a:
            time=i["expiration"]
            operations=i["operations"][0]
            types=operations["type"]
            if types == "delegate_vesting_shares_operation":
                write=1
                print("发现:",operations)
                name = operations["value"]["delegator"]
                towho = operations["value"]["delegatee"]
                vesting_shares=operations["value"]["vesting_shares"]["amount"]
                vesting = float(vesting_shares)/1000000
                number=s.vests_to_sp(vesting)
                number=round(number,2)
                print(name,towho,number,vesting,time)
                cur.execute('REPLACE INTO daili VALUES (?,?,?,?,?)', (name,towho,number,vesting,time))
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
        print(e)
        # 写入日志
        f2 = open('error.txt', 'r')
        txt = f2.read()
        txt = txt + "\n" + str(number_block) + "\n"
        with open('error.txt', "w") as f:
            f.write(txt)
        print("等待15秒后继续")
        time.sleep(15)
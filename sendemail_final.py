import smtplib
import os
import keyboard
from time import sleep
smtp=smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login("std1013314@goo.tyai.tyc.edu.tw","125143960")
from_addr='TYAIstudent'
msg="""Subject:北科附工學生會正副會長投票\n
嗨咿～我是學生會❷號候選人
［李欣妍X楊哲驊］的助選人員
在這裡邀請大家
在6/1下午1點～6/3下午1點
至下方連結投給❷號噢！
傳送門🔗

https://reurl.cc/OAR37X

［我們的政見]

《上下學更便利🚶‍♀️🚶》
舊校舍與高二樓間新增出入口
投給❷號讓你能夠減少繞到正門的多餘時間

《開放手機使用📱》
發揮自主管理之精神，修正行動載具管理要點
投給❷號讓你可以更加靈活的使用手機來進行多元學習

《增設球類設備、比賽🎱》
積極爭取更多設備、辦理更多比賽
投給❷號來讓你能有舞台展現你的長才

《三信日✉️》
全校寫下期望改變具體政策，挑三封提供回覆
投給❷號讓你的訴求能被大家聽見

《增設販賣機🥤》
增設販賣機，讓學生更快速的購買飲品
投給❷號讓你不用大老遠的跑去萊爾富或福利社還要排隊

《增設調解委員會👨‍🏫》
協助解決師生之衝突，避免單方面權益受損等情形
投給❷號你能跟有衝突的師長進行更有效快速的溝通

《校園更新🏫》
將未使用空間改變成多功能用處之場地
將老舊、損壞設備更換
投給❷號不只能有更多的新場地實現你的想法，還有新的設備圍繞在你的學習喔

《聯誼活動☎️》
爭取增加多校聯誼活動次數
投給❷號能有更多更廣的社交圈，在任何事上面能有更多的幫忙（或許還能找到合適的另一半

《增設衛生紙、棉販賣機🧻》
爭取廁所提供衛生紙及衛生棉販賣機，防止不時之需
投給❷號再也不怕沒帶個人衛生用品還要尷尬的在其他人面前買了

《販賣更多冰品及新增熱飲🧊》
投票後提議販售符合標準之提供冰品及熱飲
由萊爾富及福利社決議是否販售
投給❷號讓你有更多元性的飲料選擇，也可以喝到一些當紅的好喝飲料ㄛ
《爭取更多學習機會🎠》
爭取增加各科出遊次數
投給❷號讓你能創造更多與同學的美好回憶

《物品傳承區🔧》
將畢業學生捐贈之物品及工具提供在校生免費使用
投給❷號讓你不再怕有物品壞掉但沒有辦法買的窘境

再麻煩您花一點時間
將您寶貴的一票投給❷號候選人
感謝您的支持💗"""

# to_addr = "std1013314@goo.tyai.tyc.edu.tw"
# status=smtp.sendmail(from_addr, to_addr, msg.encode("utf-8"))#加密文件，避免私密信息被截取
# if status=={}:
#     print(to_addr)
# else:
#     print(to_addr+"Erro")
# to_addr = "std1013304@goo.tyai.tyc.edu.tw"
# status=smtp.sendmail(from_addr, to_addr, msg.encode("utf-8"))#加密文件，避免私密信息被截取
# if status=={}:
#     print(to_addr)
# else:
#     print(to_addr+"Erro")
# smtp.quit()
# print("Are U ok?","ok請按e","不ok請按q")
# state = 1
# while state:
#     if keyboard.is_pressed("e"):
#         state = 0
#     if keyboard.is_pressed("q"):
#         os._exit(0)

class_number1 = ["111","113","115","117","118","121",
                "122","131","132","133","134"]
class_number2 = ["141","142","123","124","125","127",
                "151","152","312","181","182"]
# class_number_test = ["133"]
grade = ["10","09","08"]
# grade_test = ["10"]
email = ["tyai35th2@gmail.com","tyai35th2a@gmail.com","tyai35th2b@gmail.com","tyai35th2c@gmail.com",
        "tyai35th2d@gmail.com","tyai35th2e@gmail.com"]
password = ["hsvdtbszycmftlyz","nmivzoydmefltuzc","vuafgytesmsadihf","whfwonzlfvwimpqy",
        "wkapymchybxgxkrr","rsvtklyukbybqetf"]
sended = 0
ac = 0
grade_num = 0
people = 0

for e in email:
    class_num = 0
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(e,password[ac])
    print(e,password[ac],"changed password")
    for k in range(1,12):
        if (ac+1) % 2 == 0:
            c = class_number2[class_num]
        else:
            c = class_number1[class_num]
        for i in range(1,41):
            std_email = "std"+grade[grade_num]+c+"%02d"%i+"@goo.tyai.tyc.edu.tw"
            to_addr=std_email
            if int(grade[grade_num]) >= 9:
                if i > 0 and c == "181" and int(grade[grade_num]) == 9:
                    status=smtp.sendmail(from_addr, to_addr, msg.encode("utf-8"))#加密文件，避免私密信息被截取
                    if status=={}:
                        print(std_email)
                        people += 1
                    else:
                        print(std_email+"Erro")
                elif int(c)>181 and int(grade[grade_num]) == 9:
                    status=smtp.sendmail(from_addr, to_addr, msg.encode("utf-8"))#加密文件，避免私密信息被截取
                    if status=={}:
                        print(std_email)
                        people += 1
                    else:
                        print(std_email+"Erro")
            else:
                status=smtp.sendmail(from_addr, to_addr, msg.encode("utf-8"))#加密文件，避免私密信息被截取
                if status=={}:
                    print(std_email)
                    people += 1
                else:
                    print(std_email+"Erro")
            if people >= 50:
                people = 0
                sleep(80)
            # print(std_email)
            sended += 1
        class_num += 1
    if (ac+1)%2 == 0 and ac != 5:
        grade_num += 1
    ac += 1
print(sended)              
smtp.quit()
print("任務完成，按E結束")
state = 1
while state:
    if keyboard.is_pressed("e"):
        state = 0
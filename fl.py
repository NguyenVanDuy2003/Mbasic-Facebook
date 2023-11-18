from colorama import Fore, Back, Style, init
import requests,re
from datetime import datetime
import time

class ApiFacebook:
    def __init__(self,cookies) -> None:
        cookie = cookies.split(';')
        title = []
        value = []
        for i in range(len(cookie)-1):
            title.append(cookie[i].split('=')[0].strip())
            value.append(cookie[i].split('=')[1].strip())
        self.cookies = dict(zip(title,value))
        self.headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'referer': 'https://mbasic.facebook.com',
            'sec-ch-prefers-color-sheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-full-version-list':'"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-model':'""',
            'sec-ch-ua-platform':'"Windows"',
            'sec-ch-ua-platform-version':'"7.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'viewport-width': '708',
        }
        self.uid = self.cookies['c_user']
    def GetUserName(self):
        Home = requests.get(f"https://mbasic.facebook.com/{self.uid}",headers=self.headers,
        cookies=self.cookies).text
        self.username = Home.split('<title>')[1].split('</')[0]
        print(Fore.BLUE + f"Your User Name Account:  {self.username} / UID : {self.uid}")
    def LikePost(self,id_post):
        Home = requests.get(f"https://mbasic.facebook.com/" + id_post,headers=self.headers,
        cookies=self.cookies).text
        try:
            likeNode = "https://mbasic.facebook.com/a/like.php?"+Home.split("/a/like.php?")[1].split('"')[0].replace("amp;","")
            liked = requests.get(likeNode,headers=self.headers,cookies=self.cookies)
            if liked.status_code == 200:
                print(Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Da Like : {id_post}")
        except:
            print(str(datetime.now().time()).split(".")[0]+ " | Post da duoc like / khong tim thay nut like")
    def LikeCommentPost(self,id_post):
        Home = requests.get(f"https://mbasic.facebook.com/" + id_post,headers=self.headers,
        cookies=self.cookies).text
        try:
            likeNode = "https://mbasic.facebook.com/a/comment.php?"+Home.split("/a/comment.php?")[1].split('"')[0].replace("amp;","")
            liked = requests.get(likeNode,headers=self.headers,cookies=self.cookies)
            if liked.status_code == 200:
                print( Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Da Like Comment : {id_post}")
        except:
            print(str(datetime.now().time()).split(".")[0]+ f" | Comment Post Đã Được LIKE / Không Tìm Thấy Nút Like Comment | {id_post}")
    def ReactionPost(self,id_post,Reaction):
        Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers,cookies=self.cookies).text
        try:
            React = "https://mbasic.facebook.com/reactions/picker/?"+ Home.split("/reactions/picker/?")[1].split('"')[0].replace("amp;","")
            ReactWeb = requests.get(React,headers=self.headers,cookies=self.cookies).text
            ReactList = re.findall('\/ufi\/reaction\/\?.*?"',ReactWeb)
            index = 1 if Reaction == "LOVE" else 2 if Reaction == "CARE" else 3 if Reaction == "HAHA" else 4 if Reaction == "WOW" else 5 if Reaction == "SAD" else 6
            ReactComplete = requests.get("https://mbasic.facebook.com"+ReactList[index].replace("amp;","").replace('"',""),headers=self.headers,cookies=self.cookies)
            if ReactComplete.status_code == 200:
                print(Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Đã Thả {Reaction} Vào Post : {id_post}")
        except:
            print(Fore.RED + str(datetime.now().time()).split(".")[0]+" | Không Tìm Thấy Reaction ")
    def ReactionCommentPost(self,id_post,Reaction):
        Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers,cookies=self.cookies).text
        try:
            React = "https://mbasic.facebook.com/reactions/picker/?"+ Home.split("/reactions/picker/?")[2].split('"')[0].replace("amp;","")
            ReactWeb = requests.get(React,headers=self.headers,cookies=self.cookies).text
            ReactList = re.findall('\/ufi\/reaction\/\?.*?"',ReactWeb)
            index = 1 if Reaction == "LOVE" else 2 if Reaction == "ANGRY" else 3 if Reaction == "HAHA" else 4 if Reaction == "WOW" else 5 if Reaction == "SAD" else 6
            ReactComplete = requests.get("https://mbasic.facebook.com"+ReactList[index].replace("amp;","").replace('"',""),headers=self.headers,cookies=self.cookies)
            if ReactComplete.status_code == 200:
                print(Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Đã Thả {Reaction} Vào Comment Post : {id_post}")
        except:
            print(Fore.RED + str(datetime.now().time()).split(".")[0]+" | Không Tìm Thấy Reaction ")
    def CommentPost(self,id_post,content):
        Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers,cookies=self.cookies).text
        try:
            UrlPost = 'https://mbasic.facebook.com/a/comment.php'+Home.split('action="/a/comment.php')[1].split('"')[0].replace("amp;","")
            fb_dtsg = Home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = Home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
            data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'comment_text': content,
            }
            Comment = requests.post(UrlPost,headers=self.headers,cookies=self.cookies,data=data)
            if Comment.status_code == 200: 
                print(Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Da Comment post: {id_post} voi noi dung la: {content}")

        except:
            print(str(datetime.now().time()).split(".")[0]+f" | Khong tim thay noi Comment")
    def SharePost(self, id_post,content_share=""):
        Home = requests.get(f"https://mbasic.facebook.com/{id_post}",headers=self.headers,cookies=self.cookies).text
        try: 
            ShareNode = 'https://mbasic.facebook.com/composer/mbasic/?'+ Home.split("/composer/mbasic/?")[1].split('"')[0].replace("amp;","")
            ShareWeb = requests.get(ShareNode, headers=self.headers,cookies=self.cookies).text
            UrlPost = "https://mbasic.facebook.com/composer/mbasic/?csid="+ShareWeb.split('action="/composer/mbasic/?csid=')[1].split('"')[0].replace("amp;","")
            fb_dtsg = ShareWeb.split('name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = ShareWeb.split('name="jazoest" value="')[1].split('"')[0]
            target = ShareWeb.split('name="target" value="')[1].split('"')[0]
            csid = ShareWeb.split('name="csid" value="')[1].split('"')[0]
            privacyx = ShareWeb.split('name="privacyx" value="')[1].split('"')[0]
            appid = ShareWeb.split('name="appid" value="')[1].split('"')[0]
            sid = ShareWeb.split('name="sid" value="')[1].split('"')[0]
            shared_from_post_id = ShareWeb.split('name="shared_from_post_id" value="')[1].split('"')[0]
            data = {
                'fb_dtsg':fb_dtsg,
                'jazoest':jazoest,
                'target':target,
                'csid':csid,
                'c_src':'share',
                'referrer':'permalink',
                'ctype':'advanced',
                'cver': 'amber_share',
                'waterfall_source': 'advanced_composer_timeline',
                'privacyx':privacyx,
                'appid': appid,
                'sid': sid,
                'm': 'self',
                'xc_message': content_share,
                'view_post': 'Chia sẻ',
                'shared_from_post_id': shared_from_post_id
                }
            Share = requests.post(UrlPost,headers=self.headers,cookies=self.cookies,data=data)
            if Share.status_code == 200:
                print(Fore.GREEN + str(datetime.now().time()).split(".")[0]+f" | Dã Chia Sẻ POST: {id_post} Với Nội Dung Là: {content_share}")
        except:
            print(str(datetime.now().time()).split(".")[0]+f" | Khong tim thay nut share")
    def FollowUser(self,uid):
        Home = requests.get(f"https://mbasic.facebook.com/{uid}",headers=self.headers,cookies=self.cookies).text
        try:
            FollowNode = "https://mbasic.facebook.com/a/subscribe.php?"+ Home.split('/a/subscribe.php?')[1].split('"')[0].replace("amp;","")
            Follow = requests.get(FollowNode,headers=self.headers,cookies=self.cookies)
            if Follow.status_code == 200:
                print(str(datetime.now().time()).split(".")[0]+f" | Da follow UID: {uid}")
            else:
                print(str(datetime.now().time()).split(".")[0]+f" | Bi loi gi day khong the follow")
        except: 
            print(str(datetime.now().time()).split(".")[0]+f" | Khong tim thay nut follow / da follow")
    def JoinGroup(self,uid):
        Home = requests.get(f"https://mbasic.facebook.com/groups/{uid}",headers=self.headers,cookies=self.cookies).text
        try:
            UrlPost = "https://mbasic.facebook.com/a/group/join?" + Home.split('action="/a/group/join/?')
            [1].split('"')[0].replace("amp;","")
            fb_dtsg = Home.split('name="fb_dtsg" value="')[1].split('"')[0]
            jazoest = Home.split('name="jazoest" value="')[1].split('"')[0]
            data = {
                'fb_dtsg':fb_dtsg,
                'jazoest':jazoest
            }
            join = requests.post(UrlPost,headers=self.headers,cookies=self.cookies,data=data)
            if join.status_code == 200:
                print(str(datetime.now().time()).split(".")[0]+f" | Da tham gia Group: {uid}")
            else:
                print(str(datetime.now().time()).split(".")[0]+" | Bi loi gi day khong the join group: {uid}")
        except:
            print(str(datetime.now().time()).split(".")[0]+" | Khong tim thay nut join group / da join: {uid}")


Facebook = ApiFacebook("c_user=61552931384448; xs=35:M1kHcChBHOVUZA:2:1699236418:-1:-1; fr=0BBvrTxDZYYNIDZXX.AWWGyjFrbj8vjQhbZhE4cJkPcT0.BlSEo2..AAA.0.0.BlSEo2.AWVjqn_ziEM; datr=NkpIZUrnEJe8qPt-jg3v-kDM")
Facebook.GetUserName()
# Facebook.LikePost('776304867204579')
# Facebook.ReactionPost('122102255294104790','LOVE')

# Facebook.SharePost('pfbid02kdepRpvKXRr8sZGxfvB3cJ44XwZF1E9hSuMvAJWxjJ5AwQpcFvHBEF2rzzcK2oDEl', "duy test")
# Facebook.FollowUser('100089904416985')
id='61552931384448'
tds_token = 'TDSQfigjclZXZzJiOiIXZ2V2ciwiIzIzM5VHZ5VHZ5VHZiojIyV2c1Jye'
account = requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={tds_token}')
while True :
    if True:
        fields = 'reaction'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        try:
            for mission in data:
                Facebook.ReactionPost(mission['id'],mission['type'])
                receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type={mission["type"]}&id={mission["id"]}&access_token={tds_token}')
                coin = receiveCoins.json()
                try:
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
                except:
                    print(Fore.RED + f"Không Tìm Thấy Nút {mission['type']}")

        except:
            print(Fore.YELLOW + f"Vui lòng đợi REACTION {getListMission.json()['countdown']} Giây.")
    if True:
        fields = 'like'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        try:
            for mission in data:
                Facebook.LikePost(mission['id'])
                receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type={mission["type"]}&id={mission["id"]}&access_token={tds_token}')
                coin = receiveCoins.json()
                try:
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
                except:
                    print(Fore.RED + f"Không Tìm Thấy Nút LIKE")

        except:
            print(Fore.YELLOW + f"Vui lòng đợi LIKE {getListMission.json()['countdown']} Giây.")

    if True:
        fields = 'share'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&ac8cess_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        try:
            for mission in data:
                print(mission)
                Facebook.SharePost(mission['id'],"")
                receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type=SHARE&id={mission["id"]}&access_token={tds_token}')
                if receiveCoins.status_code == 200:
                    coin = receiveCoins.json()
                    print(coin)
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")

                else :
                    print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
        except:
            print(Fore.YELLOW + f"Vui lòng đợi SHARE {getListMission.json()['countdown']} Giây.")
    if True:
        fields = 'follow'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        try:
            for mission in data:
                try:
                    Facebook.FollowUser(mission['id'])
                    receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type=FOLLOW&id={mission["id"]}&access_token={tds_token}')
                    coin = receiveCoins.json()
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
                   
                except:
                    print(Fore.RED + f"{mission['id']} | Không Tìm Thấy Nút Follow")
        except:
            print(Fore.YELLOW + f"Vui lòng đợi Follow {getListMission.json()['countdown']} Giây.")

    if True:
        fields = 'comment'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        try:
            for mission in data:
                try:
                    Facebook.CommentPost(mission['id'],mission['msg'])
                    receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type=COMMENT&id={mission["id"]}&access_token={tds_token}')
                    coin = receiveCoins.json()
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
                except:
                    print(Fore.RED + f"{mission['id']} + Không Tìm Thấy Nút Comment")
        except:
            print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
    if True:
        fields = 'reactcmt'
        getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
        while 'countdown' in getListMission.json():
            if(int(getListMission.json()['countdown']) < 10):
                print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")
                time.sleep(int(getListMission.json()['countdown']))
                getListMission = requests.get(f'https://traodoisub.com/api/?fields={fields}&access_token={tds_token}')
            else:
                time.sleep(5)
                break;
        data = getListMission.json()
        print(data)
        try:
            for mission in data:
                if mission["type"] == 'LIKECMT':
                    Facebook.LikeCommentPost(mission['id'])
                else:
                    Facebook.ReactionCommentPost(mission['id'],mission['type'])

                receiveCoins = requests.get(f'https://traodoisub.com/api/coin/?type={mission["type"]}CMT&id={mission["id"]}&access_token={tds_token}')
                coin = receiveCoins.json()
                try:
                    if 'data' in coin:
                        print(Fore.GREEN + f"Dã nhận Thành Công | {coin['data']['msg']}")
                    else:
                        print(Fore.RED + f"Nhận Không Thành Công | {receiveCoins.json()['error']}")
                except:
                    print(Fore.RED + f"Không Tìm Thấy Nút {mission['type']}")

        except:
            print(Fore.YELLOW + f"Vui lòng đợi {getListMission.json()['countdown']} Giây.")

        





            
        

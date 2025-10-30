import get_url
import requests
import re
def get_art_data(artworkAPI):
    # print(artworkAPI)
    headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
        }
    #获取作品like，bookmarks，views值，为后续排序做准备
    artCollect = []
    time = 1
    for item in artworkAPI:
        respArt = requests.get(item,headers=headers)
        respArt.encoding = 'utf-8'
        print(time)
        #限制请求次数
        time += 1
        likeCount = re.findall(r'"likeCount":(\d+)', respArt.text)
        bookMarkCount = re.findall(r'"bookmarkCount":(\d+)', respArt.text)
        viewsCount = re.findall(r'"viewCount":(\d+)', respArt.text)
        artWorkID = re.findall(r'https://www.pixiv.net/ajax/illust/(\d+)',item)
        artCollect.append([likeCount[0],bookMarkCount[0],viewsCount[0],artWorkID[0]])
        if time > 200:
            break
    return artCollect

#自定义三个函数，分别以likeCount,bookCount,viewsCount为依据进行排序
def likecount_rank(artCollect):
    artCollect.sort(key=lambda x:x[0], reverse=True)
    return

def bookmarkcount_rank(artCollect):
    artCollect.sort(key=lambda x:x[1], reverse=True)
    return

def viewscount_rank(artCollect):
    artCollect.sort(key=lambda x:x[2], reverse=True)
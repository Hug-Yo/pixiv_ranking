import requests
import re
def get_artworks_url():
    #输入排行榜url
    rankURL = 'https://www.pixiv.net/ranking.php'
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
    }
    respRank = requests.get(rankURL,headers=headers)
    # print(respRank.text)
    #抓取页面中作品的url，此处暂不对动态加载做应对处理
    artWorkID = re.findall(r'"/artworks/(\d*?)"',respRank.text)
    artWorkID = list(set(artWorkID))
    artWorkAPI = []
    for _ in range(len(artWorkID)):
        artWorkAPI.append('https://www.pixiv.net/ajax/illust/'+artWorkID[_])
    return artWorkAPI
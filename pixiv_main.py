import get_url
import data_analysis

print('-'*20+'欢迎使用'+'-'*20)
print('正在获取今日pixiv排行榜信息...')
artWorkAPI = get_url.get_artworks_url()
print('正在获取作品详情...')
artCollect = data_analysis.get_art_data(artWorkAPI)
ans = input('''
请选择排序方式：
按喜欢数量排序（输入1）
按收藏数量排序（输入2）
按浏览数量排序（输入3）
''')
if ans == '1':
    print('按喜欢排序的作品pid为：')
    data_analysis.likecount_rank(artCollect)
    for item in artCollect:
        print(item[3])
if ans == '2':
    print('按收藏排序的作品pid为：')
    data_analysis.bookmarkcount_rank(artCollect)
    for item in artCollect:
        print(item[3])
if ans == '3':
    print('按浏览量排序的作品pid为：')
    data_analysis.viewscount_rank(artCollect)
    for item in artCollect:
        print(item[3])
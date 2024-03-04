import requests
import time


# 'https://stickershop.line-scdn.net/stickershop/v1/sticker/605235406/android/sticker.png?v=1'
# Divide the url into 3 parts
url_front ='https://stickershop.line-scdn.net/stickershop/v1/sticker/'
url_rear = '/android/sticker.png?v=1'
start_num = 605235406

#nums of stamp
n = 40

jpg_header = {
    #your user-agnet
}

for i in range(n):
    num = start_num + i
    jpg = requests.get(url_front+str(num)+url_rear, headers=jpg_header)  
    f = open('./yourfolder/' + str(i+1)+'.png/gif/...', 'wb')
    f.write(jpg.content)
    f.close()
    time.sleep(0.2)

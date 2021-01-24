

import requests


json={"cityCode":"AR00357","checkInDate":"2021-01-24","days":1,"districtCode":"",
      # "keyWord":"","brands":[],"starTypes":[],"bzLat":"","bzLng":"",
      # "loLat":29.563009,"loLng":106.551556,"sort":7,"minPrice":0,"maxPrice":
      #     "9999","page":1,"size":10,"oversea":'false',"channelCode":"CA00046","webSource":"PC_JINJIANG"
      }
header={
'Host': 'hotel.bestwehotel.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
# 'Accept': 'application/json, text/plain, */*',
# 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Content-Type': 'application/json;charset=utf-8',
# 'Content-Length': '300',
# 'Origin': 'https://hotel.bestwehotel.com',
# 'Connection': 'keep-alive',
# 'Referer': 'https://hotel.bestwehotel.com/HotelSearch/?checkinDate=2021-01-24&checkoutDate=2021-01-25&cityCode=AR00357&queryWords=Cookie: tongji_key=4f1642f8-9733-11c9-e2a8-07b8f4a91e92; Hm_lvt_b6e767c4467dcad9be907eab9e9c78ac=1611495966; Hm_lpvt_b6e767c4467dcad9be907eab9e9c78ac=1611496474',
# 'Pragma': 'no-cache',
# 'Cache-Control': 'no-cache',
# 'TE': 'Trailers',
}


response=requests.post("https://hotel.bestwehotel.com/api/hotel/searchHot",headers=header,json=json)


print(response)
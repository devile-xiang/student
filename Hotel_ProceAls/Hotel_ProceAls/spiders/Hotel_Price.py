
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from scrapy import Spider



class Hotel_Price(Spider):

    name='hotelspider'

    # chorme_options = Options()
    # chorme_options.add_argument("--headless")
    # chorme_options.add_argument("--disable-gpu")


    def start_requests(self):
        driver=webdriver.Chrome()
        driver.get("https://hotel.bestwehotel.com/HotelSearch/?checkinDate=2021-01-24&checkoutDate=2021-01-25&cityCode=AR00357&queryWords=")

        page_so=driver.page_source

        print(page_so)














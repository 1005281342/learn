import random
from time import sleep

from selenium import webdriver

url_list = [
    'https://www.zhipin.com/job_detail/',

]


def ni_hao(m):
    # liuLanQi.find_element_by_xpath('//*[@id="quick_reply"]').click()

    sleep(1+random.randint(1, 10))
    print(m)

    a = ['Python', 'Python实习', '上海Python', '上海Python实习', '深圳Python', '深圳Python实习',
         '杭州Python', '杭州Python实习']
    neiRong = liuLanQi.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input')
    # //*[@id="keyword"]
    neiRong.clear()
    neiRong.send_keys(a[random.randint(0, 8)])

    # 提交
    print('提交')
    liuLanQi.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button').click()


if __name__ == '__main__':

    for url_item in url_list:  # 'D:\c\chromedriver4win1064\chromedriver.exe'
        liuLanQi = webdriver.Chrome()
        liuLanQi.get(url_item)
        liuLanQi.maximize_window()

        # qieHuan = liuLanQi.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()
        dengLu = liuLanQi.find_element_by_xpath('//*[@id="header"]/div/div[3]/div/a[4]').click()

        # user = liuLanQi.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/form/div[1]/span[2]/input')
        # user.send_keys('17673502448')

        # passw = liuLanQi.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/form/div[2]/span/input')
        # passw.send_keys('qq1005281342')

        sleep(10)

        # submit = liuLanQi.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/form/div[4]/button').click()
        print('模拟登录成功')

        qiuZhi = liuLanQi.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[2]/a').click()

        for url_item in range(10):
            sleep(1)

        a = ['Python', 'Python实习', 'python应届生']
        neiRong = liuLanQi.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input')

        neiRong.send_keys(a[random.randint(0, 2)])
        # 提交
        print('提交')
        liuLanQi.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button').click()

        i = 1

        while i < 666:
            sleep(5)
            if (i > 30) and (i % 30) == 0:
                print('已经连续搜索30次了，休息2S')
                sleep(2)
            try:
                ni_hao(i)
                print(i)

            except Exception as e:
                print('网络延迟，沉默2S: '+str(e))
                sleep(2)

            i = i + 1

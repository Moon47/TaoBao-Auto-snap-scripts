from selenium import webdriver
import datetime
import time


def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在5秒内完成扫码")
        time.sleep(5)
        browser.get("https://cart.taobao.com/cart.htm")

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times, choose):
    # 点击购物车里全选按钮
    if choose == 2:
        print("请手动勾选需要购买的商品")
        time.sleep(5)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        # 对比时间，时间到的话就点击结算
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element_by_id("J_SelectAll2"):
                            browser.find_element_by_id("J_SelectAll2").click()
                            break
                    except Exception:
                        print("找不到购买按钮")
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print("结算成功")
                        break
                except Exception:
                    pass
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                except Exception:
                    print("再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":
    # times = input("请输入抢购时间，格式如(2024-06-05 19:35:00):")
    times = "2024-06-05 19:35:00"
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    # choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(times, 2)

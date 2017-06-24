from selenium import webdriver
from urllib.parse import urljoin
import time
from crontab import CronTab

#Phanttomjs Driverを入手
browser = webdriver.PhantomJS(
    '/home/ubuntu/workspace/node_modules/.bin/phantomjs')

#メールアドレスとパスワードを変数に保存

EMAIL = "kdmgs110@icloud.com"
PASSWORD = "kdmgs110"

#いいねしたいカテゴリを指定する

timeline = "https://newspicks.com/timeline/"

#いいねした人の数をセット(後でインクリメントします。)

numberOfLikes = 0



#暗黙的な待機時間を3秒
browser.implicitly_wait(3)

#urlを読み込む
browser.set_window_size(1124, 850) # set browser size.
login_url = "https://newspicks.com/"


#News Picksにログインする
browser.get(login_url)
print("https://newspicks.com/にアクセスしました")
browser.implicitly_wait(5)

#画面右上のログインボタンを押して、ログインモーダルを読み込む（これをしないとログインのinputが読み込まれない）

e = browser.find_element_by_class_name("login")
e.click()
browser.implicitly_wait(5)

#フォームにEMAILとPASSWORDを入力する

e = browser.find_element_by_id("login-username")
print(e)
e.clear()
e.send_keys(EMAIL)
e = browser.find_element_by_id('login-password')
e.send_keys(PASSWORD)

#フォームを送信

frm = browser.find_element_by_xpath("//*[@id='login-form-dialog']/div/div[5]/div[2]/button[1]") #classが複数存在するので、Xpathで指定
print(frm.text)
frm.click()

#ログイン後のデータの読み込みを行うために5秒まち、ログインに成功しているか確認する

browser.implicitly_wait(10)
messages = browser.find_element_by_class_name("display-name")

print(messages.text,end="")
print("としてログインしました")

#カテゴリに移動してスクロールする
browser.get(timeline)
print("タイムラインにアクセスしました。")

# ページを一番下までスクロールし、記事のlikeボタンを全部取得する
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("1度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("2度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("3度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("1度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("2度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("3度目のスクロールです")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("1度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("2度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("3度目のスクロールです")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("1度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("2度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("3度目のスクロールです")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("1度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("2度目のスクロールです")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("3度目のスクロールです")



users = browser.find_elements_by_class_name("like")
	
	
# 全部いいねする
	   
for user in users:
	user.click()
	numberOfLikes += 1
	print("いいねしました")
	
print('いいねした人の数:', end='')
print(len(users))
	   

#ブラウザーを終了
print("合計" + str(numberOfLikes) + "いいねしました")
browser.quit
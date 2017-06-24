from selenium import webdriver
from urllib.parse import urljoin
import time

#Phanttomjs Driverを入手
browser = webdriver.PhantomJS(
    '/home/ubuntu/workspace/node_modules/.bin/phantomjs')

#メールアドレスとパスワードを変数に保存

EMAIL = "kdmgs110@icloud.com"
PASSWORD = "kdmgs110"


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

#カテゴリに移動する

#いいねしたいカテゴリを指定する

categories = ['https://newspicks.com/theme-news/technology/',
    'https://newspicks.com/theme-news/business/',
    'https://newspicks.com/theme-news/economic/',
    'https://newspicks.com/theme-news/market/',
    'https://newspicks.com/theme-news/education/',
    'https://newspicks.com/theme-news/sports/',
    'https://newspicks.com/theme-news/innovation/']

for category in categories:
    browser.get(category)
    print("カテゴリ名:", end="")
    print(category)
    print("このカテゴリの記事をすべて取得します")
    browser.implicitly_wait(5)
    
    #News Picksの絶対パスを指定する
    base = "https://newspicks.com/"
    
    #教育カテゴリのタイトルのオブジェクトを取得する
    
    e = browser.find_elements_by_css_selector(".news-card.vertical") #これでタイトルのdivが取れます。
    numberOfPage = len(e)
    print('取得する記事の数:', end="")
    print(numberOfPage)
    
    	
    #カテゴリのすべての記事のURLを取得し、一つ一つの記事にアクセスし、そこのユーザー全員をいいねする
    
    for i in range(numberOfPage): #取得した記事数
    	print("現在のページ:" + str(i + 1) + "/" + str(numberOfPage))
    	e = browser.find_elements_by_css_selector(".news-card.vertical")
    	
    	
    	#記事の取得に成功したら、その記事にアクセスし全部いいね、失敗したら次のカテゴリに移ります
    	try:
        	print(e[i].get_attribute("data-id"))
        	# http://newspicks.com/news/[data-id]となるよう加工する
        	data_id = e[i].get_attribute("data-id") #記事のIDを返す
        	news = "news/"
        	newspage = news + data_id #/news/数字となる 
        	url = base + newspage # http://newspicks.com/news/2311428
        	print(url)
        	
        	# 取得したURLにアクセスして、5秒待つ
        	browser.get(url)
        	print("アクセスしたURL:", end="")
        	print(url)
        	browser.implicitly_wait(5)
        	
        	# ほかのピックをクリックして、ページ一番下までスクロールする
        	
        	e = browser.find_element_by_class_name("show-other-pick") #他ピックを表示する
        	users = browser.find_elements_by_class_name("like")
        	
        	
        	# 全部いいねする
        	   
        	for user in users:
        	   		user.click()
        	   		numberOfLikes += 1
        	   		print("いいねしました")
        	
        	print('いいねした人の数:', end='')
        	print(len(users))
        	   
        	# 10秒待って、元のURLに戻る
        	   
        	print("10秒待機します")
        	browser.implicitly_wait(50)
    	except:
            print("記事の取得に失敗しました。次のカテゴリに移動します")
            browser.implicitly_wait(50)
    	#カテゴリすべての記事をいいねしたら、次のカテゴリに移動する
    	browser.get(category)
    	print("現在のカテゴリに戻りました。次のカテゴリに行きます。")
	
	
	#ブラウザーを終了
print("合計" + str(numberOfLikes) + "いいねしました")
print(str(numberOfPage) + "記事をピックしたすべてのユーザーをいいねしました。プログラムを終了します。")
browser.quit
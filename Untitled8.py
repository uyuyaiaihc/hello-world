#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[76]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
##進入uber eat
driver = webdriver.Chrome("/Users/huangziyong/chromedriver")
driver.get("https://www.google.com")
s = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
s.send_keys('uber eat')
s.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="vn1s0p1c0"]/h3').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div/div/div/a[2]').click()
##登入
email = driver.find_element_by_xpath('//*[@id="useridInput"]')
email.send_keys('0912697877')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app-body"]/div/div[1]/form/button').click()
time.sleep(2)
passwords = driver.find_element_by_xpath('//*[@id="password"]') 
passwords.send_keys('je890301ffery')
driver.find_element_by_xpath('//*[@id="app-body"]/div/div/form/button').click()
###輸地址
address = driver.find_element_by_xpath('//*[@id="location-enter-address-input"]')
address.send_keys('台大社會科學院')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div/div/div/div[6]/div[1]/button/div[3]').click()
##想要吃的東東
food_you_may_want = input()
search_food = driver.find_element_by_xpath('//*[@id="search-suggestions-input"]')
search_food.send_keys(food_you_may_want)
driver.find_element_by_xpath('//*[@id="search-suggestions-item-0"]')
##結帳
def pay_the_bill(driver):
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[4]/div/div[2]/div/button').click()
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[5]/div/div[10]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div[2]/div[4]/div[7]/button').click()
##pop up food
sample_code = '//*[@id="wrapper"]/div[2]/div[4]/div[1]/a/article/div/div[1]'
sample_code = list(sample_code)
count = 0
while True:
    count += 1
    w = str(count)
    a[37]=w
    fl = "".join(a)
    driver.find_element_by_xpath(fl).click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="clamped-content-menu_item_title"]').click()
    asking1 = input()
    if asking1 == "n":
        driver.back()
        driver.back()
        time.sleep(3)
    elif asking1 =="y":
        break
##確定點完商品and 結帳
asking2 = input()
if asking2 == "y":
    pay_the_bill(driver)


# In[78]:


###輸地址
address = driver.find_element_by_xpath('//*[@id="location-enter-address-input"]')
address.send_keys('台大社會科學院')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div/div/div/div[6]/div[1]/button/div[3]').click()
##想要吃的東東
food_you_may_want = input()
search_food = driver.find_element_by_xpath('//*[@id="search-suggestions-input"]')
search_food.send_keys(food_you_may_want)
driver.find_element_by_xpath('//*[@id="search-suggestions-item-0"]')


# In[84]:


##結帳
def pay_the_bill(driver):
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[4]/div/div[2]/div/button').click()
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[5]/div/div[10]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div[2]/div[4]/div[7]/button').click()
##pop up food
sample_code = '//*[@id="wrapper"]/div[2]/div[4]/div[1]/a/article/div/div[1]'
sample_code = list(sample_code)
count = 0
while True:
    count += 1
    w = str(count)
    a[37]=w
    fl = "".join(a)
    driver.find_element_by_xpath(fl).click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="clamped-content-menu_item_title"]').click()
    asking1 = input()
    if asking1 == "n":
        driver.back()
        driver.back()
        time.sleep(3)
    elif asking1 =="y":
        break
##確定點完商品
asking2 = input()
if asking2 == "y":
    pay_the_bill(driver)


# In[43]:


##結帳
def pay_the_bill(driver):
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[4]/div/div[2]/div/button').click()
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div[6]/div[5]/div/div[10]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div[2]/div[4]/div[7]/button').click()


# In[71]:


driver.close()


# In[81]:


##想要吃的東東
food_you_may_want = input()
search_food = driver.find_element_by_xpath('//*[@id="search-suggestions-input"]')
search_food.send_keys(food_you_may_want)
driver.find_element_by_xpath('//*[@id="search-suggestions-item-0"]').click()


# In[ ]:


import tkinter as tk  
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 建立視窗window
window = tk.Tk()

# 給視窗起名字
window.title('Wellcome to food 4 you')

# 設定視窗的大小
window.geometry('400x300')  # 這裡的乘是小x

# 設定背景格式
canvas = tk.Canvas(window, width=400, height=135, bg='blue')
canvas.pack(side='top')
tk.Label(window, text='Welcome Lazy',font=('Arial', 16)).pack()

# 使用者資訊
tk.Label(window, text='Your Phone:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)


# 使用者名稱
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)


# 使用者密碼
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14))
entry_usr_pwd.place(x=120,y=215)

def login():
    driver=webdriver.Chrome()
    driver.get('https://www.ubereats.com/zh-TW/?utm_source=google&utm_medium=cpc-nonbrand&utm_campaign=search-google-nonbrand_195_94_tw-taipei_e_acq_all_cpc_ja_bmm_cuisine_ds3&adgroup_name=Cuisine_%E9%9F%93%E5%9C%8B%E7%BE%8E%E9%A3%9F+Korean%3EDS3&utm_term=%E7%BE%8E%E9%A3%9F%E5%A4%96%E9%80%81&kw=%E7%BE%8E%E9%A3%9F%E5%A4%96%E9%80%81&campaign_id=71700000041525777&cid=71700000041525777&adgroup_id=58700004434865151&adg_id=58700004434865151&kw_id=p39796722699&kwid=p39796722699&ad_id=338712388037&ext_id=&ran=17859406132257543620&lint_id=&lphy_id=9040379&pos=1t1&dev=c&net=g&match=b&placement=&target=&ds_rl=1263979&ds_rl=1265363&ds_rl=1273461&ds_rl=1263979&ds_rl=1265363&gclid=EAIaIQobChMIy4rPjfGY5gIVSGoqCh3kdAQ9EAAYASAAEgInBvD_BwE&gclsrc=aw.ds')
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/div/div/div/a[2]').click()
    username = driver.find_element_by_xpath('//*[@id="useridInput"]')
    username.send_keys('ZZZ')
   
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app-body"]/div/div[1]/form/button/span').click()
    password = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]')))
    password.send_keys('zzz')
    
    driver.find_element_by_xpath('//*[@id="app-body"]/div/div/form/button/span').click() 
    

btn_login = tk.Button(window, text='Ready for food', command=login)
btn_login.place(x=120, y=240)


window.mainloop()


# In[ ]:


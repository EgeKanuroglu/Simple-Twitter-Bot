from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "enteryourusername"
password = "enteryourpassword"
url = "https://twitter.com/"

while True:
    deger = input("1- Normal Değer 1\n2- Ortalama Değer 1.3\n3- Yavaş Değer 1.6\nSayı Seçiniz : ")
    if deger == "1":
        katsayi = 1
        break
    elif deger == "2":
        katsayi = 1.3
        break
    elif deger == "3":
        katsayi = 1.6
        break
    else:
        print("1,2 ve 3 değerleri haricinde değer girmeyiniz.")

class Twitter:
    def __init__(self):
        # alttaki ifade ile chrome ayarlarına ulaşıp web sitesinde değişiklikler yapabiliriz.
        self.browserProfile = webdriver.ChromeOptions()
        # alttaki ifade ile chrome ayarlarına gidip tercihler kısmına girip dilleri ingilizce olarak ayarlıyoruz.
        self.browserProfile.add_experimental_option("prefs" , {"intl.accept_languages" : "en,en_US"})
        # yaptığımız ayar değişikiklerini web sitesinde kullanmak için de chrome ifadesi ile
        # driverı çalıştırırken parametre olarak çalıştırılacak exe dosyası ve ayarları yaptığımız değişkeni yolluyoruz.
        self.browser = webdriver.Chrome("chromedriver.exe" , chrome_options = self.browserProfile)
        self.username = username
        self.password = password
    
    def signIn(self):
        # login işlemleri
        self.browser.get(url)
        time.sleep(3)
        self.browser.maximize_window()
        time.sleep(1)

        signbut = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
        signbut2 = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span')
        signbut.click()
        time.sleep(0.5 * katsayi)
        signbut2.click()
        time.sleep(6 * katsayi) # şaka gibi en az 5 saniye istiyor diyalog kutusu

        userinp = self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        userinp.send_keys(username)
        userinp.send_keys(Keys.ENTER)
        time.sleep(1 * katsayi)
        
        passinp = self.browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input')
        passinp.send_keys(password)
        passinp.send_keys(Keys.ENTER)

    def searchHashtage(self , hashtage):
        searchbut = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
        searchbut.send_keys(hashtage)
        searchbut.send_keys(Keys.ENTER)
        time.sleep(3 * katsayi)
        clickit = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[3]/div/a')
        clickit.click()
        time.sleep(2 * katsayi)
        # data-testid si tweet isimli olan etiketin altındaki 2. div i ve 2. div in altındaki 2. div
        # etiketinin içindeki tüm etiketleri liste içerisine alıyoruz.
        liste = self.browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div')
        print("\n\n")
        print(liste)
        print("\n\n")
        for item in liste:
            # döngü ile gelen her etiketin text bilgisini ekrana yazdırarak atılan tweetin text
            # bilgilerine ulaşabiliriz.
        #    print("\n")
            print(item.text)
    
    def search(self , hashtage):
        searchbut = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
        searchbut.send_keys(hashtage)
        searchbut.send_keys(Keys.ENTER)
        time.sleep(3 * katsayi)
        clickit = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[3]/div/a')
        clickit.click()
        time.sleep(2 * katsayi)
        # selenium kütüphanesi ile web sitesinin console kısmına javascript kodu yollayıp çalıştırabiliriz.
        # execute_script ifadesi ve gönderdiğimiz javascript kodu ile scroll barının uzunluğunu alabiliriz.
        loopCounter = 0 # aşırı fazla tweet olduğundan sınırlandırmak için değişken.
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        liste = []
        while True:
            if loopCounter < 5:
                loopCounter += 1
            else:
                break
            action = webdriver.ActionChains(self.browser) 

            for q in range(3):
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform() 

            time.sleep(2 * katsayi)

            ticket = self.browser.find_elements_by_css_selector("div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-dnmrzs > div.css-901oao.r-1awozwy.r-18jsvk2.r-6koalj.r-37j5jr.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0 > span > span")
            for tic in ticket:
                liste.append(tic.text)

            print(f"ticket : {len(ticket)}")
            print(f"liste : {len(liste)}")
            print("\n")
            # scroll barının yüksekliğini return ile kaydedip scrollTo ifadesi ile scroll barı
            # uzunluğu kadar yani scroll barının sonuna kadar aşağıya iniyoruz.
            #    self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
            #   time.sleep(2 * katsayi)
            # yüklenen tweetlerin ardından uzayan scroll barının uzunluğunu tekrardan alıyoruz.
            #    new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            #if last_height == new_height: # eğer son uzunluk ile yeni uzunluk eşit ise tweetlerin
            #    break                     # sonuna geldiğimizden döngüden çıkıyoruz.
            #last_height = new_height
        
        liste.sort()
        filtered = []
        metin = ""
        indeks = 0
        for tweet in liste:
            if metin == tweet:
                pass
            else:
                metin = tweet
                indeks += 1
                filtered.append(tweet)
        print(liste)
        print("\n\n")
        print(filtered)
        print("\n\n")
        return filtered
        #ticket = self.browser.find_elements_by_css_selector("div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-dnmrzs > div.css-901oao.r-1awozwy.r-18jsvk2.r-6koalj.r-37j5jr.r-a023e6.r-b88u0q.r-rjixqe.r-bcqeeo.r-1udh08x.r-3s2u2q.r-qvutc0 > span > span")
        #ticket2 = ticket.find_elements_by_css_selector("div")
    
    def importNamesToFile(self , liste):
        with open("usernames.txt" , "w" , encoding = "utf-8") as file:
            for value in liste:
                file.write(value + "\n")

twitter = Twitter()

twitter.signIn()
time.sleep(5 * katsayi)
filtliste = twitter.search("python")
time.sleep(1 * katsayi)
twitter.importNamesToFile(filtliste)

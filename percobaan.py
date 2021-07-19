from appium import  webdriver

# desired capability
desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\ThinkPad\\Downloads\\tokko.apk",
    "appPackage": "tokko.onlineshop.jual.mitra.app",
    "appWaitActivity": "tokko.onlineshop.jual.mitra.app.MainActivity"
}

# remote appium server
drivur = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# tunggu 30 mlidetik agar element muncul
drivur.implicitly_wait(30)

# tekan button daftar
el = drivur.find_element_by_accessibility_id('uspSplashPage_getStartedButton')
el.click()

# masukan no hp
pi = drivur.find_element_by_accessibility_id('loginPage_phoneNumberInput')
pi.send_keys('081234213123')

# otp via whatsapp
ot = drivur.find_element_by_accessibility_id('loginPage_whatsappLoginButton')
ot.click()





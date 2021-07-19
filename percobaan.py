from appium import  webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:\\Users\\ThinkPad\\Downloads\\tokko.apk",
    "appPackage": "tokko.onlineshop.jual.mitra.app",
    "appWaitActivity": "tokko.onlineshop.jual.mitra.app.MainActivity"
}

drivur = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

drivur.implicitly_wait(30)
el = drivur.find_element_by_accessibility_id('uspSplashPage_getStartedButton')
el.click()


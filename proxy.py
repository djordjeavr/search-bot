from selenium import webdriver
from selenium.webdriver.chrome.options import Options
PROXY = "11.456.448.110:8080"
if __name__ == '__main__':
    chromedriver_path = 'C:\SeleniumDrivers\chromedriver'
    window_size = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)

    random_proxy = '124.240.187.80:82'
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": random_proxy,
        "ftpProxy": random_proxy,
        "sslProxy": random_proxy,
        "proxyType": "MANUAL"
    }

    webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

    chromedriver = webdriver.Chrome(
        executable_path=chromedriver_path,
        options=chrome_options
    )

    chromedriver.get('https://whatismyip.com')
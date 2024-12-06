
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.configBase import  Config
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 设置请求头
def set_custom_headers(driver, token, uid, domain):
    # 通过 DevTools Protocol 设置请求 headers
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
    })
    driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
        'headers': {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'referer': 'https://' + domain + '/app/submission/submit',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'signature': 'ba85bed3b90d13e6a1ebbc7542ab8b35',
            'timestamp': '1725966557096',
            'token': token,
            'uid': uid
        }
    })

# 初始化
def init():
    # 配置 ChromeOption
    chrome_options = Options()
    if Config.CHROME_OPTIONS_ADD_ARGUMENT:
        chrome_options.add_argument("--incognito")
    if Config.CHROME_OPTIONS_ADD_ARGUMENT_HEAD:
        chrome_options.add_argument("--headless")
    if Config.CHROME_OPTIONS_START_MAXIMIZED:
        chrome_options.add_argument("--start_maximized")
    if Config.CHROME_OPTIONS_AUTO_OPEN_DEVTOOLS:
        chrome_options.add_argument("--auto_open_devtools_for_tabs")
    if Config.CHROME_OPTIONS_DISABLE_EXTENSIONS:
        chrome_options.add_argument("--disable_extensions")
    if Config.CHROME_OPTIONS_DISABLE_GPU:
        chrome_options.add_argument("--disable_gpu")
    if Config.CHROME_OPTIONS_NO_SANDBOX:
        chrome_options.add_argument("--no_sandbox")
    # 初始化 ChromeDriver
    # 在mac本地使用
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # 访问网页
    driver.get( 'https://'+ Config.DOMAIN ) # type: ignore
    # 设置 Cookies
    for name, value in Config.COOKIES.items():
        driver.add_cookie({'name': name, 'value': value, 'domain': Config.DOMAIN})
    # 设置 Local Storage 数据
    local_storage_data = {
        "adbws_marker": "1726020453740",
        "binance-https://" + Config.DOMAIN + '"': "{}",
        "codatta-connect-last-used": "{\"connector\":\"codatta-connect\",\"method\":\"injected\",\"walletName\":\"OKX Wallet\"}",
        "dynamic_auth_mode": "\"connect-and-sign\"",
        "dynamic_captcha_token": "\"P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQUvYKGYUy1r4j4hQ6AmpQtfyYggD9FsAcvVPjzyE0JVr76ua10DXoLKsV_KPv-DA30_Ix2Q8EDvTPl-y2OP3eLZMwmljwYRGstsQs_m4S0Qo4L1R9zfYbP8dBNsWUMMZeqz5X6AxAeig3UWovrsoRnMIJRRkevIuCpQ2CrWLxXb5rADljxmgxk2YZ28ouNmPSmUox8AhUaGLSc0g8Bi1-tJhGLw5MJWtJD4g08Cmw6lk-fUV7hUWqscOqps9vy4DXmcc5yJ-4oFDjOpjMDAd7LG1IWeuFsJiVO-l8fTLjqoaixRYVg4XgH232l09cx1wCW3YaQuGlTTLwXLq3GWgiTne15MjuVzTYCaJQiYldQ1PmNPlXGszxFpKsT_NaiATkyEV_k5iYReYTYQLx02WUsNGBw2zahvjT03GcwTAHMQYwlf3lF40Qtlvt7QDQqMtuv32RjVeC88IBEdobOcqC50K6dsQm2rscoCMFh-sIa7SFOCLa8NZhzGtV_ShFXdfQNOJfi0yGNqS2MUArDGoTGv0XxZ10TUszITuTWZhkRbrcUG5WkFfz7FEKsaqU3MEEm5ODI8PODgysaamValb8JYna_4KRBSELmJ_Hn_YiuZd4_j4yzgm7C0Uw2jd9TbfKbYveMah82a6t3-eoxUDVhGylgGgRbOLnsyjXdqVfImYaQ5iShSvjV6mEOr2i1DfdbnnEqjcAEPE-Aal2qhK1OtHILRp3j0KkFOSKmHwDSnaqXJLDTbC5uoDOyb-DNaLoq6gK_8jyoKyM3lPSxVX1RMxM8q7eIIR51qX18ALPjUTRIeSPPS7zreiUfRZDU0fl2CJeyW4VX6nVMexYKArgeEVD1Jo-iVP1VxKp8J_e8rV287rrIr6KC5JNaXPumij2JS8a_9Y3Rx2kY63YBoj6sSaI5YdYv22YzWFYYD8klg1CJsHU…\"",
        "dynamic_context_session_settings": "\"1725958319698\"",
        "dynamic_cookie_enabled": "false",
        "dynamic_last_used_wallet": "\"metamask\"",
        "dynamic_nonce": "{\"environmentId\":\"a55eb2b4-84ca-41ff-a369-fc52646ed585\",\"expiry\":1726044719702,\"value\":\"bc73df670d3b439f94254a95457bbf57\"}",
        "dynamic_store": "{\"state\":{\"environmentId\":\"a55eb2b4-84ca-41ff-a369-fc52646ed585\",\"networkConfigurations\":{\"expiresAt\":1726020754470,\"networkConfigurations\":{\"evm\":[{\"blockExplorerUrls\":[\"https://etherscan.io/\"],\"chainId\":1,\"iconUrls\":[\"https://app.dynamic.xyz/assets/networks/eth.svg\"],\"name\":\"Ethereum Mainnet\",\"nativeCurrency\":{\"decimals\":18,\"name\":\"Ether\",\"symbol\":\"ETH\"},\"networkId\":1,\"rpcUrls\":[\"https://rpc.ankr.com/eth\"],\"vanityName\":\"Ethereum\"},{\"name\":\"Metis\",\"rpcUrls\":[\"https://andromeda.metis.io/?owner=1088\",\"https://lb.nodies.app/v1/f5c5ecde09414b3384842a8740a8c998\"],\"nativeCurrency\":{\"name\":\"Metis\",\"symbol\":\"METIS\",\"decimals\":18},\"iconUrls\":[\"https://bridge.metis.io/logo.svg\"],\"networkId\":1,\"chainId\":1088,\"blockExplorerUrls\":[\"https://andromeda-explorer.metis.io/\"]},{\"name\":\"Manta Pacific Mainnet\",\"rpcUrls\":[\"https://pacific-rpc.manta.network/http\",\"https://manta-pacific.drpc.org\",\"https://www.tencentcloud-rpc.com/v2/manta/manta-rpc\",\"https://r1.pacific.manta.systems/http\",\"https://manta.nir…\"",
        "dynamic_wallet_picker_search": "\"\"",
        "ethereum-https://" + Config.DOMAIN + '"': "{\"chainId\":\"0x1\"}",
        "feh--1789f": "0001726020456875899f2541b7254d00ca9875f47be0d87e",
        "feh--19c44": "0001726020453755ce0059dd0654694ec28224b0ee2dcb4c",
        "feh--1b2b8": "0001726020390410ff5b2f733bff45cb5b2108e534bd508d",
        "feh--1bc22": "0001726020453751f081ba5184bff885a3e0556a2f02b0f4",
        "feh--1bda6": "0001725878250387f69144d6250158eadd2cc521a65745fe",
        "feh--30cb83": "0001726020453773ab80940dfc826f1c2535f951cf600c6d",
        "feh--330df5": "00017260204537454230f8e72a15f6d837a072f5174c55c9",
        "feh--37d28a": "0001726020384590b8b535e274db41b117c59c2a35d9df39",
        "feh--6bc5339": "0001726020384773b85650705407cf2837561e7144b50fa9",
        "feh--8ff2b28": "0001726020384141a553978655d7f862ec61b7185e20d934",
        "feh--9fd29358": "0001726020384136dfa004ad8ed49872c74f1c78cd7d4a85",
        "feh--c52": "0001726020384764cba6ba0ec5bc4f0312dbebed0c7556bf",
        "feh--da4": "00017260204542478b4adcc9d20e15998e19c7beafbe10e9",
        "feh--e3a677a0": "0001726020384142a1b87221a13b15123b1c8b79a866f388",
        "forterToken": "d5297dd8fe5547538571215e2d31706c,1726020456556",
        "isWhitelist": "false",
        "loglevel": "SILENT",
        "session": "42c74f48-1931-4786-aae2-d01b944",
        "token": Config.TOKEN,
        "tour_status": "{\"submission_home\":\"finish\",\"submission_form\":\"finish\",\"submission_list\":\"finish\",\"validation_filter\":\"finish\",\"validation_list\":\"finish\",\"validation_detail\":\"finish\"}",
        "trust:cache:timestamp": "{\"timestamp\":1725958315257}",
        "uid": Config.UID
    }

    # 设置 Local Storage 数据
    for key, value in local_storage_data.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")
    # 设置请求头
    set_custom_headers(driver, Config.TOKEN, Config.UID, Config.DOMAIN)
    # 刷新页面以应用 Cookies 和 Local Storage 数据
    time.sleep(2)
    driver.refresh()
    time.sleep(7)
    return driver

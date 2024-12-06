import os

class Config:
    IMPLICIT_WAIT_TIME = 20
    PAGE_LOAD_TIMEOUT = 30
    SCREENPATH = os.path.expanduser("resource/screenshot")
    LOGS=os.path.expanduser("resource/logs")
    # 测试token
    TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzkwNjI2NTM0MTA5MTg0IiwiY29ubmVjdG9yIjoid2FsbGV0IiwiYWNjb3VudF90eXBlIjoid2FsbGV0IiwiYWNjb3VudCI6IjB4YjQ3Zjc1YjFlYWFiOWE3MzJiNWZjNmQ5NjQ5ZGJkZjM2ZWY0ZDZjOCIsImxvZ2luX3NvdXJjZSI6ImNvZGF0dGEiLCJsb2dpbl93YWxsZXRfc291cmNlIjoiT0tYIFdhbGxldCJ9.ebqc0FlL8uROrCba6id3lENdR2JnWUUFVeecKfFdmKk'
    COOKIE_STRING = '_ga=GA1.1.1344376451.1732246450; forterToken=32d5f233d1c648c98652263294a1bcd8_1733453382847_2958_UDF43-m4_21ck_; _ga_K8V0FL9E1N=GS1.1.1733453380.31.1.1733453475.0.0.0'
    COOKIES = dict(item.split('=', 1) for item in COOKIE_STRING.split('; '))
    UID = '390626534109184'
    DOMAIN = 'app.codatta.io'
    REPORT_PATH = os.path.join(os.getcwd(), 'reports', 'test_report.html')  # 测试报告路径
    CHROME_OPTIONS_ADD_ARGUMENT = True  # 启用无痕模式
    CHROME_OPTIONS_ADD_ARGUMENT_HEAD = False  # 设置为 False 以启用可视化模式
    CHROME_OPTIONS_START_MAXIMIZED = False  # 启动时最大化窗口
    CHROME_OPTIONS_AUTO_OPEN_DEVTOOLS = False  # 启动时自动打开开发者工具
    CHROME_OPTIONS_DISABLE_EXTENSIONS = False  # 禁用扩展
    CHROME_OPTIONS_DISABLE_GPU = True  # 禁用 GPU 硬件加速
    CHROME_OPTIONS_NO_SANDBOX = True  # 解决无沙盒环境问题

    COUNT = 0
    MISTAKECOUNT = 0
    DICT = {
        "Worldcoin",
        "0x",
        "0xGames",
        "0xMons",
        "1inch",
        "1xBet",
        "256ART",
        "60cek",
        "7Tron",
        "888Bet",
        "AAX",
        "ABCC",
        "ACE",
        "AEX",
        "ALIS Token",
        "AOFEX",
        "ATL Token",
        "Aave",
        "Abracadabra",
        "Across Protocol",
        "AirSwap",
        "Alchemist Coin",
        "AltCoinTrader",
        "Alterdice",
        "Amber",
        "Amber Group",
        "Anonymous Mixer",
        "Any.Cash",
        "ApeSwap",
        "Arcx",
        "Arina Land Tycoon",
        "Arken Finance",
        "Armor",
        "AscendEX",
        "Atom Solutions",
        "Augmented Finance",
        "Aura Finance",
        "Authereum",
        "Avalanche Bridge",
        "Axie Infinity",
        "BC.Game",
        "BKEX",
        "BTC Blender",
        "BTSE",
        "Baby Doge Swap",
        "Badbit Games",
        "Balancer",
        "Bancor",
        "Bancor Network",
        "Barbooth.Bet",
        "Base Protocol",
        "BeGlobal",
        "Bear Escape",
        "Belt Finance",
        "Bestmixer",
        "BetSwirl",
        "Bettown",
        "Bgogo",
        "BiKi",
        "Bibox",
        "BigONE",
        "Binance",
        "BingX",
        "Bingbon",
        "Bingo Cash Finance",
        "Bison",
        "Bison Bank",
        "BitBase",
        "BitDAO",
        "BitFlyer",
        "BitForex",
        "BitKan",
        "BitKeep",
        "BitMart",
        "BitMix",
        "BitPay",
        "BitZ",
        "Bitbns",
        "Bitcoin Blender",
        "Bitcoin Laundry",
        "Bitcoin Mixer",
        "BitcoinMix",
        "BitcoinWallet.com",
        "Bitexlive",
        "Bitfinex",
        "Bitget",
        "Bitkub",
        "BitoPro",
        "Bitpie",
        "Bitrue",
        "Bitso",
        "Bitstamp",
        "Bittrex",
        "Bitverk",
        "Bitzlato",
        "Bixin",
        "Bleutrade",
        "BlinkPay"
    }
    DICT_LIST = list(DICT)

import time

from playwright.sync_api import sync_playwright

# 设置 MetaMask 扩展路径和用户数据目录
extension_path = "/Users/haoli/PycharmProjects/autoTest/resource/metamask-chrome-12.9.3"  # MetaMask 扩展解压后的文件夹路径
user_data_dir = "./data"  # 持久化上下文目录


def run(playwright):
    # 启动浏览器并加载扩展
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
            f"--disable-extensions-except={extension_path}",
            f"--load-extension={extension_path}",
            "--start-maximized"
        ],
    )

    # 打开一个新页面
    page = context.new_page()# 设置视口大小（例如 1920x1080）
    page.set_viewport_size({"width": 1920, "height": 1080})
    # page.goto("chrome://extensions/")
    # page.click("button[aria-label='固定 MetaMask']")
    # 打开 MetaMask 的扩展页面（通常是插件的初始设置页面）
    page.goto("chrome-extension://ibgpmbnfphhegicmgfcceacokbjfmfmg/home.html")  # 替换 <extension-id> 为 MetaMask 的实际扩展 ID
    # 模拟用户登录（假设用户需要输入密码）
    page.fill("input[type='password']", "316105WWll@")  # 替换为实际的密码输入框选择器和密码

    page.click("button[data-testid='unlock-submit']")
    # 访问需要使用 MetaMask 的页面（如 dApp）t

    page.goto("https://www.bitrefill.com/us/zh-Hans/gift-cards/apple-usa/")  # 示例 DApp    # 清除页面的 cookies
    # 监听弹窗事件
    # page.on('dialog', lambda dialog: dialog.dismiss())  # 自动接受弹窗

    context.clear_cookies()
    # 清除 localStorage
    page.evaluate("localStorage.clear()")
    # 清除 sessionStorage
    page.evaluate("sessionStorage.clear()")
    # 重新加载页面以确保状态已清除
    page.reload()
    time.sleep(3)
    try:
        iframe_selector = 'iframe[id^="cf-chl-widget-"]'  # 匹配动态 ID 的 iframe
        page.wait_for_selector(iframe_selector, timeout=3000)  # 等待 iframe 元素加载
        iframe = page.locator('iframe[id^="cf-chl-widget-"]')
        print(iframe)
        frame = iframe.content_frame()
        print("---------------:",iframe)
        print("Iframe loaded successfully.")
        # iframe = page.frame(name="cf-chl-widget-x9cdi")
        # iframe.locator('span:has-text("确认您是真人")').click()

    except Exception as e:
        print("Iframe not found, but no error raised:", e)

    print(page.locator('button:has(svg.lucide-chevron-down)').click())
    # 通过 ID 定位并点击该项
    # page.locator('#downshift-91-item-0').click()
    # page.locator('#downshift-130-menu ._item_rpopo_55').first.click()
    # 使用定位器定位并点击该元素
    time.sleep(1)
    print(page.locator('li#downshift-0-item-0').click())
    # 通过文本 "添加到购物车" 定位并点击
    time.sleep(1)
    # print(page.locator('span:has-text("添加到购物车")').click())
    # 点击 "添加到购物车" 按钮
    page.locator('button[data-cy="checkout-button"]').click()
    time.sleep(1)
    # print(page.locator('span:has-text("付款")').click())
    # 定位并点击 '付款' 按钮
    page.locator('a[data-cy="cart-widget-checkout-button"]').click()
    time.sleep(1)
    # 登录
    # 使用 XPath 定位并点击按钮
    page.locator('xpath=/html/body/div[1]/div/div[2]/div/div/div/div[2]/p/button').click()
    # 连接钱包
    button = page.locator('xpath=/html/body/div[6]/div/div/form/div/button[1]')
    button.click()
    context.on("page", lambda page: handle_popup(page))
    button = page.locator('xpath=/html/body/div[9]/div/div/div/div/div/ul/li[1]/button')
    button.click()

    time.sleep(2)
    page.locator('xpath=/html/body/div[8]/div/div/div/div/div/div[1]/div[1]/div/input').fill("17628193294@163.com")
    page.locator('xpath=/html/body/div[9]/div/div/div/div/div/div[2]/button').click()

    # page.locator('span:has-text("继续付款")').click()
    time.sleep(1)
    page.locator('span:has-text("Ethereum")').first.click()
    time.sleep(1)
    page.locator('span:has-text("MetaMask")').first.click()

    # page.on('dialog', lambda dialog: dialog.accept())  # 自动接受弹窗
    # context.on("page", lambda page: handle_popup(page))
    page.pause()
    # 关闭浏览器上下文
    context.close()


def handle_popup(page):
    # 当新页面或弹窗打开时，这个方法会被调用
    print(f"New popup opened: {page.url}")

    # 在新弹窗页面上等待并点击按钮
    page.wait_for_selector('button[data-testid="confirm-footer-button"]')  # 等待确认按钮可用

    page.click('button[data-testid="confirm-footer-button"]')  # 点击确认按钮

def swipe_with_mouse(page):
    # 获取屏幕大小
    viewport_size = page.viewport_size

    # 滑动起点和终点坐标
    start_x = viewport_size['width'] // 2
    start_y = viewport_size['height'] // 2
    end_x = start_x
    end_y = start_y - 600

    # 模拟鼠标拖动
    page.mouse.move(start_x, start_y)
    page.mouse.down()  # 按下鼠标
    page.mouse.move(end_x, end_y, steps=10)  # 移动到目标点
    page.mouse.up()  # 松开鼠标


def check_and_click(page, button_selector):
    """
    检查控件是否存在并点击，等待控件出现。

    Args:
        page: Playwright 页面对象。
        button_selector: 控件的选择器（CSS 选择器或其他支持的格式）。
    """
    try:
        # 等待控件可见，最多等待 5 秒
        button = page.locator(button_selector).wait_for(state="visible", timeout=5000)
        print("控件已出现，点击它")
        button.click()
    except Exception as e:
        print(f"控件未出现或操作失败: {e}")
        raise e


# 启动 Playwright
with sync_playwright() as playwright:
    run(playwright)

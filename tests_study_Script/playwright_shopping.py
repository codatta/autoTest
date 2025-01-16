
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
            f"--load-extension={extension_path}"
        ],
    )

    def handle_metamask_popup(context):
        for _ in range(10):  # 轮询检查是否有新页面
            for page in context.pages:
                if "metamask" in page.title().lower():
                    print("找到 MetaMask 弹窗！")
                    page.wait_for_selector('button[data-testid="confirm-footer-button"]')  # 等待确认按钮可用

                    print(page.click('button[data-testid="confirm-footer-button"]'))
                    return
            time.sleep(1)  # 等待新窗口打开
            print("1s")
        # 在执行授权时调用


    # 打开一个新页面
    page = context.new_page()# 设置视口大小

    page.goto("chrome-extension://ibgpmbnfphhegicmgfcceacokbjfmfmg/home.html")  # 替换 <extension-id> 为 MetaMask 的实际扩展 ID

    # 模拟用户登录钱包（假设用户需要输入密码）
    page.fill("input[type='password']", "316105WWll@")  # 替换为实际的密码输入框选择器和密码
    page.click("button[data-testid='unlock-submit']")

    page.goto("https://www.bitrefill.com/us/zh-Hans/gift-cards/apple-usa/") #购物网站
    context.clear_cookies()
    # 清除 localStorage
    page.evaluate("localStorage.clear()")
    # 清除 sessionStorage
    page.evaluate("sessionStorage.clear()")
    # 重新加载页面以确保状态已清除
    page.reload()
    time.sleep(3)

    #可能有人机验证
    try:
        iframe_selector = 'iframe[id^="cf-chl-widget-"]'  # 匹配动态 ID 的 iframe
        page.wait_for_selector(iframe_selector, timeout=3000)  # 等待 iframe 元素加载
        iframe = page.locator('iframe[id^="cf-chl-widget-"]')
        frame = iframe.content_frame()
        print("Iframe loaded successfully.")
        # iframe = page.frame(name="cf-chl-widget-x9cdi")
        # iframe.locator('span:has-text("确认您是真人")').click()
    except Exception as e:
        print("Iframe not found, but no error raised:", e)
    #点击价格框
    print(page.locator('button:has(svg.lucide-chevron-down)').click())
    time.sleep(1)

    #点击2美元
    print(page.locator('li#downshift-0-item-0').click())
    time.sleep(1)

    # 点击 "添加到购物车" 按钮
    page.locator('button[data-cy="checkout-button"]').click()
    time.sleep(1)

    # 定位并点击 '付款' 按钮
    page.locator('a[data-cy="cart-widget-checkout-button"]').click()
    time.sleep(3)

    # 登录/html/body/div[1]/div/div[2]/div/div/div/div[2]/p/button
    page.locator('xpath=/html/body/div[6]/div/div/form/div/button[1]').click()
    # 使用 XPath 定位并点击按钮

    page.locator('xpath=/html/body/div[8]/div/div/div/div/div/ul/li[1]/button').click()
    page.locator('xpath=/html/body/div[6]/div/div/form/div/button[1]').click()
    # 连接钱包'
    page.pause()
    time.sleep(3)
    button = page.locator('xpath=/html/body/div[9]/div/div/div/div/div/ul/li[1]/button')
    button.click()
    handle_metamask_popup(context)

    print("已经到了邮箱这里")

    # 确保输入框可见
    try:
        page.locator('#email').wait_for(state="visible", timeout=5000)
    except Exception as e:
        print(e)
    # 输入邮箱地址
    page.fill('#email', '17628193294@163.com')

    # 使用 evaluate 执行 JavaScript 代码点击按钮
    page.evaluate("""
          const button = document.querySelector('button:has-text("创建帐号")');
          if (button) {
              button.click();
          }
      """)

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

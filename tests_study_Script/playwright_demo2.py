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
        ],
    )

    # 打开一个新页面
    page = context.new_page()
    # page.goto("chrome://extensions/")
    # page.click("button[aria-label='固定 MetaMask']")
    # 打开 MetaMask 的扩展页面（通常是插件的初始设置页面）
    page.goto("chrome-extension://ibgpmbnfphhegicmgfcceacokbjfmfmg/home.html")  # 替换 <extension-id> 为 MetaMask 的实际扩展 ID
    # 模拟用户登录（假设用户需要输入密码）
    page.fill("input[type='password']", "316105WWll@")  # 替换为实际的密码输入框选择器和密码

    page.click("button[data-testid='unlock-submit']")
    # 访问需要使用 MetaMask 的页面（如 dApp）t

    page.goto("https://app.codatta.io/app")  # 示例 DApp    # 清除页面的 cookies
    context.clear_cookies()
    # 清除 localStorage
    page.evaluate("localStorage.clear()")
    # 清除 sessionStorage
    page.evaluate("sessionStorage.clear()")
    # 重新加载页面以确保状态已清除
    page.reload()

    page.click("div.xc-rounded-lg.xc-group.xc-flex.xc-cursor-pointer.xc-items-center.xc-gap-2.xc-border.xc-border-white.xc-border-opacity-15.xc-px-4.xc-py-2.xc-transition-all.hover\\:xc-shadow-lg")
    # 监听新打开的窗口（例如 MetaMask 弹窗）

    context.on("page", lambda page: handle_popup(page))

    # context.wait_for_event('backgroundpage')
    # background_page = context.background_pages[0]  # 获取背景页面
    # 等待弹窗元素可见
    # page.wait_for_selector('button[data-testid="confirm-footer-button"]')
    #
    # # 点击弹窗中的确认按钮
    # page.click('button[data-testid="confirm-footer-button"]')

    # background_page = context.wait_for_event('backgroundpage')
    # # 点击 MetaMask 扩展中的确认按钮
    # print(background_page.click('button[data-testid="confirm-footer-button"]'))

    # # 切换到插件弹出窗口进行操作
    # popup = context.wait_for_event("page")
    # popup.click("text='Next'")  # 点击“下一步”
    # popup.click("text='Connect'")  # 点击“连接”

    # 暂停以手动完成 MetaMask 操作（如登录或授权）
    page.pause()

    # 关闭浏览器上下文
    context.close()


def handle_popup(page):
    # 当新页面或弹窗打开时，这个方法会被调用
    print(f"New popup opened: {page.url}")

    # 在新弹窗页面上等待并点击按钮
    page.wait_for_selector('button[data-testid="confirm-footer-button"]')  # 等待确认按钮可用

    page.click('button[data-testid="confirm-footer-button"]')  # 点击确认按钮

# 启动 Playwright
with sync_playwright() as playwright:
    run(playwright)

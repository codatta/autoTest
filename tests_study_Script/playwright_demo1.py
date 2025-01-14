from playwright.sync_api import sync_playwright

# 扩展的文件路径
extension_path = "/path/to/extension"

with sync_playwright() as p:
    # 启动浏览器，加载扩展
    browser = p.chromium.launch_persistent_context(
        user_data_dir="/tmp/playwright",  # 必须使用持久化上下文加载扩展
        headless=False,  # 扩展需要在有头模式下运行
        args=[f"--disable-extensions-except={extension_path}",
              f"--load-extension={extension_path}"]
    )

    # 打开新页面
    page = browser.new_page()

    # 访问一个页面以测试扩展
    page.goto("https://example.com")

    # 与页面交互（扩展可能对页面内容进行修改）
    print(page.title())

    # 关闭浏览器
    browser.close()

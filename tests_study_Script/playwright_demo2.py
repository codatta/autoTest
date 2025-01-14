from playwright.sync_api import sync_playwright, Playwright

path_to_extension = "./resource"
user_data_dir = "./data"


def run(playwright: Playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    if len(context.background_pages) == 0:
        background_page = context.wait_for_event('backgroundpage')
    else:
        background_page = context.background_pages[0]

    # Test the background page as you would any other page.
    context.close()


with sync_playwright() as playwright:
    run(playwright)
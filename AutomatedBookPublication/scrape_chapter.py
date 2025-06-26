from playwright.sync_api import sync_playwright

def scrape_and_screenshot():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Screenshot of the full page
        page.screenshot(path="chapter1.png", full_page=True)

        # Get the chapter content
        content = page.inner_text("div#mw-content-text")

        # Save the text into a file
        with open("chapter1.txt", "w", encoding="utf-8") as file:
            file.write(content)

        print("✅ Done: Screenshot + Chapter saved!")

        browser.close()

scrape_and_screenshot()

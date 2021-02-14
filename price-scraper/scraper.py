from pyppeteer import launch
from typing import Dict, List

async def fetchPrice(urls: List[str]) -> Dict[str, str]:
    browser = await launch(headless=True)
    page = await browser.newPage()

    urlToPrice = {}
    for url in urls:
        print(url)
        await page.goto(url)
        price = await page.evaluate('() => document.getElementById(\'priceblock_ourprice\').textContent') 
        print(price)
        urlToPrice[url] = price

    await browser.close()
    return urlToPrice
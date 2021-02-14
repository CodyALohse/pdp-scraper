import azure.functions as func
from .slack import sendWebHook, SlackData
from .googleSheets import GSheets
from .scraper import fetchPrice
from typing import List

async def main(mytimer: func.TimerRequest) -> None:
    gServ = GSheets()
    urls = gServ.getRange("Sheet1!A2:A", False)

    data: List[SlackData] = []
    priceData = await fetchPrice(urls)

    for key in priceData.keys():
        data.append(SlackData(key, priceData[key]))

    sendWebHook("Amazon Price Scraper", data)
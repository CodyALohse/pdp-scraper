# Price Scraper

Price Scraper is a project to scrape a price from a product page url defined in a Google Sheet, and then send the results to a Slack web hook url.

Implementation uses a Google Sheet with URLS defined in column A to scrape a price from each URL. The URL is loaded via Pyppeteer and the price is scraped. The results are assembled and sent to a Slack web hook. A Google Sheets service account is used to access the Google Sheet.

## Azure Functions

The project uses Azure Functions to trigger the event based on a cron schedule. The schedule is defined in the function.json file.

Useful Utility for cron job schedules

https://crontab.guru/

[Azure functions and Python][2]

[Azure functions in VS Code][1]

The following Environment Variables are expected in the Azure Function app settings or in the local.settings.json ([Azure functions in VS Code][1]):

```
"SLACK_WEB_HOOK_URL": "your_slack_web_hook_url",
"GOOGLE_SHEET_ID": "your_google_sheet_id",
"GOOGLE_SERVICE_ACCT_FILE": "your_google_sheet_service_acct_creds.json"
```

[1]: <https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=csharp> "Azure Functions VS Code"

[2]: <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python> "Azure Functions and Python"
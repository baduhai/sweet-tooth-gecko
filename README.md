## Sweet Tooth Gecko

Automatically collect CoinGecko candies.

### Requirements

- Firefox
- GeckoDriver
- Python requests
- Selenium

Use your package manager to install Firefox and GeckoDriver, if GeckoDriver isn't available in your repositories, you can also find it [here](https://github.com/mozilla/geckodriver/releases/latest). To install Selenium and Requests, simply run:

`pip install requests selenium`

### Usage

`TIMEOUT=10 USEREMAIL=<email> PASSWORD=<password> GOTIFY=true GOTIFY_ADDRESS=http://127.0.0.1:8080 GOTIFY_TOKEN=<token> python sweet-tooth.py`

Or write a shell script that exports the variables and put it in your crontab!
# Scrapy settings for douyin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douyin'

SPIDER_MODULES = ['douyin.spiders']
NEWSPIDER_MODULE = 'douyin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'douyin (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'douyin.middlewares.DouyinSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'douyin.middlewares.DouyinDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'douyin.pipelines.DouyinPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'

DOWNLOAD_DELAY = 5  # 下载延迟5秒
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HEADERS = {
  'authority': 'www.douyin.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'cookie': 'ttwid=1%7CW3T43Rf1pupf6aDA7X4PlCWr8agB5B7nRlWhZQcMLbI%7C1679034471%7C0e00540cde28638166d5ff105245ce7acd4c66a039f67b56c27c54ced923260c; SEARCH_RESULT_LIST_TYPE=%22single%22; passport_csrf_token=cc544186cdda93bd857ce6572739acf6; passport_csrf_token_default=cc544186cdda93bd857ce6572739acf6; strategyABtestKey=%221681869343.881%22; s_v_web_id=verify_lgn1l08x_rblJywVH_iDdt_46LI_BTCY_jO20I03g4cu0; download_guide=%223%2F20230419%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtY2xpZW50LWNzciI6Ii0tLS0tQkVHSU4gQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbk1JSUJEekNCdFFJQkFEQW5NUXN3Q1FZRFZRUUdFd0pEVGpFWU1CWUdBMVVFQXd3UFltUmZkR2xqYTJWMFgyZDFcclxuWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUWNEUWdBRTU3OU5EdTNvMnd4SXU3UzF6Z3JPUEFCK1xyXG5lNis2K1hublJON3pZODl2U2ZjbDVmZ05XNmo5T09oZlZUbnVBYlJaMjlzNVEvNEtpaHl5dVBCV0QxcUV5YUFzXHJcbk1Db0dDU3FHU0liM0RRRUpEakVkTUJzd0dRWURWUjBSQkJJd0VJSU9kM2QzTG1SdmRYbHBiaTVqYjIwd0NnWUlcclxuS29aSXpqMEVBd0lEU1FBd1JnSWhBSTVZdmdSR1lWTnRiN3U0NldFN3ZCaUlCL2VMTjU3WVVocHRDT3MxU2VkeVxyXG5BaUVBbk4rL0EyN0wrL095M3E5VU11ZXdtZ241a3lxd2F3a2tZdE94aWI3Q0QvND1cclxuLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tXHJcbiJ9; __ac_signature=_02B4Z6wo00f01AFpGBQAAIDDlb9DGv7gFWQBSRyAAGRrFmz18OfIDEQoEdUBojR.qMdbFGLjFG-HrKoP3-rSJcIesdg3kkgTRUcfFn.3ThMldFTMHLCg5xOB5gghpuP3m-ZakltxgWnKwSFQ0a; home_can_add_dy_2_desktop=%221%22; tt_scid=G3eZzX-ISo4IzeP8WwGAJ8uwzldW9QpQcaYvhLCvsiIzxeRrsfZ81LORk8k04rBo8fdc; pwa2=%222%7C1%22; msToken=c6ZNc031bKJ7UBj37-vtvaZvdHNY-5dn5BpUURmS4p9hnq2GbiCkwYrvPUfdz5z04VdyppHrmZYNQGXoFnCAaqf3n7nu2BgVauLnuY8YlAa_m3ejpSB1zBcb3y4p4l0=; msToken=PCPuoJBsvg4nM7ZihHlROTesus7rjEMaMr3qU5be76fY2H7T2uNktX_bEX06ummMd8Fl-gE9S46D4bU99bRNAATS3kWKHZH99SmknHaGET9kKzJufOANaQNoEScRqPQ=',
  'referer': 'https://www.douyin.com/search/%E8%90%8C%E5%AE%A0%E7%8C%AB%E5%92%AA?aid=6ca52fe9-2d7b-44d4-936d-5e610ab2f680&publish_time=0&sort_type=0&source=normal_search&type=video',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

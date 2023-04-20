import scrapy
from scrapy.loader import ItemLoader

from douyin.items import DouyinItem


class Douyin1Spider(scrapy.Spider):
    name = "douyin"
    allowed_domains = ["www.douyin.com"]
    start_urls = [
        "https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=0&keyword=%E8%90%8C%E5%AE%A0%E7%8C%AB%E5%92%AA&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=&offset=10&count=10&search_id=202304191734387CE978593B699210CC8C&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=900&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=112.0.0.0&browser_online=true&engine_name=Blink&engine_version=112.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=4&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7211398056938522127&msToken=PCPuoJBsvg4nM7ZihHlROTesus7rjEMaMr3qU5be76fY2H7T2uNktX_bEX06ummMd8Fl-gE9S46D4bU99bRNAATS3kWKHZH99SmknHaGET9kKzJufOANaQNoEScRqPQ=&X-Bogus=DFSzswVLN/2ANCNQtVzJjp7TlqSI"
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'douyin.pipelines.MyVideoPipeline': 10,
            'douyin.pipelines.JsonPipeline': 100,
        },
        'FILES_STORE': 'videos'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.crawler.settings.get("HEADERS"),
                callback=self.parse
            )

    def parse(self, response, **kwargs):
        resp_json = response.json()
        results = resp_json['data']
        for result in results:

            item = DouyinItem()
            item.setdefault('desc', result['aweme_info']['desc'])
            item.setdefault('author', result['aweme_info']['author']['nickname'])
            item.setdefault('signature', result['aweme_info']['author']['signature'])
            item.setdefault('video_urls', [result['aweme_info']['video']['play_addr']['url_list'][0]])
            item.setdefault('video_hash', result['aweme_info']['video']['play_addr']['file_hash'])

            yield item
        # if resp_json.get('has_more'):
        #     yield scrapy.Request(
        #         url=response.url,
        #         headers=self.crawler.settings.get("HEADERS"),
        #         callback=self.parse
        #     )


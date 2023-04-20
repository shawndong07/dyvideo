# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import os

import requests
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline
from scrapy.utils.misc import arg_to_iter


class JsonPipeline:
    def __init__(self):
        self.file = open('items.json', 'wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False, indent=4)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        print(f'process_item: {item}')
        self.exporter.export_item(item)
        return item


class MyVideoPipeline(FilesPipeline):
    FILES_URLS_FIELD = 'video_urls'

    def file_path(self, request, response=None, info=None, *, item=None):
        flist = request.url.split('?')[0].split('/')
        filename = flist[-1] if flist[-1] else flist[-2]
        return filename + '.mp4'

    def item_completed(self, results, item, info):
        print(f'item: {item} result: {results}')
        video_paths = [os.path.join(self.store.basedir, x['path']) for ok, x in results if ok]
        if video_paths:
            item['video_paths'] = video_paths
        return item

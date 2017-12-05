from lxml import etree

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

class WixFilePipeline(object):
    """
    WIXファイルを作成するPipeline
    """

    #############
    # CONSTANTS #
    #############

    COMMENT = 'tabelog.com'
    DESCRIPTION = ''
    LANGUAGE = 'ja'
    DOCTYPE = '<!DOCTYPE WIX SYSTEM "http://wixdemo.db.ics.keio.ac.jp/wixfile.dtd">'
    FILE = 'tabelog_all.wix'


    def open_spider(self, spider):
        self.wix = etree.Element('WIX')

        self.header = etree.SubElement(self.wix, 'header')
        self.body = etree.SubElement(self.wix, 'body')

        self.comment = etree.SubElement(self.header, 'comment')
        self.description = etree.SubElement(self.header, 'description')
        self.language = etree.SubElement(self.header, 'language')

        self.comment.text = self.COMMENT
        self.description.text = self.DESCRIPTION
        self.language.text = self.LANGUAGE

        self.wixtree = etree.ElementTree(element=self.wix)

    def close_spider(self, spider):
        f = open(self.FILE, 'w')
        f.write(etree.tostring(self.wixtree, encoding='utf-8', xml_declaration=True, pretty_print=True, doctype=self.DOCTYPE).decode('utf-8'))
        f.close()

    def process_item(self, item, spider):
        self.entry = etree.SubElement(self.body, 'entry')

        self.keyword = etree.SubElement(self.entry, 'keyword')
        self.keyword.text = item['keyword']

        self.target = etree.SubElement(self.entry, 'target')
        self.target.text = item['target']

        return item


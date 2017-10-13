from lxml import etree

#############
# CONSTANTS #
#############

COMMENT = 'コメント'
DESCRIPTION = '説明'
LANGUAGE = 'ja'

DOCTYPE = '<!DOCTYPE WIX SYSTEM "http://wixdemo.db.ics.keio.ac.jp/wixfile.dtd">'

FILE = 'wixtest.wix'

class WixFileCreator():


    def generate(self, entries, file=FILE):

        wix = etree.Element('WIX')

        header = etree.SubElement(wix, 'header')
        body = etree.SubElement(wix, 'body')

        comment = etree.SubElement(header, 'comment')
        description = etree.SubElement(header, 'description')
        language = etree.SubElement(header, 'language')

        comment.text = COMMENT
        description.text = DESCRIPTION
        language.text = LANGUAGE

        for input_entry in entries:
            entry = etree.SubElement(body, 'entry')

            keyword = etree.SubElement(entry, 'keyword')
            keyword.text = input_entry['keyword']

            target = etree.SubElement(entry, 'target')
            target.text = input_entry['target']

        wixtree = etree.ElementTree(element=wix)

        f = open(file, 'w')
        f.write(etree.tostring(wixtree, encoding='utf-8', xml_declaration=True, pretty_print=True, doctype=DOCTYPE).decode('utf-8'))
        f.close()


def main():
    entries = [
        {'keyword': '日本', 'target': 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'},
        {'keyword': 'アメリカ', 'target': 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%A1%E3%83%AA%E3%82%AB%E5%90%88%E8%A1%86%E5%9B%BD'},
    ]

    wi = WixFileCreator()
    wi.generate(entries)

if __name__ == '__main__':
    main()

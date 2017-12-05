from lxml import etree
import sys

def main():
    args = sys.argv
    gen = WixFileGenerator()
    gen.writer(gen.enwiki_to_entries(args[1]))

class WixFileGenerator(object):
    #############
    # CONSTANTS #
    #############

    COMMENT = 'Wikipedia-en'
    DESCRIPTION = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz \n05-Nov-2017 05:41'
    LANGUAGE = 'en'
    DOCTYPE = '<!DOCTYPE WIX SYSTEM "http://wixdemo.db.ics.keio.ac.jp/wixfile.dtd">'
    FILE = 'wikipedia_en.wix'

    def enwiki_to_entries(self, file):

        f = open(file, 'r')
        entry_list = []

        for line in f:
            keyword = line.rstrip()
            target = "https://en.wikipedia.org/wiki/" + keyword
            entry = {"keyword": keyword, "target": target}
            if keyword != "":
                entry_list.append(entry)
                
        f.close()

        return entry_list


    def writer(self, itemlist):
        wix = etree.Element('WIX')

        header = etree.SubElement(wix, 'header')
        body = etree.SubElement(wix, 'body')

        comment = etree.SubElement(header, 'comment')
        description = etree.SubElement(header, 'description')
        language = etree.SubElement(header, 'language')

        comment.text = self.COMMENT
        description.text = self.DESCRIPTION
        language.text = self.LANGUAGE

        wixtree = etree.ElementTree(element=wix)

        for item in itemlist:
            entry = etree.SubElement(body, 'entry')

            keyword = etree.SubElement(entry, 'keyword')
            keyword.text = item['keyword']

            target = etree.SubElement(entry, 'target')
            target.text = item['target']

        f = open(self.FILE, 'w')
        f.write(etree.tostring(wixtree, encoding='utf-8', xml_declaration=True, pretty_print=True, doctype=self.DOCTYPE).decode('utf-8'))
        f.close()

if __name__ == '__main__':
    main()
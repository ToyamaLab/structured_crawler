from lxml import etree
import sys

def main():
    args = sys.argv
    gen = WixFileGenerator()
    gen.writer(args[1], args[2])

class WixFileGenerator(object):
    #############
    # CONSTANTS #
    #############

    COMMENT = 'dblp'
    DESCRIPTION = ''
    LANGUAGE = 'en'
    DOCTYPE = '<!DOCTYPE WIX SYSTEM "http://wixdemo.db.ics.keio.ac.jp/wixfile.dtd">'
    # FILE = 'dblp.wix'

    PLEFIX = 'http://dblp.uni-trier.de/'

    def dblp_wix_entry_generator(self, etree_root):

        articles = etree_root.xpath('//article')
        inproceedings_es = etree_root.xpath('//inproceedings')
        proceedings_es = etree_root.xpath('//proceedings')
        books = etree_root.xpath('//books')

        contents_list = [articles, inproceedings_es, proceedings_es, books]

        for contents in contents_list:
            for instance in contents:

                try:
                    entry = {}
                    entry['keyword'] = instance.xpath('title')[0].text
                    entry['target'] = self.PLEFIX + instance.xpath('url')[0].text
                    yield entry
                except TypeError:
                    print("TypeError: pass")
                except IndexError:
                    print("IndexError: pass")


    def test(self):
        pass

    def writer(self, input_file, output_file):

        counter = 0

        print("start parse")

        tree = etree.parse(input_file, parser=etree.XMLParser(recover=True))
        root = tree.getroot()

        print("finite parse")

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

        for item in self.dblp_wix_entry_generator(root):

            entry = etree.SubElement(body, 'entry')

            keyword = etree.SubElement(entry, 'keyword')
            keyword.text = item['keyword']

            target = etree.SubElement(entry, 'target')
            target.text = item['target']

            counter += 1
            if (counter % 10000) == 0:
                print(str(counter) + "entries processed.")

        f = open(output_file, 'w')
        f.write(etree.tostring(wixtree, encoding='utf-8', xml_declaration=True, pretty_print=True, doctype=self.DOCTYPE).decode('utf-8'))
        f.close()

if __name__ == '__main__':
    main()
'''
@author: Yiz56865
'''

from lxml import etree
from xml.dom import minidom

class XMLFileParser:
    def __init__(self, XMLContent, XMLFileName):
        self._fileName = XMLFileName
        #f = open(self._fileName, "wt")
        self._node = etree.fromstring(XMLContent)
        
        self._node_store = etree.fromstring(XMLContent)
        self.removeElements()
        
        self._cont = etree.tostring(self._node_store, pretty_print=True)        
        self._fmtc = minidom.parseString(self._cont).toprettyxml()
        with open(self._fileName, 'w') as doc:
            doc.write(self._fmtc)
            
    def getText(self, xpath):
        for quote in self._node.xpath(xpath+"/text()"):
            return quote;
    
    def getAttr(self, xpath):
        for quote in self._node.xpath(xpath):
            return quote;
                
    def removeElements(self):
        pass;


class XMLFileParserWithFilter(XMLFileParser):
    
    Filters = ['']
    
    def removeElements(self):
        for flt in self.Filters:
            bads = self._node_store.xpath(flt)
            for bad in bads:
                bad.getparent().remove(bad)
        
    
if __name__ == "__main__":

    from lxml import etree
    import chardet
    
    html = '''
        <html>
            <body>
                <div class='d1'>
                    <ul>
                        <li class='a1' style='s1'> 1 </li>
                        <li class='a2' style='s2'> 2 </li>
                    </ul>
                    <ul>
                        <li class='a3' style='s3'> 3 </li>
                        <li class='a4' style='s4'> 4 </li>
                    </ul>
                </div>
                <div id='spec' class='d2'>
                    <ul>
                        <li class='a5' style='s5'> 5 </li>
                        <li class='a6' style='s6'> 6 </li>
                    </ul>
                    <ul>
                        <li class='a7' style='s7'> 7 </li>
                        <li class='a8' style='s8'> 8 </li>
                    </ul>
                </div>                
            </body>            
        </html>
    '''
    
    sel = etree.HTML(html)
    
    print("\n")
    print("* Example 1: select node")
        
    for quote in sel.xpath('//div[@id="spec"]/ul/li'):
        #print(quote)
        print(quote.attrib)
        print(quote.text)
    
    print("\n")
    print("* Example 2: select node\'s attributes")
    for quote in sel.xpath('//div/ul/li/@style'):
        print(quote)
    
    print("\n")
    print("* Example 3: select node by position")
    for quote in sel.xpath('//div/ul/li[1]'):
        print(quote.attrib)
        print(quote.text)
    
    print("\n")  
    print("* Example 4: select node by relative path")
    for quote in sel.xpath('//li[@class="a5"]'):
        f_quote = quote.xpath('../../@id')
        print(f_quote)
        for f_quote in quote.xpath('../../../div'):
            print(f_quote.attrib)
            print(f_quote.text)
    
    print("\n")     
    print("* Example 5: select node's text")
    for quote in sel.xpath('//div[@id="spec"]/ul/li/text()'):
        print(quote.strip())
    
    html = '''
        <li>  
               盲赂鈧ぢ嘎� <a href="/w/index.php?title=%E5%BF%AB%E4%B9%90&amp;action=edit&amp;redlink=1" class="new" title="氓驴芦盲鹿锟矫妓喢┞÷得╋拷垄盲赂锟矫ヂ溍ヅ撀尖��">氓驴芦盲鹿锟�</a>  
            莽拧鈥灻ぢ郝好︹偓禄忙藴炉忙禄隆猫露鲁盲赂沤忙麓禄盲潞沤氓陆鈥溍ぢ糕�姑寂捗ㄢ偓艗茅锟脚久β德绰姑︹�斅睹┾�斅疵︼拷拢忙茠鲁<a href="/wiki/%E6%9C%AA%E6%9D%A5" title="忙艙陋忙锟铰�">忙艙陋忙锟铰�</a>  
            茫鈧��  
    </li>
    '''
    html_b = bytes(html, 'gbk')
    print("yiz, detect: " + chardet.detect(html_b)['encoding']) 
        
    sel = etree.HTML(html)
    
    print("\n")
    print("* Example 6: using string()")
    for quote in sel.xpath("//li"):
        s_quote = quote.xpath('string(.)')
        print(s_quote.encode("utf-8"))
    
                
    html = '''<li class="spec">
                    This is a useful sentence.            
                <ul style="ul-s">
                    <li style="li-s">
                            orignal text:
                        <i style="i-s">
                                this is useless sentence.              
                        </i>
                    </li>
                </ul>
            </li>'''
    
    print("\n")
    print("* Example 7: converting to string and print element")    
    node = etree.fromstring(html)
    print(type(node))
    print(etree.tounicode(node, pretty_print=True))
    
    sel = etree.HTML(html)
    print(type(sel))
    print(etree.tounicode(sel, pretty_print=True))
    
    print("\n")
    print("* Example 8: using _Element and _ElementTree")
    node = etree.fromstring(html)
    print(type(node))
        
    rootTree = node.getroottree()
    print(type(rootTree))
     
    rootElem = rootTree.getroot()
    print(type(rootElem))
    print(etree.tounicode(rootElem, pretty_print=True))
    
    print(rootElem.items())
    print(rootElem.keys())
    print(rootElem.get('class', ''))
    
    print("\n")
    print("* Example 9: using remove()")
    node = etree.fromstring(html)
    for quote in node.xpath("/li"):
        print(quote.xpath("string(.)"))
    
    for quote in node.xpath("/li"):
        origin = quote.xpath("./ul")
        bads = quote.xpath("./ul")
        for bad in bads:
            bad.getparent().remove(bad)
        
        disp = quote.xpath("string(.)")
        print(disp.strip())
        
        if len(origin) > 0:
            print(origin[0].xpath("string(.)").strip())
        
        f = open("c:\\test.xml", "w")
        print(etree.tounicode(quote, pretty_print=True), file=f)
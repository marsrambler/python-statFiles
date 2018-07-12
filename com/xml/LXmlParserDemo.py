'''
@author: Yiz56865
'''


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
               一个 <a href="/w/index.php?title=%E5%BF%AB%E4%B9%90&amp;action=edit&amp;redlink=1" class="new" title="快乐（页面不存在）">快乐</a>  
            的人总是满足与活于当下，而非浪费时间揣想<a href="/wiki/%E6%9C%AA%E6%9D%A5" title="未来">未来</a>  
            。  
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
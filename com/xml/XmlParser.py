'''
@author: Yiz56865
'''

import xml.parsers.expat

class AbstractXmlParser:
    Parser = ""
    
    def __init__(self, xml_fileName):
        assert xml_fileName != ""
        if not isinstance(xml_fileName, str):
            raise TypeError('bad file name')
        
        self._xml_fileName = xml_fileName
        self.Parser = xml.parsers.expat.ParserCreate()
        self.Parser.CharacterDataHandler = self.handleCharData
        self.Parser.StartElementHandler  = self.handleStartElement
        self.Parser.EndElementHandler    = self.handleEndElement
        
    def parse(self):
        try:
            _xml_file = open(self._xml_fileName, "rb")
        except:
            print("Error, Can not open %s"%self._xml_fileName)
        else:
            try:
                self.Parser.ParseFile(_xml_file)
            finally:
                _xml_file.close()
        
    def handleCharData(self, data):
        pass;
    
    def handleStartElement(self, name, attrs):
        pass;
    
    def handleEndElement(self, name):
        pass
    

class SingleValueXmlParser(AbstractXmlParser):
    
    def __init__(self, xml_fileName):
        AbstractXmlParser.__init__(self, xml_fileName)
    
    def setTags(self, *args):
        self.tags  = list(args)
        self.flags = [False]*len(args)
        self.values = [""]*len(args)
    
    def handleCharData(self, data):
        idx = 0
        for flag in self.flags:
            if flag:
                if self.values[idx] == "":
                    self.values[idx] = data
                else:
                    if isinstance(self.values[idx], str):
                        self.values[idx] = [self.values[idx],]                    
                    self.values[idx].append(data)
            idx += 1
    
    def handleStartElement(self, name, attrs):
        idx = 0
        for tag in self.tags:
            if name == tag:
                self.flags[idx] = True
            idx += 1
    
    def handleEndElement(self, name):
        idx = 0
        for tag in self.tags:
            if name == tag:
                if not self.flags[idx]:
                    raise RuntimeError('bad xml file format %s'%name)
                else:
                    self.flags[idx] = False
            idx += 1
            
    def parse(self):
        AbstractXmlParser.parse(self)
        result = dict(zip(self.tags, self.values))
        return result
    
if __name__ == "__main__":
    
    parser = SingleValueXmlParser("Z:\\D\\200-1464-001-2018-06-27-11-19-41.xml") 
    parser.setTags("dasff", "fda", "daf")
    values = parser.parse()
    print(values) 
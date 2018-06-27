'''
@author: Yiz56865
'''

import os
from com.xml import XmlParser 

if __name__ == "__main__":
    parser = XmlParser.SingleValueXmlParser("Z:\\D\\200-1464-001-2018-06-27-11-19-41.xml") 
    parser.setTags("dsaf", "afds", "adf")
    values = parser.parse()
    print(values)     

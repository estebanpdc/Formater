
class TLV:
    tag =""
    len = ""
    value = ""

    def toString(self, formated):
        if(formated):
            return self.tag + "\n   " + self.len + "\n      " + self.value + "\n"
        else:
            return self.tag + " " + self.len + " " + self.value
        
    def parseTLV(self,data):
        #remove whitespaces
        data = data.replace(" ","").replace("\n","")
        if(len(data) < 4):
            return
        self.tag = data[0:2]
        self.len = data[2:4]
        #check if there is enough value
        if(len(self.tag) + len(self.len) + int( int(self.len) * 2) > len(data)):
            self.tag = ""
            return
        self.value = data[len(self.tag) + len(self.len) : len(self.tag) + len(self.len) + int( int(self.len) * 2)]
        return len(self.tag) + len(self.len) + int( int(self.len) * 2);

        
    def isWellFormated(self):
        return self.tag is not "" and int(self.len) == len(self.value)/2
     
class TLVDecoder:
    TLVList = []
    
    def parse(self, data):
        #remove whitespaces
        data = data.replace(" ","").replace("\n","")
        offset = 0
        while(offset < len(data)):
            tlv = TLV()
            offset += tlv.parseTLV(data[offset:])
            self.TLVList.append(tlv)
            
    def toString(self):
        ret = ""
        for tlv in self.TLVList:
            ret += tlv.toString(True)
        return ret
            
            
tlv = TLVDecoder()
tlv.parse("A0 02 01 01 A1 01 01")
print(tlv.toString())

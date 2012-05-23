class SofeaEmployerMock(ServiceMock):
 def __init__(self):
  super(SofeaEmployerMock, self,).__init__('serviceHost')
 def fetch_request(self, req, callback = None):
   if '/vacancy/short?lang=RU&id=1' == req.url:
     return 200, 
       '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <vacancies>
             <vacancy>
               <vacancyId>1</vacancyId>
               <name>Merchandizer</name>
               <company>
                 <id>63357</id>
                 <name>PROFPARK, ZAO</name>
             </vacancy>
           </vacancies>'''

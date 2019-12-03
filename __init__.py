from adapt.intent import IntentBuilder

from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.skills.context import adds_context, removes_context
from mycroft.util.log import getLogger

import requests
import json
import re


prdLocation = 'storage'


def getPrdInfo(prdName):

    if prdName == 'visa101':
        prdLocation = 'On Way' 
    else:
        prdLocation = 'Lost'

    return prdLocation

class Productinfotest(MycroftSkill):
    def __init__(self):
       
        super().__init__()
        


    @intent_handler(IntentBuilder("ProdMyIntent")
                    .require("productinfotest").require("productserkw").build()) 
    @adds_context('MoreInfoContext')                
    def handle_prod_my_intent(self, message):

        # semainder = str(message.utterance_remainder())
        preNumber = message.data.get("productserkw")
        prdLocation = getPrdInfo(preNumber)
        # prdLocation = "Storage"
        self.log.info(preNumber)
        self.speak_dialog("productinfotest", data={"prdloc": prdLocation})
        self.speak('would you like get more information?', expect_response=True)
    
        
     
    @intent_handler(IntentBuilder('NoInfoInetnt').require("NoKword").require('MoreInfoContext').build())
    @removes_context('MoreInfoContext')
    def handle_no_info_intnet(self, message):
        self.speak('Sure')

def create_skill():
    return Productinfotest()
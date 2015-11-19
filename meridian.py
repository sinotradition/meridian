# -*-coding: utf8 -*-
'''This the base definition of meridian

@version: 0.0.1
@author: sheng
@contact: sinotradition@gmail.com
@copyright: License according to the project lincese.
'''


'''acupoint: 腧穴，extraordinary:奇穴，ashi:阿是穴'''
point_type = ('acupoint', 'extraordinary', 'ashi')
'''JING_WELL 井, XING_SPRING 荥, SHU_STREAM 俞, JING_RIVER 经, HE_SEA 合, YUAN_PRIME 原'''
acupointtype = ('well','spring','stream','river','sea','prime')

'''五脏:心、肝、脾、肺、肾'''
zang = ('heart','liver','spleen','lung','kidney')
'''六腑:胆、小肠、胃、大肠、膀胱、三焦'''
fu = ('gallbladder','smallintestine','stomach','largeintestine','bladder','sanjiao')
'''六阴经:肺经,脾经,心经,肾经,心包经,肝经'''
yangchannels=('lung','spleen','heart','kidney','pericardium','liver')
'''六阳经:大肠经,胃经,小肠经,膀胱经,三焦经,胆经'''
yinchannels=('largeintestine','stomach','smallintestine','bladder','sanjiao','gallbladder')
'''奇经八脉:任脉,督脉,冲脉,带脉,阴维(腧)脉,阳维(腧)脉,阴跷脉,阳跷脉'''
extraordinarychannels=('ren', 'du', 'chong', 'dai', 'yinwei', 'yangwei', 'yinqiao', 'yangqiao')

class acupoint(object):
    def __init__(self,pointname,pointtype,pointchannel):
        self.name=pointname
        self.type=pointtype
        self.channel=pointchannel if pointchannel else None
    
class acuchannel(object):
    def __init__(self,channelname,acupoints=()):
        self.name=channelname
        self.member=acupoints

acuchannels=("a")

if __name__ == "__main__":
    pass


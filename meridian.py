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

'''手太阴肺经穴位: 中府，云门，天府，侠白，尺泽，孔最，列缺，经渠，太渊，鱼际，少商'''
lungaps=('zhongfu', 'yunmen', 'tianfu', ' xiabai', ' chize', 'kongzui', 'lieque', 'jingqu', 'taiyuan', 'yuji', 'shaoshang')
'''手阳明大肠经腧穴：商阳、二间、三间、合谷、阳溪、偏历、温溜、下廉、上廉、手三里、曲池、肘髎、手五里、臂臑、肩髃、巨骨、天鼎、扶突、禾髎、迎香'''
largeintestineaps=('shangyang', 'erjian', 'sanjian', 'hegu', 'yangxi', 'pianli', 'wenliu', 'xialian', 'shanglian', 'shousanli', 'quchi', 'zhouliao', 'shouwuli', 'binao', 'jianyu', 'jugu', 'tianding', 'futu', 'heliao', 'yingxiang')
'''足阳明胃经腧穴：'''
stomachaps=('')
'''足太阴脾经腧穴：隐白、大都、太白、公孙、商丘、三阴交、漏谷、地机、阴陵泉、血海、箕门、冲门、府舍、腹结、大横、腹哀、食窦、天溪、胸乡、周荣、大包'''
spleenaps=('yinbai', 'dadu', 'taibai', 'gongsun', 'shangqiu', 'sanyinjiao', 'lougu', 'diji', 'yinlingquan', 'xuehai', 'jimen', 'chongmen', 'fushe', 'fujie', 'daheng', 'fuai', 'shidou', 'tianxi', 'xiongxiang', 'zhourong', 'dabao')
'''手少阴心经腧穴：'''
heartaps=('')
'''手太阳小肠经腧穴：'''
smallintestineaps=('')
'''足太阳膀胱经腧穴：'''
bladderaps=('')
'''足少阴肾经腧穴：'''
kidneyaps=('')
'''手厥阴心包经穴位：天池、天泉、曲泽、郄门、间使、内关、大陵、劳宫、中冲'''
percardiumaps=('tianchi', 'tianquan', 'quze', 'qiemen', 'jianshi', 'neiguan', 'daling', 'laogong', 'zhongchong')
'''手少阳三焦经腧穴：'''
sanjiaoaps=('')
'''足少阳胆经腧穴：'''
gallbladderaps=('')
'''足厥阴肝经腧穴：'''
liveraps=('')



class acupoint(object):
    def __init__(self,pointname,pointtype,pointchannel):
        self.name=pointname
        self.type=pointtype
        self.channel=pointchannel if pointchannel else None
    
class acuchannel(object):
    def __init__(self,channelname,acupoints=()):
        self.name=channelname
        self.member=acupoints

class meridian(object):
    def __init__(self):
        self.taiying=acuchannel('taiyin', ('acupoints',))

if __name__ == "__main__":
    pass


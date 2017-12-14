# -*- coding: utf-8 -*-
import json
import sys 

def test_json():
#    str1 = '{"web_tags": ["viedo_rb"], "from_src": "iqiyi", "author": null, "update_progress": "04:59", "title": "薛之谦怒摔话筒罢录", "brief": "《娱乐评什么》是一档娱乐评论节目。用独特视角，从娱乐新闻中挖掘最具吸引力的头条，展现给大家，并加以犀利的评论。", "episode_brief": "          薛之谦摔话筒惊爆黑幕，节目现场陷入尴尬……        ", "play_tags": ["独家", "热点", "原创"], "channel_tags": [{"text": "娱乐", "label": "频道："}, {"text": "独家", "label": "内容类型："}, {"text": "内地", "label": "地区："}, {"text": "音乐", "label": "类型："}], "id": ["v_19rr86wd3s"]}'
#    str1Arr = json.loads(str1)
#    print str1Arr

    str2 = '{"web_tags": ["viedo_rb"], "from_src": "iqiyi", "author": null, "update_progress": "01:12", "play_tags": ["独家", "港台", "新闻"], "title": "周杰伦小巨蛋演唱会 现场拿陈奕迅开涮", "brief": "出道十周年站上小巨蛋，周杰伦和南拳妈妈LARA同台来上一段蛇舞，令人惊艳！周杰伦不改一贯作风，演唱会情义相挺自家人和师妹袁咏琳合唱经典歌曲黑色幽默。新人浪花兄弟SOLO表演周董也来参一脚，...", "publish_time": "2010-6--3 ", "episode_brief": "出道十周年站上小巨蛋，周杰伦和南拳妈妈LARA同台来上一段蛇舞，令人惊艳！周杰伦不改一贯作风，演唱会情义相挺自家人和师妹袁咏琳合唱经典歌曲黑色幽默。新人浪花兄弟SOLO表演周董也来参一脚，...", "channel_tags": [{"text": "娱乐", "label": "频道："}, {"text": "独家", "label": "内容类型："}, {"text": "港台", "label": "地区："}, {"text": "音乐", "label": "类型："}], "id": ["v_19rrj5jvvs"]}'
    str2Arr = json.loads(str2)
    print str2Arr['brief']
    print str2Arr['publish_time']
    print str2Arr['episode_brief']

if __name__ == '__main__':
    test_json()

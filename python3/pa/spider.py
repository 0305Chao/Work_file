from urllib import request
import re

#BeautifulSoup, Scrapy
#爬虫 ， 反爬虫 ， 反反 爬虫
#如果自己的ip 频繁爬数据就会封ip
#这里用代理ip

class Spider():
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = 'span class="video-number">([\s\S]*?)</span>'
    
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        
        #print(root_html[0])
        #打印第一个元素
        #print(anchors[0])
        #打印全部的
        #print(anchors)
        return anchors
        a = 1

    def __refine(self, anchors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
         }
        return map(l, anchors)

    def __sort(self, anchors):
        #这样会报错'not supported between instances of 'dict' and 'dict''
        #anchors = sorted(anchors)
        anchors = sorted(anchors, key=self.__sort_seed,reverse=True)
        return anchors
    
    def __sort_seed(self, anchor):
        #这样是安照数字排序
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        #排序前面加序号
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1)
            + ':' + anchors[rank]['name']
            + '====' + anchors[rank]['number']
            )
    
    def go(self):
        htmls = self.__fetch_content()
        #self.__analysis(htmls)
        anchors = self.__analysis(htmls)
        #这里是列表
        anchors = list(self.__refine(anchors))
        #调用函数sort
        anchors = self.__sort(anchors)
        # print(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()







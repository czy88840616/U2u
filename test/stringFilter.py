#encoding=gbk
__author__ = 'czy-thinkpad'
gs='截取没问题x的x时候不会的,显示正常的.昨晚这么做的,到目前为止还不错.对编码一直都搞得不太明白,所以'

def CutString(gs):
    t = gs[-1]
    unicode(t, 'gbk')
    return t

#while True:
#    try:
#        unicode(t, 'gbk')
#        break
#    except:
#        n -= 1
#        t = gs[:n]
#return t

print(CutString(gs[0:10]))
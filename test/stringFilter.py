#encoding=gbk
__author__ = 'czy-thinkpad'
gs='��ȡû����x��xʱ�򲻻��,��ʾ������.������ô����,��ĿǰΪֹ������.�Ա���һֱ����ò�̫����,����'

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
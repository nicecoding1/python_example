from jmunja import smssend

uid = "" #제이문자 아이디 (jmunja.com)
upw = "" #API Key
subject = "파이썬 python"
content = "파이썬 모듈 테스트\npython module test"
hpno = "01012345678"
callback = "01012345678"

jweb = smssend.JmunjaWeb(uid, upw)
wresult = jweb.send(subject, content, hpno, callback)

if wresult:
    print("웹문자 %s건 발송 성공" % (wresult))
else:
    print("발송 실패")

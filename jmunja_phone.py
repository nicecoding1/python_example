from jmunja import smssend

uid = "" #제이문자 아이디 (jmunja.com)
upw = "" #API Key
subject = "파이썬 python"
content = "파이썬 모듈 테스트\npython module test"
hpno = "01012345678"
callback = "01012345678"

jphone = smssend.JmunjaPhone(uid, upw)
presult = jphone.send(subject, content, hpno)

if presult:
    print("폰문자 %s건 발송 성공" % (presult))
else:
    print("발송 실패")

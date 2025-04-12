_OOO00O000O0OOOO00 ='follow'#line:1
_OO0OO000000000O00 ='success'#line:2
_O0000O000O0O0OOOO ='","token":"'#line:3
_O00O0O0O0OOOO0O0O =True #line:4
from datetime import datetime #line:5
import pyfiglet ,requests ,base64 #line:6
from time import *#line:7
import sys ,json ,os ,platform ,random #line:8
def detect_environment ():#line:9
	O0O00OO00OO000OO0 =platform .system ()#line:10
	if O0O00OO00OO000OO0 =='Windows':print ('CMD (Windows)');return 0 #line:11
	elif O0O00OO00OO000OO0 =='Linux':#line:12
		if 'TERMUX_VERSION'in os .environ :print ('Termux (Android)');return 1 #line:13
		print ('Linux Terminal');return 2 #line:14
	else :print ('Không xác định')#line:15
print ('Đang kiểm tra thiết bị: ',end ='')#line:16
ctb =detect_environment ()#line:17
try :from colorama import Back ,Fore ,Style ,init ;import pyfiglet #line:18
except :print ('Bắt đầu cài bổ xung thư viện !');os .system ('pip install colorama pyfiglet')#line:19
if ctb ==0 :init (convert =_O00O0O0O0OOOO0O0O )#line:20
class firmware :#line:21
	def __init__ (OO0OO0O0000OOOOOO ):0 #line:22
	
	
	def banner (O0OO0O0O00000O00O ):print ('\x1bc',end ='');O00OO0O00O0OOOOOO =pyfiglet .figlet_format ('RVTOOL',font ='small_slant',width =80 );OOO00OOO00O00OO00 =[OO0OOO0OO0O00OO0O for OO0OOO0OO0O00OO0O in O00OO0O00O0OOOOOO .splitlines ()if OO0OOO0OO0O00OO0O .strip ()];OO0O0O000000O0O0O ='\n'.join (OOO00OOO00O00OO00 );OO0O0O000000O0O0O =f"{Fore.CYAN}{OO0O0O000000O0O0O}{Style.RESET_ALL}";print (OO0O0O000000O0O0O );print ('-'*20 )#line:42
class tiktok :#line:43
	def __init__ (OOOO0000O0OO00000 ,O0OO00O0O00O00OO0 ,O000O000O0O0OOOO0 ):OOOO0000O0OO00000 .user =O0OO00O0O00O00OO0 ;OOOO0000O0OO00000 .tp =O000O000O0O0OOOO0 ;OOOO0000O0OO00000 .session =requests .Session ();OOOO0000O0OO00000 .get =OOOO0000O0OO00000 .session .get ;OOOO0000O0OO00000 .post =OOOO0000O0OO00000 .session .post ;OOOO0000O0OO00000 .err =0 ;OOOO0000O0OO00000 .headers ={'accept':'*/*','accept-language':'vi-VN,vi;q=0.9','content-type':'text/plain;charset=UTF-8','origin':'https://tikfollowers.com','priority':'u=1, i','referer':'https://tikfollowers.com/free-tiktok-followers','sec-ch-ua':'"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'};OOOO0000O0OO00000 .token =OOOO0000O0OO00000 .get_token ()#line:44
	def get_token (O0O0OOO000OOOO0O0 ):#line:45
		O00O0OO00O0OOO0O0 ='https://tikfollowers.com/'#line:46
		try :print ('Đang Login ... \r',end ='');O0O00OOO00OO0OO00 =O0O0OOO000OOOO0O0 .get (url =O00O0OO00O0OOO0O0 ,headers =O0O0OOO000OOOO0O0 .headers );O0O000O0O0O0OOOOO =O0O00OOO00OO0OO00 .text .split ("csrf_token = '")[1 ].split ("'")[0 ];print ('                                           \r',end ='');return O0O000O0O0O0OOOOO #line:47
		except :print ('không thể kết nối với server hãy thử lại sau !');sys .exit ()#line:48
	def c_time (OOOO000O0000OOO00 ,O000OO0O0O0O0O00O ):#line:49
		O000000O000OOOOO0 =[Back .BLACK ,Back .RED ,Back .GREEN ,Back .YELLOW ,Back .BLUE ,Back .MAGENTA ,Back .CYAN ,Back .WHITE ]#line:50
		try :#line:51
			for OO0O0O000O000000O in range (O000OO0O0O0O0O00O ,-1 ,-1 ):OOO00O0OOOOO0OO0O =random .choice (O000000O000OOOOO0 );print (OOO00O0OOOOO0OO0O +Fore .BLACK +f" Vui lòng Chờ {OO0O0O000O000000O} giây \r"+Style .RESET_ALL ,end ='');sleep (1 )#line:52
			print ('                                    \r',end ='')#line:53
		except :pass #line:54
	def fmt (O0O0O0OO000O0O0O0 ,OO000O0O00000OOOO ):return f"{Fore.CYAN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {Fore.MAGENTA} --> {Fore.GREEN}{OO000O0O00000OOOO}{Fore.RESET}"#line:55
	def free (O0O00OOO0OOOOOOOO ):#line:56
		OO000O0O0000OOOOO ='https://tikfollowers.com/api/free';print ('Get data ... \r',end ='');O0O00OOO0OOOOOOOO .gg_token ='03AFcWeA6JMsHnFA92hVyaQGJepvRgKvByZ42vh8GhzCKAZNkn34uyhA8HDhiOseNFPlOCCy2L2IB7RZ4dw1vcHtqoY7gBqsvTJAhFRUryRWAjwcllWZ4Ghp10FBhLsrnB8gHVUywzurcmjEBEJJKW7HnFWnmn-KzxVQ-ZUse0A42fsKDH1uXKqeSGjMWQZRC4rxkhAeZ4t_CySMzRTq67BdTa0K4LQNGH2C3K2uWuHE8YFlKRoHnvCW3fV4cxmuXDtQCs_CBYaTK-TDlDxNeKnKpQTKr66UB-GK952BZJ4qkA4kZMsTNSD3ADgF_r6xHXE8ZQFqVB37-7ubCDmJ1uljrQ9YyxgdL4dZw08wlUzY690d2vCJLk-824obisjBhGJJ0SIGzN7GPTyuEDMINoO63pXnR0vuc_L_7aLMLRjDidVycGdEH5GcBReqHV5fRO0G_VOjFuhy42feeShWafAFg1Sr4ePStylHfa00KDRVW_qrpQvQ7Rmx3kM-TOoK1CTSWKcOkkoAcwLlr5qm0qa_UKsNYjj6fJPyS1BSB-rrT4CaS7rWwyuBjRvpLiO43eUMIIC7xrmy1AGHb3-6hHoezlUxSPTEVMgL4HiNLFqXx_xJQFfOrca4AdWiAokITYHRtrILg2YuyaSkpYZ9FGKNYifF2NiK-VshkGEUr-PyIzm8tylMIfkHY8vSHU64aLcs2BxSvOANOejmKWbpDJVP69H_P7rQTuGv2bbSLTS4bRDQEfF3QEAtEtUBYd0RiZX-ks55U3RnOUyCrYh_ex87z7g4Y5MPdrQosKVzzRpfTthqwmvIRhmObYX2g5gt-6kXuxQav1r6HH9KZYLeoD0zyo47ejbmXAclE1KGkrEyb_Qn7LGTRlJOL2QOy91SlSfengQFgWQuB1Nx7pJmq4uhfSwUkpWQmlf6e4yYQq2dCFP9l3WdSN-aFgHPbzWbcXyLyphBt6IlS6ic7siDO4NGDi8gIl3gAAiLNbY-vBeOd1HJbLLYpEQjIYofLCGonGA0sRX6eoYIPRYKla2ZXxFE44lw1xAul4AygLa2mn8mWkhWf14vUQStwN3UlFbyi1OELnqsKua93r1N3m7D-94O280jtN7IuiFHYAF8TwHLkfH_6sB7pjep7oNVSGY0PD2rJ80VkM6t2PuJtxmQqovzlsOg2wwnAmt9fudJZkGuJGWwyjRzwJskkDxkeTjO3bwesWRM4dIbF6xUjrl5H-UPSBwFBqDps_BUIIVxivEeNnTi6je2KU9pepBeg2uBUXiqpts8j7U73Ax7ncs2rhVBTMvw02xzDfOnIlTKnOjvs4B0vuav3PbuthoXCiXKOmQEEg3kREAyhDCct_XNRrFAcmFaaJWKkmBLC6qqdyJdPnHzaMyK7mpDQiMiNEillv0i2T2iE6Geb8UXXkANupmW6jdVA-s9HeEhUXfy1yQQoL1AjQnp6g71SG1Hixs8tyu7kQxWr9AvucCCFUYlvVTUiUvAwLm1lP6cy31fkmkOC-U8wlUMz8qWdPVNVRRvNoSr5oI_u2Uqlf4i9FAEPs-eoQ9oEZEltzA-pfX7hBx77jxPbLhT2IPFC8OC0U-xNZTWKW2JUyh77_y3Yq2Ht7JkhHmdov1Rl1FYFZJs-KDrfc0mgCSuaiOO8FbE26IHYNXPNpbmN6khcH2m2oH6q8YfakCnknidz68-_Th0ey-67qxUoXifD1BAxfoKpPhYfU7P_YpskaQa_uGYw__c8H5TO7T1fF7dKEwST4TlIUZSzb5rPqhq-fISrYE1w-gNPlxVpBS5wx6sUw2fHsBtO_SC58e9qmWhtcf460f-SVAgH6fUUCSrqv2vxva_BfIdxjVpFip3XeKr3HQ5IPutvVhyQMEQ911HL32xP6lsLOIglyizH0RKJF7tSrr__p6BnbMrv0xaFGB2houn2HtuxdkvVvbDOP9sTpTPDdBt6e2OawwW1ZtDMHg64SZ_-dQvwAlrMwIhjw5RdsptxSNwxrH11M_1rG7l4H9A';O0O0OOOOOOO0OO0O0 ='{"type":"'+tp +'","q":"'+O0O00OOO0OOOOOOOO .user +'","google_token":"'+O0O00OOO0OOOOOOOO .gg_token +_O0000O000O0O0OOOO +O0O00OOO0OOOOOOOO .token +'"}';OOO0000O000O0OOOO =0 #line:57
		try :#line:58
			O0OO0O0OO0O000OOO =O0O00OOO0OOOOOOOO .post (url =OO000O0O0000OOOOO ,headers =O0O00OOO0OOOOOOOO .headers ,data =O0O0OOOOOOO0OO0O0 );O00O0O000O00OOO0O =json .loads (O0OO0O0OO0O000OOO .text )#line:59
			if O00O0O000O00OOO0O [_OO0OO000000000O00 ]:O0O00OOO0OOOOOOOO .dt =O00O0O000O00OOO0O ['data'];return 0 #line:60
			else :O0O00OOO0OOOOOOOO .c_time (60 );O0O00OOO0OOOOOOOO .err +=1 #line:61
		except :print ('yêu cầu thất bại hãy thử lai sau !');O0O00OOO0OOOOOOOO .err =2 #line:62
		if O0O00OOO0OOOOOOOO .err ==2 :sys .exit ()#line:63
		else :O0O00OOO0OOOOOOOO .free ()#line:64
	def send (O0OOOOOO00O0OO0O0 ):#line:65
		O0OO0O0000O0OOO00 ='https://tikfollowers.com/api/free/send'#line:66
		try :#line:67
			print ('Buff '+O0OOOOOO00O0OO0O0 .tp +' ...\r',end ='');O0OOO0OOO0000000O ='{"google_token":"'+O0OOOOOO00O0OO0O0 .gg_token +_O0000O000O0O0OOOO +O0OOOOOO00O0OO0O0 .token +'","data":"'+O0OOOOOO00O0OO0O0 .dt +'","type":"'+O0OOOOOO00O0OO0O0 .tp +'"}';O0OOO0OO0OO0O0O00 =O0OOOOOO00O0OO0O0 .post (url =O0OO0O0000O0OOO00 ,headers =O0OOOOOO00O0OO0O0 .headers ,data =O0OOO0OOO0000000O );OOO0OOOO0OOO000OO =json .loads (O0OOO0OO0OO0O0O00 .text )#line:68
			if OOO0OOOO0OOO000OO [_OO0OO000000000O00 ]:print (O0OOOOOO00O0OO0O0 .fmt (O0OOOOOO00O0OO0O0 .tp +' successfully sent.'));O0OOOOOO00O0OO0O0 .c_time (605 )#line:69
			else :O00O0OOO0O00O000O =int (OOO0OOOO0OOO000OO ['message'].split (': ')[1 ].split (' Minutes')[0 ])*60 +5 ;O0OOOOOO00O0OO0O0 .c_time (O00O0OOO0O00O000O )#line:70
		except :print ('Lỗi ! không thể tăng '+O0OOOOOO00O0OO0O0 .tp +' !');sys .exit ()#line:71
fw =firmware ()#line:72
fw .banner ()#line:73
fw .banner ()#line:75
print ('1. Follow\n2. Like')#line:76
while _O00O0O0O0OOOO0O0O :#line:77
	sl =int (input ('Nhập lựa chọn: '))#line:78
	if sl ==1 :tp =_OOO00O000O0OOOO00 ;break #line:79
	elif sl ==2 :tp ='like';break #line:80
	else :print ('nhập lại lựa chọn đúng ')#line:81
user =input ('nhập user: ')#line:82
try :#line:83
	if tp ==_OOO00O000O0OOOO00 :tp =tp .split ('@')[1 ].split ('/')[0 ]#line:84
except :pass #line:85
print ('-'*20 )#line:86
while _O00O0O0O0OOOO0O0O :tt =tiktok (user ,tp );tt .free ();tt .send ()

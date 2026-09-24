import urllib.request,urllib.error,http.cookiejar,json,uuid,time,re
root='http://localhost:5173'
jar=http.cookiejar.CookieJar();client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
checks=[]
def call(path,method='GET',data=None,origin=root):
 headers={'Origin':origin}
 if data is not None:headers['Content-Type']='application/json'
 req=urllib.request.Request(root+path,data=json.dumps(data).encode() if data is not None else None,headers=headers,method=method)
 try:
  with client.open(req,timeout=25) as r:return r.status,r.read().decode(),dict(r.headers)
 except urllib.error.HTTPError as e:return e.code,e.read().decode(),dict(e.headers)
def check(name,ok):
 checks.append({'test':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
for path in ['/','/commissions','/work','/studio','/approach','/accessibility','/journal','/inquiry','/privacy','/journal/wedding-flower-planning','/work/forbidden-fruit-at-thornwood-castle','/work/dreamy-mauve-s-and-peach-in-september']:
 status,html,h=call(path);check('Route '+path,status==200 and len(re.findall(r'<h1(?:\s|>)',html))==1 and 'lang="en"' in html)
check('Anonymous owner API denied',call('/api/workspace')[0]==403)
check('Anonymous client update denied',call('/api/client-events','PATCH',{'id':str(uuid.uuid4()),'approval':'Approved'})[0]==404)
lead={'requestId':str(uuid.uuid4()),'startedAt':int(time.time()*1000)-10000,'name':'HTTP Review Test','email':'http-review@example.invalid','dateUnknown':True,'venue':'Test venue','service':'full-service','budget':'50000-75000','privacy':'on','planner':'Test planner','scope':'Ceremony and reception','drawn':'Color','logistics':'Test only','inspiration':'https://example.com','vision':'Test only','source':'','website':''}
check('Cross origin inquiry denied',call('/api/inquiries','POST',lead,'https://untrusted.example')[0]==403)
bad=lead|{'email':'invalid'};check('Invalid email rejected',call('/api/inquiries','POST',bad)[0]==400)
bad=lead|{'dateUnknown':False,'eventDate':'2027-02-31'};check('Invalid calendar date rejected',call('/api/inquiries','POST',bad)[0]==400)
status,raw,h=call('/api/inquiries','POST',lead);check('Review inquiry durably accepted',status==201);id=json.loads(raw)['id']
retry=call('/api/inquiries','POST',lead);check('Inquiry retry returns same receipt',retry[0]==200 and json.loads(retry[1])['id']==id)
check('Marketing endpoint retired',call('/api/subscriptions','POST',{})[0]==410)
check('Statistics require explicit consent',call('/api/events','POST',{'name':'service_view','path':'/commissions','service':'full-service','eventId':str(uuid.uuid4())})[0]==400)
check('Unknown statistics event rejected',call('/api/events','POST',{'consent':True,'name':'capture_email','path':'/commissions','service':'','eventId':str(uuid.uuid4())})[0]==400)
call('/signin-with-chatgpt?return_to=%2Fworkspace')
status,raw,h=call('/api/workspace');data=json.loads(raw);check('Owner queue available after local sign-in',status==200 and any(l['id']==id for l in data['leads']));check('No review delivery queued',data['pending']==0); stored=next(l for l in data['leads'] if l['id']==id);check('Creative details and consent durably stored',json.loads(stored['details'])['planner']=='Test planner' and stored['consent_version']=='2026-09-24' and bool(stored['consented_at']))
update={'id':id,'status':'Completed','assignedTo':'Owner','nextAction':'Test','nextDate':'','lostReason':'','adminMinutes':2}
check('Booking gate covers final/completed states',call('/api/workspace','PATCH',update)[0]==400)
update['status']='Lost';check('Lost stage requires reason',call('/api/workspace','PATCH',update)[0]==400)
update.update(status='Qualified',responded='on');check('Owner pipeline edit saved',call('/api/workspace','PATCH',update)[0]==200)
status,raw,h=call('/api/workspace/export');check('Owner export private and contains test',status==200 and 'no-store' in next((v for k,v in h.items() if k.lower()=='cache-control'),'') and 'HTTP Review Test' in raw)
check('Portal deferred',call('/client-space')[0]==404)
status,raw,h=call('/api/outbox','POST',{});check('Review mode blocks delivery',status==200 and 'No messages were sent' in raw)
check('Review record cleanup',call('/api/workspace','DELETE',{'id':id})[0]==200)
check('Sitemap includes migrated stories','/work/forbidden-fruit-at-thornwood-castle' in call('/sitemap.xml')[1])
check('Crawler excludes protected paths','Disallow: /' in call('/robots.txt')[1])
check('Custom missing page',call('/missing-review-route')[0]==404)
from pathlib import Path
(Path(__file__).resolve().parent.parent/'VERIFICATION.json').write_text(json.dumps({'scope':'Local development with platform mock sign-in. No production email, external identity, live domain, or real customer tests.','checks':checks},indent=2))
print(f'{len(checks)} checks passed')

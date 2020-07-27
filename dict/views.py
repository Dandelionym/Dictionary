from django.shortcuts import render
from django.http import JsonResponse
from lib import sqlhelpers
from lib import meaninghelpers

# Create your views here.

def index(request):
	result = []
	if request.method == 'GET':
		obj = sqlhelpers.SqlHelper()
		result = obj.get_list('select id,label,word,mean1,mean2 from words', [])
		obj.close()
	
	words_list = {}
	for i in result[:]:
		words_list[i['id']] = i
	
	return render(request, 'index.html', {'words': words_list.values(), 'sum': len(words_list)})

def egstc(request):
	print("...")
	ret = {'status': True, 'msg': None, 'eg': "undefined"}
	try:
		word = request.POST.get('word')
		word = word.strip('\n').strip('\t').strip('\n').strip(' ')
		word = "".join(word)
		print(" --- ",list(word))
		ret['eg'] = meaninghelpers.get_mean(word)
		print(ret)
	except Exception as E:
		ret['status'] = False
		ret['msg'] = E
		print(ret)
	return JsonResponse(ret)
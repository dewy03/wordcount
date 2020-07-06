from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def result(request):
    full_text = request.GET['totaltext']
    word_num = full_text.split()#word_num->list. 
    
    word_dict = {}

    for word in word_num:
        if word in word_dict:
            word_dict[word] +=1
            #있으면 vaule+1 -> value가 단어가 중복된 횟수
        else:
            word_dict[word]=1
            #없으면 value를 1로  

    return render(request, 'result.html', {'total_text': full_text, 'num': len(word_num), 'wordcount': word_dict.items()})
from bs4 import BeautifulSoup
import requests

r = requests.get('https://namu.wiki/w/%ED%96%89%EC%A0%95%EB%8F%99/%EB%AA%A9%EB%A1%9D')

target_html = r.text

bs = BeautifulSoup(target_html, 'lxml')

title = bs.find_all("h3")
gugun = bs.find_all("h4")
dong = bs.select("table tbody")
gugun_list ={}
city_list = {}
dong_list = {}
new_list = {}
for i in title:

    city_list[i.find_all('a')[0].text] = i.find_all('a')[1].text
    
# print(city_list)
# for j in city_list:
    # print(j,city_list[j])


for i in gugun:
    gugun_list[i.find_all('a')[0].text] = i.find_all('a')[1].text
    if i.find_all('a')[0].text == '3.7.4.':
        gugun_list['3.8.1.'] = "세종특별자치시"

gugun_list['3.8.1.'] = "세종특별자치시"
# print(gugun_list)
numbering = 1
for i in gugun_list:
    numbering +=1
for i in city_list:
    new_list[city_list[i]] = []
for i in gugun_list:
    for j in city_list:
        if j == i[:len(j)]:
            # print(j, i)

            new_list[city_list[j]].append(gugun_list[i])
            break

# print(new_list)
del new_list["[편집]"]
del new_list["미수복지역"]
new_list["세종특별자치시"] = ['세종특별자치시']

# for i in new_list:
#     print(i,new_list[i])

flag = -3
for k in dong:
    dong_list[flag] = [i.td.div.text for i in k.find_all('tr')][1:]
    flag += 1

# for i in range(1,5):
#     del dong_list[i]
# 작업완료
del gugun_list['3.18.1.']
del gugun_list['3.18.2.']
del gugun_list['3.18.3.']
del gugun_list['3.18.4.']
del gugun_list['3.18.5.']

# for k in gugun_list:
#     print(k,gugun_list[k])
numbering_gugun = {}
nu = 1
for i in gugun_list:
    numbering_gugun[nu] = gugun_list[i]
    nu +=1

# for i in gugun_list:
#     print(i,gugun_list[i])
# for i in numbering_gugun:
#     print(i,numbering_gugun[i])
cncn = 101
test_dict ={}
for i in numbering_gugun:
    test_dict[str(cncn)+numbering_gugun[i]] = dong_list[i]
    # print(cncn,i, numbering_gugun[i])
    cncn += 1

# for j in dong_list:
#     print(j,dong_list[j])
# for i in test_dict:
#     print(i, test_dict[i])
# for i in new_list:
#     print(i, new_list[i])

# cn = 1
# for j in test_dict:
#     print(cn,j,test_dict[j])
#     cn += 1

cn2 = 101
real_num = 1
for i in new_list:
    for j in new_list[i]:
        # print(i,j,test_dict[str(cn2) + j])
        for k in test_dict[str(cn2) + j]:
            print(real_num,k)
            real_num += 1
        cn2 += 1
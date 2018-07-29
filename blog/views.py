from django.shortcuts import render
import urllib.request as url
import random
import bs4
import re
import os
import sys

def post_list(request):
    f=open(os.path.join(sys.path[0], "irasutoya.txt"), "r")
    line = f.readlines()
    f.close
    location=line[random.randrange(len(line))]

    html = url.urlopen(location)

    soup = bs4.BeautifulSoup(html, "html.parser")

    div1 = soup.find('div', class_='title').getText()

    div2 = soup.find_all('div', class_="separator")

    img = div2[0].find('img')

    ans = div1.replace("のイラスト","")

    description=div2[1].getText()

    return render(request, 'blog/post_list.html', {
        'answer': ans,
        'imageurl': img['src'],
        'location': location,
        'description' : description,
    })

from django.shortcuts import render
import requests
def main_page(request):
     urls="https://newsapi.org/v2/everything?q=all&from=2024-04-20&sortBy=popularity&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
   #  url=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
         # url.append(f['url'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'main_page.html',context)

def games(request):
     return render(request,'games.html')

def students(request):
     return render(request,'students.html')

def bollywood(request):
     urls="https://newsapi.org/v2/everything?q=bollywood&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
   #  url=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
         # url.append(f['url'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'bollywood.html',context)

def hollywood(request):
     urls="https://newsapi.org/v2/everything?q=hollywood&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
   #  url=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
         # url.append(f['url'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'hollywood.html',context)

def tollywood(request):
     urls="https://newsapi.org/v2/everything?q=tollywood&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
   #  url=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
         # url.append(f['url'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'hollywood.html',context)

def crime(request):
     urls="https://newsapi.org/v2/everything?q=crime&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
   #  url=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
         # url.append(f['url'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'crime.html',context)

def fashion(request):
     urls="https://newsapi.org/v2/everything?q=fashion&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'fashion.html',context)

def animal(request):
     urls="https://newsapi.org/v2/everything?q=animals&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render (request,'animal.html',context)

def business(request):

     urls="https://newsapi.org/v2/everything?q=business&from=2024-04-20&sortBy=popularity&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     
     return render(request,'business.html',context)

def sports(request):
     urls="https://newsapi.org/v2/everything?q=sports&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'sports.html',context) 

def entertainment(request):
     urls="https://newsapi.org/v2/everything?q=entertainment&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'entertainment.html',context) 

def technology(request):
     urls="https://newsapi.org/v2/everything?q=laptop&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'technology.html',context) 

def life_style(request):
     urls="https://newsapi.org/v2/everything?q=life&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'life_style.html',context) 

def food(request):
     urls="https://newsapi.org/v2/everything?q=food&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'food.html',context) 

def weather(request):
     urls="https://newsapi.org/v2/everything?q=weather&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'weather.html',context) 

def education(request):
     urls="https://newsapi.org/v2/everything?q=education&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'education.html',context) 

def politics(request):
     urls="https://newsapi.org/v2/everything?q=politics&from=2024-03-07&sortBy=popularity&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'politics.html',context) 

def pollution(request):
     urls="https://newsapi.org/v2/everything?q=pollution&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'pollution.html',context) 

def world(request):
     urls="https://newsapi.org/v2/everything?q=world&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'world.html',context) 

def health(request):
     urls="https://newsapi.org/v2/everything?q=health&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'health.html',context) 

def science(request):
     urls="https://newsapi.org/v2/everything?q=science&from=2024-03-12&sortBy=publishedAt&apiKey=b81af5ba763045708c8099dec810b563"
     cricket_news=requests.get(urls).json()
     a=cricket_news['articles']
     desc=[]
     title=[]
     img=[]
     for i in range(len(a)):
          f=a[i]
          title.append(f['title'])
          desc.append(f['description'])
          img.append(f['urlToImage'])
     mylist=zip(title,desc,img)
     context={'mylist':mylist}
     return render(request,'science.html',context) 
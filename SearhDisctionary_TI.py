def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)

            
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return []
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1 : end_quote]
    return url,end_quote


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled = []
    index = {} #start with a empty dictionary,earlier we started with empty list
    while tocrawl and max_pages>0: 
        page = tocrawl.pop()
        max_pages = max_pages - 1
        if page not in crawled:
            content = get_page(page)
            if content != []:
                add_page_to_index(index, page, content)
                union(tocrawl, get_all_links(content))
                crawled.append(page)
                #print 'here'
    return index

def add_page_to_index(index, url, content): #no change required
    words = content.split()
    com_list = ['the','be','to','of','and','a','in','that','have','I','it','for',
                'not','on','with','he','as','you','do','at','this','but','his','by',
                'from','they','we','say','her','she','or','an','will','my','one','us'
                'all','would','there','their','what','so','is','into','The','To','are',
                'our','any','its','me','or','like','can','only','well','new','these',
                'day','because','also','over',
                '<html>','<head>',
                '<meta','<link','>','<script','//','</head>','<body','<table',
                'this','var','if','at','<td','<td>','</td>','<script>','<img','<tr>',
                '</tr>','</script>','</html>','}','{','[',']',
                '1','2','3','4','5','6','7','8','9',
                '</table>','<form','</form>','<option','<input','<a','<p']
    for word in words:
        if word not in com_list:
            add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append(url)
    else:
        #not found, add new keyword
        index[keyword]=[url]
    

def lookup(index, keyword):
    keylist =keyword.split()
    result = []
    for key in keylist:
        if key in index:
            union(result,index[key])
    return result

seed = "https://www.ti.com"
findex = crawl_web(seed,100)
print lookup(findex,"TI Analog")

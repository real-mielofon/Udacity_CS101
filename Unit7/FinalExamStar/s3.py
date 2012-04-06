################################################################################
# doctest testcases
"""
# Basic Udacity tests
>>> sorted(multi_lookup(index, ['Python']))
['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html']

>>> sorted(multi_lookup(index, ['Monty', 'Python']))
['http://www.udacity.com/cs101x/final/a.html']

>>> sorted(multi_lookup(index, ['Python', 'programming', 'language']))
['http://www.udacity.com/cs101x/final/b.html']

>>> sorted(multi_lookup(index, ['Thomas', 'Jefferson']))
['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html']

>>> sorted(multi_lookup(index, ['most', 'powerful', 'weapon']))
['http://www.udacity.com/cs101x/final/a.html']

# Empty results
>>> sorted(multi_lookup(index, []))
[]
>>> sorted(multi_lookup(index, ['']))
[]
>>> sorted(multi_lookup(index, [' ']))
[]
>>> sorted(multi_lookup(index, ['not_exist']))
[]
>>> sorted(multi_lookup(index, ['python']))
[]
>>> sorted(multi_lookup(index, ['Python', 'not_exist']))
[]
>>> sorted(multi_lookup(index, ['not_exist', 'Python']))
[]
>>> sorted(multi_lookup(index, ['Python', 'Python']))
[]
>>> sorted(multi_lookup(index, ['University', 'Virginia']))
[]

A sentence that appears forward should not appear backwards.
(Thanks to @slothmaster)
>>> sorted(multi_lookup(index, ['Python','Monty']))
[]

Two pages contain programming language,
>>> sorted(multi_lookup(index, ['programming', 'language']))
['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html']

but only one followed by Udacity,
>>> sorted(multi_lookup(index, ['programming', 'language', 'Udacity']))
['http://www.udacity.com/cs101x/final/a.html']

and only one preceded by Python.
>>> sorted(multi_lookup(index, ['Python', 'programming', 'language']))
['http://www.udacity.com/cs101x/final/b.html']

Two pages have all the keywords but only one in this order.
>>> sorted(multi_lookup(index, ['Thomas', 'Jefferson', 'founded']))
['http://www.udacity.com/cs101x/final/b.html']

A page has two sentences that start with the first word,
>>> sorted(multi_lookup(index, ['is']))
['http://www.udacity.com/cs101x/final/a.html']

but only one sentence is followed by 'not about'.
>>> sorted(multi_lookup(index, ['is', 'not', 'about']))
['http://www.udacity.com/cs101x/final/a.html']

All pages start with <html> <body> words.
>>> sorted(multi_lookup(index, ['<html>', '<body>']))
['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/multi.html']

A long sentence.
>>> sorted(multi_lookup(index, ['Thomas', 'Jefferson', 'founded', 'the', 'University', 'of', 'Virginia']))
['http://www.udacity.com/cs101x/final/b.html']

Test cases below are weird and not expected to be tried by Udacity.
------------------------------------------------------------------
Word combined with empty string and blank string
Should be empty string considered as a searchable word?
>>> sorted(multi_lookup(index, ['', 'Virginia']))
['http://www.udacity.com/cs101x/final/b.html']

Should be blank string considered as a searchable word?
>>> sorted(multi_lookup(index, [' ', 'Virginia']))
['http://www.udacity.com/cs101x/final/b.html']
"""
################################################################################

#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.


def multi_lookup(index, query):
    result_filter = {}
    flag_firstword = True
    for word in query:
        if word not in ['', ' ']:
            result_for_word = lookup(index, word)
            if result_for_word == None:
                return [] # not found word
            if flag_firstword:
                # first word
                result_filter = result_for_word
                flag_firstword = False
            else:
                # next word
                result_filter_next = {}        
                for url in result_filter:
                    # if it next word
                    for pos1 in  result_filter[url]:
                        if url in result_for_word and pos1+1 in result_for_word[url]:
                            if url in result_filter_next:
                                result_filter_next[url].append(pos1+1)
                            else:
                                result_filter_next[url] = [pos1+1]
                result_filter = result_filter_next         

    # generate result without indexword dictonary -> list keys
#    return result_filter.keys() # change code which below
    result = []
    for url in result_filter:
        result.append(url) 
    return result


def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

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


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    pos_word = 0
    for word in words:
        add_to_index(index, word, pos_word, url)
        pos_word = pos_word + 1 
        
def add_to_index(index, keyword, pos_word, url):
    if keyword in index:
        if url in index[keyword]:
            index[keyword][url].append(pos_word)
        else:
            index[keyword][url] = [pos_word]
    else:
        index[keyword] = {url:[pos_word]}

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    



cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.
</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    





#Here are a few examples from the test site:

#index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')

#print multi_lookup(index, ['Python'])
#print ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']
#
#print multi_lookup(index, ['Monty', 'Python'])
#print ['http://www.udacity.com/cs101x/final/a.html']
#
#print multi_lookup(index, ['Python', 'programming', 'language'])
#print ['http://www.udacity.com/cs101x/final/b.html']
#
#print multi_lookup(index, ['Thomas', 'Jefferson'])
#print ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']
#
#print multi_lookup(index, ['most', 'powerful', 'weapon'])
#print ['http://www.udacity.com/cs101x/final/a.html']
#
#print multi_lookup(index, 'step by step'.split())
#print ['http://www.udacity.com/cs101x/final/a.html', 'http://www.udacity.com/cs101x/final/b.html']


################################################################################
# Crawl the cached web.
index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')

print sorted(multi_lookup(index, ['is', 'not', 'about']))

if __name__ == "__main__":
    # Standard
    import doctest
    doctest.testmod(report=True, verbose=True, exclude_empty=True)
elif __name__ == "main":
    # Udacity
    import doctest, main
    doctest.testmod(main,report=True, verbose=True, exclude_empty=True)
################################################################################
#Triple Gold Star

#Only A Little Lucky

#The Feeling Lucky question (from the regular homework) assumed it was enough to
#find the best-ranked page for a given query. For most queries, though, we don't
#just want the best page (according to the page ranking algorithm), we want a
#list of many pages that match the query, ordered from the most likely to be
#useful to the least likely.

#Your goal for this question is to define a procedure, ordered_search(index,
#ranks, keyword), that takes the same inputs as lucky_search from Question 5,
#but returns an ordered list of all the URLs that match the query.

#To order the pages, use the quicksort algorithm, invented by Sir Tony Hoare in
#1959. Quicksort provides a way to sort any list of data, using an expected
#number of comparisons that scales as n log n where n is the number of elements
#in the list.

#The idea of quicksort is quite simple:

#If the list has zero or one elements, it is already sorted.

#Otherwise, pick a pivot element, and split the list into two partitions: one
#contains all the elements equal to or lower than the value of the pivot
#element, and the other contains all the elements that are greater than the
#pivot element. Recursively sort each of the sub-lists, and then return the
#result of concatenating the sorted left sub-list, the pivot element, and the
#sorted right sub-list.

#For simplicity, use the first element in the list as your pivot element (this
#is not usually a good choice, since it means if the input list is already
#nearly sorted, the actual work will be much worse than expected).


def qsort(list, compare):
    if len(list) <= 1:
        return list
    list_left = []
    list_right = []
    node_pivot = list[0]
    for node in list[1:]:
        if compare(node, node_pivot) > 0:
            list_right.append(node)
        else:
            list_left.append(node)
    #sort parts
    list_left = qsort(list_left, compare)+[node_pivot]
    list_right = qsort(list_right, compare)
    
    #merge
    result = []
    i,j = 0,0
    for k in range(len(list)):
        if (i >= len(list_left)) or (((j < len(list_right))) and compare(list_left[i], list_right[j]) > 0):
            result.append(list_right[j])
            j = j + 1
        else:   
            result.append(list_left[i])
            i = i + 1
    return result

def compare_rank(node1, node2):
    return node1[1] < node2[1]

def ordered_search(index, ranks, keyword):
    if keyword in index:
        url_ranks = []
        for url in index[keyword]:
            url_ranks.append([url, ranks[url]])
        url_ranks = qsort(url_ranks, compare_rank)
        #extract urls
        result = []
        for node in url_ranks:
            result.append(node[0])
        return result            
    else:
        return None











cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""


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
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

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

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#Here are some example showing what ordered_search should do:

#Observe that the result list is sorted so the highest-ranking site is at the
#beginning of the list.

#Note: the intent of this question is for students to write their own sorting
#code, not to use the built-in sort procedure.

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print ordered_search(index, ranks, 'Hummus')
#>>> ['http://udacity.com/cs101x/urank/kathleen.html', 
#    'http://udacity.com/cs101x/urank/nickel.html', 
#    'http://udacity.com/cs101x/urank/arsenic.html', 
#    'http://udacity.com/cs101x/urank/hummus.html', 
#    'http://udacity.com/cs101x/urank/index.html'] 

print ordered_search(index, ranks, 'the')
#>>> ['http://udacity.com/cs101x/urank/nickel.html', 
#    'http://udacity.com/cs101x/urank/arsenic.html', 
#    'http://udacity.com/cs101x/urank/hummus.html', 
#    'http://udacity.com/cs101x/urank/index.html']


print ordered_search(index, ranks, 'babaganoush')
#>>> None






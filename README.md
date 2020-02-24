Instruction for install crawler
-------------------------------

<b>1</b>. In order to start working with a web crawler, you need to install the <b>pip</b> dependencies:
  - scrapy
  - datetime

To do this, open a terminal, and write the following command:

    $ pip install scrapy datetime
    
Do not forget to remove the dependencies if something went wrong or you delete the program and you do not need these dependencies!
    
<b>2</b>. Go to the cloned project folder:

    $ git clone https://github.com/mutedSpectre/lentascraper/ && cd lentascraper
    
Run the program
---------------

You can run the program with several parameters in order to filter the output:
  - rubric (for selection by category, and if the parameter is not specified, then all articles will be selected (where mainly all articles for today))
  - date (for selection by date, and if you do not specify a date, today's date will be applied)

At the same time, it is completely optional to indicate these parameters. Then all articles for today will be selected.<br><br>

Example:
    
    $ scrapy crawl lentascraper -o output.json -a rubric=russia -a date=2020/02/20 
    
Where:
  - lentascraper - spider name (/lentascraper/lentascraper/spider/lenta_ru_spider.py)
  - -o - option to specify output files (format can only be: json, jsonlines, jl, csv, xml, marshal, pickle)
  - -a - option to pass an attribute
  
Attributes
----------
##### rubric
This attribute gives the crawler the rubric by which articles are to be sorted.
##### date
This attribute gives the crawler the date by which articles are to be sorted.<br>
Date must be in format: YYYY/MM/DD

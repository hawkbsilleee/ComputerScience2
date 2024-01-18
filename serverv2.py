from flask import Flask, request
import news
import filters 
# TODO 2 - Import your news and filters modules

FEED_URLS = ["https://feeds.npr.org/1001/rss.xml", "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"]

# Initialize a Flask object which handles requests from the browser
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():

    # The basic html template which will be returned 
    # and sent to the user's browser
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Stories from NPR and NY Times</title>
    </head>
    <body>
        <h1>Stories from NPR and NY Times</h1>
        <h2>Filters</h2>
        <!-- Form for collecting TitleFilter phrases  -->
        <form action="/">
            <label for="title_phrase">Phrases in Title:</label>
            <!-- The title_phrase url parameter is used as the default value  -->
            <input type="text" id="title_phrase" name="title_phrase" value="{request.args.get('title_phrase', '')}" /><br><br>
            <input type="submit" value="Submit and Refresh">
        </form>
        <!-- Form for collecting DescriptionFilter phrases  -->
        <form action="/">
            <label for="description_phrase">Phrases in Description:</label>
            <input type="text" id="description_phrase" name="description_phrase" value="{request.args.get('description_phrase', '')}" /><br><br>
            <input type="submit" value="Submit and Refresh">
        </form>
        <hr>
        <h2>Stories</h2>
    """

    filter_list = []
    
    # TODO 2 - create a new method in the NewsStory class named get_html().
    # The method should return a well formatted html string to display
    # the NewsStory's title (hyperlinked to the link), pubdate, and description.
    # Use this method to add the stories to the html string.

    # TODO 3 - use request.args.get('title_phrase') to check if 
    # there is a url parameter named title, if there is create 
    # a TitleFilter object and add it to the filter_list.  Then generate 
    # a list of NewStorys by creating a filter_list and calling filters.filter_stories

    # input phrases/times user is searching for 
    title_phrase = request.args.get('title_phrase')
    description_phrase = request.args.get('description_phrase')

    filter_builder = [filters.TitleFilter(title_phrase), filters.DescriptionFilter(description_phrase)]
    query_list = [title_phrase, description_phrase]
   
    # if user doesn't input a filter query, display all stories in NewsFeed 
    if title_phrase == None and description_phrase == None:
        # loop through each website URL (NPR and NY Times)
        for url in FEED_URLS:
            # create a NewsFeed object with each URL and generate all its news stories 
            # one-by-one. 
            for story in news.NewsFeed(url).get_stories():
               # convert story to proper html format and then add to html string. 
                html += story.get_html()
    # if user does input a filter query, only display stories that satisfy it 
    else:
        for index in range(len(query_list)): 
            if query_list[index] != None:
                filter_list.append(filter_builder[index])

        # create new TitleFilter with user inputed search query and add to Filter_list 
        # filter_list.append(filters.TitleFilter(title_phrase))
        
        # loop through each website URL (NPR and NY Times)
        for url in FEED_URLS:
            # apply the filters in Filter_list and loop through each story that passes 
            for story in filters.filter_stories(news.NewsFeed(url), filter_list):
                # convert story to proper html format and then add to html string. 
                html += story.get_html()

    # close the body and html tags from the html template
    html += "</body></html>"  

    return html


if __name__ == '__main__':
    # Start the debug server so you can access the website at 
    app.run(debug = True)

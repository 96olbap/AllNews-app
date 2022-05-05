from flask import render_template,request,redirect,url_for
from app import app
from app.requests import get_articles,get_sources,search_source

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting news articles
    news_articles = get_articles()
    news_sources = get_sources()
    

    title = 'Home - Welcome to your One-stop News Website Online'
    
    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html', title = title, articles = news_articles, sources = news_sources)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {source_name}'
    
    return render_template('search.html', sources = searched_sources)
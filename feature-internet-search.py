import webbrowser

class searchTerminal: 
    # webbrowser.open_new("https://www.google.com/")
    def __init__(self):
        self.history = {}
        self.search_index = 0

    def search_engine(self):  
        #* encode the users input for Google search engine.
        search=input("Enter your search: ").strip().replace(' ','+') 
        #increase search index
        self.search_index += 1   
        #* Create URL for the search. 
        URL='https://google.com/search?q=' + search 
        #* Open and search the URL 
        webbrowser.open_new_tab(URL) 
        #Store search history into dictionary 
        self.history[self.search_index] = {search : URL}

    def search_history(self):
        print(self.history)
        history_request = int(input("Which URL do you want to access (0 to exit): "))
        if history_request >= 1:
            URL = list(self.history[history_request].values())[0]
            webbrowser.open_new_tab(URL) 
            

# search_data = searchTerminal()
# search_data.search_engine()
# search_data.search_history()





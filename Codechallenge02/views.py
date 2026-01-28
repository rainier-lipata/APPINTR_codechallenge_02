from django.shortcuts import render

# Class

class Topic:
    def __init__(self, topic,description):
        self.topic = topic
        self.description = description

    def get_details(self):
        return f'{self.topic} {self.description}'

# View

def home(request):
    t1 = Topic('Models', 'Handles your database structure and data.')
    t2 = Topic('Views', 'The logic that processes requests and returns responses')
    t3 = Topic('Templates','The HTML files that display data to the user.')
    t4 = Topic('URLs','The address book that routes requests to views  ')
    t5 = Topic('Admin','A built-in interface to manage your data easily')
    t6 = Topic('MVT','Stands for Model-View-Template architecture.')
    t7 = Topic('ORM','Allows you to talk to a database using Python code')
    t8 = Topic('Migrations','Propagates changes you make to models to the database')
    t9 = Topic('Forms','Handles user input and validation safely')
    t10 = Topic('Middleware','Hooks into Django request/response processing')

   
    all_topics = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

    search_query = request.GET.get('q', '').strip()

    if search_query:
        filtered_topics = [
            topic for topic in all_topics
            if search_query.lower() == topic.topic.lower()  # Exact match
        ]
        return render(request, 'index.html', {
            'all_topics': all_topics,
            'filtered_topics': filtered_topics,
            'search_query': search_query
        })

    return render(request, 'index.html', {'all_topics': all_topics})
    

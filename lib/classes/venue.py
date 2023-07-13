from classes.concert import Concert

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and title != '':
            self._title = title
        else:
            raise Exception
    
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        if isinstance(city, str) and city != '':
            self._city = city
        else:
            raise Exception
    
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return [concert.band for concert in Concert.all if concert.venue == self]
    
    #this deliverable feels weirdly worded and I'm not sure I did it correctly, but
    #all the tests work and technically it does what the description says
    #would make much more sense if there was some concrete way to order the concerts (i.e. times)
    #maybe I'm looking at it wrong, let me know please
    def concert_on(self, date):
        first_concert = None
        concerts = [concert for concert in Concert.all if concert.date == date]
        print(concerts)
        if len(concerts) != 0:
            first_concert = concerts[-1]
        return first_concert
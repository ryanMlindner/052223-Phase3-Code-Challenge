
class Concert:
    
    all = []
    
    def __init__(self, date, band, venue):
        from classes.band import Band
        from classes.venue import Venue
        self.date = date
        self.band = band
        self.venue = venue
        self.all.append(self)

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str) and date != '':
            self._date = date
        else:
            raise Exception
        
    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, band):
        from classes.band import Band
        if isinstance(band, Band):
            self._band = band
        else:
            raise Exception
    
    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, venue):
        from classes.venue import Venue
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            raise Exception

    def hometown_show(self):
        if self.venue.city == self.band.hometown:
            return True
        else:
            return False
    
    def introduction(self):
        intro = f"Hello {self.venue.city}!!!!!, we are {self.band.name} and we're from {self.band.hometown}"
        return intro

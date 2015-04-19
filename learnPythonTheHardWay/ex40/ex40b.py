class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy birthday to you,",
    "You're older than in the past,",
    "But that doesn't rhyme."])
    
bulls_on_parade = Song(["They rally around the family,",
    "With pockets full of shells."])
    
happy_bday.sing()

bulls_on_parade.sing()

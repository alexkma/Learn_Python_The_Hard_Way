class Song(object):
# basically the same as this.lyrics = lyrics in Java
# self is referencing an instance of the class
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

gucci_line = ["gucci gucci impala", 3]	
gucci_lyrics = Song(gucci_line)
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

gucci_lyrics.sing_me_a_song()
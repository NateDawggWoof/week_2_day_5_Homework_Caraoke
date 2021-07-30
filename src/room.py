class Room:
    def __init__(self,room_name):
        self.room_name = room_name
        self.room_occupants = []
        self.playlist_queue = []


    def check_number_of_occupants(self):
        return len(self.room_occupants)

    def search_for_song(self,caraoke_bar,song_request):
        for song in caraoke_bar.music_librairy:
            if song_request == song.song_name:
                return True
                

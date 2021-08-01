class Room:
    def __init__(self,room_name, occupancy_limit=0):
        self.room_name = room_name
        self.occupancy_limit = occupancy_limit
        self.room_occupants = []
        self.playlist_queue = []



    def check_number_of_occupants(self):
        return len(self.room_occupants)

    def search_for_song(self,caraoke_bar,song_request):
        for song in caraoke_bar.music_librairy:
            # print(caraoke_bar.count_songs_in_music_librairy())
            if song_request.lower() == song.song_name.lower():
                return True
            else:
                return False
            

    def add_song_to_playlist_queue(self,Song):
        self.playlist_queue.append(Song)

    def remove_song_from_playlist_queue(self,Song):
        self.playlist_queue.remove(Song)

    def count_songs_in_playlist_queue(self):
        return len(self.playlist_queue)

    def check_space_availability(self):
        return self.occupancy_limit-self.check_number_of_occupants()

    def play_next_song(self):
        song = self.playlist_queue[0]
        print(f"{song.song_name} by {song.band_or_artist_name} is now playing")
        for person in self.room_occupants:
            if person.favourite_song == song:
                print(f"{person.guest_name} : {person.favourite_song_response}")
        self.remove_song_from_playlist_queue(song)


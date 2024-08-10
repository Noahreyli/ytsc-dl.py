import asyncio
import os
from sclib.asyncio import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()  

async def get_track():
    track = await api.resolve('https://soundcloud.com/casso-wav/prada')
    assert type(track) is Track
    return track


async def write_track_to_file(track, filename):
    if not os.path.exists('./track_downloads'):
        os.makedirs('./track_downloads')
    with open(filename, 'wb+') as file:
        await track.write_mp3_to(file)

track = asyncio.run(get_track())
filename = f'./track_downloads/{track.artist} - {track.title}.mp3'
asyncio.run(write_track_to_file(track, filename))

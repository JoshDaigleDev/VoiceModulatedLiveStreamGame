import threading
import time
import pyglet
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from TikTokLive.types.errors import *

class LiveSource(pyglet.event.EventDispatcher):
    def __init__(self, username):
        self.username = username
        self.client = TikTokLiveClient(unique_id=self.username)
        self.clientConnected = False

    async def on_connect(self, event: ConnectEvent):
        self.dispatch_event('on_tiktok_connect')

    async def on_comment(self, event: CommentEvent):
        print(f"{event.user.nickname}: {event.comment}")
    
    async def on_gift(self, event: GiftEvent):
        user = event.user.nickname
        gift = event.gift.info.name
        diamonds = event.gift.info.diamond_count
        eventData = {"user": user, "gift": gift, "diamonds": diamonds}
        self.dispatch_event('on_tiktok_gift', eventData)

    async def on_like(self, event: LikeEvent):
        user = event.user.nickname
        eventData = {"user": user}
        self.dispatch_event('on_tiktok_like', eventData)
    
    async def on_follow(self, event: FollowEvent):
        user = event.user.nickname
        eventData = {"user": user}
        self.dispatch_event('on_tiktok_follow', eventData)

    def start(self):
        self.client.add_listener("connect", self.on_connect)
        self.client.add_listener("comment", self.on_comment)
        self.client.add_listener("follow", self.on_follow)
        self.client.add_listener("gift", self.on_gift)
        self.client.add_listener("like", self.on_like)
        thread = threading.Thread(target=self._run_client)
        thread.daemon = True
        thread.start()

    def _run_client(self):
        while not self.clientConnected:
            try:
                self.client.run()
                self.clientConnected = True
            except LiveNotFound:
                print("Streamer Offline")
                self.client.stop()
                self.client = TikTokLiveClient(unique_id=self.username)
                time.sleep(60)

    def stop(self):
        self.client.stop()
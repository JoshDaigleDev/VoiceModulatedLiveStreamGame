import threading
from TikTokLive import TikTokLiveClient
import time
from TikTokLive.types.events import *
from TikTokLive.types.errors import *
from LiveEvent import *

class LiveSource:
    def __init__(self, username, queue):
        self.client = TikTokLiveClient(unique_id=username)
        self.clientConnected = False
        self.eventQueue = queue

    async def on_connect(self, event: ConnectEvent):
        print("Connected to Room ID:", event)

    async def on_comment(self, event: CommentEvent):
        print(f"{event.user.nickname} -> {event.comment}")
    
    async def on_gift(self, event: GiftEvent):
        print(f"{event.user.unique_id} sent \"{event.gift.info.name}\"")
        print(f"Diamonds: {event.gift.info.diamond_count}")
        print(f"Views: {self.client.viewer_count}")
        diamonds = event.gift.info.diamond_count

        self.eventQueue.push(DonationEvent(diamonds))

        # It's not type 1, which means it can't have a streak & is automatically over

    def start(self):
        @self.client.on("connect")
        async def on_connect_wrapper(event: ConnectEvent):
            await self.on_connect(event)


        @self.client.on("gift")
        async def on_gift(event: GiftEvent):
            await self.on_gift(event)

        self.client.add_listener("comment", self.on_comment)
        self.client.add_listener("gift", self.on_gift)
        thread = threading.Thread(target=self._run_client)
        thread.start()

    def _run_client(self):
        self.client.run()

    def stop(self):
        self.client.stop()
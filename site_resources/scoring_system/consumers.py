import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

# from .models import

class ScoreConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected ", event)
        await self.send({
            'type': 'websocket.accept'
        })
        await self.send({
            'type': 'websocket.send',
            'text': 'Help me'
        })


    async def websocket_receive(self, event):
        print("receive ", event)
        data = event.get('text', None)
        print(data)
        if data:
            loaded_data = json.loads(data)
            await self.send({
                'type': 'websocket.send',
                'text': loaded_data['message']
            })

    async def websocket_disconnect(self, event):
        print("disconnected ", event)

    # @database_sync_to_async
    # def get_thread(self):
    #     pass

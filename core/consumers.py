import json
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# class CoreConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

        
#         self.send(text_data=json.dumps({
#             'type': 'coneciton_established',
#             'message': 'You are now connected!'
#         }))

class CoreConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)('grupo_de_datos', self.channel_name)
        self.send(text_data=json.dumps({
            'type': 'coneciton_established',
            'message': 'You are now connected!'
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('grupo_de_datos', self.channel_name)

    def nuevos_datos(self, event):
        # Enviar el mensaje al cliente
        self.send(text_data=json.dumps(event['data']))

from .api_classes import ApiClass

#
#
#
# class TestApiCheck:
#
#     def __init__(self, url):
#         self.url = url
#
#     def CheckConnection(self):
#         response = None
#         try:
#             response = requests.get("{}/latest?limit=1".format(self.url)).json()
#
#         except Exception as error:
#             print("ERROR:\n{}".format(error))
#
#         return response

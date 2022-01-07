from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVint(ClientsManager.GetCount())
        self.writeString("Brawl Stars\n"f"Version: {player.ClientVersion}")
        self.writeVint(0)

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVint()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVint()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion
import time

from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(0) # Selected Skins

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        self.writeVInt(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(141)
        self.writeVInt(135)

        self.writeVInt(5)

        self.writeVInt(93)
        self.writeVInt(206)
        self.writeVInt(456)
        self.writeVInt(792)
        self.writeVInt(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        self.writeVInt(1) # Offers count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(6)  # ItemType
            self.writeVInt(0)
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(666)
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeInt(0)
        self.writeString("Unlock all skins")
        self.writeBoolean(False)
        self.writeString()
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 0)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 1)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 1)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 1)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(2)  # Brawlpass
        for i in range(8, 10):
            self.writeVInt(i)
            self.writeVInt(34500)
            self.writeBoolean(True)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25) # Count

        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(3) # Events

        eventIndex = 1
        for i in [5, 7, 24]:
            self.writeVInt(-1)
            self.writeVInt(eventIndex)  # EventType
            self.writeVInt(0)  # EventsBeginCountdown
            self.writeVInt(51208)  # Timer
            self.writeVInt(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVInt(-1)  # GameModeVariation
            self.writeVInt(2)  # State
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # Modifiers
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVInt(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # ChronosTextEntry
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            eventIndex += 1

        self.writeVInt(0) # Comming Events

        self.writeVInt(10)  # Brawler Upgrade Cost
        self.writeVInt(20)
        self.writeVInt(35)
        self.writeVInt(75)
        self.writeVInt(140)
        self.writeVInt(290)
        self.writeVInt(480)
        self.writeVInt(800)
        self.writeVInt(1250)
        self.writeVInt(1875)
        self.writeVInt(2800)

        self.writeVInt(4)  # Shop Coins Price
        self.writeVInt(20)
        self.writeVInt(50)
        self.writeVInt(140)
        self.writeVInt(280)

        self.writeVInt(4)  # Shop Coins Amount
        self.writeVInt(150)
        self.writeVInt(400)
        self.writeVInt(1200)
        self.writeVInt(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0)

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000036)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 0)  # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0)  # Double Token Event
        self.writeLong(31, 0)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVInt(0) # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(0) # NotificationFactory

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVInt(15)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(99999) # Club coins

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
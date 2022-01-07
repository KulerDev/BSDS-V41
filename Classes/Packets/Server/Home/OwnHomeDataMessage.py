import time
import json

from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    events = json.loads(open("events.json", 'r').read())
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

        self.writeVint(int(time.time()))
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(player.Trophies) # Trophies
        self.writeVint(player.HighestTrophies) # Highest Trophies
        self.writeVint(player.HighestTrophies)
        self.writeVint(player.TrophyRoadTier)
        self.writeVint(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVint(0)

        self.writeVint(0) # Selected Skins

        self.writeVint(0) # Randomizer Skin Selected

        self.writeVint(0) # Current Random Skin

        self.writeVint(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVint(0) # Unlocked Skin Purchase Option

        self.writeVint(0) # New Item State

        self.writeVint(0)
        self.writeVint(player.HighestTrophies)
        self.writeVint(0)
        self.writeVint(1)
        self.writeBoolean(True)
        self.writeVint(player.TokensDoubler)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(141)
        self.writeVint(135)

        self.writeVint(5)

        self.writeVint(93)
        self.writeVint(206)
        self.writeVint(456)
        self.writeVint(792)
        self.writeVint(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVint(2)  # Token Doubler New Tag State
        self.writeVint(2)  # Event Tickets New Tag State
        self.writeVint(2)  # Coin Packs New Tag State
        self.writeVint(0)  # Change Name Cost
        self.writeVint(0)  # Timer For the Next Name Change

        self.writeVint(1) # Offers count

        self.writeVint(1)  # RewardCount
        for i in range(1):
            self.writeVint(6)  # ItemType
            self.writeVint(0)
            self.writeDataReference(0)  # CsvID
            self.writeVint(0)

        self.writeVint(0)
        self.writeVint(666)
        self.writeVint(950400)
        self.writeVint(2)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(3917)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(49)
        self.writeInt(0)
        self.writeString("Unlock all skins")
        self.writeBoolean(False)
        self.writeString()
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVint(0)

        self.writeVint(player.Tokens)
        self.writeVint(-1)

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVint(19)
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

        self.writeVint(0)

        self.writeVint(2)  # Brawlpass
        for i in range(8, 10):
            self.writeVint(i)
            self.writeVint(34500)
            self.writeBoolean(True)
            self.writeVint(0)

            self.writeUInt8(2)
            self.writeUInt(4294967292)
            self.writeUInt(4294967295)
            self.writeUInt(511)
            self.writeUInt(0)

            self.writeUInt8(1)
            self.writeUInt(4294967292)
            self.writeUInt(4294967295)
            self.writeUInt(511)
            self.writeUInt(0)

        self.writeVint(0)

        self.writeBoolean(True)
        self.writeVint(0)

        self.writeBoolean(True)
        self.writeVint(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVint(0)

        self.writeVint(25) # Count

        # Event Slots IDs Array Start #
        self.writeVint(1) # Gem Grab
        self.writeVint(2) # Showdown
        self.writeVint(3) # Daily Events
        self.writeVint(4) # Team Events
        self.writeVint(5) # Duo Showndown
        self.writeVint(6) # Team Events 2
        self.writeVint(7) # Special Events(Big Game and other…)
        self.writeVint(8) # Solo Events (As well as Seasonal Events)
        self.writeVint(9) # Power Play (As well as Seasonal Events)
        self.writeVint(10) # Seasonal Events
        self.writeVint(11) # Seasonal Events 2
        self.writeVint(12) # Candidates of The Day
        self.writeVint(13) # Winner of The Day
        self.writeVint(14) # Solo Mode Power League
        self.writeVint(15) # Team Mode Power League
        self.writeVint(16) # Club League(Default Map)
        self.writeVint(17) # Club League(Power Match)
        self.writeVint(20) # Championship Challenge (Stage 1)
        self.writeVint(21) # Championship Challenge (Stage 2)
        self.writeVint(22) # Championship Challenge (Stage 3)
        self.writeVint(23) # Championship Challenge (Stage 4)
        self.writeVint(24) # Championship Challenge (Stage 5)
        self.writeVint(30) # Team Events 3?
        self.writeVint(31) # Team Events 4?
        self.writeVint(32) # Team Events 5?
        # Event Slots IDs Array End #

        events = json.loads(open("events.json", 'r').read()) # import json
        
        self.writeVint(len(events) + 5) # Events Count(5 it a ChampionShip(3 Stages) and ClubLeague(PowerMatch and Default Game Mode))
        for event in events:
              # Default Slots Start Array #
              self.writeVint(0)
              self.writeVint(events.index(event) + 1)  # EventType
              self.writeVint(event['CountdownTimer'])  # EventsBeginCountdown
              self.writeVint(event['Timer'])  # Timer
              self.writeVint(event['TokensReward'])  # tokens reward for new event
              self.writeDataReference(15, event['ID'])  # MapID
              self.writeVint(-64)  # GameModeVariation
              self.writeVint(event['Status'])  # Status
              self.writeString()
              self.writeVint(0)
              self.writeVint(0)
              self.writeVint(0)
              self.writeVint(event['Modifier'])  # Modifiers
              self.writeVint(0)
              self.writeVint(0)
              self.writeBoolean(False)  # Map Maker Map Structure Array
              self.writeVint(0)
              self.writeBoolean(False)  # Power League Data Array
              self.writeVint(0)
              self.writeVint(0)
              self.writeBoolean(False)  # ChronosTextEntry
              self.writeBoolean(False)
              self.writeBoolean(False)
              self.writeVint(-1)
              self.writeBoolean(False)
              self.writeBoolean(False)
              # Default Slots End Array #

        # Championship Challenge Slot Start Array #
        # Championship Challenge Stage 1 #
        self.writeVint(0)
        self.writeVint(20)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(51208)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 10)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(0)  # State
        self.writeString() #?
        self.writeVint(0) #?
        self.writeVint(0) #Defeates?
        self.writeVint(3) #Wins In Event Choose
        self.writeVint(0)  # Modifiers
        self.writeVint(0) #Wins
        self.writeVint(0) #???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(9) #Total Wins
        self.writeVint(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Championship Challenge Stage 2 #   
        self.writeVint(0)
        self.writeVint(21)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(51208)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 53)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(0)  # State
        self.writeString() #?
        self.writeVint(0) #?
        self.writeVint(0) #Defeates?
        self.writeVint(3) #Wins In Event Choose
        self.writeVint(0)  # Modifiers
        self.writeVint(0) #Wins
        self.writeVint(0) #???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(9) #Total Wins
        self.writeVint(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Championship Challenge Stage 3 #   
        self.writeVint(0)
        self.writeVint(22)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(51208)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 293)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(0)  # State
        self.writeString() #?
        self.writeVint(0) #?
        self.writeVint(0) #Defeates?
        self.writeVint(3) #Wins In Event Choose
        self.writeVint(0)  # Modifiers
        self.writeVint(0) #Wins
        self.writeVint(0) #???(Dont Change!)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(9) #Total Wins
        self.writeVint(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        # Championship Slots End Array #
        
        # Club League Slots Start Array #
        # Club League Default Map Array #
        self.writeVint(0)
        self.writeVint(16)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(51208)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(2)  # State
        self.writeString()
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Club League Power Match Array #
        self.writeVint(0)
        self.writeVint(17)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(51208)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(2)  # State
        self.writeString() 
        self.writeVint(0) 
        self.writeVint(0) 
        self.writeVint(0)
        self.writeVint(0)  # Modifiers
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        # Club League Slots End Array #

        self.writeVint(0) # Comming Events

        self.writeVint(10)  # Brawler Upgrade Cost
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)
        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)
        self.writeVint(1875)
        self.writeVint(2800)

        self.writeVint(4)  # Shop Coins Price
        self.writeVint(20)
        self.writeVint(50)
        self.writeVint(140)
        self.writeVint(280)

        self.writeVint(4)  # Shop Coins Amount
        self.writeVint(150)
        self.writeVint(400)
        self.writeVint(1200)
        self.writeVint(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVint(0)

        self.writeVint(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000037)  # ThemeID
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

        self.writeVint(0) # Timed Int Value Entry

        self.writeVint(0)  # Custom Event

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVint(0) # NotificationFactory

        self.writeVint(-1)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVint(15)

        self.writeVint(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVint(1)

        self.writeDataReference(5, 8)
        self.writeVint(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVint(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVint(99999) # Club coins

        self.writeVint(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["Trophies"])

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["HighestTrophies"])

        self.writeVint(0)

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["PowerPoints"])

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["PowerLevel"] - 1)

        self.writeVint(0)

        self.writeVint(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVint(brawlerInfo["State"])

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(player.Gems)  # Diamonds
        self.writeVint(player.Gems)  # Free Diamonds
        self.writeVint(player.Level)  # Player Level
        self.writeVint(100)
        self.writeVint(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVint(0)  # Battle Count
        self.writeVint(0)  # WinCount
        self.writeVint(0)  # LoseCount
        self.writeVint(0)  # WinLooseStreak
        self.writeVint(0)  # NpcWinCount
        self.writeVint(0)  # NpcLoseCount
        self.writeVint(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVint(0)

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
        # fields["SecondsUntilAccountDeletion"] = self.readVint()
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

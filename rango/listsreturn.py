import pickle


glist = ['altgonewild', 'ArtGW', 'AsiansGoneWild', 'assholegonewild', 'BDSMGW', 'BigBoobsGW', 'BigBootiesGoneWild', 'brasgonewild', 'ChangingRoom', 'couplesgonewild', 'DirtyPantiesGW', 'dykesgonewild', 'gifsgonewild', 'GirlsGoneBitcoin', 'GirlsGoneDogeCoin', 'girlskissing', 'GoneErotic', 'GoneMildInPublic', 'gonewild30plus', 'gonewildcouples', 'GoneWildGifs', 'GoneWildPetite', 'GoneWildScrubs', 'GoneWildSmokingFetish', 'gonewildtrees', 'grool', 'GroolGoneWild', 'GWbanned', 'gwchallenge', 'GWCouples', 'GWCouples4Ladies', 'gwcumsluts', 'gwpublic', 'HighheelsGW', 'kinksters_gone_wild', 'lacegonewild', 'GWNerdy', 'socksgonewild', 'Swingersgw', 'TallGoneWild', 'treesgonewild', 'UnderwearGW', 'WeddingsGoneWild', 'Workoutgonewild']
glist2 = ['altgonewild', 'ArtGW', 'AsiansGoneWild', 'assholegonewild', 'BDSMGW', 'BigBoobsGW', 'BigBootiesGoneWild', 'brasgonewild', 'ChangingRoom', 'couplesgonewild', 'DirtyPantiesGW', 'dykesgonewild', 'gifsgonewild', 'GirlsGoneBitcoin', 'GirlsGoneDogeCoin', 'girlskissing', 'GoneErotic', 'GoneMildInPublic', 'gonewild30plus', 'gonewildcouples', 'gonewildernessporn', 'gonewildflicks', 'GoneWildGifs', 'GoneWildPetite', 'GoneWildScrubs', 'GoneWildSmokingFetish', 'gonewildtrees', 'GoneWildTube', 'gonewildvideos', 'grool', 'GroolGoneWild', 'GWbanned', 'gwchallenge', 'GWCouples', 'GWCouples4Ladies', 'gwcumsluts', 'gwpublic', 'HighheelsGW', 'kinksters_gone_wild', 'lacegonewild', 'ModelsGoneMild', 'NerdyGoneWild', 'pantyselling', 'socksgonewild', 'Swingersgw', 'TallGoneWild', 'treesgonewild', 'UnderwearGW', 'WeddingsGoneWild', 'WorkgoneMild', 'Workoutgonewild', 'WouldYouFuckMyWife']
blist = ['cock', 'gaynsfw', 'gayporn', 'Gaypornpics', 'ladybonersgw', 'mangonewild']
nlist = ['195', '30dayshred', '3DS', '420_Girls', '4chan', 'AbandonedPorn', 'ableton', 'AdoptASilver', 'AdrianaLima', 'Advice', 'AdviceAnimals', 'AgedBeauty', 'agedlikefinewine', 'airsoft', 'AJJupiter', 'AlbumArtPorn', 'AlessandraAmbrosio', 'alisonangel', 'AmericanHorrorStory', 'amisexy_over30', 'amiugly', 'Anarcho_Capitalism', 'AndroidMasterRace', 'AngieVaronaLegal', 'AnimalPorn', 'Animals', 'AnimalsBeingJerks', 'animelegwear', 'Animesuggest', 'Anjelica_Ebbi', 'AnythingGoesPics', 'Aquariums', 'arielrebel', 'Art', 'AsianCuties', 'AsianGirlsWithGlasses', 'AsianHotties', 'AsianHottiesVideos', 'AsianLadyboners', 'AsianNurses', 'ask', 'Ask_Politics', 'AskGames', 'AskMen', 'AskReddit', 'askscience', 'AskWomen', 'assassinscreed', 'Assistance', 'atheism', 'AthleticGirls', 'Audi', 'AustraliaPics', 'AutoDetailing', 'Autos', 'AutumnPorn', 'Awww', 'Babes', 'babyelephants', 'backdimples', 'BadDragon', 'BaileyJay', 'BarbaraPalvin', 'batman', 'bdsm', 'BDSMpersonals', 'beachgirls', 'beagle', 'beatles', 'Beautiful', 'Beautiful_Women', 'bigdickgirl', 'bigdickproblems', 'Bikini', 'BikiniBeauties', 'bikinibridge', 'bikinis', 'bimbofetish', 'Bitcoin', 'BlackMetal', 'blacktears', 'Blonde', 'blondehairblueeyes', 'Blondes', 'blue_balls', 'BoardsOfCanadaVisuals', 'bodybuilding', 'bodypaint', 'bodyshots', 'BoltedOnBooty', 'boltedondicks', 'boltedontits', 'BonerMaterial', 'BonersInPublic', 'boobbounce', 'boobgifs', 'boobgrabs', 'Boobies', 'Boobies_Are_Awesome', 'boobjobs', 'boobland', 'boobs', 'booty', 'booty_gifs', 'boyshorts', 'braandpanties', 'braceface', 'BreastEnvy', 'BreastExpansion', 'breastplay', 'brony', 'brunette', 'brunetteass', 'BubbleButtBlackGirls', 'budapest', 'Buddhism', 'buildapc', 'buildapcforme', 'Bulges', 'burstingout', 'bustyasians', 'bustybabes', 'ButterflyWings', 'ButtsAndBareFeet', 'cakeday', 'Calligraphy', 'CamShow', 'candiceswanepoel', 'CandidFashionPolice', 'cars', 'casualiama', 'cat_girls', 'CatGifs', 'Catloaf', 'catpictures', 'cats', 'CatsInSinks', 'CelebFakes', 'celebgifs', 'CelebrityButts', 'CelebrityFeet', 'Celebs', 'chastity', 'chastitytraining', 'CheckUsOut', 'CherokeeXJ', 'Cheza2920Playground', 'chicksinhockeyjerseys', 'chickswearingchucks', 'ChicksWithGuns', 'ChicksWithWeapons', 'Chihuahua', 'chillwave', 'ChineseHotties', 'ChristianGirls', 'Christianity', 'Christy_Mack', 'chrome', 'chubby', 'chuck', 'circlejerk', 'CitiesSkylines', 'civ', 'classicrage', 'ClassicScreenBeauties', 'classywomenofcolor', 'cleavage', 'ClopClop', 'Clopsplay', 'cocklady', 'collared', 'college', 'comicbooks', 'concertposterporn', 'confessions', 'ConfusedBoners', 'consciousgrowth', 'corgi', 'corsets', 'cosplay', 'Cosplayheels', 'Cougar', 'cougars', 'CrappyDesign', 'CrazyIdeas', 'creampie', 'creepy', 'cringe', 'crochet', 'crossedlegs', 'CryptoCurrency', 'cuckoldcaptions', 'Curls', 'curlyhair', 'curvesarebeautiful', 'curvy', 'DaftPunk', 'dailymilf', 'Damnthatsinteresting', 'DaniDaniels', 'DarkAngels', 'DarwinAwards', 'dayz', 'DCcomics', 'de', 'deadpool', 'DesignPorn', 'Dexter', 'DinosaurDrawings', 'dirtykikpals', 'dirtypenpals', 'dirtyr4r', 'DirtySnapchat', 'DIY', 'dmmill', 'DnB', 'DobermanPinscher', 'doctorwho', 'dogpictures', 'DomesticGirls', 'doodles', 'Dope_As_Fuck_Cooking', 'Drama', 'Drugs', 'DrugStashes', 'drunk', 'DSLR', 'DSLs', 'duolingo', 'dvdcollection', 'easterneuropeangirls', 'Ebony', 'Ebonyasshole', 'EbonyMILF', 'education', 'electrohouse', 'Elephants', 'Eliza_cs', 'ElsaHosk', 'EmilyRatajkowski', 'emmaglover', 'emogirls', 'enf', 'Enhancement', 'environment', 'Erotica', 'eroticliterature', 'Etsy', 'eufrat', 'EuroGirls', 'everquest', 'excel', 'explainlikeimfive', 'Eyebleach', 'eyes', 'facepalm', 'FancyFollicles', 'FapDeciders', 'FapFap', 'fashion', 'fatpeoplehate', 'FayeReagan', 'feet', 'feetish', 'FemaleChubbyChasers', 'fetish', 'FetishItems', 'fffffffuuuuuuuuuuuu', 'FFSocks', 'FiftyFifty', 'Filmmakers', 'FilthyGirls', 'findareddit', 'FineLadies', 'Firearms', 'FireCrotch', 'firefly', 'firstworldanarchists', 'firstworldproblems', 'fishnets', 'FitAndNatural', 'fitgirls', 'Fitness', 'flexi', 'food', 'foodfuckers', 'FootFetish', 'FootJewelery', 'Footjob', 'foreignpolicyanalysis', 'foxes', 'FreckledGirls', 'frenchmaid', 'freshalbumart', 'freshfromtheshower', 'FuckMarryOrKill', 'funny', 'funnyvideos', 'futanari', 'futarp', 'gallifreyan', 'Games', 'gaming', 'gamingsuggestions', 'Gamingtiles', 'GarterBelts', 'gentlemanboners', 'geography', 'gfycat', 'Giantess', 'gif', 'gifs', 'GiftofGames', 'gilf', 'ginger', 'girlsgivingthefinger', 'girlsinanklesocks', 'girlsinhoodies', 'girlsinleggings', 'girlsinpantyhose', 'GirlsinPinkUndies', 'GirlsinSchoolUniforms', 'GirlsInSocks', 'GirlsinStripedSocks', 'girlsinyogapants', 'girlsinyogashorts', 'girlsontheirbacks', 'GirlsWearingVS', 'GirlswithGlasses', 'GirlsWithiPhones', 'GirlswithNeonHair', 'GirlsWithToys', 'gis', 'glitch_art', 'GlobalOffensive', 'GloriaV', 'goddesses', 'GoForGold', 'gofuckyourself', 'gonemildcurvy', 'gonewildaudio', 'GoneWildNotReviled', 'gonewildstories', 'Gore', 'Gotham', 'government', 'Gravure', 'Green', 'GTAV', 'Guerlain_Raisa', 'guns', 'gwbooks', 'haiku', 'haikugonewild', 'hairbra', 'HairyArmpits', 'HairyAssGirls', 'hairychicks', 'HamptonRoads', 'handbra', 'handinpanties', 'happygirls', 'HardBoltOns', 'hardcoreaww', 'hbogoshare', 'heavyhangers', 'helgalovekaty', 'HellenicPolytheism', 'HENTAI_GIF', 'HerPOV', 'HighHeels', 'hiking', 'hiphopheads', 'Holly_Peers', 'Homebrewing', 'honeybooboo', 'hookah', 'hooters', 'HotBlackChicks', 'hotchickswithafros', 'Hotchickswithtattoos', 'Hotness', 'Hotwife', 'house0pain', 'HouseOfCards', 'httyd', 'hugeboobs', 'Hugeboobshardcore', 'hugenaturals', 'HungryButts', 'Hunting', 'HusbandSharing', 'IAmA', 'IBTC', 'Ifyouhadtopickone', 'ifyoulikeblank', 'im14andthisisdeep', 'imaginarymaps', 'ImGoingToHellForThis', 'imgurnsfwalbums', 'IncestGifs', 'indiangirls', 'Innie', 'insertions', 'interestingasfuck', 'InternetIsBeautiful', 'inthenews', 'investing', 'ITCareerQuestions', 'iWantToFuckHer', 'IzabelGoulart', 'jacking', 'JapaneseHotties', 'JapanesePorn', 'Jeep', 'Jeepsgonewild', 'JenniferLawrence', 'JenniferLopez', 'jennyscordamaglia', 'Jenya_D', 'Jessica_Davies', 'jilling', 'jilling_under_panties', 'joeyfisher', 'Jokes', 'juicyasians', 'justneckbeardthings', 'JustOneBoob', 'justperfect', 'KatelynByrd', 'kateupton', 'KatieCrossing', 'KatyaClover', 'katyperry', 'keto', 'ketorage', 'KiDIcaruS', 'KillYourConsole', 'KimKardashianPics', 'KinkyStuff', 'knifeclub', 'KoreanHotties', 'kotor', 'kristenbell', 'KSHE', 'LaBeauteFeminine', 'labrador', 'Lacey_Banghard', 'lactation', 'LadiesInBlack', 'ladiesinblue', 'LadiesInGreen', 'LadiesInLeather', 'ladiesinred', 'LadiesInWhite', 'ladiesinyellow', 'LadyBoners', 'latexclothing', 'latinas', 'learnmath', 'learnprogramming', 'legaladvice', 'LegalTeens', 'leggings', 'legogaming', 'legs', 'legsup', 'leotards', 'lesbians', 'LetsTalkMusic', 'LetsTalkPolitics', 'LexiBelle', 'Liberal', 'lickingdick', 'LifeProTips', 'lineups', 'lingerie', 'lipbite', 'LisaAnn', 'listentothis', 'longbeach', 'lookatmydog', 'lootcrate', 'LosAngeles', 'loseit', 'LoveToWatchYouLeave', 'LSD', 'Maddox', 'MakeupAddiction', 'MakeUpFetish', 'MapPorn', 'Maria_Ozawa', 'masseffect', 'mature', 'maturemilf', 'maturepics', 'maturewoman', 'maturewomen', 'mazda', 'me_irl', 'MeanJokes', 'MechanicalKeyboards', 'Megamind', 'MelisaMendiny', 'memes', 'MensRights', 'MenWithToys', 'metacirclejerk', 'Metal', 'MetalMemes', 'metart', 'MiaMalkova', 'MiaSollis', 'MiddleEasternHotties', 'mildlyinfuriating', 'mildlyinteresting', 'MildlyStartledCats', 'milf', 'milf_nowandforever', 'milfalbum', 'MILFDreamLand', 'MILFHeaven_Matures', 'Milfie', 'Milfinstockings', 'MilfsAndHousewives', 'Military', 'minnesota', 'MissKC', 'mixes', 'Models', 'modhelp', 'MonsterHunter', 'Mooning', 'motorcycles', 'MotoX', 'MoviePosterPorn', 'movies', 'multihub', 'MURICA', 'Music', 'mycleavage', 'mylittlepony', 'MyNjoy87', 'needamod', 'newreddits', 'newreddits_nsfw', 'news', 'NewsOfTheWeird', 'nextdoorasians', 'Nina_Agdal', 'NinaAgdal', 'nintendo', 'Nipples', 'NordicWomen', 'nosleep', 'NoStupidQuestions', 'NoTorso', 'NotSafeForNature', 'nottheonion', 'nsfw', 'nsfw2', 'NSFW_China', 'NSFW_GFY', 'NSFW_HTML5', 'NSFW_Japan', 'NSFW_Korea', 'NSFW_nospam', 'nsfw_sets', 'NSFW_Snapchat', 'nsfw_videos', 'NSFW_Wallpapers', 'nsfwcomics', 'NSFWfashion', 'NSFWFunny', 'NSFWIAMA', 'nsfwnew', 'nsfwoutfits', 'nsfwshoops', 'nsfwvideos', 'NudeBeach', 'nymphsphinx', 'occupywallstreet', 'oddlysatisfying', 'ODU', 'Offensive_Wallpapers', 'OfficialNYLDY', 'offmychest', 'Oilporn', 'OkCupid', 'OldenPorn', 'OldSchoolCool', 'omegle', 'omgbeckylookathiscock', 'onions', 'onlyblondes', 'OnlyGoodPorn', 'OnlyOpaques', 'onoffcollages', 'openholes', 'Oriental', 'orlando', 'OutOfTheLoop', 'PacificHotties', 'Page3Glamour', 'palegirls', 'paleskin', 'PandR', 'panties', 'Pantyfetish', 'Pantyhosedgirls', 'Pareidolia', 'partymusic', 'patriciacaprice', 'pawg', 'pcmasterrace', 'PCpurism', 'Pee', 'peeing', 'Pegging', 'penis', 'penpals', 'pepsi_next', 'personalfinance', 'petite', 'PetiteGirls', 'petplay', 'PGWVideo', 'philosophy', 'photobomb', 'photoshopbattles', 'pic', 'picrequests', 'pics', 'PictureGame', 'piercednipples', 'PinkandBare', 'Pinup', 'Piracy', 'pitbulls', 'PKA', 'PKAGaming', 'Playboy', 'plugged', 'plumper', 'PocketPlanes', 'pokemon', 'pokies', 'POLITIC', 'PoliticalScience', 'politics', 'popping', 'porn_gifs', 'pornID', 'PornPleasure', 'PornStars', 'PowerMetal', 'preggo', 'Presenting', 'PrettyCowgirls', 'PrettyGirls', 'proghouse', 'progressive', 'progresspics', 'promotereddit', 'Psychonaut', 'PsychoticTaylorSwift', 'pugs', 'PullUp', 'punk', 'Punk_Rock', 'QuotesPorn', 'r4r', 'RachelStarr', 'rage', 'Random_Acts_Of_Pizza', 'RandomActsofCards', 'RandomActsOfFootRub', 'randomsexiness', 'rant', 'Rateme', 'ravenhaired', 'rct', 'reactiongifs', 'realasians', 'realbikinis', 'realdubstep', 'RealGirls', 'realmilf', 'realolderwomen', 'RearView', 'reddit.com', 'redditamateurvids', 'redditgetsdrawn', 'redditlogos', 'redditrequest', 'redhead', 'Redheadass', 'redheads', 'Reflections', 'reggae', 'relationship_advice', 'relationships', 'residentevil', 'RetroVideos', 'Ribcage', 'Roleplay', 'RuinedOrgasms', 'rule34', 'running', 'runwaynudity', 'Saggy', 'SaraSampaio', 'Sashagrey', 'satanism', 'SCBackstage', 'scent_of_women_feet', 'scifi', 'scotus', 'screenshots', 'secretsanta', 'seethru', 'self', 'selfpix', 'SelfshotAsians', 'sellingsocks', 'serialpodcast', 'Sexsells', 'sexting', 'SexWithDogs', 'Sexy', 'SexyButNotPorn', 'sexyfinds', 'SexyFrex', 'sexygirls', 'SexyGirlsInBoots', 'sexygirlsinjeans', 'SexyGoosebumps', 'SexyInJeans', 'SexyNurses', 'sexypantyhose', 'SexyShemales', 'sexystories', 'sexytgirls', 'shamelessplug', 'Shemales', 'shemalesinboots', 'shewantstofuck', 'SHHHHHEEEEEEEEIIIITT', 'ShinyFetish', 'shinypants', 'shittyaskscience', 'ShittyLifeProTips', 'shittyreactiongifs', 'shoejob', 'shorthairchicks', 'shorthairedhotties', 'Showerthoughts', 'sideboob', 'sideboobs', 'Sissies', 'sixwordstories', 'sizecomparison', 'SkincareAddiction', 'skinny_dipping', 'skinnyfit', 'skinnytail', 'SkinnyWithAbs', 'SkypeShows', 'SkyPorn', 'skyrimmods', 'slingbikini', 'slutsbedrunk', 'smokingfetish', 'SoBadItsGoodFilms', 'soccer', 'socialism', 'softies', 'southpark', 'spaceporn', 'spaceships', 'Spanking', 'spiderbro', 'spiritual', 'SpitRoasted', 'spotify', 'SquaredCircle', 'StaceyPoole', 'Stacked', 'StandingAsshole', 'starlets', 'StarWars', 'Steam', 'stockingmatures', 'stockings', 'stocks', 'StonerProTips', 'StreetFights', 'submittedstraight', 'submittedts', 'sugarlifestyleforum', 'SUMMERtimeheat', 'Sundresses', 'sweatermeat', 'SwingCommunity', 'tanlines', 'TanyaMityushina', 'tattoos', 'TaylorSwift', 'TaylorSwiftsLegs', 'TeaseAndDenial', 'technology', 'techsupport', 'teenagers', 'television', 'TellReddit', 'Tgirls', 'tgirlselfie', 'ThaiHotties', 'thebutton', 'TheCreatures', 'Thefappening3', 'TheFapping3_celebrity', 'thefullbush', 'THEGOLDSTANDARD', 'TheHangingBoobs', 'ThePodcastShow', 'TheSimpsons', 'TheStrain', 'TheTVShowClub', 'TheUnderboob', 'TheUnderbun', 'thewalkingdead', 'thick', 'ThickThighs', 'thighhighs', 'thong', 'thongs', 'thongsandals', 'ThriftStoreHauls', 'tickling', 'tifu', 'tight_shorts', 'tightdress', 'tightdresses', 'tights', 'TightShirts', 'TightShorts', 'tightsqueeze', 'til', 'TinyTits', 'tipofmypenis', 'tipofmytongue', 'tits', 'TitsAndAss', 'todayilearned', 'TodayIWore', 'ToeSucking', 'TOR', 'Tori_Black', 'torrents', 'TotallyStraight', 'trance', 'Transex', 'travel', 'treatemright', 'treemusic', 'trees', 'trippy', 'Trophies', 'TrueAskReddit', 'truegaming', 'tsexual', 'ttotm', 'tubetop', 'Turkey', 'TwinGirls', 'Twistys', 'Twitch', 'TwoXChromosomes', 'UHDnsfw', 'ukraine', 'Unashamed', 'underarms', 'underboob', 'Unexpected', 'unitedstatesofamerica', 'upherbutt', 'usedpanties', 'VanessaMarano', 'vaporents', 'vegan', 'vegetarian', 'Vermiculture', 'vgb', 'Victory_Girls', 'videos', 'VietnameseHotties', 'VintageBabes', 'VintageSmut', 'vinyl', 'Virginia', 'VirginiaBeach', 'VirginiaPolitics', 'voluptuous', 'VoyeurBoard', 'wallpapers', 'WarriorWomen', 'WastedGifRequests', 'WatchItForThePlot', 'waterporn', 'watersports', 'webm', 'weed', 'weightroom', 'wet', 'WetAndMessy', 'wetfetish', 'wetontheoutside', 'whaletail', 'Whatcouldgowrong', 'whatsthisplant', 'wicked_edge', 'wifeyworld', 'windows', 'woahdude', 'WoahPoon', 'WomenLookingDown', 'WomenOfColor', 'womenofcolorgifs', 'WoodNymphs', 'worldnews', 'worstof', 'WouldTotallyFuck', 'Wrasslin', 'WritingPrompts', 'WTF', 'WTFNews', 'WtSSTaDaMiT', 'xboxone', 'xPosing', 'xray', 'XXX_Animated_Gifs', 'yoga', 'YogaPants', 'ZettaiRyouiki']
ulist = ['CollegeInitiation', 'datgap', 'DatV', 'dirtykik', 'gay', 'GayKink', 'gonewildcolor', 'GoneWildPlus', 'gwcurvy', 'RedditorCum', 'ShinyPorn', 'slutwife', 'SpeculumCuties', 'ssbbw', 'wetspot', 'WheelsGoneWild', 'wifesharing', 'Wifey', 'windowshots', 'womenofcolorXXX', 'WomenOfColour']
olist = ['4orn20', '60fpsporn', 'aa_cups', 'AboveXXX', 'accidentalnudity', 'AddictedToBlackGirls', 'adultgifs', 'AerialPorn', 'Amateur', 'AmateurArchives', 'AmateurAsianGirls', 'amateurcumsluts', 'AmateurHotties', 'amateurlesbians', 'amateurs', 'AmateurWifes', 'anal', 'anal_gifs', 'analcreampiepics', 'AnalFisting', 'AnalGaping', 'analgif_nsfw', 'AnalGW', 'AnalLadies', 'AnalPorn', 'anklepanties', 'areolapeaks', 'areolas', 'AsianChicksBlackDicks', 'AsianNSFW', 'AsianPorn', 'AsianPussy', 'ass', 'AssAndBoobs', 'assgifs', 'AssholeBehindThong', 'assinthong', 'asslick', 'ballsdeepandcumming', 'BareGirls', 'Bathing', 'BBCSluts', 'BBW', 'BBWGW', 'beef_flaps', 'BeefFlaps', 'bigareolas', 'bigasses', 'BigBlackBootyGIFS', 'bigboobs', 'bigdicklovers', 'bignips', 'bigtitsmallnip', 'Bigtitssmalltits', 'blackchickswhitedicks', 'BlackGirlCunnilingus', 'BlackGirlGifs', 'BlackGirlOnOff', 'BlackGirlsGreatSlaves', 'BlackGirlsLoveAnal', 'BlackGirlsLoveFacials', 'blowbang', 'BlowJob', 'blowjob_eyes', 'BlowjobGifs', 'Blowjobs', 'blowjobsandwich', 'Bondage', 'Bottomless', 'Bottomless_Vixens', 'BrasNSFW', 'Bukkake', 'Bustyfit', 'BustyPetite', 'buttsex', 'CagedAndFucked', 'cameltoe', 'CamGirls', 'camwhores', 'celebnsfw', 'CelebPokies', 'CelebrityNipples', 'CelebrityPussy', 'celebsnaked', 'celebsunleashed', 'celebupskirts', 'cfnmfetish', 'cheerleaders', 'chickflixxx', 'ClassicXXX', 'ClassyPornstars', 'collegensfw', 'collegesluts', 'corsetsnsfw', 'CosplayBoobs', 'cosplaybutts', 'cosplaygirls', 'couplesgonewildplus', 'creampiegifs', 'creampies', 'Cuckold', 'cuckolding', 'cumcoveredfucking', 'cumfetish', 'CumFromAnal', 'CumHaters', 'CumInTheAir', 'Cumontits', 'cumshot', 'cumshots', 'cumsluts', 'CumSwap', 'cunnilingus', 'damngoodinterracial', 'deepthroat', 'dildo', 'Dildo_Gifs', 'dildos', 'dirtysmall', 'doublepenetration', 'downblouse', 'DrunkGirls', 'EthnicGirlFacials', 'Exhibitionizm', 'exposedinpublic', 'FaceFuck', 'facesitting', 'facial', 'facialcumshots', 'FacialFun', 'Facials', 'Feet_NSFW', 'fellatio', 'femalechastity', 'femalepov', 'Femdom', 'FestivalSluts', 'Fisting', 'FlashingGirls', 'forcedorgasms', 'FreeBoob', 'gag_spit', 'gape', 'gettingherselfoff', 'GirlsFinishingTheJob', 'girlsflashing', 'Gloryholes', 'GroupOfNudeGirls', 'groupsex', 'HairyPussy', 'Handjob', 'handjobs', 'HardcoreSex', 'highheelsNSFW', 'HighResNSFW', 'holdthemoan', 'homegrowntits', 'HomemadeNsfw', 'horsemaskgw', 'HugeDickTinyChick', 'interracial_porn', 'KIKSnaps', 'kinky', 'landingstrip', 'LegalTeensXXX', 'Lesbian_gifs', 'MuricaNSFW', 'nakedbabes', 'naturaltitties', 'nippleplay', 'NipsAndPits', 'nipslip', 'nopanties', 'NotADildo', 'nsfw_celebrity', 'nsfw_gifs', 'NSFW_Hardbodies', 'nsfwcelebs', 'nsfwcosplay', 'NSFWCostumes', 'nsfwhardcore', 'NudeInPublic', 'nudists', 'O_Face', 'O_Faces', 'OldSchoolCoolNSFW', 'OnAllFours', 'oneboobout', 'OneInOneOut', 'OnHerKnees', 'OralSex', 'OrgasmContractions', 'orgasmiccontractions', 'Orgasms', 'Pantiesdown', 'PantiesToTheSide', 'PantyStuffing', 'peachfuzz', 'PerfectPussies', 'PerfectPussy', 'PiercedNSFW', 'PornGifs', 'PreggoPorn', 'PUBLICNUDITY', 'PublicUpskirts', 'PussyFlashing', 'pussygape', 'PussyJuices', 'PussyMound', 'RandomActsOfBlowJob', 'RandomActsOfMuffDive', 'RandomActsOfNSFW', 'realamateurpics', 'RealPublicNudity', 'rimjob', 'selfshots', 'SexiestPetites', 'SexInFrontOfOthers', 'shavedpussies', 'SheLikesItRough', 'simps', 'SoFuckable', 'spreadeagle', 'SpreadEm', 'spreading', 'squirting', 'Strippersonthejob', 'tailplug', 'TheLandingStrip', 'TheRearPussy', 'ThickChixxx', 'Threesome', 'TittyDrop', 'Topless_Vixens', 'ToplessInJeans', 'TopsAndBottoms', 'torpedotits', 'Upskirt', 'upskirtpics', 'vagina', 'VintageCelebsNSFW', 'vintagensfw', 'vintagepornvids', 'Wardrobemalfunction', 'WeddingRingsShowing', 'WetTshirts', 'WowThisSubExistsNSFW', 'youngporn']
favorites = []








































def read_file(filename):
    lis = pickle.load(open( filename, "rb"))
    return lis

def write_file(filename, lis):

    print "running writefile"
    pickle.dump(lis, open( filename, 'wb'))












def getGlist():
    print "returning glist"
    return glist





def addToFavorites(redditor, img):
    print redditor + ' ' + img
    favs = []
    favsRedditor = []
    favs = read_file('blah.p')
    for x in favs:
        print x
        favsRedditor.append(x[0])
    if redditor not in favsRedditor:
        print "here is " + redditor + " " + img
        favs.append([redditor,img])
        print favs
    write_file("blah.p",favs)
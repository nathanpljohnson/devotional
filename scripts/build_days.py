# -*- coding: utf-8 -*-
"""Build data/days.json. Every quote here was extracted verbatim from a text in ../corpus,
or (for in-copyright authors) verified against published sources and kept short."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

WEEKS = {
    1: {"title": "The Call and the Refusal",
        "blurb": "Almost no one in Scripture who is given authority wants it. That is the first thing to notice."},
    2: {"title": "Power and What It Does to You",
        "blurb": "The corruption of a good ruler is not an event. It is a sequence, and it is gradual."},
    3: {"title": "Counsel, Dissent, and Truth-Telling",
        "blurb": "Every one of these leaders had someone who told him the truth. Some listened."},
    4: {"title": "Command, War, and Restraint",
        "blurb": "The hardest question in the use of force is not whether you can win. It is where you stop."},
    5: {"title": "The Kingdom That Isn't Yours",
        "blurb": "Exile, suffering, and the political meaning of a king who refuses to be one."},
}

D = {}


def day(n, date, week, title, ref, context, v1, v2=None):
    D[str(n)] = {"day": n, "date": date, "week": week, "weekTitle": WEEKS[week]["title"],
                 "title": title, "ref": ref, "context": context,
                 "voice1": v1, "voice2": v2,
                 "bg": f"w{week}{'a' if n % 2 else 'b'}"}


def V(text, author, work, year, note=None):
    q = {"text": text, "author": author, "work": work, "year": year}
    if note:
        q["note"] = note
    return q


# ─────────────────────────── WEEK 1 ───────────────────────────
day(1, "2026-07-25", 1, "Who Am I That I Should Go", "Exodus 3",
    "Moses is roughly eighty, forty years into exile in Midian after killing an Egyptian and fleeing "
    "Pharaoh's court. He is keeping another man's sheep. The chapter is his commissioning: God gives him a "
    "name, a mandate, and a diplomatic brief to deliver to the most powerful man in the world. Moses' first "
    "recorded response to all of it is a question about his own credentials.",
    V("No one presumes to teach an art till he has first, with intent meditation, learnt it. What rashness "
      "is it, then, for the unskilful to assume pastoral authority, since the government of souls is the art "
      "of arts! For who can be ignorant that the sores of the thoughts of men are more occult than the sores "
      "of the bowels? And yet how often do men who have no knowledge whatever of spiritual precepts fearlessly "
      "profess themselves physicians of the heart, though those who are ignorant of the effect of drugs blush "
      "to appear as physicians of the flesh!",
      "Gregory the Great", "The Book of Pastoral Rule, I.1", "c. 590"),
    V("Man is but a reed, the most feeble thing in nature; but he is a thinking reed.",
      "Blaise Pascal", "Pensées, 347", "1670"))

day(2, "2026-07-26", 1, "Send Someone Else", "Exodus 4",
    "This is the continuation of the same conversation, and it is the part usually left out. Moses raises "
    "four separate objections, God answers each one, and Moses then asks God to send somebody else anyway. "
    "The chapter ends with Aaron appointed as his mouthpiece — a concession, not a promotion.",
    V("The soul of the Priest should shine like a light beaming over the whole world. But mine has so great "
      "darkness overhanging it, because of my evil conscience, as to be always cast down and never able to "
      "look up with confidence to its Lord.",
      "John Chrysostom", "On the Priesthood, VI", "c. 390"),
    V("It is not from space that I must seek my dignity, but from the government of my thought.",
      "Blaise Pascal", "Pensées, 348", "1670"))

day(3, "2026-07-27", 1, "The Least in My Father's House", "Judges 6",
    "Israel is under Midianite occupation and hiding its harvests. Gideon is threshing wheat in a winepress "
    "to avoid detection when he is addressed as a warrior. He asks for evidence twice, destroys his father's "
    "altar at night rather than by day, and describes his clan as the weakest in Manasseh and himself as the "
    "least in his own household.",
    V("Man is but a reed, the most feeble thing in nature; but he is a thinking reed. The entire universe need "
      "not arm itself to crush him. A vapour, a drop of water suffices to kill him. But, if the universe were "
      "to crush him, man would still be more noble than that which killed him, because he knows that he dies "
      "and the advantage which the universe has over him; the universe knows nothing of this.",
      "Blaise Pascal", "Pensées, 347", "1670"))

day(4, "2026-07-28", 1, "I Am Only a Youth", "Jeremiah 1",
    "Jeremiah is commissioned around 627 BC, in the thirteenth year of Josiah, and will spend roughly forty "
    "years telling Jerusalem that it is going to fall. His objection is his age. The job description he "
    "receives is unusually specific about failure: he is told in advance that the nation will not listen.",
    V("His wish was, to have been with Abraham on the three days' journey, when he rode with sorrow before him "
      "and with Isaac at his side. His wish was, to have been present at the moment when Abraham lifted up his "
      "eyes and saw Mount Moriah afar off; to have been present at the moment when he left his asses behind "
      "and wended his way up to the mountain alone with Isaac. For the mind of this man was busy, not with the "
      "delicate conceits of the imagination, but rather with his shuddering thought.",
      "Søren Kierkegaard", "Fear and Trembling", "1843",
      "Kierkegaard is describing a man who cannot stop thinking about Abraham — his stand-in for anyone who "
      "takes a divine command literally enough to be frightened by it."))

day(5, "2026-07-29", 1, "Here Am I, Send Me", "Isaiah 6",
    "Dated to the year King Uzziah died, around 740 BC. Isaiah sees the throne room, and his reaction is not "
    "eagerness but a conviction that he is disqualified by his speech. He volunteers only after his mouth is "
    "burned clean. The commission he then accepts is, like Jeremiah's, explicitly one that will not succeed.",
    V("Trust thyself: every heart vibrates to that iron string. Accept the place the divine providence has "
      "found for you, the society of your contemporaries, the connection of events. Great men have always done "
      "so, and confided themselves childlike to the genius of their age, betraying their perception that the "
      "absolutely trustworthy was seated at their heart, working through their hands, predominating in all "
      "their being.",
      "Ralph Waldo Emerson", "Self-Reliance", "1841"))

day(6, "2026-07-30", 1, "Give Us a King", "1 Samuel 8",
    "Samuel is old, his sons are taking bribes, and the elders ask for a king so Israel can be like other "
    "nations. Samuel's warning is a list of what centralised power will cost them: conscription, taxation, "
    "requisition of land and labour. They hear the list and want the king anyway.",
    V("It has long (perhaps throughout the entire duration of British freedom) been a common form of speech, "
      "that if a good despot could be insured, despotic monarchy would be the best form of government. I look "
      "upon this as a radical and most pernicious misconception of what good government is, which, until it "
      "can be got rid of, will fatally vitiate all our speculations on government.",
      "John Stuart Mill", "Considerations on Representative Government, ch. 3", "1861"),
    V("Of all tyrannies, a tyranny sincerely exercised for the good of its victims may be the most oppressive.",
      "C. S. Lewis", "“The Humanitarian Theory of Punishment”", "1949"))

day(7, "2026-07-31", 1, "Hidden Among the Baggage", "1 Samuel 10",
    "Saul is anointed privately, then selected publicly by lot at Mizpah — and cannot be found, because he is "
    "hiding among the luggage. He is brought out, acclaimed, and goes home to farm. He says nothing about the "
    "kingdom to his own uncle. Some men despise him from the start; he lets it pass.",
    V("Scoffers of old time were too proud to be convinced; but these are too humble to be convinced. The meek "
      "do inherit the earth; but the modern sceptics are too meek even to claim their inheritance.",
      "G. K. Chesterton", "Orthodoxy, ch. 3", "1908"))

# ─────────────────────────── WEEK 2 ───────────────────────────
day(8, "2026-08-01", 2, "The Law Written Above the King", "Deuteronomy 17",
    "Centuries before Israel has a king, the law anticipates one and fences him in: no accumulating horses, "
    "no multiplying wives, no amassing silver and gold. Most striking, he must hand-copy the law himself and "
    "read it every day of his life, so that his heart is not lifted above his countrymen. The constraint is "
    "written before the office exists.",
    V("A tyrannical law, through not being according to reason, is not a law, absolutely speaking, but rather "
      "a perversion of law; and yet in so far as it is something in the nature of a law, it aims at the "
      "citizens' being good.",
      "Thomas Aquinas", "Summa Theologica, I-II, q. 92, a. 1", "c. 1270"),
    V("It is nothing else than an ordinance of reason for the common good, made by him who has care of the "
      "community, and promulgated.",
      "Thomas Aquinas", "Summa Theologica, I-II, q. 90, a. 4 — his definition of law", "c. 1270"))

day(9, "2026-08-02", 2, "The Season When Kings Go Out", "2 Samuel 11",
    "The chapter opens by noting that it was the season when kings went out to battle, and that David stayed "
    "home. What follows is adultery, an attempted cover-up, the recall of Uriah from the front, and finally "
    "orders sent by Uriah's own hand arranging his death. David never appears to hesitate. The last line "
    "records that the thing displeased the Lord.",
    V("In his article all men are divided into “ordinary” and “extraordinary.” Ordinary men have to live in "
      "submission, have no right to transgress the law, because, don't you see, they are ordinary. But "
      "extraordinary men have a right to commit any crime and to transgress the law in any way, just because "
      "they are extraordinary.",
      "Fyodor Dostoevsky", "Crime and Punishment, part III", "1866",
      "The examining magistrate Porfiry is summarising an article Raskolnikov wrote before the murder."),
    V("The line dividing good and evil cuts through the heart of every human being.",
      "Aleksandr Solzhenitsyn", "The Gulag Archipelago", "1973"))

day(10, "2026-08-03", 2, "You Are the Man", "2 Samuel 12",
    "Nathan approaches the most powerful man in Israel, who has just successfully concealed a murder, and "
    "tells him a story about a rich man stealing a poor man's lamb. David passes furious judgment on the man "
    "in the story. Nathan applies it to him in four words. The consequences announced here run through the "
    "rest of David's reign and his family.",
    V("They love truth when she enlightens, they hate her when she reproves. For since they would not be "
      "deceived, and would deceive, they love her when she discovers herself unto them, and hate her when she "
      "discovers them.",
      "Augustine", "Confessions, X.23", "c. 400"))

day(11, "2026-08-04", 2, "His Heart Was Turned Away", "1 Kings 11",
    "The wisest king in Israel's history ends up maintaining shrines to Ashtoreth, Milcom, and Molech on the "
    "hills outside Jerusalem. The text is careful about the mechanism: it happens through his marriages, "
    "gradually, when he is old. Nothing here is a single dramatic apostasy. The kingdom is torn in two as a "
    "consequence, but not in his lifetime.",
    V("We must speak also of the earthly city, which, though it be mistress of the nations, is itself ruled by "
      "its lust of rule.",
      "Augustine", "The City of God, I.1", "c. 426"))

day(12, "2026-08-05", 2, "He Forsook the Counsel of the Old", "1 Kings 12",
    "Rehoboam inherits a united kingdom and loses most of it inside a week. Asked to lighten his father's "
    "labour burdens, he consults the elders who served Solomon, rejects their advice, then consults the men "
    "he grew up with and adopts theirs. Ten tribes secede. He reigned in Jerusalem over Judah alone.",
    V("If circumspection and caution are a part of wisdom, when we work only upon inanimate matter, surely they "
      "become a part of duty too, when the subject of our demolition and construction is not brick and timber, "
      "but sentient beings, by the sudden alteration of whose state, condition, and habits, multitudes may be "
      "rendered miserable. But it seems as if it were the prevalent opinion in Paris, that an unfeeling heart "
      "and an undoubting confidence are the sole qualifications for a perfect legislator. Far different are my "
      "ideas of that high office. The true lawgiver ought to have a heart full of sensibility. He ought to love "
      "and respect his kind, and to fear himself.",
      "Edmund Burke", "Reflections on the Revolution in France", "1790"))

day(13, "2026-08-06", 2, "Driven from Among Men", "Daniel 4",
    "Unusually, this chapter is written in the first person by the king himself — a Babylonian state document "
    "recording his own humiliation. Nebuchadnezzar dreams of a felled tree, Daniel tells him what it means and "
    "urges him to change, and twelve months later, mid-boast about the city he built, he loses his mind for "
    "seven seasons. He is restored, and the account closes with his own doxology.",
    V("And it is in fact the greatest source of happiness in the condition of kings, that men try incessantly "
      "to divert them, and to procure for them all kinds of pleasures.",
      "Blaise Pascal", "Pensées, 137", "1670"),
    V("Let us leave a king all alone to reflect on himself quite at leisure, without any gratification of the "
      "senses, without any care in his mind, without society.",
      "Blaise Pascal", "Pensées, 139", "1670"))

day(14, "2026-08-07", 2, "Your Heart Is Lifted Up", "Ezekiel 28",
    "An oracle against the ruler of Tyre, the wealthiest trading power on the Levantine coast. The charge is "
    "specific: by great wisdom and by trade he increased his riches, and his heart is lifted up because of it, "
    "so that he says he is a god. The language then widens into something older and larger than one Phoenician "
    "king, which is why the chapter has been read as being about the first fall of all.",
    V("Here at least We shall be free; th' Almighty hath not built Here for his envy, will not drive us hence: "
      "Here we may reign secure; and, in my choice, To reign is worth ambition, though in Hell: Better to reign "
      "in Hell than serve in Heaven.",
      "John Milton", "Paradise Lost, I.258–263", "1667",
      "Satan, having just been thrown out of heaven, choosing sovereignty over subordination."))

# ─────────────────────────── WEEK 3 ───────────────────────────
day(15, "2026-08-08", 3, "You Will Surely Wear Away", "Exodus 18",
    "Jethro, a Midianite priest and Moses' father-in-law, watches him judge cases alone from morning to "
    "evening and tells him the arrangement is not good — he will wear himself and the people out. The remedy "
    "is a tiered judiciary: capable men over thousands, hundreds, fifties and tens, with only the hard cases "
    "escalating. The best administrative advice Moses receives comes from outside Israel.",
    V("Municipal freedom is not the fruit of human device; it is rarely created; but it is, as it were, "
      "secretly and spontaneously engendered in the midst of a semi-barbarous state of society. The constant "
      "action of the laws and the national habits, peculiar circumstances, and above all time, may consolidate "
      "it; but there is certainly no nation on the continent of Europe which has experienced its advantages. "
      "Nevertheless local assemblies of citizens constitute the strength of free nations.",
      "Alexis de Tocqueville", "Democracy in America, I.5", "1835"))

day(16, "2026-08-09", 3, "Four Hundred Against One", "1 Kings 22",
    "Ahab and Jehoshaphat want to retake Ramoth-Gilead and assemble four hundred prophets, who unanimously "
    "promise victory. Jehoshaphat asks whether there is anyone else. Micaiah is fetched from prison, sarcastically "
    "agrees with the majority, is ordered to tell the truth, and predicts disaster. He is struck, mocked, and "
    "returned to prison. Ahab goes to battle in disguise and is killed by an arrow shot at random.",
    V("If all mankind minus one, were of one opinion, and only one person were of the contrary opinion, mankind "
      "would be no more justified in silencing that one person, than he, if he had the power, would be justified "
      "in silencing mankind.",
      "John Stuart Mill", "On Liberty, ch. 2", "1859"),
    V("The abolition of plain speaking, a great affectation of humility, but banishment of truth, the suppression "
      "of convictions and reproofs… while against those who are invested with power no one dare open his lips.",
      "John Chrysostom", "On the Priesthood, III", "c. 390"))

day(17, "2026-08-10", 3, "Purposed in His Heart", "Daniel 1",
    "Daniel and three others are deported as teenagers, renamed, and enrolled in a three-year programme "
    "training them for Babylonian civil service. They comply with almost all of it — the language, the "
    "literature, the new names, the career. They draw one line, over food, and they negotiate rather than "
    "defy, proposing a ten-day trial to the official responsible. All four end up in the king's service.",
    V("For most princes apply themselves more to affairs of war than to the useful arts of peace; and in these "
      "I neither have any knowledge, nor do I much desire it; they are generally more set on acquiring new "
      "kingdoms, right or wrong, than on governing well those they possess.",
      "Thomas More", "Utopia, Book I", "1516",
      "More's Book I is an argument with himself about whether a person of conscience should take a job "
      "advising a king at all."))

day(18, "2026-08-11", 3, "For Such a Time as This", "Esther 4",
    "Haman has secured a decree to destroy the Jews throughout the Persian empire. Esther is queen but has "
    "not been summoned by the king in thirty days, and approaching him uninvited carries the death penalty. "
    "Mordecai's message is partly an appeal and partly a warning that her position will not protect her. She "
    "asks for a three-day fast and goes in. God is not mentioned anywhere in the book.",
    V("Courage is almost a contradiction in terms. It means a strong desire to live taking the form of a "
      "readiness to die. “He that will lose his life, the same shall save it,” is not a piece of mysticism for "
      "saints and heroes. It is a piece of everyday advice for sailors or mountaineers.",
      "G. K. Chesterton", "Orthodoxy, ch. 6", "1908"))

day(19, "2026-08-12", 3, "Prophesy Not Again at Bethel", "Amos 7",
    "Amos is a herdsman from Judah prophesying in the northern kingdom during a period of prosperity. "
    "Amaziah, the priest at Bethel, reports him to King Jeroboam II and then tells him to go home and earn "
    "his living elsewhere — the sanctuary is royal property. Amos replies that he is not a professional "
    "prophet and did not choose the work.",
    V("Society everywhere is in conspiracy against the manhood of every one of its members. Society is a "
      "joint-stock company, in which the members agree, for the better securing of his bread to each "
      "shareholder, to surrender the liberty and culture of the eater. The virtue in most request is "
      "conformity. Self-reliance is its aversion.",
      "Ralph Waldo Emerson", "Self-Reliance", "1841"))

day(20, "2026-08-13", 3, "I Did Not So, Because of the Fear of God", "Nehemiah 5",
    "Mid-reconstruction, Nehemiah discovers the crisis is internal: Jewish nobles are lending at interest to "
    "their own countrymen, who are mortgaging fields and selling children into slavery to buy grain. He calls "
    "an assembly, forces restitution, and makes them swear to it. He then notes that he declined the "
    "governor's food allowance for twelve years, unlike his predecessors.",
    V("Contempt of the poor, paying court to the rich, senseless and mischievous honors, favors attended with "
      "danger both to those who offer and those who accept them, sordid fear suited only to the basest of "
      "slaves.",
      "John Chrysostom", "On the Priesthood, III", "c. 390",
      "Chrysostom's list of what corrupts men who hold office."))

day(21, "2026-08-14", 3, "A Ruler Who Listens to Lies", "Proverbs 29",
    "A chapter of political maxims rather than narrative: what flattery does to a court, what happens to a "
    "land whose ruler takes bribes, why a king who listens to falsehood ends up surrounded by officials who "
    "supply it. Verse 14 makes the standard concrete — the throne is established by judging the poor "
    "faithfully.",
    V("The creed which accepts as the foundation of morals, Utility, or the Greatest Happiness Principle, holds "
      "that actions are right in proportion as they tend to promote happiness, wrong as they tend to produce "
      "the reverse of happiness.",
      "John Stuart Mill", "Utilitarianism, ch. 2", "1863",
      "Mill credits the phrase to Bentham: “the principle of utility, or as Bentham latterly called it, the "
      "greatest happiness principle.”"))

# ─────────────────────────── WEEK 4 ───────────────────────────
day(22, "2026-08-15", 4, "Be Strong and Courageous", "Joshua 1",
    "Moses is dead and Joshua inherits an unfinished campaign. The commissioning is short and repetitive: be "
    "strong and courageous, three times, alongside an instruction to keep the book of the law in his mouth "
    "day and night. The courage required is tied to a text he is not allowed to depart from.",
    V("I conclude, therefore, that, fortune being changeful and mankind steadfast in their ways, so long as the "
      "two are in agreement men are successful, but unsuccessful when they fall out.",
      "Niccolò Machiavelli", "The Prince, ch. 25", "1532"))

day(23, "2026-08-16", 4, "When You Besiege a City", "Deuteronomy 20",
    "Israel's law of war. Before a battle, whole categories of men are sent home: the newly married, the "
    "recently built, the recently planted, and anyone afraid. Cities are to be offered terms first. Fruit "
    "trees may not be cut down for siege works, on the stated grounds that a tree is not your enemy. The "
    "chapter also contains the harder provisions on the Canaanite cities, and does not soften them.",
    V("Every possible precaution requisite to spare the innocent — Especially children, women, and the aged, "
      "except they have committed atrocious acts — Clergymen, men of letters, husbandmen, merchants, prisoners "
      "— Conditional surrender not to be rejected — Delinquents when numerous to be spared — Hostages to be "
      "spared — Unnecessary effusion of blood to be avoided.",
      "Hugo Grotius", "The Rights of War and Peace, Book III — chapter summary", "1625",
      "Grotius is the origin point of modern international law. This is his own contents-summary of the "
      "chapters on restraint in victory."),
    V("Might is that which makes a thing of anybody who comes under its sway.",
      "Simone Weil", "“The Iliad, or the Poem of Force”", "1939"))

day(24, "2026-08-17", 4, "Israel Has Sinned", "Joshua 7",
    "After Jericho, a small force is routed at Ai and thirty-six men die. Joshua tears his clothes and blames "
    "God; the answer is that Israel has taken plunder that was under a ban. The search narrows by tribe, "
    "clan, household, and man, to Achan, who confesses that he saw, coveted, and hid. The punishment falls on "
    "his whole household. It is the Bible's starkest treatment of collective liability in a military unit.",
    V("Love God's people. Because we have come here and shut ourselves within these walls, we are no holier "
      "than those that are outside, but on the contrary, from the very fact of coming here, each of us has "
      "confessed to himself that he is worse than others, than all men on earth.",
      "Fyodor Dostoevsky", "The Brothers Karamazov — Father Zossima", "1880"),
    V("It was sheer thoughtlessness — something by no means identical with stupidity — that predisposed him to "
      "become one of the greatest criminals of that period.",
      "Hannah Arendt", "Eichmann in Jerusalem", "1963"))

day(25, "2026-08-18", 4, "I Will Not Stretch Out My Hand", "1 Samuel 24",
    "David is a fugitive with a price on his head, hiding in a cave at En-gedi, when Saul enters that cave "
    "alone. His men read it as providence. David cuts off a corner of Saul's robe instead, and his conscience "
    "troubles him even for that. He then calls out to Saul from a distance and makes his case in public. Saul "
    "weeps and admits David will be king.",
    V("The best kind of revenge is, not to become like unto them.",
      "Marcus Aurelius", "Meditations, VI.5", "c. 175"))

day(26, "2026-08-19", 4, "Blessed Be Your Discretion", "1 Samuel 25",
    "Nabal insults David's men after they have protected his flocks, and David sets out with four hundred "
    "armed men intending to kill every male in the household. Abigail, Nabal's wife, intercepts him on the "
    "road with provisions and an argument, and talks him out of it. David's reply credits her with keeping "
    "him from bloodshed. She acted without her husband's knowledge.",
    V("The correction of the wrongdoer is a remedy which should be employed against a man's sin. Now a man's "
      "sin may be considered in two ways, first as being harmful to the sinner, secondly as conducing to the "
      "harm of others, by hurting or scandalizing them, or by being detrimental to the common good, the "
      "justice of which is disturbed by that man's sin.",
      "Thomas Aquinas", "Summa Theologica, II-II, q. 33, a. 1", "c. 1270"))

day(27, "2026-08-20", 4, "A Prince Has Fallen This Day", "2 Samuel 3",
    "Abner, the commander who kept Saul's house in power, defects to David and begins delivering the northern "
    "tribes. Joab, David's own general, murders him at the gate of Hebron — officially for his brother's "
    "death in battle, in practice removing a rival. David cannot punish Joab. He stages a public funeral, "
    "walks behind the bier, fasts, and makes sure everyone knows the killing was not his doing.",
    V("It will have blood, they say, blood will have blood.",
      "William Shakespeare", "Macbeth, III.iv", "1606"))

day(28, "2026-08-21", 4, "Set Bread and Water Before Them", "2 Kings 6",
    "Elisha has been feeding Israel's king the Syrian army's movements. Syria sends a force to capture him; he "
    "prays, they are struck blind, and he personally leads the entire army into Samaria and into the hands of "
    "the king who has been fighting them. The king asks twice whether he should kill them. Elisha tells him to "
    "feed them and send them home. The raids stop.",
    V("“I say unto you,” is written in the Gospel, “resist not evil,” do not oppose injury with injury, but "
      "rather bear repeated injury from the evil doer. What was permitted is forbidden.",
      "Leo Tolstoy", "The Kingdom of God Is Within You", "1894"))

# ─────────────────────────── WEEK 5 ───────────────────────────
day(29, "2026-08-22", 5, "Justice for the Poor of the People", "Psalms 72",
    "A coronation prayer, attributed to or for Solomon. It asks for an enormous reign — tribute from Tarshish "
    "and Sheba, dominion from sea to sea — and it grounds the whole request in one test, stated at the "
    "beginning and repeated at the centre: that the king judge the poor with justice, save the children of "
    "the needy, and break the oppressor.",
    V("The definition of law may be gathered; and it is nothing else than an ordinance of reason for the common "
      "good, made by him who has care of the community, and promulgated.",
      "Thomas Aquinas", "Summa Theologica, I-II, q. 90, a. 4", "c. 1270"))

day(30, "2026-08-23", 5, "Seek the Peace of the City", "Jeremiah 29",
    "A letter from Jerusalem to the deportees in Babylon, written against other prophets promising a quick "
    "return. Jeremiah tells them to build houses, plant gardens, marry, have children, and pray for the "
    "welfare of the city that conquered them — because in its peace they will have peace. The exile will last "
    "seventy years. Verse 11 belongs to this letter, and to that timetable.",
    V("It is our interest that it enjoy this peace meanwhile in this life; for as long as the two cities are "
      "commingled, we also enjoy the peace of Babylon… And the prophet Jeremiah, when predicting the captivity "
      "that was to befall the ancient people of God, and giving them the divine command to go obediently to "
      "Babylonia, and thus serve their God, counselled them also to pray for Babylonia, saying, “In the peace "
      "thereof shall ye have peace,” — the temporal peace which the good and the wicked together enjoy.",
      "Augustine", "The City of God, XIX.26", "c. 426"))

day(31, "2026-08-24", 5, "The King Was Afraid", "Jeremiah 38",
    "Jerusalem is under Babylonian siege. Jeremiah is thrown into a muddy cistern for telling soldiers the "
    "city will fall; an Ethiopian court official, Ebed-melech, gets him out. Zedekiah then consults him "
    "secretly and is given a way to save the city and his own family. He admits he is afraid of what his own "
    "officials will do to him, and does nothing. Jerusalem burns.",
    V("Above all, don't lie to yourself. The man who lies to himself and listens to his own lie comes to such a "
      "pass that he cannot distinguish the truth within him, or around him, and so loses all respect for "
      "himself and for others.",
      "Fyodor Dostoevsky", "The Brothers Karamazov — Father Zossima", "1880"),
    V("Trample! It was to be trampled on by men that I was born into this world.",
      "Shūsaku Endō", "Silence", "1966"))

day(32, "2026-08-25", 5, "We Have No Need to Answer You", "Daniel 3",
    "Three senior civil servants refuse to bow to a ninety-foot golden statue at the dedication ceremony. "
    "Given a second chance by a furious king, they decline to argue their case: God can deliver them, and if "
    "he does not, they still will not bow. They are thrown in bound and walk out unbound, with a fourth "
    "figure seen in the fire. Nebuchadnezzar promotes them.",
    V("Obviously a suicide is the opposite of a martyr. A martyr is a man who cares so much for something "
      "outside him, that he forgets his own personal life. A suicide is a man who cares so little for anything "
      "outside him, that he wants to see the last of everything.",
      "G. K. Chesterton", "Orthodoxy, ch. 6", "1908"),
    V("Live not by lies.",
      "Aleksandr Solzhenitsyn", "essay title, circulated in Moscow the day of his arrest", "1974"))

day(33, "2026-08-26", 5, "No Beauty That We Should Desire Him", "Isaiah 53",
    "The fourth of Isaiah's servant songs, and the passage the New Testament quotes more than almost any "
    "other. Its subject has no advantages: no appearance worth noticing, no following, no legal protection. "
    "He is silent at his own trial. The chapter insists that this is not defeat but the mechanism — that the "
    "suffering is doing the work.",
    V("It says, on the contrary, that God is a hidden God, and that, since the corruption of nature, He has left "
      "men in a darkness from which they can escape only through Jesus Christ, without whom all communion with "
      "God is cut off.",
      "Blaise Pascal", "Pensées, 242", "1670",
      "Pascal's term for it, taken from Isaiah 45, is Deus absconditus — the hidden God."))

day(34, "2026-08-27", 5, "Not So Among You", "Mark 10",
    "James and John ask for the two best seats in the coming kingdom. The other ten are indignant, which "
    "suggests they wanted them too. Jesus does not tell them ambition is wrong; he tells them the ranking "
    "system is inverted — the Gentile rulers lord it over people, and among them it will not work that way. "
    "The chapter also contains the rich young ruler and the healing of a blind beggar who will not be "
    "silenced.",
    V("Accordingly, two cities have been formed by two loves: the earthly by the love of self, even to the "
      "contempt of God; the heavenly by the love of God, even to the contempt of self… In the one, the princes "
      "and the nations it subdues are ruled by the love of ruling; in the other, the princes and the subjects "
      "serve one another in love, the latter obeying, while the former take thought for all.",
      "Augustine", "The City of God, XIV.28", "c. 426"))

day(35, "2026-08-28", 5, "My Kingdom Is Not of This World", "John 18",
    "The arrest, Peter's denials, and two interrogations. The second is a political hearing: Pilate, who holds "
    "the power of execution in Judea, asks a prisoner whether he is a king. The answer concedes the title and "
    "relocates the jurisdiction. Pilate's reply — what is truth — is the last thing he says before going out "
    "to manage the crowd.",
    V("But Thou wouldst not deprive man of freedom and didst reject the offer, thinking, what is that freedom "
      "worth, if obedience is bought with bread?",
      "Fyodor Dostoevsky", "The Brothers Karamazov — “The Grand Inquisitor”", "1880",
      "The Inquisitor is explaining to a silent Christ why the Church was right to take back the freedom he "
      "insisted on giving people."))

out = {"weeks": {str(k): v for k, v in WEEKS.items()}, "days": D}
(ROOT / "data" / "days.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))

assert len(D) == 35, f"expected 35 days, got {len(D)}"
words = sum(len(d["context"].split()) + len(d["voice1"]["text"].split()) +
            (len(d["voice2"]["text"].split()) if d["voice2"] else 0) for d in D.values())
print(f"{len(D)} days, {words} words of quote+context -> data/days.json")
print(f"days with a second voice: {sum(1 for d in D.values() if d['voice2'])}")

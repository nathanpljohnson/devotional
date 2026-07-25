"""The 35-day plan. Single source of truth for passages, themes, and art targets."""

WEEKS = {
    1: "The Call and the Refusal",
    2: "Power and What It Does to You",
    3: "Counsel, Dissent, and Truth-Telling",
    4: "Command, War, and Restraint",
    5: "The Kingdom That Isn't Yours",
}

# day, date, week, title, passage (bible-api slug), art search terms
PLAN = [
    (1,  "2026-07-25", 1, "Who Am I That I Should Go",        "exodus+3",      ["Moses burning bush", "Moses"]),
    (2,  "2026-07-26", 1, "Send Someone Else",                 "exodus+4",      ["Moses Aaron", "Moses rod"]),
    (3,  "2026-07-27", 1, "The Least in My Father's House",    "judges+6",      ["Gideon"]),
    (4,  "2026-07-28", 1, "I Am Only a Youth",                 "jeremiah+1",    ["Jeremiah prophet"]),
    (5,  "2026-07-29", 1, "Here Am I, Send Me",                "isaiah+6",      ["Isaiah prophet vision"]),
    (6,  "2026-07-30", 1, "Give Us a King",                    "1+samuel+8",    ["Samuel prophet", "Saul king"]),
    (7,  "2026-07-31", 1, "Hidden Among the Baggage",          "1+samuel+10",   ["Saul anointed Samuel"]),

    (8,  "2026-08-01", 2, "The Law Written Above the King",    "deuteronomy+17",["Moses tablets law"]),
    (9,  "2026-08-02", 2, "The Season When Kings Go Out",      "2+samuel+11",   ["Bathsheba David"]),
    (10, "2026-08-03", 2, "You Are the Man",                   "2+samuel+12",   ["Nathan David prophet"]),
    (11, "2026-08-04", 2, "His Heart Was Turned Away",         "1+kings+11",    ["Solomon"]),
    (12, "2026-08-05", 2, "He Forsook the Counsel of the Old", "1+kings+12",    ["Rehoboam"]),
    (13, "2026-08-06", 2, "Driven from Among Men",             "daniel+4",      ["Nebuchadnezzar"]),
    (14, "2026-08-07", 2, "Your Heart Is Lifted Up",           "ezekiel+28",    ["fall of Lucifer", "pride angel"]),

    (15, "2026-08-08", 3, "You Will Surely Wear Away",         "exodus+18",     ["Moses Jethro", "Moses judging"]),
    (16, "2026-08-09", 3, "Four Hundred Against One",          "1+kings+22",    ["Micaiah prophet", "Ahab"]),
    (17, "2026-08-10", 3, "Purposed in His Heart",             "daniel+1",      ["Daniel court Babylon"]),
    (18, "2026-08-11", 3, "For Such a Time as This",           "esther+4",      ["Esther Mordecai"]),
    (19, "2026-08-12", 3, "Prophesy Not Again at Bethel",      "amos+7",        ["Amos prophet"]),
    (20, "2026-08-13", 3, "I Did Not So, Because of the Fear", "nehemiah+5",    ["Nehemiah", "rebuilding Jerusalem"]),
    (21, "2026-08-14", 3, "A Ruler Who Listens to Lies",       "proverbs+29",   ["Solomon wisdom judgment"]),

    (22, "2026-08-15", 4, "Be Strong and Courageous",          "joshua+1",      ["Joshua"]),
    (23, "2026-08-16", 4, "When You Besiege a City",           "deuteronomy+20",["siege ancient battle"]),
    (24, "2026-08-17", 4, "Israel Has Sinned",                 "joshua+7",      ["Achan", "Joshua Ai"]),
    (25, "2026-08-18", 4, "I Will Not Stretch Out My Hand",    "1+samuel+24",   ["David Saul cave"]),
    (26, "2026-08-19", 4, "Blessed Be Your Discretion",        "1+samuel+25",   ["Abigail David"]),
    (27, "2026-08-20", 4, "A Prince Has Fallen This Day",      "2+samuel+3",    ["Abner Joab", "David mourning"]),
    (28, "2026-08-21", 4, "Set Bread and Water Before Them",   "2+kings+6",     ["Elisha", "Elisha Syrians"]),

    (29, "2026-08-22", 5, "Justice for the Poor of the People","psalms+72",     ["Solomon throne", "king justice"]),
    (30, "2026-08-23", 5, "Seek the Peace of the City",        "jeremiah+29",   ["exile Babylon", "rivers of Babylon"]),
    (31, "2026-08-24", 5, "The King Was Afraid",               "jeremiah+38",   ["Jeremiah cistern", "Jeremiah prophet"]),
    (32, "2026-08-25", 5, "We Have No Need to Answer You",     "daniel+3",      ["fiery furnace", "three Hebrews"]),
    (33, "2026-08-26", 5, "No Beauty That We Should Desire",   "isaiah+53",     ["man of sorrows", "ecce homo"]),
    (34, "2026-08-27", 5, "Not So Among You",                  "mark+10",       ["Christ washing feet", "Christ disciples"]),
    (35, "2026-08-28", 5, "My Kingdom Is Not of This World",   "john+18",       ["Christ before Pilate", "ecce homo Pilate"]),
]

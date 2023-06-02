Classes = [
    'destroyer','warlord','berserker','holyknight',
    'slayer',
    'striker',
    'battlemaster', 'infighter', 'soulmaster', 'lancemaster',
    'devilhunter', 'blaster', 'hawkeye', 'scouter',
    'gunslinger',
    'bard', 'summoner', 'arcana', 'sorceress',
    'blade', 'demonic', 'reaper',
    'artist', 'aeromancer',
]

Classes_kor = {
    "전사": {
        '디스트로이어':['디트', '디붕이', '망치맨'],
        '워로드':['워붕이', '워황', '어항'],
        '버서커':[],
        '홀리나이트':[],
        
        '슬레이어':[],
        },
    "무도가": {
        '스트라이커':[],
        
        '배틀마스터':[],
        '인파이터':[],
        '기공사':[],
        '창술사':[],
    },
    "헌터": {
        '데빌헌터':[],
        '블래스터':[],
        '호크아이':[],
        '스카우터':[],
    
        '건슬링어':[],
    },
    "마법사": {
        '바드':[],
        '서머너':[],
        '아르카나':[],
        '소서리스':[],
    },
    "암살자": {
        '블레이드':[],
        '데모닉':[],
        '리퍼':[],
    },
    "스페셜리스트": {
        '도화가':[],
        '기상술사':[],
    }
}
def getClassesToList():
    names = []
    for detail in Classes_kor.values():
        names.extend(list(detail.keys()))
        for nicknames in detail.values():
            names.extend(nicknames)
    return names
    
Contents = [
    [1, "발탄", "마수군단장"],
    [2, "비아키스", "욕망군단장"],
    [4, "쿠쿠세이튼", "광기군단장"],
    [8, "아브렐슈드", "몽환군단장"],
    [16, "일리아칸", "질병군단장"],
    [32, "카양겔", ""],
    [64, "혼돈의상아탑", ""],
]
def convertToList(code):
    return [c[1] for c in Contents if code&c[0]==c[0]]


getClassesToList()
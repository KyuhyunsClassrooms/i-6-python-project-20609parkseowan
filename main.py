# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20609 박서완
# 프로젝트 주제: 메이플 헌터 (Maple Hunter)

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 예시는 "활동 추천 프로그램"입니다.
# 자신의 주제에 맞게 data를 만드세요.
#
# 현재 열의 의미:
# 0번 열: 활동 이름
# 1번 열: 필요한 시간(분)
# 2번 열: 추천 기분
# 3번 열: 활동 유형
# ------------------------------------------------------------

# 빈 공간은 0으로 채워진 12x20 격자판입니다.
map_template = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 0 (벽)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # row = 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # row = 11 (벽)
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 조작법을 알려주는 환영 메시지 출력"""
    print("=" * 70)
    print(" 🎮  Welcome to Maple Hunter (메이플 헌터) 🎮 ")
    print("=" * 70)
    print(" [조작법]  W: 위 | A: 왼쪽 | S: 아래 | D: 오른쪽 | F: 공격")
    print(" [규칙]    12x20 크기의 맵을 탐색하며 몬스터 5마리를 사냥하세요!")
    print("           맵에 떨어진 검(🗡️) 위로 이동하면 턴 소모 없이 즉시 획득합니다.")
    print("           - 기본칼: ATK +5  |  - 단검: ATK +7  |  - 카람빗: ATK +10")
    print("           - 쉬움 모드 혜택: 몬스터 처치 시 HP가 20 회복됩니다!")
    print("=" * 70)


def init_game(difficulty_choice, pattern_choice):
    """
    random 모듈을 쓰지 않고, 사용자가 선택한 난이도와 '행운의 번호(패턴)'에 따라 
    몬스터와 아이템의 배치를 조건문(if-elif)으로 결정하여 반환합니다.
    """
    # [★ 수정] 플레이어 기본 정보 (체력 100, 초기 공격력을 15로 낮춤, 12x20 맵 중앙에 배치)
    player = {
        'x': 10,      # 가로 위치 (0~19)
        'y': 6,       # 세로 위치 (0~11)
        'hp': 100,    # 현재 체력
        'max_hp': 100,# 최대 체력
        'atk': 15,    # [★ 수정] 초기 공격력 20 -> 15로 감소
        'kills': 0    # 처치한 몬스터 수
    }
    
    monsters = []
    items = []
    
    if difficulty_choice == '1':
        # 쉬움 모드: 기존 구석 배치 패턴 적용
        monsters = [
            ["슬라임", 30, 8, 3, 2, True],       
            ["리본돼지", 50, 12, 16, 2, True],    
            ["주황버섯", 70, 15, 3, 9, True],     
            ["와일드보어", 100, 20, 16, 9, True],  
            ["발록의영혼", 25, 45, 10, 2, True]    
        ]
        items = [
            ["기본칼", 5, 6, 4, True],
            ["단검", 7, 14, 4, True],
            ["카람빗", 10, 10, 9, True]
        ]
    else:
        # 어려움 모드: random 없이 사용자가 선택한 행운의 번호(pattern_choice)에 따라
        # 가로/세로 각각 3칸 축소된 구역(가로 3~16, 세로 3~8) 내부의 서로 다른 안전한 위치 세트로 배정합니다.
        
        if pattern_choice == '1':
            # 어려움 패턴 A (X자 배치 형태)
            monsters = [
                ["슬라임", 30, 8, 4, 3, True],       
                ["리본돼지", 50, 12, 15, 3, True],    
                ["주황버섯", 70, 15, 4, 8, True],     
                ["와일드보어", 100, 20, 15, 8, True],  
                ["발록의영혼", 25, 45, 9, 5, True]    
            ]
            items = [
                ["기본칼", 5, 5, 6, True],
                ["단검", 7, 13, 6, True],
                ["카람빗", 10, 10, 3, True]
            ]
        elif pattern_choice == '2':
            # 어려움 패턴 B (마름모형 배치 형태)
            monsters = [
                ["슬라임", 30, 8, 9, 3, True],       
                ["리본돼지", 50, 12, 3, 5, True],    
                ["주황버섯", 70, 15, 16, 5, True],     
                ["와일드보어", 100, 20, 9, 8, True],  
                ["발록의영혼", 25, 45, 10, 5, True]    
            ]
            items = [
                ["기본칼", 5, 6, 4, True],
                ["단검", 7, 13, 7, True],
                ["카람빗", 10, 6, 7, True]
            ]
        else:
            # 어려움 패턴 C (지그재그 및 대칭 배치 형태)
            monsters = [
                ["슬라임", 30, 8, 6, 4, True],       
                ["리본돼지", 50, 12, 13, 4, True],    
                ["주황버섯", 70, 15, 6, 7, True],     
                ["와일드보어", 100, 20, 13, 7, True],  
                ["발록의영혼", 25, 45, 10, 3, True]    
            ]
            items = [
                ["기본칼", 5, 10, 8, True],
                ["단검", 7, 4, 5, True],
                ["카람빗", 10, 15, 5, True]
            ]
            
    return player, monsters, items


def draw_screen(player, monsters, items):
    """현재 플레이어 상태바와 12x20 격자 맵을 그립니다."""
    # 1단계: 플레이어 HP 바 제작 (10칸 크기 게이지)
    hp_ratio = max(0, player['hp']) // 10
    hp_bar = "■" * hp_ratio + "□" * (10 - hp_ratio)
    
    print("\n" + "=" * 65)
    print(f" PLAYER HP: [{hp_bar}] {player['hp']}/{player['max_hp']} | ATK: {player['atk']} | 사냥: {player['kills']}/5")
    print("=" * 65)
    
    # 2단계: 빈 맵 템플릿 복사하기 (12행 20열)
    game_map = []
    for row in map_template:
        game_map.append(list(row))
        
    # 3단계: 살아있는 몬스터들의 위치를 번호(2~6)로 맵에 매핑
    for idx, monster in enumerate(monsters):
        name, hp, atk, mx, my, is_alive = monster
        if is_alive:
            game_map[my][mx] = idx + 2
            
    # 4단계: 존재하는 아이템의 위치를 번호(7~9)로 맵에 매핑 (검 기호용)
    for idx, item in enumerate(items):
        iname, iatk, ix, iy, is_exist = item
        if is_exist:
            game_map[iy][ix] = idx + 7
            
    # 5단계: 플레이어의 위치를 맵에 1로 배치
    px, py = player['x'], player['y']
    if 0 <= px < 20 and 0 <= py < 12:
        game_map[py][px] = 1
        
    # 6단계: 이중 반복문을 활용하여 화면에 시각화 (12행 20열)
    for r in range(12):
        for c in range(20):
            cell = game_map[r][c]
            if cell == 1:
                print("🧝", end="")  # 플레이어 기호
            elif cell == 2:
                print("🟢", end="")  # 슬라임
            elif cell == 3:
                print("🐷", end="")  # 리본돼지
            elif cell == 4:
                print("🍄", end="")  # 주황버섯
            elif cell == 5:
                print("🐗", end="")  # 와일드보어
            elif cell == 6:
                print("😈", end="")  # 발록의 영혼
            elif cell in [7, 8, 9]:
                print("🗡️", end="")  # 검 아이템 기호
            else:
                # 12x20 맵 벽 경계 처리
                if r == 0 or r == 11 or c == 0 or c == 19:
                    print("# ", end="")  # 테두리 벽
                else:
                    print(". ", end="")  # 빈 땅
        print() # 줄바꿈
    print("=" * 65)


def move_player(player, key, items):
    """
    WASD 키에 맞춰 플레이어를 이동시킵니다.
    이동 후, 새로운 위치에 아이템이 있다면 턴 소모 없이 즉시 획득합니다.
    """
    key = key.upper()
    next_x = player['x']
    next_y = player['y']
    
    if key == 'W':
        next_y -= 1
    elif key == 'S':
        next_y += 1
    elif key == 'A':
        next_x -= 1
    elif key == 'D':
        next_x += 1
        
    # 12x20 맵 벽 경계 조건 검사 (가로 1~18, 세로 1~10 범위 내부만 이동 허용)
    if 1 <= next_x <= 18 and 1 <= next_y <= 10:
        player['x'] = next_x
        player['y'] = next_y
        
        # 이동 후 즉시 아이템 획득 검사 (실시간 충돌 체크)
        for item in items:
            iname, iatk, ix, iy, is_exist = item
            if is_exist and next_x == ix and next_y == iy:
                # 공격력 상승 및 상태 업데이트
                player['atk'] += iatk
                item[4] = False  # 맵에서 아이템 제거
                print("\n" + "*" * 50)
                print(f"🗡️  [아이템 획득] {iname}을(를) 장착했습니다!")
                print(f"✨  공격력이 {iatk}만큼 상승했습니다! (현재 공격력: {player['atk']})")
                print("*" * 50)
    else:
        print("\n🛑 앗! 맵의 단단한 경계 벽에 막혀 움직일 수 없습니다!")


def check_battle(player, monsters, difficulty_choice):
    """
    플레이어가 F(공격)를 눌렀을 때 주변에 몬스터가 있는지 확인하고 전투를 진행합니다.
    쉬움 모드('1')인 경우 몬스터 처치 시 플레이어의 HP가 20 회복되는 조건문을 추가했습니다.
    """
    px, py = player['x'], player['y']
    battle_occurred = False
    
    for monster in monsters:
        name, hp, atk, mx, my, is_alive = monster
        
        if is_alive:
            if abs(px - mx) <= 1 and abs(py - my) <= 1:
                print(f"\n⚔️ 몬스터 [{name}] 발견! 사냥을 시작합니다!")
                
                # 1. 플레이어 선공
                hp -= player['atk']
                print(f"💥 당신의 선제 공격! [{name}]에게 {player['atk']}의 데미지를 입혔습니다.")
                
                # 몬스터 처치 판정
                if hp <= 0:
                    print(f"🎉 축하합니다! [{name}]을(를) 완벽히 처치했습니다!")
                    monster[1] = 0           
                    monster[5] = False       
                    player['kills'] += 1     
                    
                    # [성장 시스템] 공격력 상승
                    player['atk'] += 5
                    print(f"✨ 사냥의 기운을 얻어 공격력이 5 상승했습니다! (현재 공격력: {player['atk']})")
                    
                    # 쉬움 모드('1')일 경우 HP 20 회복 (최대 체력을 초과하지 않도록 보정)
                    if difficulty_choice == '1':
                        recovered_hp = min(player['hp'] + 20, player['max_hp'])
                        actual_recovery = recovered_hp - player['hp']
                        player['hp'] = recovered_hp
                        print(f"💖 [쉬움 모드 보너스] 생명의 기운이 감돌아 HP가 {actual_recovery} 회복되었습니다! (현재 HP: {player['hp']}/{player['max_hp']})")
                else:
                    # 2. 몬스터가 생존 시 반격
                    monster[1] = hp          
                    player['hp'] -= atk      
                    print(f"🛡️ [{name}]의 위협적인 반격! {atk}의 피해를 입었습니다.")
                    print(f"   ({name}의 남은 HP: {hp})")
                
                battle_occurred = True
                break
                
    if not battle_occurred:
        print("\n💨 쉭쉭! 허공에 칼을 휘둘렀습니다. (주변에 몬스터가 없습니다.)")


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
def main():
    show_intro()
    
    print("\n[ 난이도 선택 ]")
    print("1. 쉬움 모드 (제한 턴: 70턴 | 탐험하기 쉬운 구조 | 처치 시 HP 20 회복)")
    print("2. 어려움 모드 (제한 턴: 45턴 | 무작위 내부 구역 배치)")
    
    while True:
        difficulty = input("원하는 난이도 번호를 입력하세요 (1 또는 2): ").strip()
        if difficulty == '1':
            turns_limit = 70
            print("\n🟢 [쉬움 모드]가 활성화되었습니다. 여유롭게 몬스터를 사냥하세요! (제한 70턴)")
            pattern_choice = '1'  # 쉬움은 단일 패턴으로 고정
            break
        elif difficulty == '2':
            turns_limit = 45
            print("\n🔴 [어려움 모드]가 활성화되었습니다! (제한 45턴)")
            
            # random 없이 무작위 배치를 구현하기 위한 '행운의 번호' 입력 시스템
            print("\n🔮 오늘 당신의 행운의 번호는 무엇인가요?")
            print("1번 대륙 | 2번 대륙 | 3번 대륙")
            while True:
                pattern_choice = input("선택할 번호 입력 (1, 2, 3 중 하나): ").strip()
                if pattern_choice in ['1', '2', '3']:
                    print(f"\n⚡ {pattern_choice}번 대륙의 사냥터 문이 열렸습니다! 몬스터들의 위치가 재배정됩니다.")
                    break
                else:
                    print("⚠️ 잘못된 입력입니다. '1', '2', '3' 중 하나를 입력해 주세요.")
            break
        else:
            print("⚠️ 잘못된 입력입니다. '1' 또는 '2'를 입력해주세요.")
            
    # 사용자가 고른 난이도와 행운의 번호 패턴을 바탕으로 맵 정보 설정
    player, monsters, items = init_game(difficulty, pattern_choice)
            
    turn = 1
    
    # 게임 시작 후 첫 화면 출력 (아이템 정보도 함께 전달)
    draw_screen(player, monsters, items)
    
    while turn <= turns_limit and player['hp'] > 0 and player['kills'] < 5:
        print(f"\n[ 턴 {turn} / {turns_limit} ]")
        action = input("행동을 입력하세요 (WASD: 이동, F: 공격, Q: 마을귀환/종료): ").strip().upper()
        
        if action == 'Q':
            print("\n🛑 사냥을 중단하고 엘리니아 마을로 안전하게 귀환합니다.")
            break
            
        if action not in ['W', 'A', 'S', 'D', 'F']:
            print("\n⚠️ 잘못된 키를 입력하셨습니다! W, A, S, D(이동) 또는 F(공격)를 누르세요.")
            continue
            
        # 정상 행동 처리
        if action in ['W', 'A', 'S', 'D']:
            move_player(player, action, items)
        elif action == 'F':
            # 난이도 매개변수를 check_battle 함수에 함께 전달합니다.
            check_battle(player, monsters, difficulty)
            
        # 상태 반영 화면 업데이트 및 턴 증가
        draw_screen(player, monsters, items)
        turn += 1
        
    print("\n" + "=" * 65)
    print("                    GAME OVER                    ")
    print("=" * 65)
    if player['kills'] == 5:
        print("🏆 대성공! 5마리의 몬스터를 모두 사냥해 광교고의 전설이 되었습니다!")
    elif player['hp'] <= 0:
        print("☠️ 으아악! 캐릭터가 쓰러졌습니다... 마을 부활 장소로 이동합니다.")
    else:
        print("⏳ 시간 초과! 사냥터 이용 시간이 종료되어 밖으로 쫓겨났습니다.")
    print("=" * 65)


if __name__ == '__main__':
    main()
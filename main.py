# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20609 박서완
# 프로젝트 주제: 1인용 RPG 헌터게임

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
# 2. 함수 정의 영역
# ------------------------------------------------------------

def show_intro():
    """
    [함수 1] 게임 타이틀과 조작법, 룰을 콘솔 화면에 깔끔하게 출력하는 길잡이 함수입니다.
    """
    print("=" * 70)
    print(" 🎮  Welcome to Maple Hunter (메이플 헌터) 🎮 ")
    print("=" * 70)
    print(" [조작법]  W: 위 | A: 왼쪽 | S: 아래 | D: 오른쪽 | F: 공격")
    print(" [규칙]    12x20 크기의 맵을 탐색하며 각 층의 몬스터 5마리를 사냥하세요!")
    print("           총 3층까지 존재하며, 층을 올라갈 때마다 체력이 최대치로 회복됩니다.")
    print("           맵에 떨어진 검(🗡️) 위로 이동하면 턴 소모 없이 즉시 획득합니다.")
    print("           - 기본칼: ATK +5  |  - 단검: ATK +7  |  - 카람빗: ATK +10")
    print("           - 쉬움 모드 혜택: 몬스터 처치 시 HP가 20 회복됩니다!")
    print("=" * 70)


def get_pseudo_random(seed, min_val, max_val):
    """
    [함수 2 ★신규 수학 난수 생성기] 
    외부 라이브러리(random) 없이 배운 산술 연산자(*, +, %)만으로 난수를 스스로 계산하는 선형 합동법(LCG) 알고리즘 함수입니다.
    - seed: 무작위성을 부여할 기준값 (매번 계속 변화하는 값)
    - min_val, max_val: 난수를 뽑아낼 범위의 최솟값과 최댓값
    반환값: (계산된 무작위 정수값, 다음 연산에 사용될 새 seed값)
    """
    # 컴퓨터 난수 생성 공식: (seed * 소수 + 임의의수) % 매우큰소수
    next_seed = (seed * 1103515245 + 12345) % 2147483647
    
    # 구한 큰 무작위 수를 우리가 원하는 범위(min_val ~ max_val) 크기로 나누어 맞춤
    range_size = max_val - min_val + 1
    random_value = min_val + (next_seed % range_size)
    
    return random_value, next_seed


def init_game(difficulty_choice, lucky_seed, existing_player=None):
    """
    [함수 3] 게임 시작 및 다음 층 이동 시 플레이어, 몬스터, 아이템 정보를 초기화하는 함수입니다.
    - difficulty_choice: 사용자가 입력한 난이도 ('1' 쉬움, '2' 어려움)
    - lucky_seed: 무작위 배치를 연산하기 위한 사용자의 행운의 번호 기반 초기 seed값
    - existing_player: 기존의 플레이어 데이터를 유지하기 위한 매개변수
    """
    # 플레이어 시작 위치와 성장 정보 초기화
    if existing_player is None:
        player = {
            'x': 10,      # 플레이어의 초기 x좌표 (가로 열 인덱스)
            'y': 6,       # 플레이어의 초기 y좌표 (세로 행 인덱스)
            'hp': 100,    # 플레이어의 현재 체력
            'max_hp': 100,# 플레이어의 최대 체력
            'atk': 15,    # 플레이어의 초기 공격력 (15로 조정됨)
            'kills': 0    # 현재 층에서 처치한 몬스터 수
        }
    else:
        player = existing_player
        player['x'] = 10
        player['y'] = 6
        player['hp'] = player['max_hp'] # 층 클리어 시 체력 최대 회복
        player['kills'] = 0             # 층 처치수 초기화
    
    # 이미 무언가 배치되어 있어서 겹치지 말아야 할 좌표 기록용 리스트
    # 플레이어의 시작 좌표(10, 6)를 가장 먼저 등록하여 보호합니다.
    occupied_coords = [[10, 6]]
    
    # 몬스터 이름과 기본 능력치 목록
    monsters_base = [
        ["슬라임", 30, 8],       
        ["리본돼지", 50, 12],    
        ["주황버섯", 70, 15],     
        ["와일드보어", 100, 20],  
        ["발록의영혼", 25, 45]    
    ]
    
    # 검 아이템 기본 이름과 공격력 보너스 목록
    items_base = [
        ["기본칼", 5],
        ["단검", 7],
        ["카람빗", 10]
    ]
    
    monsters = []
    items = []
    current_seed = lucky_seed # 난수 공식에 활용할 시드값 준비
    
    # [조건문 분기] 쉬움 모드를 선택한 경우 ('1')
    if difficulty_choice == '1':
        # 쉬움 모드는 아이템과 몬스터가 겹치지 않고 정형화된 구석에 확정 스폰됩니다. (조작이 편함)
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
        # [★ 핵심 조건문 분기] 어려움 모드를 선택한 경우 ('2')
        # 원래 맵(12x20)보다 가로, 세로가 각각 3칸씩 작은 구역 내부에서 LCG 수학 공식으로 랜덤 스폰시킵니다!
        # 가로(x) 범위 제한: 3 ~ 16
        # 세로(y) 범위 제한: 3 ~ 8
        
        # 1단계: 몬스터 5마리 무작위 위치 생성 및 중복 차단 알고리즘
        for m_data in monsters_base:
            name, hp, atk = m_data
            while True:
                # [수학적 난수 호출] x와 y 좌표를 선형합동 수식 함수를 통해 100% 무작위로 생성
                rx, current_seed = get_pseudo_random(current_seed, 3, 16)
                ry, current_seed = get_pseudo_random(current_seed, 3, 8)
                
                # 플레이어 좌표 및 이미 생성 완료된 좌표들과 겹치는지 이중 반복 검사
                overlap = False
                for coord in occupied_coords:
                    if coord[0] == rx and coord[1] == ry:
                        overlap = True
                        break
                
                # 겹치지 않는 완전하고 안전한 위치인 경우에만 승인하고 몬스터 배치 완료
                if not overlap:
                    occupied_coords.append([rx, ry]) # 중복 금지 구역 리스트에 추가 등록
                    monsters.append([name, hp, atk, rx, ry, True])
                    break # while 루프 탈출
                    
        # 2단계: 검 아이템 3종 무작위 위치 생성 및 중복 차단 알고리즘
        for i_data in items_base:
            name, bonus = i_data
            while True:
                rx, current_seed = get_pseudo_random(current_seed, 3, 16)
                ry, current_seed = get_pseudo_random(current_seed, 3, 8)
                
                overlap = False
                for coord in occupied_coords:
                    if coord[0] == rx and coord[1] == ry:
                        overlap = True
                        break
                
                if not overlap:
                    occupied_coords.append([rx, ry])
                    items.append([name, bonus, rx, ry, True])
                    break
                    
    return player, monsters, items


def draw_screen(player, monsters, items, current_floor):
    """
    [함수 4] 현재 플레이어 상태 정보와 실시간 격자 맵 환경을 콘솔 화면에 렌더링하는 함수입니다.
    """
    # 플레이어의 남은 체력을 10칸짜리 시각 게이지로 환산합니다. (음수 방지를 위한 max 활용)
    hp_ratio = max(0, player['hp']) // 10
    hp_bar = "■" * hp_ratio + "□" * (10 - hp_ratio)
    
    # 상단 인터페이스(상태바) 출력 영역
    print("\n" + "=" * 65)
    print(f" 🏰 [ 현재 사냥터: {current_floor}층 / 3층 ]")
    print(f" PLAYER HP: [{hp_bar}] {player['hp']}/{player['max_hp']} | ATK: {player['atk']} | 층 사냥: {player['kills']}/5")
    print("=" * 65)
    
    # map_template을 온전히 보존하며 새로 그릴 가상의 빈 도화지 2차원 리스트를 생성합니다. (깊은 복사)
    game_map = []
    for row in map_template:
        game_map.append(list(row))
        
    # 살아있는 몬스터들의 좌표 정보를 가상 경기장 2차원 리스트 영역에 채워 넣습니다.
    for idx, monster in enumerate(monsters):
        name, hp, atk, mx, my, is_alive = monster
        if is_alive:
            game_map[my][mx] = idx + 2
            
    # 존재하는 아이템의 위치를 번호(7~9번)로 맵에 매핑합니다.
    for idx, item in enumerate(items):
        iname, iatk, ix, iy, is_exist = item
        if is_exist:
            game_map[iy][ix] = idx + 7
            
    # 플레이어의 위치를 격자 도화지에 배치합니다 (숫자 1 기입)
    px, py = player['x'], player['y']
    if 0 <= px < 20 and 0 <= py < 12:
        game_map[py][px] = 1
        
    # [중첩 반복문 (이중 루프)] 행 12줄, 열 20줄을 탐색하면서 숫자로 기재된 정보를 예쁜 이모지로 출력합니다.
    for r in range(12):
        for c in range(20):
            cell = game_map[r][c]
            if cell == 1:
                print("🧝", end="")  # 1번 값: 플레이어
            elif cell == 2:
                print("🟢", end="")  # 2번 값: 슬라임
            elif cell == 3:
                print("🐷", end="")  # 3번 값: 리본돼지
            elif cell == 4:
                print("🍄", end="")  # 4번 값: 주황버섯
            elif cell == 5:
                print("🐗", end="")  # 5번 값: 와일드보어
            elif cell == 6:
                print("😈", end="")  # 6번 값: 최종 보스 발록의 영혼
            elif cell in [7, 8, 9]:
                print("🗡️", end="")  # 7~9번 값: 검 아이템
            else:
                # 테두리 벽면 처리
                if r == 0 or r == 11 or c == 0 or c == 19:
                    print("# ", end="")  # 외각 테두리 돌벽
                else:
                    print(". ", end="")  # 이동 가능한 바닥
        print() # 한 행 가로줄을 전부 그렸다면 줄바꿈 처리
    print("=" * 65)


def move_player(player, key, items):
    """
    [함수 5] 사용자가 누른 방향 지시 키(W, A, S, D)를 해석해 좌표를 이동시키고 실시간 아이템을 감지합니다.
    """
    key = key.upper()
    next_x = player['x']
    next_y = player['y']
    
    if key == 'W':
        next_y -= 1  # 위쪽 세로 인덱스 감소
    elif key == 'S':
        next_y += 1  # 아래쪽 세로 인덱스 증가
    elif key == 'A':
        next_x -= 1  # 왼쪽 가로 인덱스 감소
    elif key == 'D':
        next_x += 1  # 오른쪽 가로 인덱스 증가
        
    # 맵 외곽 테두리(세로 0,11 / 가로 0,19) 충돌 방지 벽 검사
    if 1 <= next_x <= 18 and 1 <= next_y <= 10:
        player['x'] = next_x  
        player['y'] = next_y
        
        # 이동 직후, 새 좌표 자리에 검 아이템이 존재하면 턴 소모 없이 즉각 획득
        for item in items:
            iname, iatk, ix, iy, is_exist = item
            if is_exist and next_x == ix and next_y == iy:
                player['atk'] += iatk  # 공격력 합산
                item[4] = False        # 맵에서 아이템 제거
                print("\n" + "*" * 50)
                print(f"🗡️  [아이템 획득] {iname}을(를) 장착했습니다!")
                print(f"✨  공격력이 {iatk}만큼 상승했습니다! (현재 공격력: {player['atk']})")
                print("*" * 50)
    else:
        print("\n🛑 앗! 맵의 단단한 경계 벽에 막혀 움직일 수 없습니다!")


def check_battle(player, monsters, difficulty_choice):
    """
    [함수 6] 플레이어 사정거리 내에 몬스터가 존재할 때 턴제 마찰 연산을 수행하는 전투 처리부입니다.
    """
    px, py = player['x'], player['y']
    battle_occurred = False 
    
    for monster in monsters:
        name, hp, atk, mx, my, is_alive = monster
        
        if is_alive:
            # abs() 절댓값 수학 함수를 활용하여 상하좌우 및 대각선 1칸 이내 근접 타격 판정
            if abs(px - mx) <= 1 and abs(py - my) <= 1:
                print(f"\n⚔️ 몬스터 [{name}] 발견! 사냥을 시작합니다!")
                
                # 1. 플레이어 공격 연산
                hp -= player['atk']
                print(f"💥 당신의 선제 공격! [{name}]에게 {player['atk']}의 데미지를 입혔습니다.")
                
                # 몬스터 사망 판정
                if hp <= 0:
                    print(f"🎉 축하합니다! [{name}]을(를) 완벽히 처치했습니다!")
                    monster[1] = 0           
                    monster[5] = False       
                    player['kills'] += 1     # 사냥수 누적
                    
                    player['atk'] += 5 # 성장 보너스
                    print(f"✨ 사냥의 기운을 얻어 공격력이 5 상승했습니다! (현재 공격력: {player['atk']})")
                    
                    # 쉬움 모드 한정 HP 20 회복 보너스 (최대치 100을 절대 넘지 않게 예외 연산)
                    if difficulty_choice == '1':
                        recovered_hp = min(player['hp'] + 20, player['max_hp'])
                        actual_recovery = recovered_hp - player['hp'] 
                        player['hp'] = recovered_hp
                        print(f"💖 [쉬움 모드 보너스] 생명의 기운이 감돌아 HP가 {actual_recovery} 회복되었습니다! (현재 HP: {player['hp']}/{player['max_hp']})")
                else:
                    # 2. 몬스터가 생존해 있다면 반격 실행
                    monster[1] = hp          
                    player['hp'] -= atk      
                    print(f"🛡️ [{name}]의 위협적인 반격! {atk}의 피해를 입었습니다.")
                    print(f"   ({name}의 남은 HP: {hp})")
                
                battle_occurred = True 
                break # 턴제 게임이므로 한 프레임에 단 1마리만 공격 후 강제 종료
                
    if not battle_occurred:
        print("\n💨 쉭쉭! 허공에 칼을 휘둘렀습니다. (주변에 몬스터가 없습니다.)")


# ------------------------------------------------------------
# 3. 메인 제어 루프 영역 (프로그램 실행)
# ------------------------------------------------------------
def main():
    show_intro() # 오프닝 인트로 호출
    
    print("\n[ 난이도 선택 ]")
    print("1. 쉬움 모드 (제한 턴: 70턴 | 탐험하기 쉬운 구조 | 처치 시 HP 20 회복)")
    print("2. 어려움 모드 (제한 턴: 45턴 | 무작위 내부 구역 배치)")
    
    while True:
        difficulty = input("원하는 난이도 번호를 입력하세요 (1 또는 2): ").strip()
        if difficulty == '1':
            turns_limit = 70  # 쉬움 70턴 바인딩
            print("\n🟢 [쉬움 모드]가 활성화되었습니다. 여유롭게 몬스터를 사냥하세요! (제한 70턴)")
            lucky_seed = 1004 # 쉬움 모드는 시드값도 심플하게 자동 고정
            break 
        elif difficulty == '2':
            turns_limit = 45  # 어려움 45턴 바인딩
            print("\n🔴 [어려움 모드]가 활성화되었습니다! (제한 45턴)")
            break
        else:
            print("⚠️ 잘못된 입력입니다. '1' 또는 '2'를 입력해주세요.")
            
    # 탑의 단계를 제어할 변수 (1층에서 출발하여 최대 3층까지)
    current_floor = 1
    max_floors = 3
    
    # [★ 핵심 연계] 무작위 난수 생성을 촉발할 사용자 고유 입력 세팅 (어려움 모드 한정)
    if difficulty == '2':
        print(f"\n🔮 [ {current_floor}층 ] 당신의 행운의 정수를 입력해 주세요!")
        print("(어떤 숫자든 마음대로 입력하면 그 수에 반응해 몬스터의 무작위 좌표가 실시간 계산됩니다.)")
        while True:
            user_input = input("원하는 정수값 입력 (예: 1~9999): ").strip()
            # 입력받은 문자가 순수한 정수 숫자인지 판단
            if user_input.isdigit():
                lucky_seed = int(user_input) # 정수 변환하여 시드값으로 장착
                print(f"\n⚡ 입력하신 행운의 수 [{lucky_seed}]에 반응해 새로운 사냥터의 시공간이 열렸습니다!")
                break
            else:
                print("⚠️ 올바른 숫자를 입력해 주세요.")

    # [함수 호출] 입력한 난이도와 시드값을 토대로 1층의 데이터셋 빌드업
    player, monsters, items = init_game(difficulty, lucky_seed)
            
    turn = 1 
    
    # 1층 사냥터 실시간 콘솔화면 렌더링
    draw_screen(player, monsters, items, current_floor)
    
    # 플레이어가 살아있고 턴 한도 이내인 동안 매칭 루프 가동
    while turn <= turns_limit and player['hp'] > 0:
        print(f"\n[ 턴 {turn} / {turns_limit} ]")
        action = input("행동을 입력하세요 (WASD: 이동, F: 공격, Q: 마을귀환/종료): ").strip().upper()
        
        if action == 'Q':
            print("\n🛑 사냥을 중단하고 엘리니아 마을로 안전하게 귀환합니다.")
            break 
            
        if action not in ['W', 'A', 'S', 'D', 'F']:
            print("\n⚠️ 잘못된 키를 입력하셨습니다! W, A, S, D(이동) 또는 F(공격)를 누르세요.")
            continue 
            
        if action in ['W', 'A', 'S', 'D']:
            move_player(player, action, items)
        elif action == 'F':
            check_battle(player, monsters, difficulty)
            
        # [★ 핵심 층 교체 알고리즘] 현재 사냥터의 몬스터 5마리 완소 퇴치 시 승급
        if player['kills'] == 5:
            if current_floor < max_floors:
                current_floor += 1 # 층 단계 증가
                print("\n" + "🎉" * 20)
                print(f"✨ 축하합니다! {current_floor - 1}층의 모든 몬스터를 처치하여 {current_floor}층 사냥터로 진입합니다!")
                print("💖 생명력이 최대로 충전되었으며, 새로운 검 아이템과 몬스터가 무작위 재배치되었습니다!")
                print("🎉" * 20)
                
                # 어려움 모드인 경우, 각 층마다 새로운 난수 시드를 입력받아 사냥터 무작위성을 연속 갱신
                if difficulty == '2':
                    print(f"\n🔮 [ {current_floor}층 ] 새로운 층을 구성할 행운의 수를 입력하세요!")
                    while True:
                        user_input = input("정수값 입력 (예: 1~9999): ").strip()
                        if user_input.isdigit():
                            # 현재 시드를 새 입력값과 층 정보를 융합해 더 무작위적인 값으로 업데이트
                            lucky_seed = int(user_input) + current_floor * 17
                            print(f"\n⚡ 새로운 시공간의 문이 무작위로 형성되었습니다!")
                            break
                        else:
                            print("⚠️ 올바른 숫자를 입력해 주세요.")
                
                # 기존 성장한 플레이어 스탯(`player`)을 함수 인자로 전달해 성장치를 그대로 살려서 새로운 사냥터 로딩
                player, monsters, items = init_game(difficulty, lucky_seed, existing_player=player)
            else:
                # 3층의 몬스터까지 다 사냥했다면 최종 게임 완벽 클리어이므로 탈출
                break
            
        # 변동 사항 화면 업데이트 및 턴 누적
        draw_screen(player, monsters, items, current_floor)
        turn += 1
        
    print("\n" + "=" * 65)
    print("                    GAME OVER                    ")
    print("=" * 65)
    
    # 최종 결과 분석 및 성공 멘트 연산 판별
    if current_floor == max_floors and player['kills'] == 5:
        print("🏆 대성공! 3층 탑의 모든 몬스터를 완벽히 사냥해 엘리니아의 대전사가 되었습니다!")
    elif player['hp'] <= 0:
        print("☠️ 으아악! 캐릭터가 쓰러졌습니다... 마을 부활 장소로 이동합니다.")
    else:
        print("⏳ 시간 초과! 사냥터 이용 시간이 종료되어 밖으로 쫓겨났습니다.")
    print("=" * 65)


# 프로그램 표준 시작 제어 진입점
if __name__ == '__main__':
    main()
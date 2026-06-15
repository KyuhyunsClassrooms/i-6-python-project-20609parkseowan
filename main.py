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

# 1. 빈 공간을 채우고 있는 12x20 격자판 템플릿입니다. (가로 20칸, 세로 12칸)
# 세로 위치(y축)는 행(row) 인덱스 0~11로 가리키고, 가로 위치(x축)는 열(column) 인덱스 0~19로 가리킵니다.
# 테두리 구역(0번 행, 11번 행, 0번 열, 19번 열)은 맵을 화면에 그릴 때 돌벽(#) 기호로 변환됩니다.
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
    [함수 1] 게임의 흥미진진한 타이틀 로고와 턴 조작법, 룰을 콘솔 화면에 인쇄하는 함수입니다.
    """
    print("=" * 70)
    print(" 🎮  Welcome to Maple Hunter (메이플 헌터) 🎮 ")
    print("=" * 70)
    print(" [조작법]  W: 위 | A: 왼쪽 | S: 아래 | D: 오른쪽 | F: 공격")
    print(" [규칙]    12x20 크기의 맵을 탐색하며 각 층의 몬스터 5마리를 사냥하세요!")
    print("           총 3층까지 존재하며, 층을 올라갈 때마다 체력이 최대치로 회복됩니다.")
    print("           또한 새로운 층에 오르면 제한 시간(턴) 보너스가 지급됩니다!")
    print("           맵에 떨어진 검(🗡️) 위로 이동하면 턴 소모 없이 즉시 획득합니다.")
    print("           - 기본칼: ATK +5  |  - 단검: ATK +7  |  - 카람빗: ATK +10")
    print("           - 쉬움 모드 혜택: 몬스터 처치 시 HP가 20 회복됩니다!")
    print("=" * 70)


def get_pseudo_random(seed, min_val, max_val):
    """
    [함수 2 ★ 수학적 의사 난수 생성기] 
    외부 모듈(random)을 일절 쓰지 않고, 오직 우리가 배운 연산자(*, +, %)를 활용하여 난수를 구하는 함수입니다.
    - 컴퓨터 과학의 기초가 되는 '선형 합동법(LCG)' 공식을 코드로 수식화한 것입니다.
    - seed: 숫자를 매번 다르게 비틀어 주는 기준값 (사용자의 입력값을 이용해 계속 순환시킴)
    - min_val, max_val: 난수를 출력하고 싶은 범위의 최솟값과 최댓값
    반환값: (계산되어 나온 랜덤 정수, 다음 계산에서 활용할 새로운 시드값)
    """
    # 선형 합동법 공식 적용: (현재 시드 * 아주 큰 소수 + 고정값) % 메모리 최대치 소수
    next_seed = (seed * 1103515245 + 12345) % 2147483647
    
    # 구한 무지막지하게 큰 수를 우리가 원하는 최소~최대 범위 크기에 맞춰 안착시킵니다.
    range_size = max_val - min_val + 1
    random_value = min_val + (next_seed % range_size)
    
    return random_value, next_seed


def init_game(difficulty_choice, lucky_seed, existing_player=None):
    """
    [함수 3] 새로운 층이 시작되거나 첫 게임 시작 시 캐릭터 정보, 몬스터, 아이템의 좌표를 정리하는 함수입니다.
    - difficulty_choice: 사용자가 누른 난이도 ('1' 쉬움, '2' 어려움)
    - lucky_seed: 무작위 배치를 연산하기 위한 최초 기준 시드값
    - existing_player: 층을 타고 올라갈 때 기존의 누적 플레이어 스탯 정보를 연계해 줄 변수 (기본값 None)
    """
    # 플레이어 사전 데이터 설정 (최초 1회 생성)
    if existing_player is None:
        player = {
            'x': 10,      # 플레이어의 초기 x좌표 (12x20 격자의 정중앙 부근)
            'y': 6,       # 플레이어의 초기 y좌표
            'hp': 100,    # 플레이어의 현재 체력
            'max_hp': 100,# 플레이어의 최대 체력 상한선
            'atk': 15,    # 플레이어의 기본 공격력 (아이템이 중요하도록 15로 낮춤)
            'kills': 0    # 현재 층에서 처치 완료한 몬스터 카운트
        }
    else:
        # 기존 스탯 정보가 있다면(2층, 3층 승급 시), 성장한 공격력 등은 그대로 유지합니다.
        player = existing_player
        player['x'] = 10              # 새로운 격자 맵 정중앙으로 좌표 리셋
        player['y'] = 6
        player['hp'] = player['max_hp'] # 다음 층 진급 보상으로 체력 가득 회복!
        player['kills'] = 0             # 다음 층 사냥 수 초기화
    
    # 맵에 배치될 요소들이 서로 겹치는 현상을 방지하기 위해 등록할 금지 좌표 구역입니다.
    # 플레이어의 대기 구역인 (10, 6)을 제일 먼저 등록하여 몬스터와 겹침을 방지합니다.
    occupied_coords = [[10, 6]]
    
    # 사냥탑에 배정될 5종류의 몬스터 능력치 기본 리스트
    monsters_base = [
        ["슬라임", 30, 8],       
        ["리본돼지", 50, 12],    
        ["주황버섯", 70, 15],     
        ["와일드보어", 100, 20],  
        ["발록의영혼", 25, 45]    
    ]
    
    # 사냥터에 숨어 있을 검 아이템의 기본 상승치 목록
    items_base = [
        ["기본칼", 5],
        ["단검", 7],
        ["카람빗", 10]
    ]
    
    monsters = []
    items = []
    current_seed = lucky_seed # 연산에 활발히 쓸 시드값 사본 저장
    
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
        # 원래 맵(12x20)보다 가로, 세로가 각각 3칸씩 좁혀진 안전 구역 범위 내에서 랜덤하게 생성시킵니다!
        # 가로(x) 생성 영역: 3 ~ 16 (돌벽 테두리로부터 3칸씩 떨어진 안전 지대)
        # 세로(y) 생성 영역: 3 ~ 8  (돌벽 테두리로부터 3칸씩 떨어진 안전 지대)
        
        # 1단계: 몬스터 5마리 무작위 위치 생성 및 겹침 방지 조건문 적용
        for m_data in monsters_base:
            name, hp, atk = m_data
            while True:
                # [수학적 난수 호출] 우리의 get_pseudo_random 함수를 실행하여 가로 및 세로의 임의 무작위 수를 산출함
                rx, current_seed = get_pseudo_random(current_seed, 3, 16)
                ry, current_seed = get_pseudo_random(current_seed, 3, 8)
                
                # 플레이어 및 먼저 스폰된 몬스터들과의 좌표 일치 여부를 순회하며 실시간 비교
                overlap = False
                for coord in occupied_coords:
                    if coord[0] == rx and coord[1] == ry:
                        overlap = True # 겹침 발생 감지
                        break
                
                # 겹치지 않는 온전히 안전한 무작위 좌표인 경우에만 몬스터 확정 배정 후 루프 격파
                if not overlap:
                    occupied_coords.append([rx, ry]) # 이 좌표를 다음 생성 방지 리스트에 즉시 추가
                    monsters.append([name, hp, atk, rx, ry, True]) # 생존 상태 True로 리스트 탑재
                    break 
                    
        # 2단계: 검 아이템 3종 무작위 위치 생성 및 겹침 방지 알고리즘 적용
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
                    items.append([name, bonus, rx, ry, True]) # 존재 여부 True로 리스트 추가
                    break
                    
    # 생성 완료된 캐릭터 사전, 몬스터 리스트, 아이템 리스트를 튜플 형태로 반환합니다.
    return player, monsters, items


def draw_screen(player, monsters, items, current_floor):
    """
    [함수 4] 현재 사냥 탑의 층수, 캐릭터 체력 상태 게이지바, 그리고 격자 맵 그래픽을 실시간으로 그려주는 함수입니다.
    """
    # 플레이어 체력 백분율 계산 및 10칸 게이지 바 설계 (체력이 음수가 되어 에러가 나지 않게 max()로 방어)
    hp_ratio = max(0, player['hp']) // 10
    hp_bar = "■" * hp_ratio + "□" * (10 - hp_ratio)
    
    # 화면 상단 인터페이스(상태창) 인쇄 영역
    print("\n" + "=" * 65)
    print(f" 🏰 [ 현재 사냥터: {current_floor}층 / 3층 ]")
    print(f" PLAYER HP: [{hp_bar}] {player['hp']}/{player['max_hp']} | ATK: {player['atk']} | 층 사냥: {player['kills']}/5")
    print("=" * 65)
    
    # 2차원 리스트 복사 알고리즘 (얕은 복사로 원본 격자판이 파괴되지 않게 수동으로 줄 하나씩 복사하는 깊은 복사 기법 구현)
    game_map = []
    for row in map_template:
        game_map.append(list(row)) # 1차원 줄을 새 객체로 쪼개 가상 격자 지도 리스트에 하나씩 탑재
        
    # 살아 있는 몬스터 정보를 가상 경기장 2차원 리스트 지도 상에 매핑 (식별 번호는 idx + 2)
    for idx, monster in enumerate(monsters):
        name, hp, atk, mx, my, is_alive = monster
        if is_alive:
            game_map[my][mx] = idx + 2
            
    # 존재하는 검 아이템 정보를 가상 경기장 2차원 리스트 지도 상에 매핑 (식별 번호는 idx + 7)
    for idx, item in enumerate(items):
        iname, iatk, ix, iy, is_exist = item
        if is_exist:
            game_map[iy][ix] = idx + 7
            
    # 플레이어의 실시간 현재 위치를 가장 최우선적으로 덮어 씌워 격자에 1 대입
    px, py = player['x'], player['y']
    if 0 <= px < 20 and 0 <= py < 12:
        game_map[py][px] = 1
        
    # [중첩 반복문 (이중 루프)] 행 12줄, 열 20줄을 탐색하면서 숫자로 기재된 정보를 예쁜 이모지 및 텍스트로 치환하여 인쇄합니다.
    for r in range(12):
        for c in range(20):
            cell = game_map[r][c]
            if cell == 1:
                print("🧝", end="")  # 1번: 플레이어 용사 캐릭터
            elif cell == 2:
                print("🟢", end="")  # 2번: 슬라임
            elif cell == 3:
                print("🐷", end="")  # 3번: 리본돼지
            elif cell == 4:
                print("🍄", end="")  # 4번: 주황버섯
            elif cell == 5:
                print("🐗", end="")  # 5번: 와일드보어
            elif cell == 6:
                print("😈", end="")  # 6번: 보스 발록의 영혼
            elif cell in [7, 8, 9]:
                print("🗡️", end="")  # 7~9번: 검 아이템
            else:
                # 돌벽 테두리 영역 검출 조건문
                if r == 0 or r == 11 or c == 0 or c == 19:
                    print("# ", end="")  # 경기장 경계 돌벽
                else:
                    print(". ", end="")  # 이동 가능한 바닥
        print() # 한 행 가로줄을 전부 그렸다면 줄바꿈 처리
    print("=" * 65)


def move_player(player, key, items):
    """
    [함수 5] 사용자가 누른 방향 지시 키(WASD)를 실제 격자 좌표 이동으로 반영하고, 테두리 충돌 및 실시간 검 습득을 연산하는 함수입니다.
    """
    key = key.upper() # 대소문자 혼동을 막기 위해 모든 알파벳 조작어를 강제 대문자화함
    next_x = player['x']
    next_y = player['y']
    
    # 조작 키에 맞는 좌표 증감 임시 계산
    if key == 'W':
        next_y -= 1  # 위로 가려면 세로 인덱스 차감
    elif key == 'S':
        next_y += 1  # 아래로 가려면 세로 인덱스 누적
    elif key == 'A':
        next_x -= 1  # 왼쪽으로 가려면 가로 인덱스 차감
    elif key == 'D':
        next_x += 1  # 오른쪽으로 가려면 가로 인덱스 누적
        
    # 테두리 돌벽 충돌 방지 구역 검사 (오직 내부 안전 범위인 가로 1~18, 세로 1~10 범위 내에서만 작동하게 제한함)
    if 1 <= next_x <= 18 and 1 <= next_y <= 10:
        player['x'] = next_x  # 승인 완료되었으므로 플레이어 사전 데이터에 실제 좌표 이입
        player['y'] = next_y
        
        # [실시간 무필드 턴 줍기] 이동 직후, 발밑에 떨어진 검 아이템이 존재하고 밟았는지를 실시간 순회 비교 감지
        for item in items:
            iname, iatk, ix, iy, is_exist = item
            if is_exist and next_x == ix and next_y == iy:
                player['atk'] += iatk  # 공격력 스탯 즉시 영구 누적 합산!
                item[4] = False        # 필드 지도 정보에서 아이템 존재 상태값을 영구 제거(False)
                print("\n" + "*" * 50)
                print(f"🗡️  [아이템 획득] {iname}을(를) 장착했습니다!")
                print(f"✨  공격력이 {iatk}만큼 상승했습니다! (현재 공격력: {player['atk']})")
                print("*" * 50)
    else:
        # 단단한 맵 경계벽에 부딪힌 경우 알림 발생 및 이동 변동 연산 원천 기각 취소
        print("\n🛑 앗! 맵의 단단한 경계 벽에 막혀 움직일 수 없습니다!")


def check_battle(player, monsters, difficulty_choice):
    """
    [함수 6] 영웅이 F(공격)를 눌렀을 때 사정거리 내 몬스터 마찰 검사 및 상호 데미지 삭감 처리를 담당하는 핵심 전투부입니다.
    """
    px, py = player['x'], player['y']
    battle_occurred = False # 유효 범위 내 몬스터 존재 여부 체크용 추적 판별 변수
    
    # 5마리의 몬스터 전체 목록을 리스트 순회 비교 대조
    for monster in monsters:
        name, hp, atk, mx, my, is_alive = monster
        
        # 살아 있는 몬스터인 경우에만 거리 계산 상호 연산
        if is_alive:
            # abs() 절댓값 수학 내장 함수를 통하여 인접한 상하좌우 및 대각선 1칸 구역 사정거리를 완벽하게 판정해 냅니다.
            if abs(px - mx) <= 1 and abs(py - my) <= 1:
                print(f"\n⚔️ 몬스터 [{name}] 발견! 사냥을 시작합니다!")
                
                # 1. 용사 선제 타격 연산
                hp -= player['atk']
                print(f"💥 당신의 선제 공격! [{name}]에게 {player['atk']}의 데미지를 입혔습니다.")
                
                # 타격 맞은 대상 몬스터의 남은 생명력 사망 검사
                if hp <= 0:
                    print(f"🎉 축하합니다! [{name}]을(를) 완벽히 처치했습니다!")
                    monster[1] = 0           # 몬스터 체력 0으로 하드 가드
                    monster[5] = False       # 몬스터의 상태 사망(False) 처리로 격자 맵에서 일소 제거
                    player['kills'] += 1     # 사냥수 추가 누적
                    
                    # [사냥 보너스] 몬스터 처치 성공 시 영웅의 공격력 상승 스탯 보너스 부여
                    player['atk'] += 5
                    print(f"✨ 사냥의 기운을 얻어 공격력이 5 상승했습니다! (현재 공격력: {player['atk']})")
                    
                    # [★ 조건문 분기] 쉬움 난이도('1')일 때만 체력 회복 혜택 작동
                    if difficulty_choice == '1':
                        # 최대 체력을 초과하지 않는 정밀 연산을 위해 min() 함수를 사용합니다.
                        # min(현재체력 + 20, 최대체력인 100)을 적용하면 체력이 100 한계점을 절대 뚫고 오버플로우 되지 않습니다.
                        recovered_hp = min(player['hp'] + 20, player['max_hp'])
                        actual_recovery = recovered_hp - player['hp'] 
                        player['hp'] = recovered_hp
                        print(f"💖 [쉬움 모드 보너스] 생명의 기운이 감돌아 HP가 {actual_recovery} 회복되었습니다! (현재 HP: {player['hp']}/{player['max_hp']})")
                else:
                    # 2. 몬스터 역습 및 피해 연산
                    monster[1] = hp          # 차감된 체력을 몬스터 사전 리스트에 최신 덮어씌우기
                    player['hp'] -= atk      # 용사의 생명력을 몬스터의 공격 강도 수치만큼 감산 처리
                    print(f"🛡️ [{name}]의 위협적인 반격! {atk}의 피해를 입었습니다.")
                    print(f"   ({name}의 남은 HP: {hp})")
                
                battle_occurred = True # 상호작용 성공 상태 기록
                break # 턴제 대항이므로 단 일격을 교환한 뒤 루프 즉각 탈출 제어
                
    # 맵 내부 사정거리 구역에 어떤 적도 발견하지 못해 허탕을 친 예외 상황 메시지 처리
    if not battle_occurred:
        print("\n💨 쉭쉭! 허공에 칼을 휘둘렀습니다. (주변에 몬스터가 없습니다.)")


# ------------------------------------------------------------
# 3. 프로그램 시작 진입점 제어부 (메인 주 루프 실행)
# ------------------------------------------------------------
def main():
    show_intro() # 오프닝 로고 인쇄 호출
    
    print("\n[ 난이도 선택 ]")
    print("1. 쉬움 모드 (제한 턴: 70턴 | 무작위 스폰 구조 | 처치 시 HP 20 회복)")
    print("2. 어려움 모드 (제한 턴: 45턴 | 무작위 스폰 구조 | 몬스터 공격력 원본 적용)")
    
    # [입력 방어 에러 핸들링 무한 루프] 정상적인 1번 또는 2번 숫자를 유저가 칠 때까지 반복 유도
    while True:
        difficulty = input("원하는 난이도 번호를 입력하세요 (1 또는 2): ").strip()
        if difficulty == '1':
            turns_limit = 70  # 쉬움 70턴 한계선 설정
            print("\n🟢 [쉬움 모드]가 활성화되었습니다. 여유롭게 몬스터를 사냥하세요! (제한 70턴)")
            lucky_seed = 1004 # 쉬움 모드는 시드값도 심플하게 자동 고정
            break 
        elif difficulty == '2':
            turns_limit = 45  # 어려움 45턴 한계선 바인딩
            print("\n🔴 [어려움 모드]가 활성화되었습니다! (제한 45턴)")
            break
        else:
            print("⚠️ 잘못된 입력입니다. '1' 또는 '2'를 입력해주세요.")
            
    # 탑의 진행 단계를 연산할 제어 인덱스 변수 (1층에서 출발하여 최대 3층까지 제공)
    current_floor = 1
    max_floors = 3
    
    # [★ 무작위 수학 난수 시드값 유도 입력 영역]
    # 이제 쉬움 모드와 어려움 모드 모두 1층부터 나만의 정수를 시드로 대입받아 실시간 무작위 계산을 처리합니다!
    if difficulty == '2':
        print(f"\n🔮 [ {current_floor}층 ] 당신의 행운의 정수를 입력해 주세요!")
        print("(어떤 숫자든 마음대로 입력하면 그 수에 반응해 몬스터와 아이템의 무작위 좌표가 실시간 계산됩니다.)")
        while True:
            user_input = input("원하는 정수값 입력 (예: 1~9999): ").strip()
            # 입력받은 문자가 순수한 정수 숫자로만 구성된 문자가 맞는지 점검
            if user_input.isdigit():
                lucky_seed = int(user_input) # 형 변환하여 무작위 공식의 시드로 사용하고자 대입
                print(f"\n⚡ 입력하신 행운의 수 [{lucky_seed}]에 반응해 새로운 사냥터의 시공간이 열렸습니다!")
                break
            else:
                print("⚠️ 올바른 숫자를 입력해 주세요.")

    # [함수 호출] 입력받은 사양을 총합 산출하여 캐릭터, 사냥꾼 맵 요소 빌드업
    player, monsters, items = init_game(difficulty, lucky_seed)
            
    turn = 1 # 턴 가중 카운팅 시작
    
    # 첫 사냥터 격자 실시간 렌더링 화면 첫 출력 호출
    draw_screen(player, monsters, items, current_floor)
    
    # [용사 행동 반복 제어 루프] 용사가 생존해 있고 제한 턴수를 초과하지 않는 동안 게임 작동
    while turn <= turns_limit and player['hp'] > 0:
        print(f"\n[ 턴 {turn} / {turns_limit} ]")
        action = input("행동을 입력하세요 (WASD: 이동, F: 공격, Q: 마을귀환/종료): ").strip().upper()
        
        # 기권 및 중간 세션 저장 종료 처리
        if action == 'Q':
            print("\n🛑 사냥을 중단하고 엘리니아 마을로 안전하게 귀환합니다.")
            break 
            
        # 조작 단어 오류 필터링 가드 조건문
        if action not in ['W', 'A', 'S', 'D', 'F']:
            print("\n⚠️ 잘못된 키를 입력하셨습니다! W, A, S, D(이동) 또는 F(공격)를 누르세요.")
            continue # 연산 단계를 생략하고 즉시 위로 올려보내 턴 소모를 억제시킴!
            
        # 정상 작동 구역
        if action in ['W', 'A', 'S', 'D']:
            # 이동 제어 함수 호출 (필드 아이템 전달 동시 연산)
            move_player(player, action, items)
        elif action == 'F':
            # 전투 제어 함수 호출 (체력 보너스 조건 판정을 위해 난이도 정보 함께 전달)
            check_battle(player, monsters, difficulty)
            
        # [★ 핵심 층 교체 알고리즘] 현재 사냥터의 몬스터 5마리 완소 퇴치 시 승급
        if player['kills'] == 5:
            if current_floor < max_floors:
                current_floor += 1 # 층 단계 증가
                
                # [★ 추가/수정] 층 승급 시 난이도별 턴 연장(보너스 턴) 보상 지급 알고리즘
                if difficulty == '1':
                    turns_limit += 30  # 쉬움 모드는 30턴 추가
                    print(f"\n⏱️ [쉬움 혜택] 시간의 틈새가 열려 제한 시간이 30턴 연장되었습니다! (총 제한: {turns_limit}턴)")
                else:
                    turns_limit += 15  # 어려움 모드는 15턴 추가
                    print(f"\n⏱️ [어려움 혜택] 제한 시간이 15턴 연장되었습니다! (총 제한: {turns_limit}턴)")
                
                print("\n" + "🎉" * 20)
                print(f"✨ 축하합니다! {current_floor - 1}층의 모든 몬스터를 처치하여 {current_floor}층 사냥터로 진입합니다!")
                print("💖 생명력이 최대로 충전되었으며, 새로운 검 아이템과 몬스터가 무작위 재배치되었습니다!")
                print("🎉" * 20)
                
                # 새로운 층 진입 시 새로운 수학 난수용 시드값을 한 번 더 입력받아 실시간 공간 형성
                print(f"\n🔮 [ {current_floor}층 ] 새로운 층을 구성할 행운의 수를 입력하세요!")
                while True:
                    user_input = input("정수값 입력 (예: 1~9999): ").strip()
                    if user_input.isdigit():
                        # 현재 층 정보 등을 추가로 수학적으로 비벼 더 무작위적이고 겹치지 않는 시드 갱신
                        lucky_seed = int(user_input) + current_floor * 17
                        print(f"\n⚡ 새로운 시공간의 문이 무작위로 형성되었습니다!")
                        break
                    else:
                        print("⚠️ 올바른 숫자를 입력해 주세요.")
                
                # [매우 중요] 기존 성장한 플레이어 정보를 보존한 채(existing_player=player) 새 층의 정보만을 조절해서 덮어씌움
                player, monsters, items = init_game(difficulty, lucky_seed, existing_player=player)
            else:
                # 3층의 몬스터까지 다 사냥했다면 최종 게임 완벽 클리어이므로 탈출
                break
            
        # 모든 업데이트 연산이 끝나면 바뀐 상태를 바탕으로 맵을 다시 렌더링하고, 턴 수 증가
        draw_screen(player, monsters, items, current_floor)
        turn += 1
        
    # [최종 게임 결말 및 판정 출력 구역]
    print("\n" + "=" * 65)
    print("                    GAME OVER                    ")
    print("=" * 65)
    
    # 3층의 탑 보스까지 전부 섬멸 완료하고 처치 카운트 승급을 이루어 냈는지 판단
    if current_floor == max_floors and player['kills'] == 5:
        print("🏆 대성공! 3층 탑의 모든 몬스터를 완벽히 사냥해 엘리니아의 대전사가 되었습니다!")
    elif player['hp'] <= 0:
        print("☠️ 으아악! 용사 캐릭터가 쓰러졌습니다... 마을 부활 장소로 이동합니다.")
    else:
        print("⏳ 시간 초과! 사냥터 이용 시간이 종료되어 밖으로 쫓겨났습니다.")
    print("=" * 65)


# 파이썬 프로그램 표준 시작 진입 제어 구절
if __name__ == '__main__':
    main()
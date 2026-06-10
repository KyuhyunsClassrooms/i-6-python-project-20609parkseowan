# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20609 박서완
# 프로젝트 주제: 2차원 격자 좌표 및 물리 공식을 활용한 2인용 2D 무술 스파링 게임

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

arena = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row = 0 (세로 높이 y = 5)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row = 1 (세로 높이 y = 4)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row = 2 (세로 높이 y = 3)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row = 3 (세로 높이 y = 2)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # row = 4 (세로 높이 y = 1)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # row = 5 (세로 높이 y = 0, 바닥)
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 조작 키 규칙을 출력합니다."""
    print("=" * 60)
    print("         🎮 파이썬 2D 콘솔 무술 스파링 게임 🎮")
    print("=" * 60)
    print(" [Player 1]  A: 왼쪽  | D: 오른쪽 | W: 점프 | F: 공격")
    print(" [Player 2]  J: 왼쪽  | L: 오른쪽 | I: 점프 | H: 공격")
    print(" ※ 입력 방법: 공백으로 구분하여 동시에 입력 (예: D J)")
    print("=" * 60)


def init_game():
    """게임 시작 시 두 캐릭터의 상태(딕셔너리)를 초기화합니다."""
    # 플레이어 1 초기 상태 (왼쪽 바닥에 배치)
    p1 = {
        'x': 2,        # 가로 위치 (0~14)
        'y': 0,        # 세로 높이 (0~5, 바닥은 0)
        'vy': 0,       # 세로 속도 (점프 시 상승하는 힘)
        'hp': 100,     # 체력
        'dir': 'right' # 바라보는 방향
    }
    
    # 플레이어 2 초기 상태 (오른쪽 바닥에 배치)
    p2 = {
        'x': 12,
        'y': 0,
        'vy': 0,
        'hp': 100,
        'dir': 'left'
    }
    
    return p1, p2


def draw_arena(p1, p2, attack_zones):
    """2차원 리스트 격자판을 기반으로 경기장 화면을 렌더링하여 출력합니다."""
    # 1단계: 상단 체력(HP) 상태 바 출력
    p1_bars = "■" * (p1['hp'] // 20) + "□" * (5 - (p1['hp'] // 20))
    p2_bars = "■" * (p2['hp'] // 20) + "□" * (5 - (p2['hp'] // 20))
    
    print(f"\nP1: {p1_bars} ({p1['hp']}/100)  |  P2: {p2_bars} ({p2['hp']}/100)")
    print("-" * 45)
    
    # 2단계: 실시간 위치를 새로 그리기 위해 템플릿 격자판을 복사합니다.
    arena = []
    for row in arena_template:
        arena.append(list(row))
        
    # 3단계: 공격 판정이 일어난 자리에 공격 이펙트(3)를 표시합니다.
    for ax, ay in attack_zones:
        if 0 <= ax < 15 and 0 <= ay < 6:
            row_idx = 5 - ay # y축 좌표를 2차원 리스트 행 인덱스로 변환
            arena[row_idx][ax] = 3

    # 4단계: 플레이어들의 실시간 위치를 격자판에 매핑합니다. (대칭 변환 row = 5 - y 적용)
    p1_row = 5 - p1['y']
    p2_row = 5 - p2['y']
    
    # 캐릭터가 경기장 범위 안에 있을 때만 격자판에 배치하여 오류를 방지합니다.
    if 0 <= p1_row < 6 and 0 <= p1['x'] < 15:
        arena[p1_row][p1['x']] = 1
    if 0 <= p2_row < 6 and 0 <= p2['x'] < 15:
        arena[p2_row][p2['x']] = 2
        
    # 5단계: 이중 반복문(다중 for문)을 사용하여 화면을 최종 출력합니다.
    for row_idx in range(6):
        for col_idx in range(15):
            cell = arena[row_idx][col_idx]
            if cell == 1:
                print("①", end="")
            elif cell == 2:
                print("②", end="")
            elif cell == 3:
                print("＊", end="")
            else:
                # 5번째 행(가장 아랫줄)이면 바닥선(_)을 그리고, 그 외에는 공중(.)을 그립니다.
                if row_idx == 5:
                    print("_", end="")
                else:
                    print(".", end="")
        print() # 한 행 출력이 끝나면 줄바꿈
    print("-" * 45)


def update_physics(player):
    """중력 법칙을 연산하여 점프 중인 캐릭터의 Y 좌표를 업데이트합니다."""
    g = 1 # 중력 가속도
    
    # 캐릭터가 공중에 있거나, 위로 올라가는 속도가 있을 때 포물선 운동 처리
    if player['y'] > 0 or player['vy'] > 0:
        player['y'] += player['vy']  # 위치 변경
        player['vy'] -= g            # 중력에 의해 속도가 매 턴 1씩 감소
        
    # 예외 처리: 만약 계산 결과 y가 바닥 아래로 내려가면 바닥(0)에 딱 고정시킵니다.
    if player['y'] < 0:
        player['y'] = 0
        player['vy'] = 0


def check_hit(attacker, defender):
    """공격자의 위치와 방향을 기준으로 상대방이 사정거리(2칸) 내에 있는지 판정합니다."""
    hit_range = 2 # 사정거리
    
    # 두 캐릭터의 높이(y)가 같을 때만 공격이 성공할 수 있습니다.
    if attacker['y'] == defender['y']:
        # 오른쪽을 보고 공격하는 경우
        if attacker['dir'] == 'right':
            # 상대가 내 오른쪽에 있고, 사정거리 이내에 있는지 검사
            if attacker['x'] < defender['x'] <= attacker['x'] + hit_range:
                return True
        # 왼쪽을 보고 공격하는 경우
        elif attacker['dir'] == 'left':
            # 상대가 내 왼쪽에 있고, 사정거리 이내에 있는지 검사
            if attacker['x'] - hit_range <= defender['x'] < attacker['x']:
                return True
                
    return False


def process_action(p1, p2, p1_key, p2_key):
    """플레이어가 입력한 행동키를 해석하여 이동, 점프, 공격을 처리합니다."""
    attack_zones = [] # 공격 이펙트를 띄울 칸들을 담을 리스트
    
    # --- Player 1 조작 처리 ---
    p1_key = p1_key.upper()
    if p1_key == 'A':
        p1['x'] = max(0, p1['x'] - 1) # 왼쪽 벽 뚫기 방지
        p1['dir'] = 'left'
    elif p1_key == 'D':
        p1['x'] = min(14, p1['x'] + 1) # 오른쪽 벽 뚫기 방지
        p1['dir'] = 'right'
    elif p1_key == 'W' and p1['y'] == 0: # 바닥에 서 있을 때만 점프 가능
        p1['vy'] = 3 # 상승 속도(vy) 인가
    elif p1_key == 'F':
        # 바라보는 방향에 맞춰 전방 2칸을 공격 범위로 시각화 리스트에 추가
        offset = 1 if p1['dir'] == 'right' else -1
        attack_zones.append((p1['x'] + offset, p1['y']))
        attack_zones.append((p1['x'] + offset * 2, p1['y']))
        
        # 피격 검사 성공 시 체력 감수 및 밀려남(넉백) 처리
        if check_hit(p1, p2):
            print("💥 Player 1의 강력한 무술 공격 적중!")
            p2['hp'] = max(0, p2['hp'] - 20)
            p2['x'] = min(14, p2['x'] + 2) if p1['dir'] == 'right' else max(0, p2['x'] - 2)

    # --- Player 2 조작 처리 ---
    p2_key = p2_key.upper()
    if p2_key == 'J':
        p2['x'] = max(0, p2['x'] - 1)
        p2['dir'] = 'left'
    elif p2_key == 'L':
        p2['x'] = min(14, p2['x'] + 1)
        p2['dir'] = 'right'
    elif p2_key == 'I' and p2['y'] == 0:
        p2['vy'] = 3
    elif p2_key == 'H':
        offset = 1 if p2['dir'] == 'right' else -1
        attack_zones.append((p2['x'] + offset, p2['y']))
        attack_zones.append((p2['x'] + offset * 2, p2['y']))
        
        if check_hit(p2, p1):
            print("💥 Player 2의 강력한 무술 공격 적중!")
            p1['hp'] = max(0, p1['hp'] - 20)
            p1['x'] = min(14, p1['x'] + 2) if p2['dir'] == 'right' else max(0, p1['x'] - 2)
            
    return attack_zones


def main():
    show_intro()
    p1, p2 = init_game()
    
    # 초기 라운드 출력
    draw_arena(p1, p2, [])
    
    # ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
turns_limit = 15 # 경기 제한 시간 (15턴)
    turn = 1
    
    # 두 플레이어의 체력이 0보다 크고 제한 시간이 남았을 때 루프 작동
    while turn <= turns_limit and p1['hp'] > 0 and p2['hp'] > 0:
        print(f"\n[라운드 {turn} / {turns_limit}]")
        
        # 키보드로부터 동시에 두 플레이어의 행동을 공백으로 받아옵니다.
        try:
            p1_in, p2_in = input("두 플레이어의 행동을 공백으로 구분하여 입력하세요: ").split()
        except ValueError:
            print("⚠️ 입력 규칙을 확인해 주세요! 두 글자 사이에 공백을 한 칸 넣어주세요. (예: D J)")
            continue # 예외 처리: 잘못 입력하면 이번 턴을 다시 진행함
            
        # 1단계: 사용자의 이동/공격 키 입력 처리
        attack_effects = process_action(p1, p2, p1_in, p2_in)
        
        # 2단계: 공중에 뜬 캐릭터에게 중력 효과 반영
        update_physics(p1)
        update_physics(p2)
        
        # 3단계: 가상 공간 격자판 화면 출력
        draw_arena(p1, p2, attack_effects)
        
        turn += 1
        
    # --- 경기 최종 승패 판정 및 출력 ---
    print("\n================== 경기 종료 ==================")
    if p1['hp'] == p2['hp']:
        print("🤝 무승부! 두 고수의 기량이 막상막하입니다.")
    elif p1['hp'] > p2['hp']:
        print("🏆 Player 1 승리! 최강의 무술 고수로 등극했습니다!")
    else:
        print("🏆 Player 2 승리! 최강의 무술 고수로 등극했습니다!")
    print("===============================================")


# 프로그램 시작점
    if __name__ == '__main__':
    main()

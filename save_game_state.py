import json

def save_game_state(character_position, timer_running, start_time, best_time):
    with open('game_state.json', 'w') as file:
        json.dump({
            'character': {
                'x': character_position[0],
                'y': character_position[1]
            },
            'timer_running': timer_running,
            'start_time': start_time,
            'best_time': best_time
        }, file)

def load_game_state():
    try:
        with open('game_state.json', 'r') as file:
            game_state = json.load(file)

        character_position = (game_state['character']['x'], game_state['character']['y'])
        timer_running = game_state['timer_running']
        start_time = game_state['start_time']
        best_time = game_state.get('best_time', float('inf'))  # 기존에 저장된 최고 기록 불러오기

        return character_position, timer_running, start_time, best_time
    
    except FileNotFoundError:
        print("저장된 게임 상태 파일이 없습니다. 새로운 게임을 시작합니다.")
        return (0, 0), False, 0, float('inf')
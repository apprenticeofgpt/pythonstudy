import tkinter as tk
import random as r

class bowling_game:
    def __init__(self):
        self.max_frames = 10
        self.pitch_record = [[0, 0, 0] for _ in range(self.max_frames)]
        self.pitch_loc_index = {"frame": 0, "pitch_order": 0}
        self.pitch_count = 0

    def init(self):
        self.pitch_record = [[0, 0, 0] for _ in range(self.max_frames)]
        self.pitch_loc_index = {"frame": 0, "pitch_order": 0}
        self.pitch_count = 0

    def frame_pitch_info_update(self, pitch_result):
        frame = self.pitch_loc_index['frame']
        pitch_order = self.pitch_loc_index['pitch_order']

        self.pitch_record[frame][pitch_order] = pitch_result
        result = f"{frame+1}-{pitch_order+1} : {pitch_result}"

        pitch_order += 1

        if frame != 9:
            if pitch_result == 10 and pitch_order == 1:
                self.pitch_loc_index['frame'] += 1
                self.pitch_loc_index['pitch_order'] = 0
            elif pitch_order == 1:
                self.pitch_loc_index['pitch_order'] = 1
            else:
                self.pitch_loc_index['frame'] += 1
                self.pitch_loc_index['pitch_order'] = 0
        else:
            if pitch_order < 3:
                self.pitch_loc_index['pitch_order'] = pitch_order
            else:
                # 마지막 프레임 종료 후 초기화는 안 함 (점수 출력 위해)
                self.pitch_loc_index['pitch_order'] = 3  # 막음 처리용

        return result

    def write_pitch_record(self, pitch_result):
        return self.frame_pitch_info_update(pitch_result)

    def calc_score(self):
        score = 0
        for i in range(10):
            f = self.pitch_record[i]
            if f[0] == 10:  # 스트라이크
                score += 10 + self._next_two(i)
            elif f[0] + f[1] == 10:  # 스페어
                score += 10 + self._next_one(i)
            else:
                score += f[0] + f[1]
        return score

    def _next_one(self, i):
        if i + 1 >= 10:
            return 0
        return self.pitch_record[i+1][0]

    def _next_two(self, i):
        if i + 1 >= 10:
            return 0
        next_frame = self.pitch_record[i+1]
        if next_frame[0] == 10 and i + 2 < 10:
            return 10 + self.pitch_record[i+2][0]
        return next_frame[0] + next_frame[1]


class bowling_gui:
    def __init__(self, root):
        self.root = root
        self.root.title("bowling game")
        self.game = bowling_game()
        self.finished = False

        self.output = tk.Text(root, height=12, width=50)
        self.output.pack(pady=10)

        self.pitch_button = tk.Button(root, text="pitch", command=self.pitch)
        self.pitch_button.pack()

        self.reset_button = tk.Button(root, text="reset", command=self.reset)
        self.reset_button.pack()

    def pitch(self):
        if self.finished:
            self.output.insert(tk.END, "game over.\n")
            return

        frame = self.game.pitch_loc_index['frame']
        pitch_order = self.game.pitch_loc_index['pitch_order']

        if frame > 9 or (frame == 9 and pitch_order >= 3):
            self.finished = True
            total = self.game.calc_score()
            self.output.insert(tk.END, f"total score: {total}\n")
            return

        # 첫 투구 또는 추가 투구
        max_pin = 10
        if pitch_order == 1 and frame < 9:
            max_pin = 10 - self.game.pitch_record[frame][0]

        result = r.randint(0, max_pin)
        msg = self.game.write_pitch_record(result)
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)

        # 마지막 투구 후 최종 점수 출력
        frame_now = self.game.pitch_loc_index['frame']
        order_now = self.game.pitch_loc_index['pitch_order']
        if frame_now == 9 and order_now >= 3:
            self.finished = True
            total = self.game.calc_score()
            self.output.insert(tk.END, f"total score: {total}\n")

    def reset(self):
        self.output.delete("1.0", tk.END)
        self.game.init()
        self.finished = False
        self.output.insert(tk.END, "game has been reset.\n")


root = tk.Tk()
app = bowling_gui(root)
root.mainloop()

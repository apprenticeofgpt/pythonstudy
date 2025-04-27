import random as r

class bowling_game:
    def __init__(self):
        self.max_frames = 10
        self.pitch_record = [[0, 0, 0] for _ in range(self.max_frames)]
        self.pitch_loc_index = {"frame": 0, "pitch_order": 0}
        self.pitch_record_comp = []
        self.frame_index = 0
        self.pitch_count = 0
        self.max_pitch_count = 30

    def init(self):
        self.pitch_record = [[0, 0, 0] for _ in range(self.max_frames)]
        self.pitch_loc_index = {"frame": 0, "pitch_order": 0}

    def frame_pitch_info_update(self, pitch_result):
        frame = self.pitch_loc_index['frame']
        pitch_order = self.pitch_loc_index['pitch_order']

        self.pitch_record[frame][pitch_order] = pitch_result
        print(f"{frame+1}-{pitch_order+1} : {pitch_result}", end=" __ ")

        pitch_order += 1  

        if pitch_result == 10:
            
            if frame != 9:
                self.pitch_loc_index['frame'] += 1
                self.pitch_loc_index['pitch_order'] = 0
            else:
                if pitch_order < 3:
                    self.pitch_loc_index['pitch_order'] = pitch_order
                else:
                    print(self.pitch_record)
                    self.init()
                    print()
        else:
            if frame != 9:
                if pitch_order == 1:
                    self.pitch_loc_index['pitch_order'] = pitch_order
                else:
                    self.pitch_loc_index['frame'] += 1
                    self.pitch_loc_index['pitch_order'] = 0
            else:
                if pitch_order < 2:
                    self.pitch_loc_index['pitch_order'] = pitch_order
                elif pitch_order == 2 and self.pitch_record[frame][0] + self.pitch_record[frame][1] >= 10:
                    self.pitch_loc_index['pitch_order'] = pitch_order
                else:
                    print(self.pitch_record)
                    self.init()
                    print()

    def write_pitch_record(self, pitch_result):
        self.frame_pitch_info_update(pitch_result)

    def play(self):
        while True:
            first_pitch_result = r.randint(0, 10)
            self.write_pitch_record(first_pitch_result)

            if first_pitch_result != 10:
                second_pitch_result = r.randint(0, 10 - first_pitch_result)
                self.write_pitch_record(second_pitch_result)
            print()

            self.pitch_count += 1
            if self.pitch_count > self.max_pitch_count:
                break
game = bowling_game()
game.play()

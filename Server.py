class Data:
    # Default Queue length
    def __init__(self, length = 1100):
        self.l_ear = deque(maxlen=length)
        self.l_forehead = deque(maxlen=length)
        self.r_forehead = deque(maxlen=length)
        self.r_ear = deque(maxlen=length)
        self.average = deque(maxlen=length)
    # Update Queue fixed size
    def increment (self, args):
        vl_ear, vl_forehead, vr_forehead, vr_ear = args
        self.l_ear.append(vl_ear)
        self.l_forehead.append(vl_forehead)
        self.r_forehead.append(vr_forehead)
        self.r_ear.append(vr_ear)
        self.average.append((vl_ear + vl_forehead + vr_forehead + vr_ear)/4)
    # Create new Queues with different max length
    # Useful for window reshaping and FFT
    def set_length(self,LENGTH):
        self.l_ear = deque(maxlen=LENGTH)
        self.l_forehead = deque(maxlen=LENGTH)
        self.r_forehead = deque(maxlen=LENGTH)
        self.r_ear = deque(maxlen=LENGTH)
        self.average = deque(maxlen=LENGTH)
class PylibloServer(ServerThread):
    # Default port is 1234
    def __init__(self, PORT=1234):
        ServerThread.__init__(self, PORT)
        self.EEG = Data()
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        self.EEG.increment(args)

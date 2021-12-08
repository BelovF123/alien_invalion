class Stats():
    """statistika"""
    def __init__(self):
        """init statistika"""
        self.reset_stat()
        self.run_game = True

    def reset_stat(self):

        self.lifes = 3
        self.score = 0
        self.hscore = 0
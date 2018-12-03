import tqdm


class TileStream:
    def __init__(self, splitting_service):
        self.iteration = 0
        self.splitting_service = splitting_service
        self.bar = tqdm.tqdm(total=len(self))

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= len(self):
            self.bar.close()
            raise StopIteration
        res = self.splitting_service._cut_tile(self.iteration)
        self.bar.update()
        self.iteration += 1
        return res

    def __len__(self):
        return len(self.splitting_service)

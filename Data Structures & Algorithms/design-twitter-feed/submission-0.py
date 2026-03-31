class Twitter:

    def __init__(self):
        self.tweet = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 
        if userId not in self.tweet:
            self.tweet[userId] = [[], []]   # tweets, followees
        self.tweet[userId][0].append((self.time, tweetId))  # append = newest last

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweet:
            return []

        res = []
        heap = []

        tweets, followeIds = self.tweet[userId]

        # user follows themselves
        users = set(followeIds)
        users.add(userId)

        # push most recent tweet of each user into heap
        for u in users:
            if u in self.tweet and self.tweet[u][0]:
                tlist = self.tweet[u][0]
                idx = len(tlist) - 1
                time, tid = tlist[idx]
                heapq.heappush(heap, (-time, tid, u, idx))

        # extract top 10
        while heap and len(res) < 10:
            _, tid, u, idx = heapq.heappop(heap)
            res.append(tid)

            # push next older tweet from same user
            if idx > 0:
                time, tid = self.tweet[u][0][idx - 1]
                heapq.heappush(heap, (-time, tid, u, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.tweet:
            self.tweet[followerId] = [[], []]
        if followeeId not in self.tweet[followerId][1]:
            self.tweet[followerId][1].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.tweet and followeeId in self.tweet[followerId][1]:
            self.tweet[followerId][1].remove(followeeId)
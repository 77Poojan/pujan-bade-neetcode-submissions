class Twitter:

    def __init__(self):
        self.tweet = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweet:
            self.tweet[userId] =[[], []]
        self.tweet[userId][0].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweet:
            return []

        res = []
        heap = []

        _, followeIds = self.tweet[userId]
        users = set(followeIds)
        users.add(userId)

        for user in users:
            if user in self.tweet and self.tweet[user][0]:
                tweetList = self.tweet[user][0]
                idx = len(tweetList) - 1
                time, tweetId = tweetList[idx]
                data = (-time, tweetId, user, idx)
                heapq.heappush(heap, data)

        while heap and len(res) < 10:
            _, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                time, tweet = self.tweet[user][0][idx - 1]
                data = (-time, tweet, user, idx - 1)
                heapq.heappush(heap, data)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.tweet:
            self.tweet[followerId] = [[], []]

        if followeeId not in self.tweet[followerId][1]:
            self.tweet[followerId][1].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.tweet and followeeId in self.tweet[followerId][1]:
            self.tweet[followerId][1].remove(followeeId)
 
"""
# A Mapping of User and his tweets
    - time = 0 which updates as soon as a tweet is made (+=1)
    
    - {
    User1 : [(tweet1,t1),(tweet2,t2),(tweet3,t3)],
    User2: [(tweet1,t4),(tweet2,t5)]
    }

# A mapping of user and his followers
    - {
    User1: [f1,f2,f3],
    User2:[f3,f4]
    }

# For the news feed:
        - We must fetch all the followers and there tweets into a single list
        - Sort them by the timestamp allocated
        - Display the top 10 from the most recent timestamp
        
        - Put all the tweets recieved into a Max-heap of size 10:- return them all in a list

"""

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.followers = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timestamp+=1
        if userId in self.users:self.users[userId].append((tweetId,self.timestamp))
        else:self.users[userId] = [(tweetId,self.timestamp)]

    def getTweet(self,userId):
        tweets = []
        
        if userId in self.users:
            tweets += self.users[userId] # fetch all the tweets by self
            
        if userId in self.followers:
            followees = self.followers[userId] # fetch all the followers
            for u_id in followees:             # fetch all the tweets of all the followers
                if u_id in self.users:         
                    tweets+=self.users[u_id]
        tweets = sorted(tweets,key = lambda posts: posts[1],reverse = True) # sort by timestamp and get the top 10
        return tweets[0:10] # return the top 10 tweets
    
            
    
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return [post[0] for post in self.getTweet(userId)]
        

        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!= followeeId:
            if followerId in self.followers:self.followers[followerId].add(followeeId)
            else:self.followers[followerId] ={followeeId}

                
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
                
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
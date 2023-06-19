def vote(votes):
    for x in votes:
        if votes.count(x) > 1:
            return x

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
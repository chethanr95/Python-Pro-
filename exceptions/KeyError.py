facebook_posts = [
    {
        "likes" : 10,
        "comments" : 12
    },
    {
        "comments" : 2,
        #"likes" : 2,
        "posts" : 5
    },
    {
        "likes" : 21,
        "posts" : 1
    },
    {
        "likes" : 4,
        "posts" : 9,
        "comments" : 13
    }
]

#option A
def count_likes() :
    total_likes = 0
    #in case of exception KeyError, consider likes as zero
    #(A)
    for post in facebook_posts :
        try :
            total_likes = total_likes + post["likes"]
        except KeyError :
            pass    
    print(f"Total Likes = {total_likes}")

    #OR (B)
    total_likes = 0
    for post in facebook_posts :
        try :
            likes = post["likes"]
        except KeyError :
            likes = 0
        #else    already evaluated from try, value obtained
        finally :
            total_likes += likes
    print(f"Total Likes = {total_likes}")

    
count_likes()
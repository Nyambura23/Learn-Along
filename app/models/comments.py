class Comment:

    all_comments = []

    def __init__(self,author,id,quote,permalink,comment):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink
        self.comment = comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

from populate import base
from django.contrib.auth.models import User
from Aarticle.models import Article, Comment


titles = ['如何像電腦科學家一樣思考', '10分鐘內學好Python', '簡單學習Django']
comments = ['文章真棒', '並不認同您的觀點', '借分享', '學好一個程式語言或框架並不容易']


def populate():
    print('Populating Article and Comment ... ', end='')
    Article.objects.all().delete()
    Comment.objects.all().delete()
    articles = []
    admin = User.objects.first()
    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        articles.append(article)
    articles = Article.objects.bulk_create(articles)
    
    for article in articles:
        commentList = []
        for comment in comments:
            commentList.append(Comment(article=article, user=admin, content=comment))
        Comment.objects.bulk_create(commentList)

    print('done')


if __name__ == '__main__':
    populate()

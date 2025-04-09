from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
# Consultar un artículo
article = Article.objects.get(id=1)

# Acceder al autor del artículo (relación ForeignKey)
print(article.author.name)


author = Author.objects.get(id=1)

# Acceder a todos los artículos de un autor (relación inversa)
articles = author.article_set.all()

for article in articles:
    print(article.title)
    
# Supongamos que tienes un artículo con ID 1 y un autor con ID 2
article = Article.objects.get(id=1)
article.author_id = 2  # Actualiza la relación con el ID del autor
article.save()

author = Author.objects.get(id=2)  # Obtener el autor con el ID 2
article = Article.objects.get(id=1)  # Obtener el artículo con el ID 1
article.author = author  # Asignar el objeto completo
article.save()

from blog.modelos import Post, Autor

estados_post = ("borrador", "publicado", "archivado")


def validar_post(post):

    # Verificar que sea un objeto Post
    if type(post) is not Post:
        return "El post debe ser un objeto de la clase Post."

    # Verificar el ID
    if type(post.id) is not int:
        return "El id debe ser un número entero."

    # Verificar el título
    if type(post.titulo) is not str or not post.titulo.strip():
        return "El título está vacío o tiene un tipo incorrecto."

    # Verificar el contenido
    if type(post.contenido) is not str or not post.contenido.strip():
        return "El contenido está vacío o tiene un tipo incorrecto."

    # Verificar el autor
    if type(post.autor) is not Autor:
        return "El autor debe ser un objeto de la clase Autor."

    # Verificar el nombre del autor
    if type(post.autor.nombre) is not str or not post.autor.nombre.strip():
        return "El autor no tiene un nombre válido."

    # Verificar que los tags sean una lista
    if type(post.tags) is not list:
        return "Los tags deben ser una lista."

    # Verificar los elementos de los tags
    for tag in post.tags:
        if type(tag) is not str or not tag.strip():
            return "Los tags contienen un dato incorrecto."

    # Verificar el estado
    if post.estado not in estados_post:
        return "El estado del post no es válido."

    return True

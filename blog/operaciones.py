# Función para mostrar publicaciones
def mostrar_posts(lista):

    if not lista:
        print("No se encontraron publicaciones.")
        return

    for post in lista:
        print(
            f"- {post.titulo} | "
            f"Autor: {post.autor.nombre} | "
            f"Estado: {post.estado}"
        )
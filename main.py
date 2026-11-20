
from blog.modelos import Autor, Post, Blog
from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu
from blog.operaciones import mostrar_posts
from blog.validaciones import validar_post


if __name__ == "__main__":

    # Cargar publicaciones desde JSON
    posts_cargados = cargar_posts()

    # Crear el objeto Blog
    mi_blog = Blog(posts_cargados)

    # Bucle principal
    while True:

        opcion = mostrar_menu()

        # Opción 1: listar posts
        if opcion == 1:
            mostrar_posts(mi_blog.listar_posts())

        # Opción 2: buscar por título
        elif opcion == 2:
            termino = input("Buscar por titulo: ").strip()

            if termino:
                resultados = mi_blog.buscar_por_titulo(termino)
                mostrar_posts(resultados)
            else:
                print("La busqueda no puede estar vacia.")

        # Opción 3: filtrar por tag
        elif opcion == 3:
            tag = input("Ingresa el tag que deseas buscar: ").strip()

            if tag:
                resultados = mi_blog.filtrar_por_tag(tag)
                mostrar_posts(resultados)
            else:
                print("El tag no puede estar vacio.")

        # Opción 4: crear un nuevo post
        elif opcion == 4:

            print("\n--- NUEVO POST ---")

            titulo = input("Titulo: ").strip()
            contenido = input("Contenido: ").strip()
            nombre_autor = input("Nombre del autor: ").strip()
            bio_autor = input("Biografia del autor: ").strip()
            tags_texto = input("Tags separados por coma: ").strip()

            if not titulo or not contenido or not nombre_autor or not bio_autor or not tags_texto:
                print("Error: todos los campos son obligatorios.")

            else:
                tags = [
                    tag.strip()
                    for tag in tags_texto.split(",")
                    if tag.strip()
                ]

                if not tags:
                    print("Debes ingresar al menos un tag.")

                else:
                    # Crear objeto Autor
                    autor = Autor(nombre_autor, bio_autor)

                    # Generar un ID nuevo
                    nuevo_id = max(
                        (
                            post.id
                            for post in mi_blog.posts
                            if type(post.id) is int
                        ),
                        default=0
                    ) + 1

                    # Crear objeto Post
                    nuevo_post = Post(
                        nuevo_id,
                        titulo,
                        contenido,
                        autor,
                        tags,
                        "borrador"
                    )

                    # Validar el nuevo post
                    resultado = validar_post(nuevo_post)

                    if resultado is True:
                        mi_blog.crear_post(nuevo_post)
                        print("El post se creó correctamente.")
                    else:
                        print(f"No se pudo crear el post: {resultado}")

        # Opción 5: validar publicaciones
        elif opcion == 5:

            print("\n--- VALIDACION DE POSTS ---")

            for post, resultado in mi_blog.validar_posts():

                if resultado is True:
                    print(f"Post {post.id}: válido")

                else:
                    print(f"Post {post.id}: error - {resultado}")

        # Opción 6: guardar en JSON
        elif opcion == 6:
            guardar_posts(mi_blog.obtener_posts())

        # Opción 7: salir
        elif opcion == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opcion no valida. Selecciona un numero del 1 al 7.")

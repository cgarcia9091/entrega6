
import json
from pathlib import Path

from blog.modelos import Autor, Post


# Ruta del archivo posts.json en la carpeta principal
RUTA_JSON = Path(__file__).resolve().parent.parent / "posts.json"


# Crear publicaciones iniciales
def crear_posts_iniciales():

    perfil_autor = Autor(
        "Juan Perez",
        "Desarrollador web y creador de contenido sobre programación.",
        "Python y Django",
        ["@juan_dev", "@juan_python"]
    )

    perfil_autor2 = Autor(
        "Pedro Gonzales",
        "Desarrollador Backend.",
        "Python y Django",
        ["@juan_dev", "@juan_python"]
    )

    return [
        Post(
            1,
            "Primeros pasos con Python",
            "En este post veremos cómo empezar a programar con Python.",
            perfil_autor,
            ["Python", "Principiantes"],
            "publicado"
        ),
        Post(
            2,
            "Qué es Django",
            "Django es un framework web creado con Python.",
            perfil_autor2,
            ["Python", "Django", "Web"],
            "borrador"
        ),
        Post(
            3,
            "Organizando datos con listas",
            "Las listas permiten guardar varios elementos en una sola variable.",
            perfil_autor,
            ["Python", "Listas"],
            "archivado"
        ),
        Post(
            4,
            "Introducción a Backend",
            "",
            perfil_autor2,
            ["Backend"],
            "publicado"
        )
    ]


# Cargar publicaciones desde JSON
def cargar_posts():

    if not RUTA_JSON.exists():
        print("No existe posts.json. Se cargarán los datos iniciales.")
        return crear_posts_iniciales()

    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if type(datos) is not list:
            raise ValueError("El contenido del archivo debe ser una lista.")

        posts = []

        for dato in datos:
            try:
                post = Post.from_dict(dato)
                posts.append(post)

            except (ValueError, TypeError, KeyError) as error:
                print(f"Se omitió un post inválido: {error}")

        return posts

    except json.JSONDecodeError:
        print("El archivo JSON está vacío o tiene un formato incorrecto.")
        return crear_posts_iniciales()

    except (OSError, ValueError) as error:
        print(f"No se pudieron cargar los posts: {error}")
        return crear_posts_iniciales()


# Guardar publicaciones en JSON
def guardar_posts(posts):

    try:
        datos = [post.to_dict() for post in posts]

        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print("Los posts se guardaron correctamente en posts.json.")
        return True

    except (OSError, TypeError, AttributeError) as error:
        print(f"Error al guardar los posts: {error}")
        return False

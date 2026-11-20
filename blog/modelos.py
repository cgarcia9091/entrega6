class Autor:

    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    # Convertir a diccionario
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    # Crear un objeto Autor 
    @classmethod
    def from_dict(cls, datos):

        if type(datos) is not dict:
            raise ValueError("Los datos del autor deben ser un diccionario.")

        if "nombre" not in datos:
            raise ValueError("Falta el nombre del autor.")

        return cls(
            datos["nombre"],
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )
class Post:

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado
  
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }
  
    @classmethod
    def from_dict(cls, datos):

        if type(datos) is not dict:
            raise ValueError("Los datos del post deben ser un diccionario.")

        claves = ["id", "titulo", "autor", "tags", "estado"]

        for clave in claves:
            if clave not in datos:
                raise ValueError(f"Falta la clave '{clave}' en el post.")

        autor = Autor.from_dict(datos["autor"])

        return cls(
            datos["id"],
            datos["titulo"],
            datos.get("contenido", ""),
            autor,
            datos["tags"],
            datos["estado"]
        )


# Clase blog
class Blog:

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def obtener_posts(self):
        return self.posts

    def listar_posts(self):
        return self.posts

    def buscar_por_titulo(self, termino):
        encontrados = []

        for post in self.posts:
            if type(post.titulo) is str:
                if termino.lower() in post.titulo.lower():
                    encontrados.append(post)

        return encontrados
   
    def filtrar_por_tag(self, tag):
        encontrados = []

        for post in self.posts:
            if type(post.tags) is list:
                for etiqueta in post.tags:
                    if type(etiqueta) is str:
                        if etiqueta.lower() == tag.lower():
                            encontrados.append(post)
                            break

        return encontrados
   
    def crear_post(self, post):
        if type(post) is Post:
            self.posts.append(post)
            return True

        return False
   
    def validar_posts(self):
        from blog.validaciones import validar_post

        resultados = []

        for post in self.posts:
            resultados.append((post, validar_post(post)))

        return resultados

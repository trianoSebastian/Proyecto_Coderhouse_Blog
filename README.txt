GENERAL:
El Blog tiene las siguientes secciones:

 -Home: que es la página de inicio.
 -BlogList: es la página donde se muestra el listado de los blogs subidos.
 -Un botón de búsqueda.
 -Un botón de Login.
 -Un botón de Register.
	Si hay un usuario logueado:
		-Create: es la página que permite crear un post nuevo.
			-La misma permite ingresar un título, el contenido, subir una imagen, seleccionar un autor y el slug.
		-Profile: es la página que permite ver y editar de forma sencilla el perfil del usuario.
		-Una sección de saludo de bienvenida con su avatar.

Funciones habilitadas sólo a usuarios registrados y logueados:
-Editar y Borrar posts.
-Dejar comentarios.

->EL blog lleva un contador de vistas, likes y comentarios de los posts, que se puede ver debajo de cada post.
->EL post tiene leyenda del tiempo desde que se subió el post.
->Cada usuario sólo puede darle like una vez a cada post.
->Cuando un usuario quiere borrar un post, se le pregunta la confirmación o cancelación


CÓDIGO:
Vistas del código:

PostHomeView: se encarga de renderizar la página de inicio.
PostListView: se encarga de renderizar la página donde se listan los posts.
PostDetailView: tiene la lógica para mostrar el renderizado de un post en particular.
PostCreateView: tiene la lógica para crear un post.
PostUpdateView: tiene la lógica para actualizar un post.
PostDeleteView: tiene la lógica para borrar un post.
PostRegisterView: tiene la lógica para registrar un usuario nuevo.
UploadAvatarView: tiene la lógica para  un post.
login_view: maneja la lógica del login de los usuarios.
like: maneja la lógica de los likes para los posts.
logout_view: maneja la lógica del logout de los usuarios.
profile_view: tiene la lógica para mostrar el perfil de un usuario en particular.
update_profile:tiene la lógica para editar el perfil de un usuario en particular.

Modelos del código:

User: modelo de personalizado de usuario.
Avatar: modelo para el avatar.
Post: modelo para los posts.
Comment: modelo para los comentarios.
PostView: modelo para las vistas de los posts.
Like: modelo para los likes de los posts.

Formularios del código:

PostForm: formulario para los posts.
CustomUserCreationForm: formulario para manejar el registro de los usuarios.
CommentForm: formulario para los comentarios.
AvatarForm: formulario para los avatares.
UserEditForm: formulario para editar los usuarios.

Nota: la implementación del buscador quedó pendiente.

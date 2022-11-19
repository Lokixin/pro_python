# Expense Tracker Backend Application 

En este tutorial aprenderemos a crear una API web para comunicarnos con una base de datos. Para ello, crearemos un
controlador de gastos e ingresos, que permita realizar analíticas. Las tecnologías que usaremos son: 

- **FastAPI:**  Un framework de python para backend.
- **MongoDB:** Base de datos de tipo textual, **NoSQL**.
- **Git&GitHub:** Gestor de versiones de código. 
- **Docker:** Software para trabajar con contenedores. 

## 1. Preparación del entorno

Antes de empezar a programar, necesitamos realizar algunos preparativos (todas las herramientas son gratuitas): 

1. Como editor de código usaremos **Pycharm**, 
[aquí lo puedes descargar](https://www.jetbrains.com/pycharm/download/#section=windows).
2. También instalaremos **git**, [aquí lo puedes descargar](https://git-scm.com/downloads).
3. Alojaremos el repositorio en GitHub, si todavía no tienes una cuenta, 
[aquí la puedes crear](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home).

Una vez instaladas todos los programas anteriores: 

1. Crearemos un nuevo proyecto en PyCharm.
2. Dentro del proyecto creamos dos `python packages`: `expense_tracker`y `tests`
3. Añadiremos el fichero **.gitignore** en el directorio principal, 
[puedes copiar esta plantilla](https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a).
4. Inicializaremos un repositorio local con el comando
```bash
git init [nombre_repositorio]
```
4. Crearemos un nuevo repositorio en GitHub
5. Una vez creado el repositorio en GitHub ejecutaremos los siguientes comandos en el terminal: 

Para añadir los cambios realizados en nuestro directorio al área de staging: 

```bash
git add -A
```

Añadimos los cambios del área de staging al repositorio de git, creando un identificador
que se asocia al estado actual del repositorio con el comando: 

```bash
git commit -m "Mensaje descriptivo: debe explicar qué y por qué. El cómo ya se ve en los cambios"
```

Renombramos la rama `master` a `main` (esto solo hay que hacerlo una vez, para que se llame igual a la de GitLab):

```bash
git branch -M main
```

A continuación añadimos el repositorio remoto (el que hemos creado en GitHub) con el comando:

```bash
git remote add origin https://github.com/{github_username}/{github_repo}.git
```

Finalmente, enviamos los cambios de nuestro repositorio local al remoto:

```bash
git push -u origin main
```

Dónde origin es el nombre que le hemos dado al repositorio remoto y main el nombre de la 
rama (branch) a la cual mandamos los cambios.
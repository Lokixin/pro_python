# Expense Tracker Backend Application 

En este tutorial aprenderemos a crear una API web para comunicarnos con una base de datos. Para ello, crearemos un
controlador de gastos e ingresos, que permita realizar analíticas. Las tecnologías que usaremos son: 

- **FastAPI:**  Un framework de python para backend.
- **MongoDB:** Base de datos de tipo textual, **NoSQL**.
- **Git&GitHub:** Gestor de versiones de código. 
- **Docker:** Software para trabajar con contenedores. 

## 0. Preparación del entorno

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


## 1. Introducción a FastAPI

Para empezar a trabajar con FastAPI primero tenemos que instalar algunos paquetes: 

```bash
pip install fastapi "uvicorn[standard]"
```

Las nuevas funcionalidades de nuestro programa las vamos a crear en una nueva rama. 
Para ello usaremos el siguiente comando, que crea una nueva rama y nos cambiamos a ella: 

```bash
git checkout -b "TASK-2/setup-inicial-fastapi"
```

En este capítulo aprenderemos lo básico sobre FastAPI y trabajaremos con los `path parameters` 
y los `query parameters`. Esto nos permite recibir información a través de la URL y definir 
tanto campos obligatorios como opcionales. 

Para ejecutar la aplicación, deberemos usar el siguiente comando: 

```bash
uvicorn expense_tracker.fastapi_app:app --reload
```

Podremos visualizar la interfaz autogenerada por FastAPI des de la URL: 
<http://localhost:8000/docs/>

Una vez terminado el ejercicio, deberemos subir nuestros cambios al repositorio:

```bash
git add -A
git commit -m "TASK-2 Mensaje descriptivo de la tarea"
git push
```

No obstante, git nos avisará de un error. Pues la rama local no existe en el repositorio 
remoto. Por tanto, tendremos que ejecutar el siguiente comando: 

```bash
 git push --set-upstream origin DIM-2/setup-inicial-de-fastapi
```

De esta forma vincularemos la rama local con la remota.


### 1.1 Merge Request

Después de haber subido los cambios de una nueva rama, deberemos revisarlos. Para 
ello, iremos a nuestro repositorio de GitHub y veremos que aparece una nueva opción: 

<span style="color:white; background-color:green; padding: 8px; border-radius: 12px">
Compare & Pull Request
</span>

Clicaremos esta opción y revisaremos los cambios en nuestro código. Una vez nos hayamos
asegurado de que todo es correcto, haremos clik en `Create Pull Request`. 

Después, tendremos que clicar en la opción `Accept pull request & Merge`. De esta forma, 
actualizaremos la rama main con todos los cambios realizados en la rama de la tarea. 

Al finalizar este proceso, nuestra rama main estará actualizada con los cambios más
recientes. Para terminar, podemos hacer un poco de limpieza y eliminar la rama local 
y la remota que ya no usaremos (pues hemos acabado la tarea):

```bash
git checkout main # volvemos a la rama principal
git branch -d origin DIM-2/setup-inicial-de-fastapi # remota
git branch -d DIM-2/setup-inicial-de-fastapi # local
```

Finalmente, queda actualizar nuestra rama local. Para ello usaremos el comando: 

```bash
git pull --rebase
```
# Instalación técnica de Pancracio Prisma

Esta instalación se hace **una vez por empresa**. Prepara la organización,
sus accesos y sus servicios. Después, cada persona instala Panky con la
carpeta de entrega que Codex genera al terminar.

La instalación técnica usa el [producto Pancracio Prisma](https://github.com/Pancracio-Prisma/pancracio-prisma).
Su contrato de agente obtiene [Prisma Tools](https://github.com/Pancracio-Prisma/prisma-tools)
y prepara sus servicios. Los programas firmados para los usuarios y las
actualizaciones salen de [Prisma Releases](https://github.com/Pancracio-Prisma/pancracio-prisma-releases).

## Antes de empezar

Abre `Documents/` como carpeta de trabajo en Codex. Deja listo:

- **Codex con acceso completo** a la computadora, terminal y perfil de Chrome
  que usarás. El agente necesita operar esas superficies durante la instalación.
- **Git y GitHub configurados.** La cuenta debe poder leer los repos privados
  de `Pancracio-Prisma` por SSH. Codex comprobará la conexión.
- **Un proyecto de Google Cloud existente**, con facturación activa y una
  sesión abierta en el perfil elegido. Se usa para identidad, signals y Gateway,
  incluso si la base de datos se aloja en IONOS.
- **Acceso a la infraestructura elegida.** Si usarás IONOS, ten abierta su
  sesión y disponible el acceso SSH protegido. Para Google, ten abierta la
  consola del proyecto. Codex pedirá los datos cuando llegue a esa etapa.

Escribe contraseñas y códigos únicamente en la página o terminal que
corresponda. No los pongas en el chat ni en archivos de configuración.

## Qué decirle a Codex

Con `Documents/` abierto, envíale este mensaje:

> Instala Pancracio Prisma en modo técnico para una empresa nueva.
> Clona https://github.com/Pancracio-Prisma/pancracio-prisma.
> Sigue `AGENT_TECH_INSTALL.md` y prepara https://github.com/Pancracio-Prisma/prisma-tools.
> Guíame, verifica todo y entrégame el kit y su mensaje de confirmación.

Codex comprueba los repos y conserva cualquier trabajo local previo.
También te dirá qué necesita de cada cuenta; no tienes que editar JSON ni
ejecutar los comandos internos de instalación.
Al comenzar te preguntará **una sola vez** si esta instancia es un POC o una
instalación definitiva. Si ya empezaste la instalación antes de que existiera
esa pregunta, puedes elegir POC durante el proceso sin empezar de cero.

## Decisiones que te pedirá

### Empresa e infraestructura

- **Etapa:** POC para probar el producto o instalación definitiva. En POC
  puedes mantener privados Core y Workspace aunque tu plan de GitHub no
  permita proteger `main`; la instancia quedará marcada POC. Se siguen
  comprobando HTTPS, identidad, permisos y publicación real. El transporte
  Git POC requiere una cuenta universal dedicada, indicada por su login público,
  con acceso a los repositorios de la instancia. Cada instalación necesita una
  clave SSH distinta. El servicio seguro para registrar esas claves todavía
  debe quedar desplegado y verificado antes de entregar un kit utilizable.
  No se comparten credenciales ni claves privadas. Producción conserva el
  transporte por Actor. Para pasar a definitiva, primero se entrega la versión
  de Panky que ya sabe migrar. Una acción gobernada publica la transición en
  Core y cada instalación recibe la señal o la recupera al reconectarse.
  Panky guía a cada Actor para vincular su cuenta GitHub y probar su clave y
  repositorios; la cuenta universal sigue activa durante este recorrido.
  Solo después de verificar todas las instalaciones activas, el DNS estable
  de Policy y la protección de Core y Workspace se publica el modo definitivo
  y se revocan las claves compartidas. La señal no requiere un kit nuevo.
- **Empresa:** nombre legal, dominio, idioma y nombre visible de Panky.
- **Modalidad:** infraestructura propia o alojada por Brunova. Hoy está
  implementada la modalidad propia. La alojada aún no tiene provisionador
  probado y no se ofrece como instalación lista.
- **Servicios propios:** Prisma Schema y Prisma Policy en una VM de Google
  Cloud o una VPS de IONOS. Puede reutilizarse PostgreSQL existente y crear
  una base dedicada. Prisma Tools Gateway corre en Cloud Run del proyecto
  Google elegido y se conecta de forma autenticada con Policy.
- **Cuentas y propiedad:** perfil de Chrome, cuenta Google, proyecto GCP,
  cuenta GitHub y organización de GitHub de la empresa. Si esa organización
  no existe, Codex te mostrará la propuesta antes de crearla.

### Organización y acceso

- **Estructura inicial:** raíz, departamentos, equipos y puestos (*Seats*).
  Indica quién ocupa cada puesto y a qué puesto reporta; una persona puede
  ocupar más de uno. Si un responsable debe consultar el trabajo de sus
  reportes, Codex registra esa relación y le concede lectura de ese contexto,
  sin permiso para modificarlo.
- **Autoridad:** administrador principal, usuarios y correos corporativos.
  Codex no deduce permisos de un título de trabajo.
- **Contexto compartido:** qué puede conocer y modificar cada puesto. Codex
  prepara un repo canónico por contexto de departamento o Seat, sin duplicar
  el mismo contenido en repos de publicación.
- **Herramientas:** Workspace, n8n u otras que use la empresa, sus recursos
  concretos, accesos entre departamentos y excepciones necesarias. Los
  conectores particulares dependen de lo que elijas; Prisma Tools es parte
  obligatoria de la instalación organizacional.

## Qué prepara y comprueba Codex

1. **Producto y Tools.** Obtiene los repos oficiales de Pancracio Prisma y
   Prisma Tools, verifica sus remotos y commits, y trabaja en una carpeta
   nueva para la empresa sin alterar otras instalaciones.
2. **Organización y servicios.** Prepara Core, repos de contexto, base de
   datos, Policy y Gateway. Publica la primera política y comprueba que cada
   persona reciba solo el contexto y los recursos autorizados.
3. **Identidad y sincronización.** Configura el inicio de sesión, Pub/Sub y
   signals. Prueba un cambio real de Core: Policy debe confirmar el mismo
   commit antes de enviar la señal. Comprueba también un acceso permitido,
   uno denegado y un aviso que llegue únicamente a quien corresponda.
4. **Entrega.** Comprueba una instalación de usuario en los sistemas que se
   usarán. Solo entonces prepara las carpetas para los nuevos usuarios.

Si falta identidad, un servicio no está sano o las pruebas de acceso fallan,
**no hay entrega lista**. Un plan o una semilla por sí solos no completan la
instalación.

## Qué recibes al terminar

Por cada sistema operativo necesario, Codex prepara **una carpeta de
instalación** que puede entregarse como ZIP. Su nombre sigue siempre este
formato:

`Pancracio-Prisma-<empresa>-<macos|windows>-v<versión>`

Por ejemplo, la carpeta de Headquarters para Mac empieza con
`Pancracio-Prisma-headquarters-macos-v`. Codex te muestra la **ruta exacta**
y la versión que generó; no tienes que adivinar el nombre.

La carpeta contiene la guía del usuario, las instrucciones para Codex, la
configuración firmada de esa empresa y el programa firmado. Puedes
comprimirla como ZIP y compartirlo por Drive. La persona descarga y extrae el
ZIP, abre la carpeta extraída como workspace de Codex y usa el mensaje
genérico de `END_USER_INSTALL.md`. El kit fija la configuración de la empresa
y las claves de confianza; al instalar, Codex verifica y obtiene el release
vigente antes del primer bootstrap. No hace falta rehacer el kit por cada
versión del producto. Si el canal no se puede verificar, la instalación se
detiene en vez de ejecutar automáticamente el release anterior del ZIP.

La carpeta incluye un **aviso de verificación**, con el mismo nombre y el
sufijo `-verification.md`. Al comprimirla, el aviso queda dentro del ZIP en
cualquier modo; no hace falta un segundo archivo ni un segundo canal.
La persona solo muestra a Codex la carpeta extraída;
Codex hace las comprobaciones.

## Altas y cambios posteriores

Después puedes pedirle a Panky, en lenguaje natural, altas de personas,
departamentos, puestos, herramientas, recursos o excepciones. Panky comprueba
tu autoridad, muestra el cambio y confirma cuándo quedó activo. Una solicitud
pendiente todavía no concede acceso.

- **Autoridad:** `super_admin` pertenece al Actor; `admin` y `basic` son tipos
  de Seat. Ser dev o tener un puesto con nombre de manager no concede permisos
  administrativos por sí solo. Un grant explícito puede delegar una acción
  concreta, como registrar herramientas, sin convertir ese Seat en admin.
- **Herramientas:** registrarlas en Panky no crea su conector. Primero un
  técnico configura y comprueba el adaptador en Gateway. Panky solo registra
  una herramienta conectada si el solicitante tiene la acción permitida; la
  nueva política rige después de que Core la publica.

Las instrucciones completas para esas altas están en
`AGENT_ENTITY_ONBOARDING.md`. Borrar o revocar acceso requiere una decisión
explícita; los cambios normales de contexto siguen el flujo gobernado.

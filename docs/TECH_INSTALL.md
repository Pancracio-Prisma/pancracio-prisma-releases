# Instalación técnica de Pancracio Prisma

Esta instalación se hace **una vez por empresa** en Codex. Deja preparada la
organización para que después cada persona solo haga la instalación de usuario.
Codex obtiene de `Pancracio-Prisma/pancracio-prisma` las instrucciones y el
instalador técnico. El paquete firmado de usuario se obtiene del canal público
`Pancracio-Prisma/pancracio-prisma-releases`; ese mismo canal alimenta las
actualizaciones posteriores. La empresa no publica una copia del producto.
El agente pregunta al inicio si la empresa usará infraestructura **propia**
(self-hosted) o **alojada por Brunova**. En ambos casos Prisma Tools es
obligatorio para el catálogo y los permisos del contexto organizacional 2.1.
La modalidad propia es la primera implementada; la alojada requiere todavía
su provisionador y pruebas de aislamiento antes de ofrecerse a una empresa.

## Antes de empezar

Deja listo esto en la computadora desde la que administrarás la instalación:

1. **Codex con acceso completo a la computadora** y capacidad de usar la
   terminal y el perfil de Chrome que tú elijas. Abre como carpeta de trabajo
   `Documents/`; no necesitas tener clonado Pancracio Prisma ni colocarte
   dentro de su repo. Codex buscará una copia local y, si no existe, traerá
   el producto desde GitHub.
2. **Git instalado y GitHub configurado** con una cuenta que pueda leer los
   repos privados de `Pancracio-Prisma`. Deja funcionando el acceso Git por
   SSH y la sesión de GitHub en el perfil de Chrome que usarás. Codex
   comprobará el acceso antes de clonar o actualizar y no te pedirá llaves ni
   códigos por el chat. Esa cuenta sirve para obtener el producto; durante la
   instalación indicarás cuál organización de GitHub será la de la empresa.

Después, Codex te pedirá el perfil y la cuenta de Google, el proyecto GCP
existente con facturación activa y, si eliges IONOS, la sesión en su UI y el
acceso SSH a la VPS. Los usará cuando llegue a esas etapas; no necesitas
introducir esos datos en el prompt inicial. Contraseñas y segundo factor se
resuelven directamente en la página o terminal correspondiente.

## Qué decirle al agente

Con `Documents/` abierto en Codex, dile:

> Instala Pancracio Prisma en modo técnico para una empresa nueva. Estoy en
> `Documents/`, sin asumir que el producto ya está clonado. Comprueba Git y
> mi acceso a GitHub; busca una copia limpia del repo privado
> `Pancracio-Prisma/pancracio-prisma` y, si no existe, clónalo por SSH desde
> GitHub. Si existe, verifica su remoto y actualízala sin sobrescribir trabajo
> local. Lee `AGENT_TECH_INSTALL.md` de ese repo y sigue sus instrucciones.
> Guíame con las decisiones que necesites; pregúntame si quiero
> infraestructura propia o alojada por Brunova. Usa únicamente las cuentas y
> el perfil de navegador que te indique. Prepara y verifica Prisma Tools y
> deja la organización lista para instalar a sus usuarios. Al terminar,
> entrégame el kit de End User Install y el aviso de verificación separado,
> con instrucciones claras para compartirlos con cada persona.

Codex leerá el contrato de instalación y conducirá los pasos. No necesitas
ejecutar manualmente los comandos del paquete técnico ni editar JSON. Si una
cuenta requiere contraseña o segundo factor, introdúcelo tú directamente en
la página correspondiente; no lo compartas en el chat.

## Qué te va a pedir

- Nombre de la empresa, dominio, idioma y nombre visible del asistente.
- Modalidad de Tools: infraestructura propia o alojada por Brunova. Si eliges
  propia, te preguntará si Prisma Schema y Prisma Policy correrán en una
  **VM de Google Cloud** o en una **VPS de IONOS**. En ambos casos puede
  reutilizar PostgreSQL ya instalado y crear una base dedicada; pedirá
  dominio HTTPS y responsable de infraestructura. El Gateway corre en
  Cloud Run del proyecto Google de la empresa y se conecta a Policy.
  Para Google, el proyecto debe existir con facturación activa y tu sesión
  debe estar abierta en la consola. Para IONOS, debes tener abierta la sesión
  de IONOS y un acceso SSH disponible en la máquina; el agente te pedirá un
  alias o ruta de llave protegida, nunca la llave privada en el chat o en un
  `.env`.
  Si eliges Brunova, te pedirá la identidad de la empresa y la autorización
  necesaria para provisionar su instancia, sin pedirte un servidor ni una
  base de datos. Esa modalidad aún no está disponible para instalación real.
- Perfil de Chrome y cuenta de GitHub de la empresa. La organización de GitHub
  puede existir ya o crearse durante esta instalación: si aún no existe, Codex
  te pedirá el nombre y quién será su propietario, te mostrará la propuesta y
  esperará tu decisión antes de crearla. Después preparará allí los
  repositorios privados de Prisma.
- Cuenta Google, proyecto GCP existente con facturación activa para identidad,
  signals y Gateway, región y dominio de Google Workspace. Indicarás el
  proyecto y abrirás sesión en su consola antes de que el agente lo configure.
  Esto también aplica cuando PostgreSQL y Policy se alojan en IONOS.
- Estructura inicial de departamentos, áreas y equipos. Para cada puesto:
  título, equipo, si lo ocupa una o varias personas, y quiénes serán los
  primeros ocupantes. Distinguirá el puesto de negocio de sus permisos.
- Usuarios iniciales, correos corporativos, administrador principal y
  decisiones de acceso a conocimiento y publicación entre áreas.
- Para cada Seat inicial, qué departamento ocupa y qué perfil de operaciones
  tendrá su rol. Una persona puede ocupar varios Seats; Panky elegirá la ruta
  autorizada según lo que le pidas, sin exigirte seleccionar un puesto.
- Un repo canónico por cada contexto organizacional, incluidos los de
  departamento y Seat. El agente preparará esos repos en GitHub como
  transporte de notas; no duplicará el contexto en repos de publicación.
- Qué herramientas usará la empresa (por ejemplo Workspace, n8n o WhatsApp),
  qué recursos concretos pertenecen a cada departamento y cuáles se comparten
  con otros. También te preguntará por excepciones de acceso, vigencia o usos
  limitados cuando las necesites.
- Qué conectores externos necesitan, si los hay. El Gateway de Prisma Tools
  se instala o conecta siempre; los conectores de Workspace, n8n u otros sí
  dependen de las herramientas que elijas.
- Equipo donde se hará la primera prueba de instalación, y quién
  recibirá el paquete de usuario.

El agente preparará el Core y los repositorios; en modalidad propia desplegará
Prisma Schema, Prisma Policy y Prisma Tools Gateway, o verificará una instalación
existente de esos servicios en la infraestructura de la empresa. Publicará la
primera política de Core y comprobará que el Gateway entrega el catálogo y
decisiones correctas mediante OIDC. Configurará el cliente OAuth de escritorio,
la identidad federada, el topic Pub/Sub, los publicadores de GitHub y las
suscripciones filtradas; probará un inicio de sesión real, un signal autorizado
y rechazos de identidad y repositorio fuera de alcance. Después preparará el
bundle firmado. Cada usuario recibe el mismo endpoint verificado; no configura
la base de datos en su equipo. El vault de Obsidian se monta durante su
instalación individual.
Te mostrará las decisiones de propiedad y permisos antes de crear recursos
externos. Al final debe entregarte un recibo de instalación comprobada y,
por cada sistema operativo necesario, **una carpeta de instalación para los
usuarios**. Su nombre es siempre
`Pancracio-Prisma-<empresa>-<macos|windows>-v<versión>`;
para Headquarters en Mac empezará con `Pancracio-Prisma-headquarters-macos-v`.
Codex muestra al final la ruta exacta de cada carpeta para que sepas cuál
compartir. Esa carpeta contiene `END_USER_INSTALL.md`, las instrucciones de
Codex, la configuración firmada de la empresa (`bundle/`) y el programa
firmado (`release/`). Puedes compartirla por Drive con las personas que la
instalarán. Codex prepara además un **aviso de verificación fuera de esa
carpeta**, con el mismo nombre seguido de `-verification.md`; envíalo por un
canal corporativo autenticado distinto del enlace al kit. La persona solo
abre ambos mensajes ante Codex; Codex hace la
comprobación. Un plan o una semilla sin esos recibos no cuenta como
instalación terminada.

La instalación técnica queda **bloqueada** si falta el release activo de
política, el Gateway no está listo, falla OIDC o no se comprueban tanto un
acceso permitido como uno denegado. No se entrega el kit de usuario en ese
estado.

**Estado del producto:** el ensayo local de instalación técnica y de usuario
pasó con un release firmado y archivos temporales eliminados. Fue una prueba
con recursos ficticios y servicios externos simulados. Para la primera empresa
real, Codex debe comprobar sus servicios, permisos y dos Actors de nodos
distintos antes de entregar paquetes a usuarios.

## Altas después de la instalación técnica

Podrás pedirle al agente en lenguaje natural: “Da de alta a una persona”,
“crea un departamento”, “abre un Seat”, “agrega un rol”, “conecta una Tool y su
Resource”, “comparte este recurso con otro departamento” o “da una excepción
temporal para este contexto”. El agente reutilizará lo existente, te pedirá
solo los datos que falten, mostrará a quién afectará el cambio y lo comprobará
antes de decirte que quedó activo. Las mutaciones normales de contexto, como
asignar encargos o enriquecer conocimiento, forman parte del flujo gobernado;
borrar o revocar requiere una autorización explícita.

La lista completa de recorridos y las verificaciones del agente están en
`AGENT_ENTITY_ONBOARDING.md`. No necesitas conocer las tablas para solicitar
un alta. Las altas que cambian permisos organizacionales exigen publicación
desde Core, activación en el backend y lectura de vuelta antes de confirmarse;
una semilla local no cumple ese requisito.

# Instala Panky Prisma en tu computadora

Esta guía es para cada persona de la empresa. La empresa ya preparó Panky;
Codex te ayudará a instalar tu copia y comprobar que quedó lista.

## Lo que necesitas recibir

El administrador te entregará dos archivos:

1. **El ZIP de instalación** para tu empresa y tu sistema (`macos` o
   `windows`). Su nombre empieza con `Pancracio-Prisma-`.
2. **Un aviso de verificación** cuyo nombre termina en `-verification.md`.
   Puede estar junto al ZIP o en la carpeta donde lo extrajiste. Codex
   comprobará las firmas; tú no necesitas interpretar sus números.

En modo POC, estos dos archivos pueden llegar juntos. Si falta el aviso,
pídelo al administrador. En modo definitivo, el administrador debe enviarlo
por un canal independiente para confirmar también el origen del paquete.

## Cómo empezar

Descarga el ZIP y extráelo en tu computadora. Abre **la carpeta extraída**
`Pancracio-Prisma-<empresa>-<macos|windows>-v<versión>` como carpeta de trabajo
en Codex. No abras una carpeta de otro Panky que ya uses. Comparte con Codex
el aviso de verificación si está en otra carpeta. Si está junto al ZIP,
Codex lo encontrará ahí.

Dile a Codex:

> Instala Panky Prisma en esta computadora siguiendo las instrucciones de
> esta carpeta. Comprueba el aviso de verificación que acompaña al kit,
> guíame hasta que quede listo y conserva cualquier otro Pancracio que ya
> tenga.

Este mensaje sirve para cualquier empresa: la carpeta contiene su
configuración firmada. Codex lee `AGENT_END_USER_INSTALL.md` dentro de ella,
comprueba el paquete y busca la versión firmada más reciente **antes de la
primera instalación**. El número en el nombre del ZIP indica la versión con
que se preparó el kit; no limita la versión que quedará instalada. Si no se
puede comprobar el canal o la firma, Codex se detiene y te explica el motivo.
No tienes que ejecutar comandos ni proporcionar identificadores de la empresa.

## Lo que te pedirá la instalación

Codex te guiará para iniciar sesión con **tu cuenta Google de trabajo**. Si
Google muestra una pantalla de permisos, revisarás y aprobarás allí el acceso
que Panky solicita para trabajar con Google Workspace, como Drive, Docs o
Sheets. Panky actúa con tu cuenta dentro de lo que Google te permite y de los
permisos que tu empresa haya configurado. Esta aprobación no le da acceso a
otras cuentas tuyas. Escribe contraseñas y códigos solo en la página de
Google; nunca los pegues en el chat.

Si tu empresa está en **modo POC**, no necesitas cuenta GitHub, una sesión
abierta en GitHub ni una llave SSH preparada en tu computadora. El kit ya
indica la cuenta de transporte de la empresa. Durante la instalación, Codex
crea una llave distinta para esta computadora, el Gateway la registra y
comprueba que la instalación trae los repositorios autorizados para tu
cuenta de trabajo. No te pedirá esa llave ni un token en el chat. Si la
comprobación falla, no declarará la instalación lista.

Fuera del POC, Codex te guiará para conectar tu cuenta GitHub individual y
verificará sus accesos antes de traer información de la empresa.

## Al terminar

Panky traerá el contexto de trabajo que te corresponde. Tu espacio personal
quedará separado. Durante el POC permanecerá en esta computadora; cuando la
empresa pase a modo definitivo podrás elegir una copia privada.

Codex te dirá cuándo la instalación esté **lista** y Panky te hará unas pocas
preguntas para empezar a trabajar contigo. Si falta el aviso, la autorización
de Google o algún acceso, Codex te dirá exactamente qué necesita del
administrador y no dará por terminado el proceso.

## Si quieres desinstalar esta copia

Dile a Codex: «Desinstala Panky Prisma de esta computadora». Codex te mostrará
la empresa y la instancia exactas y te pedirá confirmar esa instancia. Luego
detendrá su sincronización, revocará su llave de GitHub y sus credenciales de
transporte, y borrará solo sus carpetas locales. Esto incluye el contexto
personal que estuviera guardado únicamente en esa copia; pide conservar una
copia antes de confirmar si la necesitas. Si una revocación falla, Codex dejará
la instalación recuperable para reintentar y no dirá que se desinstaló.

Desinstalar tu computadora **no** da de baja tu cuenta de Panky en la empresa,
ni cambia tus Seats o permisos. Esa baja se solicita por separado a la empresa.

Para futuras actualizaciones, basta decir: **«Panky, actualízate»**.

Si la empresa termina el POC, Panky te avisará cuando llegue el cambio desde
Core. Te mostrará la cuenta GitHub asignada y te preguntará qué perfil de
Chrome la tiene abierta. Codex preparará la conexión, la llave y los accesos;
GitHub puede pedirte aprobar una invitación. No tendrás que reinstalar Panky
ni escribir comandos o compartir claves en el chat.
